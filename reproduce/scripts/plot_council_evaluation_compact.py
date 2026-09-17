#!/usr/bin/env python3
"""The council-evaluation exhibit, compact (ICLR version, Figure 1): the instantiation with its metanyms on the left;
on the right the five judges' ratings and the clause each one quotes — all five isolate the same one. Every string
verbatim from Appendix C, PC 1 (the full exhibit is plot_council_evaluation.py, shown in Appendix C).
Writes figures/council_evaluation_pc1_compact.png."""
import re
def paperterms(s):
    """The judges wrote 'Form (a)'/'Form (b)' (the prompt's names, Appendix B); shown as the paper's terms, in square brackets."""
    return re.sub(r"[Ff]orm \(b\)", "[idiomatic rewrite]", re.sub(r"[Ff]orm \(a\)", "[instantiation]", s))
from pathlib import Path
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
HERE = Path(__file__).resolve().parent
SRC = HERE.parents[0] / "submissions" / "council_evaluation_gemini-2.5-flash.md"   # the evaluation transcript, shipped in the package
BLUE, ORANGE = "#2a78d6", "#eb6834"; SURFACE, INK, INK2 = "#fcfcfb", "#0b0b0b", "#52514e"
BOX, EDGE = "#f4f3f0", "#d5d3ce"; MET_ORANGE = "#b3491a"
s = SRC.read_text(); blk = s[s.index("#### PC 1"):s.index("#### PC 2")]
def grab(pat):
    m = re.search(pat, blk, re.S); assert m, pat; return re.sub(r"\s+", " ", m.group(1)).strip()
FORM_A = grab(r"\*\*Instantiation \(Form a\):\*\*(.*?)\n\n")
JUDGES = re.findall(r"\*\*([\w.\-]+)\*\* — Rating: (\d)\s*\n(.*?)(?=\n\n\*\*|\n\n#|\Z)", blk, re.S); assert len(JUDGES) == 5
DISPLAY = {"opus-4.5": "Opus 4.5", "opus-4.1": "Opus 4.1", "opus-4.0": "Opus 4.0", "sonnet-4": "Sonnet 4", "3.1-pro": "Gemini 3.1"}
def quoted_clause(just):
    """The clause the judge quotes; one judge paraphrases instead, so fall back to its own words around 'natural selection'."""
    m = re.search(r"[\"“](nature must make natural selections[^\"”]*)[\"”]", just, re.I)
    if m: return m.group(1)
    m = re.search(r"([^.;,]*natural selection[^.;,]*)", just, re.I); assert m, just[:80]; return m.group(1).strip()
W = 5.5; M, PAD = 1.2, 1.0; BODY = 6.8
def is_metanym(tok):
    core = tok.strip(".,;:()'\"“”"); return len(core) > 1 and core.isupper()
def render(H):
    fig = plt.figure(figsize=(W, H)); fig.patch.set_facecolor(SURFACE)
    ax = fig.add_axes([0, 0, 1, 1]); ax.set_xlim(0, 100); ax.set_ylim(0, 100); ax.axis("off")
    fig.canvas.draw(); rend = fig.canvas.get_renderer(); inv = ax.transData.inverted()
    def h_of(a):
        bb = a.get_window_extent(rend); (x0, y0), (x1, y1) = inv.transform([(bb.x0, bb.y0), (bb.x1, bb.y1)]); return y1 - y0, x1 - x0
    def flow(x, y, width, text, size=BODY, ls=1.2, color=INK, mark=True):
        probe = ax.text(0, -60, "Ag", fontsize=size); lh = h_of(probe)[0] * ls; probe.remove()
        p1 = ax.text(0, -60, "a a", fontsize=size); p2 = ax.text(0, -60, "aa", fontsize=size); sw = h_of(p1)[1] - h_of(p2)[1]; p1.remove(); p2.remove()
        cx, cy = x, y
        for tok in text.split():
            met = mark and is_metanym(tok)
            t = ax.text(cx, cy, tok, fontsize=size, va="top", ha="left", zorder=3, color=MET_ORANGE if met else color, fontweight="bold" if met else "normal")
            ww = h_of(t)[1]
            if cx + ww > x + width and cx > x:
                cy -= lh; cx = x; t.set_position((cx, cy)); ww = h_of(t)[1]
            cx += ww + sw
        return cy - lh
    def box(x, top, w, bot, fill=BOX):
        ax.add_patch(FancyBboxPatch((x, bot), w, top - bot, boxstyle="round,pad=0.2,rounding_size=0.6", facecolor=fill, edgecolor=EDGE, linewidth=0.8, zorder=1))
    top = 98.0
    LW = 57.0
    t = ax.text(M + PAD, top - PAD, "INSTANTIATION", fontsize=BODY, fontweight="bold", color=BLUE, va="top", zorder=3)
    ya = flow(M + PAD, top - PAD - h_of(t)[0] - 0.6, LW - 2 * PAD, FORM_A); bot_left = ya - PAD + 0.4; box(M, top, LW, bot_left)
    RX = M + LW + 1.6; RW = 100 - M - RX
    t = ax.text(RX, top - PAD, "JUDGES — THE CLAUSE EACH CITES", fontsize=BODY, fontweight="bold", color=BLUE, va="top", zorder=3)
    y = top - PAD - h_of(t)[0] - 1.6
    for name, rating, just in JUDGES:
        ax.plot([RX + 1.6], [y - 1.0], "o", ms=11, mfc=ORANGE, mec=SURFACE, mew=0.8, zorder=3)
        ax.text(RX + 1.6, y - 1.05, rating, fontsize=BODY, fontweight="bold", color="white", ha="center", va="center", zorder=4)
        tn = ax.text(RX + 4.4, y - 1.0, DISPLAY.get(name, name), fontsize=BODY, fontweight="bold", color=INK, va="center", zorder=3)
        yq = flow(RX + 4.4, y - 2.8, RW - 4.4, "“" + quoted_clause(just) + "”", size=BODY - 0.4, color=INK2, mark=False)
        y = yq - 1.2
    return fig, min(bot_left, y)
H = 1.8
for _ in range(5):
    fig, y_end = render(H); used = (100 - y_end) / 100 * H + 0.12
    if abs(used - H) < 0.03: break
    plt.close(fig); H = used
out = HERE.parents[0] / "figures" / "council_evaluation_pc1_compact.png"; fig.savefig(out, dpi=300, facecolor=SURFACE)
print(f"compact exhibit: body {BODY}pt at {W} in wide, fitted height {H:.2f} in -> {out}")
