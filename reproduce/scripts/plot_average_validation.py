# PAPER figure — the combined factual rating  1/2 (E^F + G^F)  (X, anchored 1-10 scale,
# i.e. the factual half of the official total T, §4.7) vs self-administered GPQA Diamond
# accuracy (Y). Sibling of plot_external_validation.py / plot_generation_validation.py.
# Averaging the two key-free factual reads (judging E^F + making G^F) cancels their
# independent residuals and tracks the external capability better than either alone.
#
# Anchored E^F, G^F and their 95% CIs are read straight from the §4.2 table in the
# manuscript (the canonical published numbers); GPQA + binomial CI from the run CSV.
# The combined x-interval is the 95% joint (submission, archetype) bootstrap of
# 1/2(E^F+G^F) (combined_factual_bootstrap.py, A.5): one resample per replicate drives both
# components, so their covariance is captured rather than assumed.
#
# Usage:  python plot_average_validation.py  ->  figures/average_validation.png
"""Scatter: 1/2(E^F+G^F) vs GPQA Diamond accuracy (paper figure, small)."""
import csv
import re
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

HERE = Path(__file__).resolve().parent
DATA = HERE.parent / "data"
OUT = HERE.parent / "figures" / "average_validation.png"

SHORT = {"claude-opus-4.5": "opus-4.5", "claude-opus-4.1": "opus-4.1",
         "claude-opus-4.0": "opus-4.0", "claude-sonnet-4": "sonnet-4",
         "gemini-3.1-pro": "gemini-3.1-pro", "gemini-2.5-flash": "gemini-2.5-flash",
         "gpt-4.1-2025-04-14": "gpt-4.1", "gpt-4.1-mini": "gpt-4.1-mini",
         "gpt-4.1-nano": "gpt-4.1-nano", "gpt-4o": "gpt-4o",
         "gpt-4o-2024-08-06": "gpt-4o-0806", "gpt-4o-mini": "gpt-4o-mini"}

OFFS = {"gemini-3.1-pro": (-10, 11), "gemini-2.5-flash": (8, 14),
        "claude-opus-4.1": (12, 2), "claude-sonnet-4": (-10, 11),
        "claude-opus-4.0": (11, -13), "gpt-4.1-mini": (12, 8),
        "gpt-4.1-2025-04-14": (12, -10), "gpt-4o-2024-08-06": (13, 5),
        "gpt-4o": (-9, -13), "gpt-4.1-nano": (-9, 11), "gpt-4o-mini": (12, 6)}


def rd(p):
    return list(csv.DictReader([l for l in Path(p).read_text().splitlines()
                                if not l.lstrip().lstrip('"').startswith("#")]))


def pear(x, y):
    return float(np.corrcoef(x, y)[0, 1])


def avg_ranks(a):
    """Ranks, ties sharing their average rank -- the standard Spearman convention. Two models
    tie on GPQA accuracy, and ranking by argsort would split that tie arbitrarily instead."""
    a = np.asarray(a, float)
    order = np.argsort(a, kind="mergesort")
    r = np.empty(len(a), float)
    i = 0
    while i < len(a):
        j = i
        while j + 1 < len(a) and a[order[j + 1]] == a[order[i]]:
            j += 1
        r[order[i:j + 1]] = (i + j) / 2.0 + 1.0
        i = j + 1
    return r


def spear(x, y):
    return pear(avg_ranks(x), avg_ranks(y))


def pear_ci(x, y, n=10000, seed=20260613):
    rng = np.random.default_rng(seed); x, y = np.asarray(x), np.asarray(y); rs = []
    for _ in range(n):
        i = rng.integers(0, len(x), len(x))
        if x[i].std() > 1e-9 and y[i].std() > 1e-9:
            rs.append(pear(x[i], y[i]))
    return np.percentile(rs, 2.5), np.percentile(rs, 97.5)


def read_ef_gf():
    """Read the reproduced §4.2 Criterion-A table (E^F, G^F + CIs) from data/."""
    rows = {}
    for r in rd(DATA / "criterion_a_ef_gf.csv"):
        rows[r["model"]] = dict(ef=float(r["ef"]), ef_lo=float(r["ef_lo"]), ef_hi=float(r["ef_hi"]),
                                gf=float(r["gf"]), gf_lo=float(r["gf_lo"]), gf_hi=float(r["gf_hi"]))
    return rows


def read_joint():
    """95% joint bootstrap intervals of 1/2(E^F+G^F) (combined_factual_bootstrap.py, A.5)."""
    return {r["model"]: (float(r["lo95"]), float(r["hi95"]))
            for r in rd(DATA / "combined_factual_bootstrap.csv")}


tab = read_ef_gf()
joint = read_joint()
gpqa = {r["model"]: r for r in rd(DATA / "gpqa_selfadministered.csv")}
lb = {r["model"]: r for r in rd(DATA / "total_rating_leaderboard.csv")}
council = {m for m in lb if lb[m]["council"].strip().lower() == "yes"}


