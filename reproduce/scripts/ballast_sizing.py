#!/usr/bin/env python3
"""§4.6 — sizing the ballast. Emits the table the section reports.

A contest (§4.5) is a sub-matrix of the bootstrap: the five seats plus one
contestant, over the incumbents' portfolios, the ballast, and the contestant's own. So the
ballast can be sized by re-analysis of the pinned run, with no new generation.

For each candidate ballast the script convenes all seven possible rounds (one per
non-council model) and reports:

  range         mean across seats of a seat's anchored E^F range over the seven rounds
  sigma1/sigma2 separation of the council-alone matrix, with bootstrap interval
  seat spread   range of the seats' anchored E^F (discrimination)
  fidelity      mean |E^F - the §4.2 twelve-evaluator value| over the seats
  guards hold   fraction of bootstrap resamples in which both §4.5 guards pass

Bootstrap resamples the parallel contexts within each portfolio, matching §4.2.

Env: RUNS_GEN (the anchor-7 run directory), B (default 600).
"""
import collections, json, os, re, sys, statistics as st
from pathlib import Path
import numpy as np

JR = re.compile(r"```json\s*\n(.*?)\n```", re.DOTALL)
MODELS = ["claude-opus-4.1","claude-opus-4.5","claude-opus-4.0","claude-sonnet-4",
          "gemini-3.1-pro","gemini-2.5-flash","gpt-4.1-2025-04-14","gpt-4.1-mini",
          "gpt-4.1-nano","gpt-4o","gpt-4o-2024-08-06","gpt-4o-mini"]
FK = {"gpt-4.1-2025-04-14":"gpt-41-2025-04-14","gpt-4.1-mini":"gpt-41-mini",
      "gpt-4.1-nano":"gpt-41-nano"}
ANCHOR = "claude-opus-4.5"
COUNCIL = ["claude-opus-4.5","gemini-3.1-pro","claude-opus-4.0","claude-opus-4.1",
           "gemini-2.5-flash"]
SCORED_ARCHETYPES = 5
SEP_LO, SEP_HI, SPREAD_FLOOR = 2.0, 5.0, 2.5      # the §4.5 guards


def parse(d, ev, tg):
    fp = Path(d) / f"eval_{FK.get(ev,ev)}_x_{FK.get(tg,tg)}.json"
    if not fp.exists():
        return None
    try:
        n = json.loads(JR.search(json.load(open(fp))["Messages"][0]["Message"]["Content"]).group(1))
        n = n["scores"][list(n["scores"])[0]]
        return {ai: list(a.get("factual_per_pc") or [])
                for ai, a in enumerate(n["archetypal_contexts"], 1) if ai <= SCORED_ARCHETYPES}
    except Exception:
        return None


def build(run):
    # leave-self-out: an evaluator never scores its own portfolio (§4.2, §4.4).
    # Those cells stay at the 7.0 fill, matching build_paper1_tables.py.
    D = {(e, t): parse(run, e, t) for e in MODELS for t in MODELS if e != t}
    targets = [m for m in MODELS if any(D.get((e, m)) for e in MODELS)]
    cols = sorted({(t, ai, pi) for t in targets for ev in MODELS
                   for ai, fl in (D.get((ev, t)) or {}).items() for pi in range(len(fl))})
    ci = {c: i for i, c in enumerate(cols)}
    R = np.full((len(MODELS), len(cols)), np.nan)
    for si, ev in enumerate(MODELS):
        for t in targets:
            for ai, fl in (D.get((ev, t)) or {}).items():
                for pi, v in enumerate(fl):
                    if (t, ai, pi) in ci:
                        R[si, ci[(t, ai, pi)]] = float(v)
    by = {}
    for i, c in enumerate(cols):
        by.setdefault(c[0], []).append(i)
    return R, by, targets


def ef(R, sel, panel):
    M = np.where(np.isnan(R[np.ix_([MODELS.index(m) for m in panel], sel)]), 7.0,
                 R[np.ix_([MODELS.index(m) for m in panel], sel)])
    U, S, _ = np.linalg.svd(M - M.mean(axis=1, keepdims=True), full_matrices=False)
    f = U[:, 0]
    if f.sum() < 0:
        f = -f
    f = np.clip(f, 0, None)
    fa = f[panel.index(ANCHOR)]
    sep = float(S[0]/S[1]) if len(S) > 1 and S[1] > 0 else float("inf")
    if fa <= 0:
        return {m: float("nan") for m in panel}, sep
    return {m: 7.0*f[k]/fa for k, m in enumerate(panel)}, sep


