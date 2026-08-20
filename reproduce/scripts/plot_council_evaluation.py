#!/usr/bin/env python3
"""The council-evaluation exhibit — one parallel context, shown whole (Appendix C, PC 1).

Rev 3 (David: fill the boxes): measured layout — every text block is measured with the
renderer and each box is drawn to fit its content; the figure height is fitted in a
second pass. Metanyms coloured in Form (a); three judges + a ghost card for the two not
shown. Every string parsed verbatim from
paper/appendices/C_council_evaluation_gemini-2.5-flash.md.
Writes figures/council_evaluation_pc1.png.
"""
import re
import textwrap
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Circle

HERE = Path(__file__).resolve().parent
SRC = HERE.parents[1] / "paper" / "appendices" / "C_council_evaluation_gemini-2.5-flash.md"
BLUE, ORANGE = "#2a78d6", "#eb6834"
SURFACE, INK, INK2 = "#fcfcfb", "#0b0b0b", "#52514e"
BOX, BOX2, EDGE, GREY = "#f4f3f0", "#eef3f9", "#d5d3ce", "#c9ccd1"
MET_ORANGE = "#b3491a"    # text-orange: 4.9:1 on the box fill (WCAG small-text pass)

s = SRC.read_text()
blk = s[s.index("#### PC 1"):s.index("#### PC 2")]

def grab(pat):
    m = re.search(pat, blk, re.S)
    assert m, pat
    return re.sub(r"\s+", " ", m.group(1)).strip()

assert "PC 1 (Ecosystem Management) — a plain error, and the council converges" in blk
TITLE = "Gemini 2.5 Flash | Archetype: Resource Allocation Under Scarcity – Instantiation: Ecosystem Management"
FORM_A = grab(r"\*\*Instantiation \(Form a\):\*\*(.*?)\n\n")
FORM_B = grab(r"\*\*Idiomatic rewrite \(Form b\):\*\*(.*?)\n\n")
ADMIN = grab(r"\*\*Administrator summary:\*\*(.*?)\n\n")
CODA = grab(r"(This is the falsifiability property.*?)$")
JUDGES = re.findall(r"\*\*([\w.\-]+)\*\* — Rating: (\d)\s*\n(.*?)(?=\n\n\*\*|\n\n#|\Z)", blk, re.S)
assert len(JUDGES) == 5
SHOWN = [j for j in JUDGES if j[0] in ("opus-4.5", "opus-4.0", "3.1-pro")]
DISPLAY = {"3.1-pro": "Gemini 3.1"}          # display names; appendix keys stay verbatim
HIDDEN = [j for j in JUDGES if j[0] not in ("opus-4.5", "opus-4.0", "3.1-pro")]

W = 6.5                      # true print width: \linewidth on letter, 1in margins
M, PAD = 1.6, 1.15          # outer margin, box padding (canvas units, x-axis 0..100)

def is_metanym(tok):
    core = tok.strip(".,;:()'\"\u201c\u201d")
    return len(core) > 1 and core.isupper()

