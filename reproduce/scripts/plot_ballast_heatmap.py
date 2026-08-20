#!/usr/bin/env python3
"""§4.6 exhibit — the ballast repairs the contest's factual axis.

Heatmap: each seat's anchored E^F under contests at ballast 0/1/2/3 (mean over the
seven possible contestants) beside the twelve-evaluator reference of §4.2. Matching
column shading shows convergence without reading the numbers; the adopted
configuration (two ballast) carries a heavy border.

Values recomputed live via ballast_sizing.py's own build/ef (no hand-typed numbers).
Run with the paper's environment: RUNS_GEN defaults as in ballast_sizing.py.
"""
import os, sys, statistics as st
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))  # run from reproduce/

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import ballast_sizing as bs

OUT = Path("figures/ballast_heatmap.png")

R, by, targets = bs.build(Path(os.environ.get("RUNS_GEN", "data/probe_K_20260529T014133Z")))
council_t = [m for m in bs.COUNCIL if m in targets]
contestants = [m for m in bs.MODELS if m not in bs.COUNCIL]
pool = sorted([m for m in targets if m not in bs.COUNCIL],
              key=lambda t: float(np.nanmean(R[:, by[t]])))
ref, _ = bs.ef(R, list(range(R.shape[1])), bs.MODELS)

def cols_for(ts):
    out = []
    for t in ts:
        out += list(by[t])
    return out

means, swings = {}, {}
for n in range(4):
    base = council_t + [b for b in pool[:n] if b not in council_t]
    per = {m: [] for m in bs.COUNCIL}
    for c in contestants:
        v, _ = bs.ef(R, cols_for(base + ([c] if c not in base else [])), bs.COUNCIL + [c])
        for m in bs.COUNCIL:
            per[m].append(v[m])
    means[n] = {m: st.mean(x) for m, x in per.items()}
    swings[n] = {m: max(x) - min(x) for m, x in per.items()}

seats = sorted(bs.COUNCIL, key=lambda m: -ref[m])          # by twelve-evaluator E^F
cols = ["council\nalone", "+1 ballast", "+2 ballast", "+3 ballast",
        "all 12 participants\n(§4.2)"]
M = np.array([[means[n][m] for n in range(4)] + [ref[m]] for m in seats])

DISPLAY = {"claude-opus-4.5": "claude-opus-4.5 ★", "gemini-3.1-pro": "gemini-3.1-pro",
           "claude-opus-4.0": "claude-opus-4.0", "claude-opus-4.1": "claude-opus-4.1",
           "gemini-2.5-flash": "gemini-2.5-flash"}

fig, ax = plt.subplots(figsize=(6.5, 2.9), dpi=300)
im = ax.imshow(M, cmap="Oranges", vmin=0, vmax=8.5, aspect="auto")
for i in range(M.shape[0]):
    for j in range(M.shape[1]):
        dark = M[i, j] > 5.2
        ax.text(j, i, f"{M[i, j]:.1f}", ha="center", va="center",
                fontsize=10, color="white" if dark else "#1a1a1a",
                fontweight="bold")
ax.set_xticks(range(len(cols)))
ax.set_xticklabels(cols, fontsize=8.5)
ax.set_yticks(range(len(seats)))
ax.set_yticklabels([DISPLAY[m] for m in seats], fontsize=8.5)
ax.tick_params(length=0)
for s in ax.spines.values():
    s.set_visible(False)
# thin white grid between cells
ax.set_xticks(np.arange(-.5, len(cols)), minor=True)
ax.set_yticks(np.arange(-.5, len(seats)), minor=True)
ax.grid(which="minor", color="white", linewidth=1.5)
ax.tick_params(which="minor", length=0)
# 2pt border around the adopted configuration (+2 ballast)
ax.add_patch(Rectangle((2 - .5, -.5), 1, len(seats), fill=False,
                       edgecolor="#1a1a1a", linewidth=2, zorder=5, clip_on=False))
ax.set_title("Seat evaluator factual competence $E^F$ (anchored) by contest composition",
             fontsize=9.5, pad=10)
fig.tight_layout()
fig.savefig(OUT, bbox_inches="tight", facecolor="white")
print("wrote", OUT)
print("worst council-alone swing over the seven contestants:",
      round(max(swings[0].values()), 2))
print("fidelity |E^F - twelve| at two ballast:",
      round(st.mean(abs(means[2][m] - ref[m]) for m in bs.COUNCIL), 2))