def measure(R, by, council_t, ballast, contestants, ref, rs=None):
    def C(ts):
        out = []
        for t in ts:
            out += list(rs(by[t])) if rs else list(by[t])
        return out
    base = council_t + [b for b in ballast if b not in council_t]
    s1, sep = ef(R, C(base), COUNCIL)
    spread = max(s1.values()) - min(s1.values())
    fid = st.mean(abs(s1[m] - ref[m]) for m in COUNCIL)
    per = {s: [] for s in COUNCIL if s != ANCHOR}      # anchor is 7.00 by construction
    lows = []
    for c in contestants:
        v, _ = ef(R, C(base + ([c] if c not in base else [])), COUNCIL + [c])
        for s in per:
            per[s].append(v[s])
        lows.append(min(COUNCIL, key=lambda m: v[m]))
    ranges = [max(x) - min(x) for x in per.values()]
    return st.mean(ranges), max(ranges), sep, spread, fid, lows


def main():
    run = Path(os.environ.get("RUNS_GEN", "data/probe_K_20260529T014133Z"))
    B = int(os.environ.get("B", 600))
    if not run.exists():
        sys.exit(f"run directory not found: {run}  (set RUNS_GEN)")
    R, by, targets = build(run)
    council_t = [m for m in COUNCIL if m in targets]
    contestants = [m for m in MODELS if m not in COUNCIL]
    pool = sorted([m for m in targets if m not in COUNCIL],
                  key=lambda t: float(np.nanmean(R[:, by[t]])))
    ref, sep_ref = ef(R, list(range(R.shape[1])), MODELS)      # §4.2 twelve-evaluator
    rng = np.random.default_rng(20260811)
    rs = lambda idx: rng.choice(idx, len(idx), replace=True)

    print(f"§4.6 ballast sizing   run={run.name}  B={B}")
    print(f"reference: twelve-evaluator sigma1/sigma2 = {sep_ref:.2f}, "
          f"council E^F spread = {max(ref[m] for m in COUNCIL)-min(ref[m] for m in COUNCIL):.2f}")
    print(f"ballast candidates, poorest first: {', '.join(pool)}\n")
    print(f"{'ballast':10}{'rng(mean)':>11}{'rng(max)':>10}{'sigma1/sigma2':>22}"
          f"{'spread':>9}{'fidelity':>10}{'guards':>9}   rotations")
    demotions = {}
    for n, label in ((0, "none"), (1, "one"), (2, "two"), (3, "three")):
        b = pool[:n]
        mvm, mvx, sep, sp, fid, lows = measure(R, by, council_t, b, contestants, ref)
        acc = [measure(R, by, council_t, b, contestants, ref, rs) for _ in range(B)]
        lo, hi = np.percentile([a[2] for a in acc], [2.5, 97.5])
        hold = sum(1 for a in acc if SEP_LO <= a[2] <= SEP_HI and a[3] > SPREAD_FLOOR)/B
        band = f"{sep:5.2f} [{lo:4.2f}, {hi:4.2f}]"
        print(f"{label:10}{mvm:>11.2f}{mvx:>10.2f}{band:>22}{sp:>9.2f}{fid:>10.2f}"
              + (f"{hold:>9.2f}" if n else f"{'--':>9}")
              + f"   rotate-out->{len(set(lows))}")
        demotions[label] = list(lows)
    print("\nProtocol takes TWO: the smallest ballast whose guards hold reliably.")

    # Which seat each contest would rotate out. The count alone (rotate-out->N) does not say
    # whether the target is arbitrary or merely unstable, and the paper's §4.6 claim
    # rests on the distribution, not on N.
    print("\nrotation target per contestant (the seat with the lowest E^F in that contest):")
    for label, lows in demotions.items():
        tally = collections.Counter(lows)
        parts = ", ".join(f"{s} x{k}" for s, k in tally.most_common())
        print(f"  {label:6} {len(tally)} distinct  |  {parts}")


if __name__ == "__main__":
    main()