def render(H, K=1.0):
    fig = plt.figure(figsize=(W, H))
    fig.patch.set_facecolor(SURFACE)
    ax = fig.add_axes([0, 0, 1, 1]); ax.set_xlim(0, 100); ax.set_ylim(0, 100); ax.axis("off")
    fig.canvas.draw()
    rend = fig.canvas.get_renderer()
    inv = ax.transData.inverted()

    def h_of(artist):
        bb = artist.get_window_extent(rend)
        (x0, y0), (x1, y1) = inv.transform([(bb.x0, bb.y0), (bb.x1, bb.y1)])
        return y1 - y0, x1 - x0

    def para(x, y, w_chars, text, size, color=INK, weight="normal", style="normal", ls=1.2):
        t = ax.text(x, y, textwrap.fill(text, w_chars), fontsize=size, color=color, va="top",
                    ha="left", linespacing=ls, fontweight=weight, style=style, zorder=3)
        return y - h_of(t)[0]

    def flow(x, y, width, text, size, ls=1.22):
        probe = ax.text(0, -60, "Ag", fontsize=size, zorder=3)
        lh = h_of(probe)[0] * ls
        probe.remove()
        p1 = ax.text(0, -60, "a a", fontsize=size); p2 = ax.text(0, -60, "aa", fontsize=size)
        space_w = h_of(p1)[1] - h_of(p2)[1]
        p1.remove(); p2.remove()
        cx, cy = x, y
        for wtok in text.split():
            met = is_metanym(wtok)
            t = ax.text(cx, cy, wtok, fontsize=size, va="top", ha="left", zorder=3,
                        color=MET_ORANGE if met else INK, fontweight="bold" if met else "normal")
            ww = h_of(t)[1]
            if cx + ww > x + width and cx > x:
                cy -= lh; cx = x
                t.set_position((cx, cy))
                ww = h_of(t)[1]
            cx += ww + space_w
        return cy - lh

    def boxpatch(x, ytop, w, ybot, fill=BOX, dashed=False):
        ax.add_patch(FancyBboxPatch((x, ybot), w, ytop - ybot,
                                    boxstyle="round,pad=0.25,rounding_size=0.7",
                                    facecolor=fill, edgecolor=EDGE, linewidth=0.9, zorder=1,
                                    linestyle=(0, (4, 3)) if dashed else "solid"))

    def para_fit(x, y, width, text, size, color=INK, style="normal", ls=1.2):
        for wchars in range(150, 30, -4):
            t = ax.text(x, y, textwrap.fill(text, wchars), fontsize=size, color=color,
                        va="top", ha="left", linespacing=ls, style=style, zorder=3)
            hh, ww = h_of(t)
            if ww <= width:
                return y - hh
            t.remove()
        return y

    cur = 98.6
    tsz = 12.5 * K
    while True:
        t = ax.text(M, cur, TITLE, fontsize=tsz, fontweight="bold", color=INK, va="top", zorder=3)
        if h_of(t)[1] <= 100 - 2 * M:
            break
        t.remove(); tsz -= 0.4
    cur -= h_of(t)[0] + 0.9
    cur -= 0.6

    # forms row — column split balanced so both columns end together
    total_w = 100 - 2 * M - 1.2
    top = cur
    best = None
    for fr in (0.50, 0.52, 0.54, 0.56, 0.58, 0.60):
        wa = total_w * fr
        n0 = len(ax.texts)
        ya = flow(M + PAD, top - 3.4, wa - 2 * PAD, FORM_A, size=7.9 * K)
        yb = flow(M + wa + 1.2 + PAD, top - 3.4, total_w - wa - 2 * PAD, FORM_B, size=7.9 * K)
        for t in ax.texts[n0:]:
            t.remove()
        if best is None or abs(ya - yb) < best[0]:
            best = (abs(ya - yb), fr)
    wa = total_w * best[1]
    ya = para(M + PAD, top - PAD, 60, "INSTANTIATION — FORM (a)", 7.8, BLUE, weight="bold") - 0.6
    ya = flow(M + PAD, ya, wa - 2 * PAD, FORM_A, size=7.9 * K)
    yb = para(M + wa + 1.2 + PAD, top - PAD, 60, "IDIOMATIC REWRITE — FORM (b)", 7.8, BLUE, weight="bold") - 0.6
    yb = flow(M + wa + 1.2 + PAD, yb, total_w - wa - 2 * PAD, FORM_B, size=7.9 * K)
    bot = min(ya, yb) - PAD + 0.55
    boxpatch(M, top, wa, bot); boxpatch(M + wa + 1.2, top, total_w - wa, bot)
    cur = bot - 1.2

    # administrator summary
    top = cur
    y = para(M + PAD, top - PAD, 60, "ADMINISTRATOR (CLAUDE OPUS) SUMMARY", 7.8, BLUE, weight="bold") - 0.7
    y = flow(M + PAD, y, 100 - 2 * M - 2 * PAD, "\u201c" + ADMIN + "\u201d", size=7.9 * K)
    bot = y - PAD + 0.6
    boxpatch(M, top, 100 - 2 * M, bot, fill=BOX2)
    cur = bot - 1.2

    # council cards
    t = ax.text(M, cur, "THE COUNCIL'S RATINGS AND JUSTIFICATIONS", fontsize=8.2 * K,
                fontweight="bold", color=BLUE, va="top", zorder=3)
    cur -= h_of(t)[0] + 0.8
    row_gap = 0.9
    probes = [ax.text(0, -60, n, fontsize=8.6 * K, fontweight="bold") for n, _r, _j in SHOWN]
    LW = max(h_of(t)[1] for t in probes) + 1.6
    for t in probes:
        t.remove()
    for name, rating, just in SHOWN:
        top = cur
        lx = M + PAD
        tname = ax.text(lx, top - PAD - 1.3, DISPLAY.get(name, name), fontsize=tsz, fontweight="bold",
                        color=INK, va="center", zorder=3)
        name_w = h_of(tname)[1]
        # slider: 1..10 track, the score badge as handle; width ~ the name, centred in the div
        tw = max(name_w - 2.4, 7.5)
        cxm = lx + (LW - 1.6) / 2
        sx0, sx1 = cxm - tw / 2, cxm + tw / 2
        sy = top - PAD - 5.4
        ax.plot([sx0, sx1], [sy, sy], color=EDGE, lw=2.6, solid_capstyle="round", zorder=2)
        pos = sx0 + (int(rating) - 1) / 9.0 * (sx1 - sx0)
        ax.plot([sx0, pos], [sy, sy], color=ORANGE, lw=2.6, solid_capstyle="round",
                zorder=2, alpha=0.45)
        ax.add_patch(Circle((pos, sy), 1.7, facecolor=ORANGE, edgecolor=SURFACE,
                            lw=1.1, zorder=3))
        ax.text(pos, sy - 0.05, rating, fontsize=9 * K, fontweight="bold", color="white",
                ha="center", va="center", zorder=4)
        # divider + justification
        rx = M + PAD + LW + 1.6
        y = flow(rx, top - PAD - 0.4, 100 - M - PAD - rx,
                 "\u201c" + re.sub(r"\s+", " ", just).strip() + "\u201d", size=7.9 * K)
        bot = min(y, sy - 2.4) - PAD + 0.6
        ax.plot([rx - 1.6, rx - 1.6], [top - PAD - 0.2, bot + PAD - 0.4], color=EDGE,
                lw=0.8, zorder=2)
        boxpatch(M, top, 100 - 2 * M, bot)
        cur = bot - row_gap
    # ghost row: the two judges not shown
    top = cur
    gy = top - PAD - 1.3
    tlab = ax.text(M + PAD, gy, "+ 2 more judges:", fontsize=7.6 * K, fontweight="bold", color=INK2,
            va="center", zorder=3)
    gx = M + PAD + h_of(tlab)[1] + 3.0
    for name, rating, _j in HIDDEN:
        ax.add_patch(Circle((gx, gy), 1.45, facecolor=GREY, edgecolor=SURFACE, lw=1.0, zorder=3))
        ax.text(gx, gy - 0.05, rating, fontsize=7.9 * K, fontweight="bold", color="white",
                ha="center", va="center", zorder=4)
        ax.text(gx + 2.0, gy, name, fontsize=7.9 * K, color=INK2, va="center", zorder=3)
        gx += 13.5
    ax.text(100 - M - PAD, gy, "full justifications in Appendix C", fontsize=7.0 * K, color=INK2,
            va="center", ha="right", style="italic", zorder=3)
    bot = gy - 2.2
    boxpatch(M, top, 100 - 2 * M, bot, fill=SURFACE, dashed=True)
    cur = bot - 1.4

    # coda
    y = para_fit(M, cur - 0.2, 100 - 2 * M, CODA, 7.9 * K, color=INK2, style="italic")
    return fig, y


def fitted_height(K, H0=9.0):
    H = H0
    for _ in range(4):
        fig, y_end = render(H, K)
        used = (100 - y_end) / 100 * H + 0.24
        if abs(used - H) < 0.03:
            return fig, H
        plt.close(fig)
        H = used
    return fig, H

K = 8.0 / 7.9                     # body text = 8.0pt printed (David's ruling)
fig, H = fitted_height(K, H0=9.6)
print(f"body 8.0pt, fitted height {H:.2f} in at 6.5 in wide")
out = HERE.parents[0] / "figures" / "council_evaluation_pc1.png"
fig.savefig(out, dpi=300, facecolor=SURFACE)
print(f"wrote {out}")
