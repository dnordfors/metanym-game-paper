#!/usr/bin/env python3
"""Reproduce section 4.1 — the un-anchored full-panel leaderboard and its one break.

Reads data/probe_J_20260529T005230Z/ (the un-anchored council-of-peers evaluation: every
model grades every portfolio, no calibration anchor). Prints:

  * the leave-self-out mean overall score per generator, with a 95% percentile bootstrap CI
  * the consecutive gaps and P(adjacent pair holds)
  * the leading-eight / trailing-four division: min P across the 32 cross-pairs

These are the numbers quoted in the paper's section 4.1 paragraph (max adjacent gap inside
the upper eight ≤ 0.17; adjacent-pair probabilities 0.53–0.75; every cross-division pair
≥ 0.79). The script asserts those floors so a clean run confirms the manuscript.

Env: RUNS_UNANCHORED (default data/probe_J_20260529T005230Z).
Also writes data/section_4_1_unanchored.csv (means + CIs).
"""
from __future__ import annotations

import csv
import json
import os
import re
import statistics as st
import sys
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
DATA = HERE.parent / "data"
JR = re.compile(r"```json\s*\n(.*?)\n```", re.DOTALL)

# Display names as in the paper / file-key map used elsewhere in the package.
MODELS = [
    "claude-opus-4.5", "claude-opus-4.1", "claude-opus-4.0", "claude-sonnet-4",
    "gpt-4.1-2025-04-14", "gemini-2.5-flash", "gpt-4.1-mini", "gemini-3.1-pro",
    "gpt-4o-mini", "gpt-4o", "gpt-4o-2024-08-06", "gpt-4.1-nano",
]
FK = {
    "gpt-4.1-2025-04-14": "gpt-41-2025-04-14",
    "gpt-4.1-mini": "gpt-41-mini",
    "gpt-4.1-nano": "gpt-41-nano",
}
fk = lambda m: FK.get(m, m)

AXES6 = (
    "factual_avg", "beauty", "intelligence",
    "instantiation_distinctness", "impressive_length", "structural_diversity",
)
B_REPS = 20000
SEED = 20260529
# Paper's division: ranks 1–8 vs 9–12 under the published LSO ordering.
LEADING_N = 8


def overall(node: dict) -> float:
    arcs = node["archetypal_contexts"]
    means = {
        "factual_avg": st.mean(st.mean(a["factual_per_pc"]) for a in arcs),
        "beauty": st.mean(a["beauty"] for a in arcs),
        "intelligence": st.mean(a["intelligence"] for a in arcs),
        "instantiation_distinctness": st.mean(a["instantiation_distinctness"] for a in arcs),
        "impressive_length": st.mean(a["impressive_length"] for a in arcs),
        "structural_diversity": float(node["structural_diversity"]),
    }
    return st.mean(means[a] for a in AXES6)


def load_cells(run_dir: Path) -> dict[tuple[str, str], float]:
    """{(evaluator, generator): overall} from eval_*.json, leave-self-out ready."""
    cells = {}
    for ev in MODELS:
        for tg in MODELS:
            fp = run_dir / f"eval_{fk(ev)}_x_{fk(tg)}.json"
            if not fp.exists():
                continue
            try:
                raw = json.load(open(fp))
                node = json.loads(JR.search(raw["Messages"][0]["Message"]["Content"]).group(1))
                node = node["scores"][next(iter(node["scores"]))]
                cells[(ev, tg)] = overall(node)
            except Exception as e:
                print(f"  warn: skip {fp.name}: {e}", file=sys.stderr)
    return cells


def main() -> None:
    run = Path(os.environ.get("RUNS_UNANCHORED", DATA / "probe_J_20260529T005230Z"))
    if not run.is_dir():
        sys.exit(f"un-anchored run not found: {run}")
    cells = load_cells(run)
    print(f"loaded {len(cells)} cells from {run.name}")

    vec = {
        m: [cells[(e, m)] for e in MODELS if e != m and (e, m) in cells]
        for m in MODELS
    }
    mean = {m: st.mean(vec[m]) for m in MODELS}
    order = sorted(MODELS, key=lambda m: -mean[m])

    rng = np.random.default_rng(SEED)
    boot = {
        m: np.asarray(vec[m], float)[
            rng.integers(0, len(vec[m]), (B_REPS, len(vec[m])))
        ].mean(1)
        for m in MODELS
    }
    ci = {m: tuple(np.percentile(boot[m], [2.5, 97.5])) for m in MODELS}

    print("\n=== §4.1 un-anchored LSO leaderboard ===")
    print(f"{'rank':>4}  {'model':22} {'mean':>6}  {'95% CI':>16}")
    for i, m in enumerate(order, 1):
        lo, hi = ci[m]
        print(f"{i:>4}  {m:22} {mean[m]:6.2f}  [{lo:5.2f}, {hi:5.2f}]")

    # Consecutive gaps and adjacent-pair probabilities.
    print("\n=== consecutive gaps ===")
    gaps = []
    for i in range(len(order) - 1):
        a, b = order[i], order[i + 1]
        gap = mean[a] - mean[b]
        p = float((boot[a] > boot[b]).mean())
        gaps.append((gap, p, i + 1, a, b))
        print(f"  after rank {i+1:2}: gap {gap:5.3f}  P={p:.3f}  ({a} > {b})")

    up, lo_models = order[:LEADING_N], order[LEADING_N:]
    cross = sorted(
        (((a, b), float((boot[a] > boot[b]).mean())) for a in up for b in lo_models),
        key=lambda x: x[1],
    )
    max_gap_up = max(g[0] for g in gaps if g[2] < LEADING_N)
    adj_up = [g[1] for g in gaps if g[2] < LEADING_N]
    min_cross = cross[0][1]
    print(f"\n=== division after rank {LEADING_N}: {len(up)} vs {len(lo_models)} ===")
    print(f"  upper band: {up[0]} … {up[-1]}  ({mean[up[0]]:.2f}–{mean[up[-1]]:.2f})")
    print(f"  lower band: {lo_models[0]} … {lo_models[-1]}  ({mean[lo_models[0]]:.2f}–{mean[lo_models[-1]]:.2f})")
    print(f"  max adjacent gap inside upper band: {max_gap_up:.3f}")
    print(f"  adjacent-pair P inside upper band:  {min(adj_up):.3f}–{max(adj_up):.3f}")
    print(f"  cross-division pairs: {len(cross)}; min P = {min_cross:.3f}  ({cross[0][0][0]} > {cross[0][0][1]})")

    # Manuscript assertions (section 4.1 paragraph).
    assert max_gap_up <= 0.175, max_gap_up
    assert 0.52 <= min(adj_up) <= 0.56, min(adj_up)
    assert 0.74 <= max(adj_up) <= 0.76, max(adj_up)
    assert min_cross >= 0.79, min_cross
    assert abs(mean[order[0]] - 9.28) < 0.01
    assert abs(mean[order[7]] - 8.64) < 0.01
    assert abs(mean[order[8]] - 8.25) < 0.01
    assert abs(mean[order[-1]] - 7.32) < 0.01
    print("\nmanuscript floors confirmed.")

    out = DATA / "section_4_1_unanchored.csv"
    with open(out, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["rank", "model", "mean", "ci_lo", "ci_hi"])
        for i, m in enumerate(order, 1):
            lo, hi = ci[m]
            w.writerow([i, m, f"{mean[m]:.6f}", f"{lo:.6f}", f"{hi:.6f}"])
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
