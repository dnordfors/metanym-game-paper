#!/usr/bin/env python3
"""Criterion B — criterion reliability (anchor-shift consistency), §4.4, Appendix A.2.b.

Criterion reliability is the evaluator's capacity to hold a stable standard for each
non-factual criterion; it is measured by anchor-shift consistency. This script reproduces
the §4.4 per-axis anchor-shift-consistency table, the criterion-reliability column of the
§4.4 council table with its bootstrap interval, and Appendix A.2.b (eqs A10–A11).

Paper quote (§4.4):
    "The anchor is the fixed reference every submission is scored against; we
    sweep its value across 5, 6, 7, and 8 ... A reliable evaluator gives the
    submissions the same pattern of relative scores whichever value is used ...
    For each evaluator, and for each rating axis separately, we correlate
    (Pearson) the scores at one anchor with the scores at another, averaged over
    the six anchor pairs."

Paper quote (§4.4 gate):
    "a reliable evaluator must show ... criterion reliability on the non-factual
    axes — collapsed anchor-shift consistency rho_bar >= 0.78 (Pearson)."

**Leave-self-out.** An evaluator's ratings of its own portfolio are collected in the runs but
are excluded here, and the two submissions that returned a sixth archetype contribute their
first five only (SCORED_ARCHETYPES). So the design counts per evaluator are 50 archetype
units (the 10 *other* graded portfolios x 5 archetypes), 250 parallel contexts (10 x 25) and
10 portfolios — except for the anchor claude-opus-4.5, whose own portfolio is the reference
rather than one of the 11 graded submissions, so it grades all 11: 55 / 275 / 11. Observed
coverage sits at or just below those design counts wherever an evaluation failed to parse or
came back short (per anchor pass, 40–50 / 200–250 / 8–10; gpt-4.1-nano is the worst case).
Pearson drops the missing entries pairwise, so a short pass costs units, not correctness.

Two quantities (Appendix A.2.b):
  (A10) per-axis criterion reliability rho[s,x] — DIAGNOSTIC only (the §4.4 per-axis table):
        the mean of the six anchor-pair Pearson correlations of evaluator s's axis-x
        score vector, over that axis's units (parallel contexts for factual, archetypes
        for the four per-archetype axes, portfolios for structural-diversity).
  (A11) criterion-reliability score rho_bar[s] — THE GATE: collapse the FOUR
        non-factual per-archetype axes (beauty, intelligence,
        instantiation_distinctness, impressive_length) into one score per
        (submission, archetype) -> a 50-vector (55 for the anchor), then the mean of the
        six anchor-pair Pearson correlations.  (Factual is Criterion A's job;
        structural-diversity, one value per portfolio, is too coarse — both
        excluded.)  A constant (zero-variance) anchor pair is undefined and
        dropped from the average.  Council gate: rho_bar >= 0.78.

The point estimates below are `build_paper1_tables.py`'s — that script owns all three §4.4
exhibits — and are asserted equal at the end of the run, so the two cannot drift apart. What
this script adds is the 95% percentile bootstrap over the (submission, archetype) grid of
A.5, which is where the council table's criterion-reliability interval comes from.

Input : the four anchor sweep runs (anchor 5/6/7/8) under RUNS.
Run    : python scripts/criterion_b_stability.py
"""
from __future__ import annotations
import json, re, os, glob, statistics as st, sys
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path
import numpy as np

r2 = lambda x: float(Decimal(str(x)).quantize(Decimal("0.01"), ROUND_HALF_UP))  # as A.5 rounds
RUNS = Path(os.environ.get("RUNS", Path(__file__).resolve().parents[1] / "data"))
JSON_RE = re.compile(r"```json\s*\n(.*?)\n```", re.DOTALL)
MODELS = ["claude-opus-4.1", "claude-opus-4.5", "claude-opus-4.0", "claude-sonnet-4",
          "gemini-3.1-pro", "gemini-2.5-flash", "gpt-4.1-2025-04-14", "gpt-4.1-mini",
          "gpt-4.1-nano", "gpt-4o", "gpt-4o-2024-08-06", "gpt-4o-mini"]
FILEKEY = {"gpt-4.1-2025-04-14": "gpt-41-2025-04-14", "gpt-4.1-mini": "gpt-41-mini",
           "gpt-4.1-nano": "gpt-41-nano"}
