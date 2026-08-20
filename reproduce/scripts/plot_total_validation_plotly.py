# Interactive companion to plot_total_validation.py — same data, plotly rendering.
# supplementary: interactive companion figure; not part of the deterministic reproduce run
# Outputs BOTH figures/total_validation_plotly.html (hover cards: T with CI, all four
# components, GPQA with binomial CI, council status) and .png (static, via kaleido).
# Not part of reproduce.sh: the paper figure remains the matplotlib PNG; this is the
# interactive form (and a candidate for the archetypes.ai leaderboard drill-down style).
"""Interactive scatter: total rating T vs GPQA Diamond (plotly)."""
import csv
from pathlib import Path

import numpy as np
import plotly.graph_objects as go

HERE = Path(__file__).resolve().parent
DATA = HERE.parent / "data"
OUT = HERE.parent / "figures"

SHORT = {"claude-opus-4.5": "opus-4.5", "claude-opus-4.1": "opus-4.1",
         "claude-opus-4.0": "opus-4.0", "claude-sonnet-4": "sonnet-4",
         "gemini-3.1-pro": "gemini-3.1-pro", "gemini-2.5-flash": "gemini-2.5-flash",
         "gpt-4.1-2025-04-14": "gpt-4.1", "gpt-4.1-mini": "gpt-4.1-mini",
         "gpt-4.1-nano": "gpt-4.1-nano", "gpt-4o": "gpt-4o",
         "gpt-4o-2024-08-06": "gpt-4o-0806", "gpt-4o-mini": "gpt-4o-mini"}
# annotation offsets in pixels (ax right+, ay down+)
OFFS = {"gemini-3.1-pro": (-58, -22), "gemini-2.5-flash": (-88, 40),
        "claude-opus-4.1": (-52, -22), "claude-sonnet-4": (-40, 34),
        "claude-opus-4.0": (46, 20), "gpt-4.1-mini": (-8, -30),
        "gpt-4.1-2025-04-14": (-6, 34), "gpt-4o-2024-08-06": (28, 26),
        "gpt-4o": (-34, -24), "gpt-4.1-nano": (-40, -26), "gpt-4o-mini": (0, -30),
        "claude-opus-4.5": (16, 30)}
ANCHOR = "claude-opus-4.5"


def rd(p):
    return list(csv.DictReader([l for l in Path(p).read_text().splitlines()
                                if not l.lstrip().lstrip('"').startswith("#")]))


council = {r["model"]: r for r in rd(DATA / "total_rating_council.csv")}
gpqa = {r["model"]: r for r in rd(DATA / "gpqa_selfadministered.csv")}
ms = [m for m in council if m in gpqa]

xs = np.array([float(council[m]["T"]) for m in ms])
ys = np.array([float(gpqa[m]["gpqa_diamond_accuracy"]) for m in ms])
r = float(np.corrcoef(xs, ys)[0, 1])
z, se = np.arctanh(r), 1 / np.sqrt(len(ms) - 3)
lo, hi = np.tanh(z - 1.96 * se), np.tanh(z + 1.96 * se)
def rk(a):                                   # tie-averaged ranks (Spearman convention)
    a = np.asarray(a, float)
    order = np.argsort(a, kind="mergesort")
    r_ = np.empty(len(a)); i = 0
    while i < len(a):
        j = i
        while j + 1 < len(a) and a[order[j + 1]] == a[order[i]]:
            j += 1
        r_[order[i:j + 1]] = (i + j) / 2 + 1; i = j + 1
    return r_
rho = float(np.corrcoef(rk(xs), rk(ys))[0, 1])

fig = go.Figure()
xx = np.linspace(xs.min() - 0.25, xs.max() + 0.25, 20)
b = np.polyfit(xs, ys, 1)
fig.add_trace(go.Scatter(x=xx, y=np.polyval(b, xx), mode="lines",
                         line=dict(color="#d5d9de", width=1.2),
                         hoverinfo="skip", showlegend=False))

