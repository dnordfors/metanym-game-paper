#!/usr/bin/env python3
"""Graded vs binarised factual SVD — the empirical basis for §4.2/§5.6's
"graded, not binarised" claim.

The paper distinguishes its factual estimator from the binary label-free
aggregators (Dawid & Skene 1979; Parisi et al. 2014) by operating on the graded
1-10 integer ratings directly rather than on thresholded true/false verdicts.
This script demonstrates the difference ON THE SAME MATRIX, answering the
referee question "do the two diverge materially?":

  1. GRADED (canonical, A5-A7): the soft 1-10 factual matrix (self/missing =
     anchor 7), row-centred, leading left singular vector, clamped at 0.
  2. BINARY(t) for t in {4, 5, 6}: the SAME matrix binarised first — rating <= t
     maps to +1 ("flagged false"), rating > t to -1 — then the identical
     row-centre + SVD + clamp pipeline.

Reported:
  - the four loading vectors side by side;
  - Spearman of each binary ordering against the graded ordering;
  - pairwise Spearman among the three binary orderings (threshold sensitivity —
    a binarised estimator imports an arbitrary threshold choice the graded
    estimator does not have);
  - the top-5 (council-forming) set under each variant.

Input : RUNS = the anchor-7 evaluation run (probe_K).
Run    : RUNS=… python scripts/graded_vs_binary_svd.py
"""
from __future__ import annotations
import json, re, os, glob, sys
from itertools import combinations
from pathlib import Path
import numpy as np

JR = re.compile(r"```json\s*\n(.*?)\n```", re.DOTALL)
MODELS = ["claude-opus-4.1", "claude-opus-4.5", "claude-opus-4.0", "claude-sonnet-4",
          "gemini-3.1-pro", "gemini-2.5-flash", "gpt-4.1-2025-04-14", "gpt-4.1-mini",
          "gpt-4.1-nano", "gpt-4o", "gpt-4o-2024-08-06", "gpt-4o-mini"]
FK = {"gpt-4.1-2025-04-14": "gpt-41-2025-04-14", "gpt-4.1-mini": "gpt-41-mini",
      "gpt-4.1-nano": "gpt-41-nano"}
def fk(m): return FK.get(m, m)
ANCHOR = 7.0
THRESHOLDS = (4, 5, 6)
# Archetypes 1..5 only. Two submissions (gemini-2.5-flash, gpt-4.1-mini) carry a sixth
# archetype; its five parallel contexts are excluded so the panel stays balanced at 25
# contexts per portfolio -- 11 x 25 = 275 columns -- matching the criterion side.
SCORED_ARCHETYPES = 5


def load_matrix(runs: Path):
    """Soft factual matrix exactly as build_total_geneval.py::compute builds it."""
    F = {ev: {} for ev in MODELS}
    for ev in MODELS:
        for tg in MODELS:
            if ev == tg:
                continue
            fp = runs / f"eval_{fk(ev)}_x_{fk(tg)}.json"
            if not fp.exists():
                continue
            try:
                node = json.loads(JR.search(json.load(open(fp))["Messages"][0]["Message"]["Content"]).group(1))
                node = node["scores"][list(node["scores"])[0]]
                for ai, a in enumerate(node["archetypal_contexts"], 1):
                    if ai > SCORED_ARCHETYPES:
                        continue
                    for pi, v in enumerate(a.get("factual_per_pc") or []):
                        F[ev][(tg, ai, pi)] = float(v)
            except Exception:
                pass
    cols = sorted(set().union(*[set(F[ev]) for ev in MODELS]))
    Mat = np.array([[F[ev].get(c, ANCHOR) for c in cols] for ev in MODELS], float)
    return Mat


def leading_left(M):
    Mc = M - M.mean(axis=1, keepdims=True)
    U, _, _ = np.linalg.svd(Mc, full_matrices=False)
    f = U[:, 0]
    if f.sum() < 0:
        f = -f
    return np.clip(f, 0, None)


def spearman(x, y):
    def rank(v):
        order = np.argsort(-np.asarray(v))
        r = np.empty(len(v)); r[order] = np.arange(1, len(v) + 1)
        return r
    rx, ry = rank(x), rank(y)
    rx, ry = rx - rx.mean(), ry - ry.mean()
    return float((rx * ry).sum() / np.sqrt((rx ** 2).sum() * (ry ** 2).sum()))


def main():
    runs = Path(os.environ.get("RUNS", ""))
    if not runs.exists():
        sys.exit("set RUNS=… (anchor-7 eval run)")
    M = load_matrix(runs)
    graded = leading_left(M)
    binary = {t: leading_left(np.where(M <= t, 1.0, -1.0)) for t in THRESHOLDS}

    print(f"Factual-competence loadings, graded vs binarised (same matrix, {M.shape[1]} columns):\n")
    print(f"{'evaluator':<22}{'graded':>8}" + "".join(f"  bin<= {t}" for t in THRESHOLDS))
    for i in np.argsort(-graded):
        row = "".join(f"  {binary[t][i]:6.2f}" for t in THRESHOLDS)
        print(f"{MODELS[i]:<22}{graded[i]:>8.2f}{row}")

    print("\nOrdering agreement (Spearman):")
    for t in THRESHOLDS:
        print(f"  graded vs binary(<= {t}):  {spearman(graded, binary[t]):.3f}")
    for a, b in combinations(THRESHOLDS, 2):
        print(f"  binary(<= {a}) vs binary(<= {b}):  {spearman(binary[a], binary[b]):.3f}")

    def top5(v):
        return {MODELS[i] for i in np.argsort(-v)[:5]}
    print("\nTop-5 (council-forming) set:")
    print(f"  graded      : {sorted(top5(graded))}")
    for t in THRESHOLDS:
        diff = top5(binary[t]) ^ top5(graded)
        print(f"  binary(<= {t}): {sorted(top5(binary[t]))}   symm.diff vs graded: {sorted(diff) or '—'}")


if __name__ == "__main__":
    main()
