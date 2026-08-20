#!/usr/bin/env python3
"""Leaderboard invariance across the anchor sweep, §5.8.

The anchor sweep {5, 6, 7, 8} is four complete evaluation passes that differ
only in a non-semantic calibration value (the score the fixed reference
portfolio is pinned at). At T=0 every other token of every prompt is
identical, so the four passes are a controlled perturbation experiment — an
effective N=4 robustness check that costs no determinism.

This script recomputes the §4.3 generation rating (A3) (six-axis,
council leave-self-out mean) independently at EACH anchor value, then reports:

  1. the four per-anchor leaderboards (raw, on each anchor's own scale);
  2. pairwise Spearman rank correlations between the four leaderboards
     (6 anchor pairs) — the headline stability number;
  3. per-model rank range across the four passes (max rank − min rank);
  4. per-model score spread across passes after re-centring each pass to the
     anchor-7 scale (score − anchor + 7), as a dispersion diagnostic.

The aggregation mirrors `build_total_geneval.py::gen6` exactly (the canonical
A3 estimator): per evaluator-target cell, the mean of six axis means —
factual (mean over factual_per_pc across the portfolio), beauty, intelligence,
instantiation_distinctness, impressive_length (per-archetype means), and
structural_diversity (per portfolio) — averaged leave-self-out over the five
council seats. The anchor model (claude-opus-4.5) is ungraded.

Input : RUNS_SWEEP (parent of the four anchor runs; anchor 7 matched by
        probe_K_anchor7* or probe_K_2*).
Run    : RUNS_SWEEP=… python scripts/anchor_sweep_leaderboard.py
"""
from __future__ import annotations
import json, re, os, glob, statistics as st, sys
from itertools import combinations
from pathlib import Path

JR = re.compile(r"```json\s*\n(.*?)\n```", re.DOTALL)
MODELS = ["claude-opus-4.1", "claude-opus-4.5", "claude-opus-4.0", "claude-sonnet-4",
          "gemini-3.1-pro", "gemini-2.5-flash", "gpt-4.1-2025-04-14", "gpt-4.1-mini",
          "gpt-4.1-nano", "gpt-4o", "gpt-4o-2024-08-06", "gpt-4o-mini"]
FK = {"gpt-4.1-2025-04-14": "gpt-41-2025-04-14", "gpt-4.1-mini": "gpt-41-mini",
      "gpt-4.1-nano": "gpt-41-nano"}
def fk(m): return FK.get(m, m)
SIX = ("beauty", "intelligence", "instantiation_distinctness", "impressive_length")
COUNCIL = ["claude-opus-4.1", "claude-opus-4.5", "claude-opus-4.0",
           "gemini-3.1-pro", "gemini-2.5-flash"]
AM = "claude-opus-4.5"          # anchor model: ungraded as generator
ANCHORS = (5, 6, 7, 8)


def parse(d, ev, tg):
    fp = Path(d) / f"eval_{fk(ev)}_x_{fk(tg)}.json"
    if not fp.exists():
        return None
    try:
        node = json.loads(JR.search(json.load(open(fp))["Messages"][0]["Message"]["Content"]).group(1))
        node = node["scores"][list(node["scores"])[0]]
        sd = node.get("structural_diversity")
        sd = float(sd) if isinstance(sd, (int, float)) else None
        arch = {ai: {"fact": list(a.get("factual_per_pc") or []),
                     "six": [a[k] for k in SIX if isinstance(a.get(k), (int, float))]}
                for ai, a in enumerate(node["archetypal_contexts"], 1)}
        return {"arch": arch, "sd": sd}
    except Exception:
        return None


def gen6(cells, s):
    """The A3 generation rating of generator s: council LSO mean of the six-axis mean."""
    vals = []
    for t in COUNCIL:
        if t == s:
            continue
        rec = cells.get((t, s))
        if not rec:
            continue
        fact_means, beauty, intel, dist, length = [], [], [], [], []
        for ai, a in rec["arch"].items():
            if a["fact"]:
                fact_means.append(st.mean(a["fact"]))
            if len(a["six"]) == 4:
                beauty.append(a["six"][0]); intel.append(a["six"][1])
                dist.append(a["six"][2]); length.append(a["six"][3])
        axis_means = [st.mean(lst) for lst in (fact_means, beauty, intel, dist, length) if lst]
        if rec["sd"] is not None:
            axis_means.append(rec["sd"])
        if axis_means:
            vals.append(st.mean(axis_means))
    return st.mean(vals) if vals else None


