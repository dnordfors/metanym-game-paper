# PAPER figure — the official total rating T (§4.7, council basis, x) vs self-administered
# GPQA Diamond accuracy (y). Successor of the v1 combined-factual figure (plot_average_validation.py, retired)
# figure; the factual pair's correlations remain in Appendix D.1, this figure carries the
# total. Horizontal bars are the per-contest A.5 joint bootstrap 95% CI on T
# (data/total_rating_council.csv); vertical bars the GPQA binomial 95% CI. The r interval
# in the title is Fisher-z (see pear_ci docstring).
#
# Usage:  python plot_total_validation.py  ->  figures/total_validation.png
"""Scatter: total rating T vs GPQA Diamond accuracy (paper figure)."""
import csv
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

HERE = Path(__file__).resolve().parent
DATA = HERE.parent / "data"
OUT = HERE.parent / "figures" / "total_validation.png"

SHORT = {"claude-opus-4.5": "opus-4.5", "claude-opus-4.1": "opus-4.1",
         "claude-opus-4.0": "opus-4.0", "claude-sonnet-4": "sonnet-4",
         "gemini-3.1-pro": "gemini-3.1-pro", "gemini-2.5-flash": "gemini-2.5-flash",
         "gpt-4.1-2025-04-14": "gpt-4.1", "gpt-4.1-mini": "gpt-4.1-mini",
         "gpt-4.1-nano": "gpt-4.1-nano", "gpt-4o": "gpt-4o",
         "gpt-4o-2024-08-06": "gpt-4o-0806", "gpt-4o-mini": "gpt-4o-mini"}


def rd(p):
    return list(csv.DictReader([l for l in Path(p).read_text().splitlines()
                                if not l.lstrip().lstrip('"').startswith("#")]))


def pear(x, y):
    return float(np.corrcoef(x, y)[0, 1])


def avg_ranks(a):
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


def pear_ci(x, y):
    """Fisher-z 95% interval. The naive percentile pairs-bootstrap undercovers for a
    bounded statistic at n=12 and is retired; the BCa companion interval is reported in
    Appendix D.1 (they agree on T: [0.90,0.99] vs [0.92,0.99])."""
    r = pear(np.asarray(x), np.asarray(y))
    z, se = np.arctanh(r), 1 / np.sqrt(len(x) - 3)
    return np.tanh(z - 1.96 * se), np.tanh(z + 1.96 * se)


council_csv = {r["model"]: r for r in rd(DATA / "total_rating_council.csv")}
gpqa = {r["model"]: r for r in rd(DATA / "gpqa_selfadministered.csv")}

ANCHOR = "claude-opus-4.5"
ms = [m for m in council_csv if m in gpqa]
xs = np.array([float(council_csv[m]["T"]) for m in ms])
ys = np.array([float(gpqa[m]["gpqa_diamond_accuracy"]) for m in ms])
r = pear(xs, ys)
rho = pear(avg_ranks(xs), avg_ranks(ys))
lo, hi = pear_ci(xs, ys)

BLUE, ORANGE = "#2a78d6", "#eb6834"        # validated categorical pair (dataviz palette)
SURFACE, INK, INK2 = "#fcfcfb", "#0b0b0b", "#52514e"
GRID, BARC, LEADER = "#e7e6e2", "#c9ccd1", "#b5b3ae"

fig, ax = plt.subplots(figsize=(8.4, 5.8))
fig.patch.set_facecolor(SURFACE)
ax.set_facecolor(SURFACE)
LABEL_PTS = []
for m in ms:
    x, y = float(council_csv[m]["T"]), float(gpqa[m]["gpqa_diamond_accuracy"])
    n = float(gpqa[m]["n_total"])
    p = y / 100.0
    ye = 1.96 * (p * (1 - p) / n) ** 0.5 * 100.0
    seat = council_csv[m]["council"] == "yes"
    if m == ANCHOR:
        ax.errorbar([x], [y], yerr=[[ye], [ye]], fmt="none", ecolor=BARC,
                    elinewidth=1.0, capsize=2, zorder=3)
        ax.scatter([x], [y], marker="*", s=320, facecolor=ORANGE,
                   edgecolor=SURFACE, linewidth=1.6, zorder=6)
    else:
        xlo, xhi = float(council_csv[m]["T_lo95"]), float(council_csv[m]["T_hi95"])
        xerr = [[max(0.0, x - xlo)], [max(0.0, xhi - x)]]
        ax.errorbar([x], [y], xerr=xerr, yerr=[[ye], [ye]], fmt="none",
                    ecolor=BARC, elinewidth=0.9, capsize=2, zorder=3)
        ax.scatter([x], [y], s=86, zorder=5,
                   facecolor=BLUE if seat else SURFACE,
                   edgecolor=BLUE if seat else BLUE,
                   linewidth=2.0)
        ax.scatter([x], [y], s=150, zorder=4, facecolor=SURFACE,
                   edgecolor=SURFACE, linewidth=0)   # 2px surface ring
    LABEL_PTS.append((m, x, y))

b, cov = np.polyfit(xs, ys, 1, cov=True)
xx = np.linspace(xs.min() - 0.25, xs.max() + 0.25, 60)
yy = np.polyval(b, xx)
resid = ys - np.polyval(b, xs)
se2 = (resid @ resid) / (len(xs) - 2)
xbar = xs.mean()
band = 2.228 * np.sqrt(se2 * (1 / len(xs) + (xx - xbar) ** 2 / ((xs - xbar) ** 2).sum()))
ax.fill_between(xx, yy - band, yy + band, color="#eceae6", zorder=1)
ax.plot(xx, yy, lw=1.1, color="#c5c3be", zorder=2)
ax.set_xlabel(r"Metanym Game Benchmark  $T=\frac{1}{4}(G^F+G^C+E^F+E^C)$  (anchored, council basis)",
              color=INK, fontsize=11.5)