NONFACT_ARCH = ("beauty", "intelligence", "instantiation_distinctness", "impressive_length")
AXES = ("factual",) + NONFACT_ARCH + ("structural_diversity",)
# Archetypes 1..5 only: the two submissions carrying a sixth archetype contribute their first
# five, so every portfolio weighs the same. Same cap as build_paper1_tables.SCORED_ARCHETYPES.
SCORED_ARCHETYPES = 5


def _fk(m): return FILEKEY.get(m, m)


def _dir(anchor: int) -> str:
    if anchor == 7:
        ds = sorted(glob.glob(str(RUNS / "probe_K_anchor7*"))) or sorted(glob.glob(str(RUNS / "probe_K_2*")))
    else:
        ds = sorted(glob.glob(str(RUNS / f"probe_K_anchor{anchor}*")))
    return max(ds, key=lambda d: len(glob.glob(d + "/eval_*_x_*.json"))) if ds else ""


def read(ev, tg, d, collapse_nonfactual=False):
    if _fk(ev) == _fk(tg):          # leave-self-out (A.2.b): a model's own portfolio is not a unit
        return {}
    fp = Path(d) / f"eval_{_fk(ev)}_x_{_fk(tg)}.json"
    if not d or not fp.exists():
        return {}
    try:
        node = json.loads(JSON_RE.search(json.load(open(fp))["Messages"][0]["Message"]["Content"]).group(1))
        node = node["scores"][list(node["scores"])[0]]
        o = {}
        for ai, a in enumerate(node["archetypal_contexts"][:SCORED_ARCHETYPES], 1):
            if collapse_nonfactual:                                    # (A11) gate vector
                comp = [a[k] for k in NONFACT_ARCH if isinstance(a.get(k), (int, float))]
                if comp:
                    o[(tg, ai)] = st.mean(comp)
            else:                                                      # (A10) per-axis
                for pi, fr in enumerate(a.get("factual_per_pc") or [], 1):
                    o[("factual", (tg, ai, pi))] = fr
                for k in NONFACT_ARCH:
                    if isinstance(a.get(k), (int, float)):
                        o[(k, (tg, ai))] = a[k]
        if not collapse_nonfactual and isinstance(node.get("structural_diversity"), (int, float)):
            o[("structural_diversity", (tg,))] = node["structural_diversity"]
        return o
    except Exception:
        return {}


def pear(x, y):
    m = ~(np.isnan(x) | np.isnan(y)); x, y = x[m], y[m]
    if len(x) < 3 or x.std() < 1e-9 or y.std() < 1e-9:    # constant -> undefined, dropped
        return np.nan
    return float(((x - x.mean()) * (y - y.mean())).mean() / (x.std() * y.std()))


def mean_pairwise(rows4):       # rows4: 4 x N array (anchors 5,6,7,8); mean of 6 pairwise Pearson
    ps = [pear(rows4[i], rows4[j]) for i in range(4) for j in range(i + 1, 4)]
    ps = [p for p in ps if p == p]
    return st.mean(ps) if ps else np.nan