def spearman(xs, ys):
    def rank(v):
        order = sorted(range(len(v)), key=lambda i: v[i], reverse=True)
        r = [0.0] * len(v)
        i = 0
        while i < len(order):
            j = i
            while j + 1 < len(order) and v[order[j + 1]] == v[order[i]]:
                j += 1
            for k in range(i, j + 1):
                r[order[k]] = (i + j) / 2 + 1
            i = j + 1
        return r
    rx, ry = rank(xs), rank(ys)
    mx, my = st.mean(rx), st.mean(ry)
    num = sum((a - mx) * (b - my) for a, b in zip(rx, ry))
    den = (sum((a - mx) ** 2 for a in rx) * sum((b - my) ** 2 for b in ry)) ** 0.5
    return num / den if den else float("nan")


def main():
    sweep = os.environ.get("RUNS_SWEEP")
    if not sweep:
        sys.exit("set RUNS_SWEEP (parent dir of the four anchor runs)")
    DIRS = {}
    for a in ANCHORS:
        pats = [f"probe_K_anchor{a}_*"] + (["probe_K_2*"] if a == 7 else [])
        ds = [d for p in pats for d in glob.glob(str(Path(sweep) / p))]
        if not ds:
            sys.exit(f"no run dir for anchor {a}")
        DIRS[a] = max(ds, key=lambda d: len(glob.glob(d + "/eval_*_x_*.json")))

    cells = {a: {(ev, tg): parse(DIRS[a], ev, tg) for ev in COUNCIL for tg in MODELS}
             for a in ANCHORS}
    targets = [m for m in MODELS if m != AM]

    lb = {a: {s: gen6(cells[a], s) for s in targets} for a in ANCHORS}

    print("Per-anchor official generation leaderboards (council LSO, six-axis):")
    hdr = f"{'model':<22}" + "".join(f"  a={a:>4}" for a in ANCHORS) + "   rank@5/6/7/8   rank range"
    print(hdr)
    ranks = {}
    for a in ANCHORS:
        order = sorted(targets, key=lambda s: -(lb[a][s] if lb[a][s] is not None else -1))
        ranks[a] = {s: i + 1 for i, s in enumerate(order)}
    order7 = sorted(targets, key=lambda s: ranks[7][s])
    for s in order7:
        scores = "".join(f"  {lb[a][s]:6.2f}" if lb[a][s] is not None else "     --" for a in ANCHORS)
        rk = "/".join(str(ranks[a][s]) for a in ANCHORS)
        rr = max(ranks[a][s] for a in ANCHORS) - min(ranks[a][s] for a in ANCHORS)
        print(f"{s:<22}{scores}   {rk:<14} {rr}")

    print("\nPairwise Spearman between anchor passes:")
    rhos = []
    for a, b in combinations(ANCHORS, 2):
        common = [s for s in targets if lb[a][s] is not None and lb[b][s] is not None]
        r = spearman([lb[a][s] for s in common], [lb[b][s] for s in common])
        rhos.append(r)
        print(f"  anchor {a} vs {b}:  rho = {r:.3f}")
    print(f"  mean = {st.mean(rhos):.3f}   min = {min(rhos):.3f}")

    print("\nPer-model score spread across passes, re-centred to anchor-7 scale (score - anchor + 7):")
    for s in order7:
        adj = [lb[a][s] - a + 7 for a in ANCHORS if lb[a][s] is not None]
        if len(adj) >= 2:
            print(f"  {s:<22} mean {st.mean(adj):5.2f}   range {max(adj)-min(adj):4.2f}   sd {st.pstdev(adj):4.2f}")


if __name__ == "__main__":
    main()