ax.set_ylabel("GPQA Diamond accuracy (%)", color=INK, fontsize=11.5)
ax.set_title("The key-free Metanym Game rating tracks GPQA Diamond",
             color=INK, fontsize=13.5, fontweight="bold", pad=26, loc="left")
ax.text(0, 1.035, rf"Pearson $r = {r:.2f}$ [Fisher-z 95% {lo:.2f}–{hi:.2f}]  ·  Spearman $\rho = {rho:.2f}$  ·  $n = {len(ms)}$  ·  no answer key on the $x$ axis",
        transform=ax.transAxes, fontsize=10, color=INK2)
for side in ("top", "right"):
    ax.spines[side].set_visible(False)
for side in ("left", "bottom"):
    ax.spines[side].set_color("#d5d3ce")
ax.tick_params(colors=INK2, labelsize=10)
leg = [Line2D([], [], marker="o", ls="", mfc=BLUE, mec=BLUE, ms=9, label="council seat"),
       Line2D([], [], marker="o", ls="", mfc=SURFACE, mec=BLUE, mew=2, ms=9, label="non-council"),
       Line2D([], [], marker="*", ls="", mfc=ORANGE, mec=ORANGE, ms=14, label="anchor (T = 7 by calibration)")]
lg = ax.legend(handles=leg, loc="lower right", fontsize=9.5, frameon=True,
               facecolor=SURFACE, edgecolor="#d5d3ce", labelcolor=INK)
ax.grid(color=GRID, linewidth=0.8)
ax.set_axisbelow(True)

# --- automatic label placement: deterministic greedy, collision-aware, leader lines ----
# Works in display points after fixing the layout. A label candidate is rejected if its
# text box would overlap any marker, any error-bar span, an already-placed label, or the
# axes edge; among survivors the closest ring position wins. No external dependencies.
fig.canvas.draw()
trans = ax.transData.transform
inv = ax.transData.inverted().transform
pts_disp = {m: trans((x, y)) for m, x, y in LABEL_PTS}
# obstacle boxes: markers (padded) and x-error spans
obstacles = []
for m, x, y in LABEL_PTS:
    px, py = pts_disp[m]
    obstacles.append((px - 8, py - 8, px + 8, py + 8))
    row = council_csv[m]
    if m != ANCHOR:
        lx = trans((float(row["T_lo95"]), y))[0]
        hx = trans((float(row["T_hi95"]), y))[0]
        obstacles.append((lx, py - 4, hx, py + 4))


def overlaps(b, boxes):
    return any(not (b[2] < o[0] or b[0] > o[2] or b[3] < o[1] or b[1] > o[3])
               for o in boxes)


x0, y0_, x1, y1_ = ax.get_window_extent().extents
placed = []
order = sorted(LABEL_PTS, key=lambda t: -sum(  # most crowded first
    1 for n, a, b in LABEL_PTS if n != t[0]
    and abs(pts_disp[n][0] - pts_disp[t[0]][0]) < 60
    and abs(pts_disp[n][1] - pts_disp[t[0]][1]) < 40))
import math
FORCE = {"gemini-2.5-flash": (160, 62),        # (angle deg, radius pts)
         "claude-opus-4.0": (305, 52)}
for m, x, y in order:
    label = SHORT[m]
    w, h = 5.4 * len(label) + 4, 13
    px, py = pts_disp[m]
    best = None
    if m in FORCE:                              # authored placement: exact, unvalidated
        fa, fr = FORCE[m]
        a = math.radians(fa)
        best = (px + fr * math.cos(a), py + fr * math.sin(a), fr)
    ring = [(radius, ang) for radius in (16, 26, 38, 52, 68)
            for ang in (90, 45, 135, 0, 180, 315, 225, 270)]
    for radius, ang in ring:
        if best:
            break
        if True:
            a = math.radians(ang)
            cx, cy = px + radius * math.cos(a), py + radius * math.sin(a)
            box = (cx - w / 2, cy - h / 2, cx + w / 2, cy + h / 2)
            if box[0] < x0 + 2 or box[2] > x1 - 2 or box[1] < y0_ + 2 or box[3] > y1_ - 2:
                continue
            pad = (box[0] - 6, box[1] - 4, box[2] + 6, box[3] + 4)
            if overlaps(box, obstacles) or overlaps(pad, placed):
                continue
            best = (cx, cy, radius)
            break
    if best is None:
        best = (px + 70, py + 40, 80)          # fail loudly visible: far offset
    cx, cy, radius = best
    placed.append((cx - w / 2, cy - h / 2, cx + w / 2, cy + h / 2))
    dx_d, dy_d = inv((cx, cy)) - np.array([x, y])
    ax.annotate(label, (x, y), xytext=(x + dx_d, y + dy_d), fontsize=9.5,
                ha="center", va="center",
                color=INK, arrowprops=dict(arrowstyle="-", lw=0.8, color=LEADER,
                                shrinkA=0, shrinkB=6))

fig.tight_layout()
OUT.parent.mkdir(exist_ok=True)
fig.savefig(OUT, dpi=220, facecolor=SURFACE)
print(f"wrote {OUT}")
print(f"T vs GPQA: Pearson r = {r:.3f} [{lo:.2f}, {hi:.2f}], Spearman rho = {rho:.3f}, n = {len(ms)}")