def gpqa_acc_ci(m):
    acc = float(gpqa[m]["gpqa_diamond_accuracy"]); n = float(gpqa[m]["n_total"])
    p = acc / 100.0
    return acc, 1.96 * (p * (1 - p) / n) ** 0.5 * 100.0


plt.rcParams.update({"font.size": 12, "axes.labelsize": 13,
                     "xtick.labelsize": 11, "ytick.labelsize": 11})

ms = sorted([m for m in tab if m in gpqa], key=lambda m: -gpqa_acc_ci(m)[0])
xs = np.array([(tab[m]["ef"] + tab[m]["gf"]) / 2 for m in ms])
ys = np.array([gpqa_acc_ci(m)[0] for m in ms])

# Anchor (claude-opus-4.5): combined rating = 7 by calibration — its E^F = 7 anchors its
# own measured loading f_a (the scale reference), G^F = 7 is the anchor reference. GPQA is measured and independent of the
# anchoring, so it is a legitimate point against GPQA and is included in the fit and stats.
ANCHOR = "claude-opus-4.5"
ax_x = 7.0
ax_y, ax_ye = gpqa_acc_ci(ANCHOR)
xf = np.append(xs, ax_x); yf = np.append(ys, ax_y)

fig, ax = plt.subplots(figsize=(6.6, 5.8))
b, a = np.polyfit(xf, yf, 1)
xl = np.linspace(xf.min(), xf.max(), 50)
ax.plot(xl, a + b * xl, color="0.55", lw=1.4, zorder=1)

for i, m in enumerate(ms):
    x, y = xs[i], ys[i]
    xlo, xhi = joint[m]
    xerr = [[max(0.0, x - xlo)], [max(0.0, xhi - x)]]
    yerr = gpqa_acc_ci(m)[1]
    ax.errorbar([x], [y], xerr=xerr, yerr=yerr, fmt="none",
                ecolor="#9bb8d4", elinewidth=1.2, capsize=2.5, zorder=2)
    co = m in council
    ax.scatter([x], [y], s=95, zorder=3,
               facecolor=("#1f4e79" if co else "white"),
               edgecolor="#1f4e79", linewidth=1.8)
    dx, dy = OFFS.get(m, (8, 6))
    ax.annotate(SHORT.get(m, m), (x, y), xytext=(dx, dy),
                textcoords="offset points", fontsize=11.5, color="#111",
                ha=("left" if dx >= 0 else "right"), va="center", zorder=4,
                arrowprops=dict(arrowstyle="-", color="0.55", lw=0.7,
                                shrinkA=0, shrinkB=4))

r, rho = pear(xf, yf), spear(xf, yf)
clo, chi = pear_ci(xf, yf)
ax.text(0.03, 0.97, f"Pearson $r$ = {r:.2f}  [{clo:.2f}, {chi:.2f}]\n"
        f"Spearman $\\rho$ = {rho:.2f}   ($n$ = {len(xf)})",
        transform=ax.transAxes, va="top", ha="left", fontsize=12,
        bbox=dict(boxstyle="round,pad=0.4", fc="white", ec="0.8"))

# Anchor (opus-4.5) drawn as a blue star — it is included in the fit/stats above.
# x = 7 is exact by calibration, so no x error bar; y is its measured GPQA with binomial CI.
ax.errorbar([ax_x], [ax_y], yerr=ax_ye, fmt="none",
            ecolor="#9bb8d4", elinewidth=1.2, capsize=2.5, zorder=3)
ax.scatter([ax_x], [ax_y], s=230, marker="*", facecolor="#1f4e79",
           edgecolor="#1f4e79", linewidth=1.0, zorder=5)
ax.annotate("opus-4.5", (ax_x, ax_y), xytext=(11, -9),
            textcoords="offset points", fontsize=11.5, color="#1f4e79",
            ha="left", va="center", zorder=5)

leg = [Line2D([0], [0], marker="o", color="w", markerfacecolor="#1f4e79",
              markeredgecolor="#1f4e79", markersize=10, label="council"),
       Line2D([0], [0], marker="o", color="w", markerfacecolor="white",
              markeredgecolor="#1f4e79", markersize=10, label="non-council"),
       Line2D([0], [0], marker="*", color="w", markerfacecolor="#1f4e79",
              markeredgecolor="#1f4e79", markersize=16, label="anchor (opus-4.5)")]
ax.legend(handles=leg, loc="lower right", fontsize=11, frameon=True)

ax.set_xlabel(r"Combined factual rating  $\frac{1}{2}(E^{F}+G^{F})$  (anchored; bars = 95% CI)")
ax.set_ylabel("GPQA Diamond accuracy (%)  (bars = 95% CI)")
ax.margins(0.13)
ax.grid(alpha=0.25)
fig.tight_layout()
OUT.parent.mkdir(parents=True, exist_ok=True)
fig.savefig(OUT, dpi=200, bbox_inches="tight")
print("wrote", OUT)
print(f"1/2(E^F+G^F) vs GPQA: Pearson r = {r:.3f} [{clo:.2f}, {chi:.2f}], Spearman rho = {rho:.3f}, n = {len(xf)} (incl. opus-4.5 anchor)")
