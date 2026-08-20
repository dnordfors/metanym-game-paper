#!/usr/bin/env python3
"""Appendix D.4 figure — publicly reported GPQA Diamond (typically reasoning-on)
vs this protocol's self-administered accuracy (T=0, reasoning off), per model.

A smooth monotone relation between the two administrations is what corroborates
the self-administered numbers; the offset is the reasoning budget. Only models
with a citable public value are plotted (external_benchmarks.csv sourcing rule).

Run from reproduce/:  python3 scripts/plot_gpqa_public_vs_measured.py
Writes figures/gpqa_public_vs_measured.png and prints the correlations.
"""
import csv
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy.stats import pearsonr, spearmanr

pub = {}
with open("data/external_benchmarks.csv") as fh:
    for row in csv.DictReader(l for l in fh if not l.startswith("#")):
        if row["gpqa_diamond"].strip():
            pub[row["model"]] = float(row["gpqa_diamond"])
meas = {}
with open("data/gpqa_selfadministered.csv") as fh:
    for row in csv.DictReader(l for l in fh if not l.startswith('"#')):
        meas[row["model"]] = float(row["gpqa_diamond_accuracy"])

models = sorted(set(pub) & set(meas), key=lambda m: meas[m])
x = np.array([meas[m] for m in models])
y = np.array([pub[m] for m in models])
r, _ = pearsonr(x, y)
rho, _ = spearmanr(x, y)
print(f"n={len(models)}  Pearson r={r:.2f}  Spearman rho={rho:.2f}")
for m in models:
    print(f"  {m:24} measured {meas[m]:5.1f}   public {pub[m]:5.1f}")

fig, ax = plt.subplots(figsize=(5.4, 4.2), dpi=300)
ax.scatter(x, y, s=48, color="#2a78d6", zorder=3)
lo = min(x.min(), y.min()) - 4
hi = max(x.max(), y.max()) + 4
ax.plot([lo, hi], [lo, hi], ls=":", color="#c9ccd1", lw=1, label="y = x")
OFFSETS = {"claude-opus-4.5": (-6, -11), "gemini-3.1-pro": (6, 3)}
for m in models:
    dx, dy = OFFSETS.get(m, (6, -3))
    ax.annotate(m.replace("-2024-08-06", "").replace("-2025-04-14", ""),
                (meas[m], pub[m]), textcoords="offset points", xytext=(dx, dy),
                ha="right" if dx < 0 else "left", fontsize=7, color="#52514e")
ax.set_xlabel("self-administered GPQA Diamond, % (T=0, reasoning off)")
ax.set_ylabel("publicly reported GPQA Diamond, %")
ax.set_title(f"Two administrations of the same test  (n={len(models)}, "
             f"r={r:.2f}, ρ={rho:.2f})", fontsize=10)
ax.set_xlim(lo, hi); ax.set_ylim(lo, hi)
ax.legend(frameon=False, fontsize=8, loc="lower right")
for sp in ("top", "right"):
    ax.spines[sp].set_visible(False)
fig.tight_layout()
fig.savefig("figures/gpqa_public_vs_measured.png", facecolor="white", bbox_inches="tight")
print("wrote figures/gpqa_public_vs_measured.png")