def main():
    dirs = {a: _dir(a) for a in (5, 6, 7, 8)}
    if not all(dirs.values()):
        sys.exit(f"missing anchor sweep dirs under {RUNS}: {dirs}")
    targets = sorted({Path(f).stem.split("_x_", 1)[1] for f in glob.glob(dirs[7] + "/eval_*_x_*.json")})

    # ---- (A11) the gate: collapsed non-factual, over the 55-atom (submission, archetype) grid ----
    # The grid is 55; an individual evaluator fills 50 of them (its own portfolio is left out),
    # and the anchor fills all 55 (its portfolio is the reference, not a graded submission).
    cols = [(tg, ai) for tg in targets for ai in range(1, SCORED_ARCHETYPES + 1)]
    cidx = {c: i for i, c in enumerate(cols)}
    Amat, gate = {}, {}
    for ev in MODELS:
        A = np.full((4, len(cols)), np.nan)
        for k, a in enumerate((5, 6, 7, 8)):
            for tg in targets:
                for c, v in read(ev, tg, dirs[a], collapse_nonfactual=True).items():
                    if c in cidx: A[k, cidx[c]] = v
        Amat[ev] = A; gate[ev] = mean_pairwise(A)

    # 95% percentile bootstrap over the 55-atom grid (Appendix A.5)
    rng = np.random.default_rng(20260529); N = len(cols); ci = {}
    for ev in MODELS:
        bs = [b for b in (mean_pairwise(Amat[ev][:, rng.integers(0, N, N)]) for _ in range(2000)) if b == b]
        ci[ev] = (np.percentile(bs, 2.5), np.percentile(bs, 97.5)) if len(bs) > 20 else (np.nan, np.nan)

    print("=== Criterion B gate: collapsed non-factual criterion reliability rho_bar (A11), 95% CI ===")
    print("=== leave-self-out, archetypes 1-5; the council column of the §4.4 council table ===")
    for ev in sorted(MODELS, key=lambda m: -(gate[m] if gate[m] == gate[m] else -9)):
        lo, hi = ci[ev]
        flag = "council-eligible" if (gate[ev] == gate[ev] and gate[ev] >= 0.78) else ""
        print(f"  {ev:20}{r2(gate[ev]):6.2f}   [{r2(lo):.2f}, {r2(hi):.2f}]   {flag}")

    # ---- (A10) per-axis table (§4.4 exhibit (i)) ----
    DATA = {ev: {} for ev in MODELS}
    for k, a in enumerate((5, 6, 7, 8)):
        for ev in MODELS:
            for tg in targets:
                for key, v in read(ev, tg, dirs[a]).items():
                    DATA[ev].setdefault(key, [np.nan] * 4)[k] = v

    def axis_stab(ev, axis):
        keys = sorted(key for key in DATA[ev] if key[0] == axis)
        if len(keys) < 3: return np.nan
        A = np.array([[DATA[ev][key][a] for key in keys] for a in range(4)])
        return mean_pairwise(A)

    print("\n=== Criterion B per-axis anchor-shift consistency (A10, §4.4) ===")
    print(f"{'evaluator':20}" + "".join(f"{h:>9}" for h in ("fact","beauty","intel","distinct","length","struct")))
    for ev in sorted(MODELS, key=lambda m: -st.mean([v for v in
                     (axis_stab(m, ax) for ax in NONFACT_ARCH) if v == v] or [0])):
        vals = [axis_stab(ev, ax) for ax in AXES]
        print(f"{ev:20}" + "".join(f"{(r2(v) if v == v else 'n/a'):>9}" for v in vals))

    cross_check(gate, axis_stab)


def cross_check(gate, axis_stab):
    """Assert this script agrees with build_paper1_tables.py, the owner of the §4.4 exhibits.

    Skipped when RUNS_GEN/RUNS_SWEEP are unset (this script needs only RUNS, so it can be run
    on its own); `reproduce.sh` sets all three, so the pipeline always makes the comparison.
    """
    if not (os.environ.get("RUNS_GEN") and os.environ.get("RUNS_SWEEP")):
        print("\n(cross-check against build_paper1_tables.py skipped: RUNS_GEN/RUNS_SWEEP unset)")
        return
    import build_paper1_tables as BP
    GA, targets = BP.load(BP.run_dirs())
    comp = BP.components(GA, targets, BP.scoring_atoms(targets), diagnostics=True)
    AXMAP = {"factual": comp["RHOF"], "beauty": comp["RHO"]["beauty"],
             "intelligence": comp["RHO"]["intel"], "instantiation_distinctness": comp["RHO"]["distinct"],
             "impressive_length": comp["RHO"]["length"], "structural_diversity": comp["RHO"]["struct"]}
    worst = 0.0
    for ev in MODELS:
        a, b = gate[ev], comp["RB"][ev]
        if a == a or b == b:
            worst = max(worst, abs(a - b))
        for ax, table in AXMAP.items():
            x, y = axis_stab(ev, ax), table.get(ev)
            if (x == x) != (y is not None and y == y):
                raise SystemExit(f"criterion B disagrees with build_paper1_tables on {ev}/{ax} (defined-ness)")
            if x == x:
                worst = max(worst, abs(x - y))
    if worst > 1e-9:
        raise SystemExit(f"criterion B disagrees with build_paper1_tables by up to {worst:.2e}")
    print(f"\ncross-check vs build_paper1_tables.py: identical (max |diff| = {worst:.1e})")


if __name__ == "__main__":
    main()
