#!/usr/bin/env python3
"""The section 4.2 figure — what anchoring does to resolution (un-anchored vs anchored).

Anonymous dumbbell: each model's leave-self-out overall mean under the un-anchored pass
(probe_J) and under anchored scoring at the production anchor (probe_K), with 95%
percentile bootstrap CIs over evaluators. No model names — the message is structural:
the top of the field decompresses, the leading-eight / trailing-four division widens,
and the intervals still overlap within each band. The anchor (pinned at 7) is the
orange star on the anchored side.

Also computes and asserts the two F-statistics quoted in section 4.2 (between-target
variance over within-target variance, canonical overall-cell recipe of
section_4_1_unanchored.py): 0.33 un-anchored -> 0.66 anchored.

Env: RUNS_UNANCHORED, RUNS_GEN (default the two shipped runs). Writes
figures/anchoring_resolution.png.
"""
from __future__ import annotations

import os
import statistics as st
import sys
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from section_4_1_unanchored import load_cells, MODELS, DATA  # noqa: E402

ANCHOR = "claude-opus-4.5"
LEADING_N = 8
B, SEED = 20000, 20260529

BLUE, ORANGE = "#2a78d6", "#eb6834"
SURFACE, INK, INK2 = "#fcfcfb", "#0b0b0b", "#52514e"
BARC = "#c9ccd1"


def lso_stats(cells, targets, rng):
    out = {}
    for t in targets:
        v = np.array([cells[(e, t)] for e in MODELS if e != t and (e, t) in cells])
        boot = np.array([v[rng.integers(0, len(v), len(v))].mean() for _ in range(B)])
        out[t] = (v.mean(), *np.percentile(boot, [2.5, 97.5]))
    return out


def fstat(cells, targets):
    per = {t: [cells[(e, t)] for e in MODELS if e != t and (e, t) in cells] for t in targets}
    per = {t: v for t, v in per.items() if len(v) >= 8}
    between = st.pvariance([st.mean(v) for v in per.values()])
    within = st.mean([st.pvariance(v) for v in per.values()])
    return between / within


def main():
    J = load_cells(Path(os.environ.get("RUNS_UNANCHORED", DATA / "probe_J_20260529T005230Z")))
    K = load_cells(Path(os.environ.get("RUNS_GEN", DATA / "probe_K_20260529T014133Z")))
    rng = np.random.default_rng(SEED)

    fj, fk = fstat(J, MODELS), fstat(K, [m for m in MODELS if m != ANCHOR])
    print(f"F un-anchored = {fj:.3f}   F anchored = {fk:.3f}")
    assert round(fj, 2) == 0.33 and round(fk, 2) == 0.66, "F pair drifted from the manuscript"

    sj = lso_stats(J, MODELS, rng)
    sk = lso_stats(K, [m for m in MODELS if m != ANCHOR], rng)

    order = sorted(MODELS, key=lambda m: -sj[m][0])   # un-anchored ranking fixes band membership
    leading = set(order[:LEADING_N])

    fig, ax = plt.subplots(figsize=(7.0, 5.4))
    fig.patch.set_facecolor(SURFACE)
    ax.set_facecolor(SURFACE)
    XJ, XK = 0.0, 0.8

    for m in MODELS:
        lead = m in leading
        col = BLUE if lead else INK2
        yj = sj[m]
        if m in sk:
            yk = sk[m]
            ax.errorbar([XK], [yk[0]], yerr=[[yk[0] - yk[1]], [yk[2] - yk[0]]],
                        fmt="none", ecolor=BARC, elinewidth=1.0, capsize=2, zorder=3)
            ax.scatter([XK], [yk[0]], s=52, facecolor=col if lead else SURFACE,
                       edgecolor=col, linewidth=1.2, zorder=4)
        ax.errorbar([XJ], [yj[0]], yerr=[[yj[0] - yj[1]], [yj[2] - yj[0]]],
                    fmt="none", ecolor=BARC, elinewidth=1.0, capsize=2, zorder=3)
        ax.scatter([XJ], [yj[0]], s=52, facecolor=col if lead else SURFACE,
                   edgecolor=col, linewidth=1.2, zorder=4)

    # the anchor: a scored target on the left, the pinned reference on the right
    ax.scatter([XJ], [sj[ANCHOR][0]], marker="*", s=300, facecolor=ORANGE,
               edgecolor=SURFACE, linewidth=1.4, zorder=6)
    ax.scatter([XK], [7.0], marker="*", s=300, facecolor=ORANGE,
               edgecolor=SURFACE, linewidth=1.4, zorder=6)
    ax.annotate("anchor, pinned at 7", (XK, 7.0), textcoords="offset points",
                xytext=(14, -4), fontsize=9.5, color=INK2)

    # division band between leading eight and trailing four, per column
    for x, stats, targets in ((XJ, sj, MODELS), (XK, sk, [m for m in MODELS if m != ANCHOR])):
        lo = min(stats[m][0] for m in targets if m in leading)
        hi = max(stats[m][0] for m in targets if m not in leading)
        ax.plot([x - 0.06, x + 0.06], [(lo + hi) / 2, (lo + hi) / 2], color="#c5c3be",
                lw=0, marker=None)
        ax.fill_between([x - 0.09, x + 0.09], hi, lo, color="#eceae6", zorder=1)

    for x, f, lab in ((XJ, fj, "un-anchored"), (XK, fk, "anchored")):
        ax.text(x, 0.015, f"{lab}\nF = {f:.2f}", transform=ax.get_xaxis_transform(),
                ha="center", va="bottom", fontsize=10.5, color=INK)

    ax.set_xlim(-0.3, 1.35)
    ax.set_xticks([])
    ax.set_ylabel("overall score (1–10, leave-self-out mean, 95% CI)", color=INK, fontsize=10.5)
    ax.set_title("Anchoring decompresses the top of the field",
                 color=INK, fontsize=13, fontweight="bold", loc="left", pad=14)
    ax.text(0, 1.012, "shaded: the gap between the leading eight and the trailing four",
            transform=ax.transAxes, fontsize=9.5, color=INK2)
    for side in ("top", "right", "bottom"):
        ax.spines[side].set_visible(False)
    ax.spines["left"].set_color("#d5d3ce")
    ax.tick_params(colors=INK2)
    ax.grid(axis="y", color="#e7e6e2", lw=0.7)
    ax.set_axisbelow(True)

    out = HERE.parent / "figures" / "anchoring_resolution.png"
    out.parent.mkdir(exist_ok=True)
    fig.tight_layout()
    fig.savefig(out, dpi=200, facecolor=SURFACE)
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