groups = {"council seat": dict(symbol="circle", color="#2a78d6", line=None),
          "non-council": dict(symbol="circle-open", color="#2a78d6", line=None),
          "anchor (T=7 by calibration)": dict(symbol="star", color="#eb6834", line=None)}
for label, style in groups.items():
    sel = [m for m in ms if
           (m == ANCHOR) == (label.startswith("anchor")) and
           (label != "council seat" or (council[m]["council"] == "yes" and m != ANCHOR)) and
           (label != "non-council" or council[m]["council"] == "no")]
    if not sel:
        continue
    hover = []
    for m in sel:
        c = council[m]
        n = float(gpqa[m]["n_total"])
        p = float(gpqa[m]["gpqa_diamond_accuracy"]) / 100
        ye = 1.96 * (p * (1 - p) / n) ** 0.5 * 100
        hover.append(
            f"<b>{m}</b><br>"
            f"T = {float(c['T']):.2f}  [{float(c['T_lo95']):.2f}, {float(c['T_hi95']):.2f}]<br>"
            f"G<sup>F</sup> {float(c['GF']):.2f}   G<sup>C</sup> {float(c['GC']):.2f}   "
            f"E<sup>F</sup> {float(c['EF']):.2f}   E<sup>C</sup> {float(c['EC']):.2f}<br>"
            f"GPQA Diamond {float(gpqa[m]['gpqa_diamond_accuracy']):.2f}% ± {ye:.1f} "
            f"({gpqa[m]['n_correct']}/{int(n)})<br>"
            f"{'council seat' if c['council'] == 'yes' else 'non-council'}"
            f"{' · anchor' if m == ANCHOR else ''}")
    fig.add_trace(go.Scatter(
        x=[float(council[m]["T"]) for m in sel],
        y=[float(gpqa[m]["gpqa_diamond_accuracy"]) for m in sel],
        error_x=dict(type="data", symmetric=False,
                     array=[float(council[m]["T_hi95"]) - float(council[m]["T"]) for m in sel],
                     arrayminus=[float(council[m]["T"]) - float(council[m]["T_lo95"]) for m in sel],
                     color="#aab1b9", thickness=1),
        error_y=dict(type="data",
                     array=[1.96 * ((float(gpqa[m]["gpqa_diamond_accuracy"]) / 100)
                            * (1 - float(gpqa[m]["gpqa_diamond_accuracy"]) / 100)
                            / float(gpqa[m]["n_total"])) ** 0.5 * 100 for m in sel],
                     color="#aab1b9", thickness=1),
        mode="markers", name=label,
        marker=dict(symbol=style["symbol"], size=13 if "anchor" in label else 11,
                    color=style["color"],
                    line=dict(color=style["color"], width=2)),
        hovertext=hover, hoverinfo="text"))

for m in ms:
    dx, dy = OFFS[m]
    fig.add_annotation(x=float(council[m]["T"]), y=float(gpqa[m]["gpqa_diamond_accuracy"]),
                       text=SHORT[m], ax=dx, ay=dy, showarrow=True,
                       arrowwidth=0.8, arrowcolor="#9aa1a9", arrowhead=0,
                       standoff=6, font=dict(size=11))

fig.update_layout(
    title=dict(text=f"T vs GPQA Diamond:  Pearson r = {r:.2f} [{lo:.2f}, {hi:.2f}],  "
                    f"Spearman ρ = {rho:.2f},  n = {len(ms)}", x=0.5, font=dict(size=16)),
    xaxis_title="Metanym Game Benchmark  T = ¼(Gᶠ+Gᶜ+Eᶠ+Eᶜ)  (anchored, council basis)",
    yaxis_title="GPQA Diamond accuracy (%)",
    template="plotly_white", width=860, height=640,
    legend=dict(x=0.72, y=0.05, bordercolor="#d0d4d9", borderwidth=1),
    margin=dict(l=70, r=30, t=60, b=60))

fig.write_html(OUT / "total_validation_plotly.html", include_plotlyjs="cdn")
fig.write_image(OUT / "total_validation_plotly.png", scale=2)
print(f"wrote {OUT}/total_validation_plotly.html and .png")
