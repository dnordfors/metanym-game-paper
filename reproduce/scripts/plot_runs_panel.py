#!/usr/bin/env python3
"""Appendix panel: row 1 the three runs' council-basis T against GPQA with each run's twelve-evaluator
sigma1/sigma2; row 2 pooled runs 1+2 (left) and pooled three (right)."""
import sys, csv
from pathlib import Path
import numpy as np, matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
from scipy.stats import pearsonr, spearmanr
sys.path.insert(0, str(Path(__file__).resolve().parent))
import pooled_components as PC
from pooled_components import MODELS, COUNCIL, PKG
HERE = Path(__file__).resolve().parent.parent
rd = lambda p: {r["model"]: r for r in csv.DictReader([l for l in open(p) if not l.lstrip('"').startswith("#")])}
G = rd(PKG / "data/gpqa_selfadministered.csv"); runs = rd(PKG / "data/total_rating_runs.csv")
gap = {r: PC.components(PC.load_runs([r]), *(lambda GAs: (PC.graded_targets(GAs), PC.scoring_atoms(GAs, PC.graded_targets(GAs))))(PC.load_runs([r])), MODELS)["gap"] for r in (1, 2, 3)}
pooled = {k: rd(HERE / f"data/total_rating_council_{k}.csv") for k in ("pooled12", "pooled123")}   # HERE = the package root
short = lambda m: m.replace("claude-", "").replace("-2025-04-14", "").replace("-2024-08-06", " (08-06)")
x = np.array([float(G[m]["gpqa_diamond_accuracy"]) for m in MODELS])
def panel(a, y, title):
    for m, xx, yy in zip(MODELS, x, y):
        a.scatter(xx, yy, s=90 if m in COUNCIL else 45, marker="*" if m in COUNCIL else "o", color="tab:red" if m in COUNCIL else "tab:blue", zorder=3)
        a.annotate(short(m), (xx, yy), fontsize=7.5, xytext=(4, 3), textcoords="offset points")
    a.set_title(f"{title}\nPearson r = {pearsonr(x, y)[0]:.2f}, Spearman ρ = {spearmanr(x, y)[0]:.2f}", fontsize=10)
    a.set_xlabel("GPQA Diamond accuracy (%)"); a.grid(alpha=.3); a.set_ylim(1.2, 8.6)
fig, ax = plt.subplots(2, 3, figsize=(15, 9.6))
for j, r in enumerate((1, 2, 3)):
    panel(ax[0, j], np.array([float(runs[m][f"T_run{r}"]) for m in MODELS]), f"run {r}: total $T$   (σ₁/σ₂ = {gap[r]:.2f})")
panel(ax[1, 0], np.array([float(pooled["pooled12"][m]["T"]) for m in MODELS]), "runs 1 and 2 pooled: total $T$")
panel(ax[1, 1], np.array([float(pooled["pooled123"][m]["T"]) for m in MODELS]), "three runs pooled: total $T$")
ax[1, 2].axis("off")
ax[0, 0].set_ylabel("total $T$ (council basis)"); ax[1, 0].set_ylabel("total $T$ (council basis)")
ax[0, 0].plot([], [], "r*", ms=10, label="council seat"); ax[0, 0].plot([], [], "bo", label="other"); ax[0, 0].legend(loc="upper left", fontsize=8)
fig.tight_layout(); out = HERE / "figures/runs_panel.png"; fig.savefig(out, dpi=160); print(out)
