"""Figure 2 of the ICLR 2027 version: total rating T (council basis) vs self-administered GPQA
Diamond accuracy, in the plain style David prefers, with the information the paper figure carries:
council seats filled / non-council open / anchor as a star, all twelve models labelled, and the
r, its BCa interval, Spearman rho and n in the corner.

Provenance: reads the sibling package's pinned data (metanym-game-paper/reproduce/data/
total_rating_council.csv, gpqa_selfadministered.csv) — the same inputs as
metanym-game-paper/reproduce/scripts/plot_total_validation.py, which produced the arXiv figure.
The r interval [{RCI}] is the BCa bootstrap interval of Appendix D.1 (not recomputed here).
Writes metanym-game-paper-iclr27/submission/figures/total_validation_simple.png.
Run with the metanym-game conda env (numpy, matplotlib).
"""
import csv
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
DATA = HERE.parent / "data"; PKGD = DATA; import os; TAG = os.environ.get("TAG", "pooled123"); RCI = os.environ.get("RCI", "?")
OUT = HERE.parent / "figures" / f"total_validation_simple_{TAG}.png"   # copied into metanym-game-paper-iclr27/submission/figures/total_validation_simple.png
SHORT = {"claude-opus-4.5": "opus-4.5", "claude-opus-4.1": "opus-4.1", "claude-opus-4.0": "opus-4.0",
         "claude-sonnet-4": "sonnet-4", "gemini-3.1-pro": "gemini-3.1-pro", "gemini-2.5-flash": "gemini-2.5-flash",
         "gpt-4.1-2025-04-14": "gpt-4.1", "gpt-4.1-mini": "gpt-4.1-mini", "gpt-4.1-nano": "gpt-4.1-nano",
         "gpt-4o": "gpt-4o", "gpt-4o-2024-08-06": "gpt-4o-0806", "gpt-4o-mini": "gpt-4o-mini"}
# label offsets in points (dx, dy), chosen by hand so no label crosses a marker or a bar
OFF = {"opus-4.5": (10, -4), "gemini-3.1-pro": (-8, 12), "opus-4.1": (-70, 10), "gemini-2.5-flash": (-108, -16),
       "opus-4.0": (12, -14), "sonnet-4": (12, 6), "gpt-4.1-mini": (10, -12), "gpt-4.1": (-48, 12),
       "gpt-4.1-nano": (12, 2), "gpt-4o": (-50, 10), "gpt-4o-0806": (12, -10), "gpt-4o-mini": (8, -14)}

def rd(p):
    return list(csv.DictReader([l for l in Path(p).read_text().splitlines() if not l.lstrip().lstrip('"').startswith("#")]))

council = {r["model"]: r for r in rd(DATA / f"total_rating_council_{TAG}.csv")}
gpqa = {r["model"]: r for r in rd(PKGD / "gpqa_selfadministered.csv")}
ms = [m for m in council if m in gpqa]
assert len(ms) == 12, ms
x = np.array([float(council[m]["T"]) for m in ms]); y = np.array([float(gpqa[m]["gpqa_diamond_accuracy"]) for m in ms])
r = float(np.corrcoef(x, y)[0, 1])
def rank(a):  # average ranks for ties, as in the sibling's plot script (two models share 72.22 on GPQA)
    a = np.asarray(a, float); r = np.empty(len(a)); order = np.argsort(a, kind='mergesort'); i = 0
    while i < len(a):
        j = i
        while j + 1 < len(a) and a[order[j + 1]] == a[order[i]]: j += 1
        r[order[i:j + 1]] = (i + j) / 2.0 + 1.0; i = j + 1
    return r
rho = float(np.corrcoef(rank(x), rank(y))[0, 1])
print(f"r={r:.3f} rho={rho:.3f}")

BLUE, GREY, INK = "#2f6fd6", "#9a9a9a", "#222222"
fig, ax = plt.subplots(figsize=(6.2, 6.2), dpi=200)
ax.set_facecolor("#fbfbfb"); ax.grid(True, color="#e6e6e6", lw=0.8); ax.set_axisbelow(True)
for s in ("top", "right"): ax.spines[s].set_visible(False)
sl, ic = np.polyfit(x, y, 1); xx = np.linspace(x.min() - 0.25, x.max() + 0.25, 50)
ax.plot(xx, sl * xx + ic, color=GREY, lw=1.6, zorder=1)
for m in ms:
    xi, yi = float(council[m]["T"]), float(gpqa[m]["gpqa_diamond_accuracy"])
    n, k = int(gpqa[m]["n_total"]), int(gpqa[m]["n_correct"]); p = k / n; z = 1.96      # Wilson 95% CI
    c = (p + z*z/(2*n)) / (1 + z*z/n); h = z * np.sqrt(p*(1-p)/n + z*z/(4*n*n)) / (1 + z*z/n)
    ax.errorbar(xi, yi, xerr=[[xi - float(council[m]["T_lo95"])], [float(council[m]["T_hi95"]) - xi]],
                yerr=[[yi - 100*(c-h)], [100*(c+h) - yi]], fmt="none", ecolor="#b9b9c4", elinewidth=1.1, capsize=3, zorder=2)
    seat = council[m]["council"] == "yes"
    if m == "claude-opus-4.5":
        ax.plot(xi, yi, marker="*", ms=17, mfc="#f28c28", mec="#f28c28", ls="", zorder=4)
    else:
        ax.plot(xi, yi, marker="o", ms=11, mfc=BLUE if seat else "white", mec=BLUE, mew=2, ls="", zorder=3)
    dx, dy = OFF[SHORT[m]]
    ax.annotate(SHORT[m], (xi, yi), xytext=(dx, dy), textcoords="offset points", fontsize=10.5, color=INK, zorder=5)
ax.text(0.04, 0.96, rf"$r = {r:.2f}$  [{RCI}]" + "\n" + rf"$\rho = {rho:.2f}$,  $n = 12$", transform=ax.transAxes,
        fontsize=17, va="top", ha="left", color=INK, linespacing=1.4)
ax.plot([], [], "o", mfc=BLUE, mec=BLUE, ms=9, label="council seat"); ax.plot([], [], "o", mfc="white", mec=BLUE, mew=2, ms=9, label="non-council")
ax.plot([], [], "*", mfc="#f28c28", mec="#f28c28", ms=14, label="anchor ($T=7$ by calibration)")
ax.legend(loc="lower right", frameon=False, fontsize=10.5)
ax.set_xlabel("Metanym Game Benchmark  $T$", fontsize=15); ax.set_ylabel("GPQA Diamond Benchmark  (%)", fontsize=15)
ax.tick_params(labelsize=11.5)
fig.tight_layout(); OUT.parent.mkdir(parents=True, exist_ok=True); fig.savefig(OUT); print("wrote", OUT, f"r={r:.3f} rho={rho:.3f}")
