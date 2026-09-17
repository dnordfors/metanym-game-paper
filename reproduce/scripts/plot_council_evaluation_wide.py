#!/usr/bin/env python3
"""The council-evaluation exhibit, landscape (ICLR version, Figure 1): the instantiation with its metanyms on the
left, two of the council's cards on the right (Form b is Table 1b, the administrator's synthesis Appendix C), sized for the ICLR text width (5.5 in) at full width.
Same source and parsing as plot_council_evaluation.py; every string verbatim from Appendix C, PC 1.
Writes figures/council_evaluation_pc1_wide.png."""
import re, textwrap
from pathlib import Path
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Circle
HERE = Path(__file__).resolve().parent
SRC = HERE.parents[1] / "paper" / "appendices" / "C_council_evaluation_gemini-2.5-flash.md"
BLUE, ORANGE = "#2a78d6", "#eb6834"; SURFACE, INK, INK2 = "#fcfcfb", "#0b0b0b", "#52514e"
BOX, BOX2, EDGE, GREY = "#f4f3f0", "#eef3f9", "#d5d3ce", "#c9ccd1"; MET_ORANGE = "#b3491a"
s = SRC.read_text(); blk = s[s.index("#### PC 1"):s.index("#### PC 2")]
def grab(pat):
    m = re.search(pat, blk, re.S); assert m, pat; return re.sub(r"\s+", " ", m.group(1)).strip()
TITLE = "Gemini 2.5 Flash | Resource Allocation Under Scarcity – Ecosystem Management"
FORM_A = grab(r"\*\*Instantiation \(Form a\):\*\*(.*?)\n\n"); FORM_B = grab(r"\*\*Idiomatic rewrite \(Form b\):\*\*(.*?)\n\n")
ADMIN = grab(r"\*\*Administrator summary:\*\*(.*?)\n\n")
JUDGES = re.findall(r"\*\*([\w.\-]+)\*\* — Rating: (\d)\s*\n(.*?)(?=\n\n\*\*|\n\n#|\Z)", blk, re.S); assert len(JUDGES) == 5
SHOWN = [j for j in JUDGES if j[0] in ("opus-4.5", "3.1-pro")]; HIDDEN = [j for j in JUDGES if j[0] not in ("opus-4.5", "3.1-pro")]
DISPLAY = {"3.1-pro": "Gemini 3.1", "opus-4.5": "Opus 4.5", "opus-4.0": "Opus 4.0", "opus-4.1": "Opus 4.1", "sonnet-4": "Sonnet 4"}
W = 5.5; M, PAD = 1.2, 1.0; BODY = 6.8
def is_metanym(tok):
    core = tok.strip(".,;:()'\"“”"); return len(core) > 1 and core.isupper()

def render(H):
    fig = plt.figure(figsize=(W, H)); fig.patch.set_facecolor(SURFACE)
    ax = fig.add_axes([0, 0, 1, 1]); ax.set_xlim(0, 100); ax.set_ylim(0, 100); ax.axis("off")
    fig.canvas.draw(); rend = fig.canvas.get_renderer(); inv = ax.transData.inverted()
    def h_of(a):
        bb = a.get_window_extent(rend); (x0, y0), (x1, y1) = inv.transform([(bb.x0, bb.y0), (bb.x1, bb.y1)]); return y1 - y0, x1 - x0
    def label(x, y, text, size=BODY, color=BLUE):
        t = ax.text(x, y, text, fontsize=size, color=color, va="top", ha="left", fontweight="bold", zorder=3); return y - h_of(t)[0] - 0.5
    def flow(x, y, width, text, size=BODY, ls=1.2, color=INK):
        probe = ax.text(0, -60, "Ag", fontsize=size); lh = h_of(probe)[0] * ls; probe.remove()
        p1 = ax.text(0, -60, "a a", fontsize=size); p2 = ax.text(0, -60, "aa", fontsize=size); sw = h_of(p1)[1] - h_of(p2)[1]; p1.remove(); p2.remove()
        cx, cy = x, y
        for tok in text.split():
            met = is_metanym(tok)
            t = ax.text(cx, cy, tok, fontsize=size, va="top", ha="left", zorder=3, color=MET_ORANGE if met else color, fontweight="bold" if met else "normal")
            ww = h_of(t)[1]
            if cx + ww > x + width and cx > x:
                cy -= lh; cx = x; t.set_position((cx, cy)); ww = h_of(t)[1]
            cx += ww + sw
        return cy - lh
    def box(x, top, w, bot, fill=BOX, dashed=False):
        ax.add_patch(FancyBboxPatch((x, bot), w, top - bot, boxstyle="round,pad=0.2,rounding_size=0.6", facecolor=fill, edgecolor=EDGE, linewidth=0.8, zorder=1, linestyle=(0, (4, 3)) if dashed else "solid"))
    # title
    t = ax.text(M, 98.5, TITLE, fontsize=BODY + 0.6, fontweight="bold", color=INK, va="top", zorder=3); cur = 98.5 - h_of(t)[0] - 1.2
    # left column: the instantiation with its metanyms marked (Form b is Table 1b; the administrator's synthesis is Appendix C)
    LW = 42.0
    top = cur
    ya = label(M + PAD, top - PAD, "INSTANTIATION"); ya = flow(M + PAD, ya, LW - 2 * PAD, FORM_A)
    bot_left = ya - PAD + 0.4; box(M, top, LW, bot_left)
    # right column: council cards
    RX = M + LW + 1.6; RW = 100 - M - RX
    t = ax.text(RX, cur, "THE COUNCIL'S RATINGS", fontsize=BODY + 0.2, fontweight="bold", color=BLUE, va="top", zorder=3); y0 = cur - h_of(t)[0] - 0.8
    for name, rating, just in SHOWN:
        top = y0
        tn = ax.text(RX + PAD, top - PAD - 1.0, DISPLAY.get(name, name), fontsize=BODY + 0.4, fontweight="bold", color=INK, va="center", zorder=3)
        nx = RX + PAD + h_of(tn)[1] + 2.2
        ax.plot([nx + 1.3], [top - PAD - 1.0], "o", ms=13, mfc=ORANGE, mec=SURFACE, mew=0.8, zorder=3)
        ax.text(nx + 1.3, top - PAD - 1.05, rating, fontsize=BODY + 0.2, fontweight="bold", color="white", ha="center", va="center", zorder=4)
        y = flow(RX + PAD, top - PAD - 3.0, RW - 2 * PAD, "“" + re.sub(r"\s+", " ", just).strip() + "”")
        bot = y - PAD + 0.4; box(RX, top, RW, bot); y0 = bot - 1.0
    top = y0; gy = top - PAD - 1.0
    tl = ax.text(RX + PAD, gy, "+ 3 more judges:", fontsize=BODY, fontweight="bold", color=INK2, va="center", zorder=3); gx = RX + PAD + h_of(tl)[1] + 2.4
    for name, rating, _ in HIDDEN:
        ax.plot([gx], [gy], "o", ms=11, mfc=GREY, mec=SURFACE, mew=0.8, zorder=3)
        ax.text(gx, gy - 0.05, rating, fontsize=BODY, fontweight="bold", color="white", ha="center", va="center", zorder=4)
        tn = ax.text(gx + 1.7, gy, DISPLAY.get(name, name), fontsize=BODY, color=INK2, va="center", zorder=3); gx += 1.7 + h_of(tn)[1] + 2.0
    bot_right = gy - 2.0; box(RX, top, RW, bot_right, fill=SURFACE, dashed=True)
    return fig, min(bot_left, bot_right)

H = 2.6
for _ in range(5):
    fig, y_end = render(H); used = (100 - y_end) / 100 * H + 0.12
    if abs(used - H) < 0.03: break
    plt.close(fig); H = used
out = HERE.parents[0] / "figures" / "council_evaluation_pc1_wide.png"; fig.savefig(out, dpi=300, facecolor=SURFACE)
print(f"wide exhibit: body {BODY}pt at {W} in wide, fitted height {H:.2f} in -> {out}")
