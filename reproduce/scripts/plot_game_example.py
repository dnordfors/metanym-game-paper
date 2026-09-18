#!/usr/bin/env python3
"""Figure 1 of the ICLR version, one page: (a) generation — the anchor's first archetype as a player wrote it (context template,
metanym table, the first domain's instantiation and idiomatic rewrite), every string verbatim from the anchor's
submission submissions/anchor_claude-opus-4.5.md (run 1, the reference of §4.1); (b) evaluation — one parallel context of another submission under
the council (submissions/council_evaluation_gemini-2.5-flash.md, PC 1): the instantiation with its metanyms marked, three judges (Opus 4.5, Gemini 3.1, Sonnet 4) with their ratings and complete justifications; the judges' 'Form (a)' and 'Form (b)'
(the prompt's names, Appendix B) are shown as the paper's terms, in square brackets: [instantiation], [idiomatic rewrite].
Writes figures/game_example.png (or --out)."""
import re, sys
from pathlib import Path
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
HERE = Path(__file__).resolve().parent; PKG = HERE.parents[0]
OUT = Path(sys.argv[sys.argv.index("--out") + 1]) if "--out" in sys.argv else PKG / "figures" / "game_example.png"
BLUE, ORANGE = "#2a78d6", "#eb6834"; SURFACE, INK, INK2 = "#fcfcfb", "#0b0b0b", "#52514e"; BOX, EDGE = "#f4f3f0", "#d5d3ce"; EVAL_BOX = "#eef3fa"; MET_ORANGE = "#b3491a"   # evaluation panel: a cool tint against the warm generation panel
# (a) generation source
P = (PKG / "submissions" / "anchor_claude-opus-4.5.md").read_text(); blk = P[P.index("## Archetype Proposal: Gradient-Guided Navigation"):P.index("### Mountain Climbing")]
TEMPLATE = re.sub(r"\s+", " ", re.search(r"### Context-template\s*\n+\"?(.+?)\"?\n\n", blk, re.S).group(1)).strip().strip('"')
TABLE = [[c.strip() for c in ln.strip().strip("|").split("|")] for ln in blk[blk.index("| [SLOT]"):].split("\n\n")[0].splitlines() if not re.match(r"^\|[-| ]+\|$", ln.strip())]
DROP = sys.argv[sys.argv.index("--drop-domain") + 1] if "--drop-domain" in sys.argv else "Gradient Descent"   # one domain column omitted for space (David, 2026-09-17); "" keeps all five
if DROP: j = TABLE[0].index(DROP); TABLE = [row[:j] + row[j + 1:] for row in TABLE]
dom = blk[blk.index("### Bacterial Chemotaxis"):]; FA = re.sub(r"\s+", " ", re.search(r"\*\*Instantiation \(Form a\):\*\*\s*\n\"?(.+?)\"?\n\n", dom, re.S).group(1)).strip().strip('"'); FB = re.sub(r"\s+", " ", re.search(r"\*\*Idiomatic rewrite \(Form b\):\*\*\s*\n\"?(.+?)\"?\n\n", dom, re.S).group(1)).strip().strip('"')
def first_n(s, n): return " ".join(re.split(r"(?<=[.!?])\s+", s)[:n])
# (b) evaluation source (as plot_council_evaluation_compact.py)
SRC = PKG / "submissions" / "council_evaluation_gemini-2.5-flash.md"; s = SRC.read_text(); eb = s[s.index("#### PC 1"):s.index("#### PC 2")]
FORM_A = re.sub(r"\s+", " ", re.search(r"\*\*Instantiation \(Form a\):\*\*(.*?)\n\n", eb, re.S).group(1)).strip()
JUDGES = re.findall(r"\*\*([\w.\-]+)\*\* — Rating: (\d)\s*\n(.*?)(?=\n\n\*\*|\n\n#|\Z)", eb, re.S); assert len(JUDGES) == 5
DISPLAY = {"opus-4.5": "Opus 4.5", "opus-4.1": "Opus 4.1", "opus-4.0": "Opus 4.0", "sonnet-4": "Sonnet 4", "3.1-pro": "Gemini 3.1"}
def quoted_clause(just):
    m = re.search(r"[\"“](nature must make natural selections[^\"”]*)[\"”]", just, re.I)
    if m: return m.group(1)
    m = re.search(r"([^.;,]*natural selection[^.;,]*)", just, re.I); assert m; return m.group(1).strip()
W = 5.5; M, PAD = 1.2, 1.0; BODY = float(sys.argv[sys.argv.index("--body") + 1]) if "--body" in sys.argv else 6.9   # 6.9 fills the ICLR page (5.5 x 9 in) with the caption
def is_slot(tok): core = tok.strip(".,;:()'\"“”"); return len(core) > 1 and core.isupper()
def render(H):
    fig = plt.figure(figsize=(W, H)); fig.patch.set_facecolor(SURFACE); ax = fig.add_axes([0, 0, 1, 1]); ax.set_xlim(0, 100); ax.set_ylim(0, 100); ax.axis("off")
    fig.canvas.draw(); rend = fig.canvas.get_renderer(); inv = ax.transData.inverted()
    def h_of(a):
        bb = a.get_window_extent(rend); (x0, y0), (x1, y1) = inv.transform([(bb.x0, bb.y0), (bb.x1, bb.y1)]); return y1 - y0, x1 - x0
    def flow(x, y, width, text, size=BODY, ls=1.2, color=INK, mark=True):
        probe = ax.text(0, -60, "Ag", fontsize=size); lh = h_of(probe)[0] * ls; probe.remove(); p1 = ax.text(0, -60, "a a", fontsize=size); p2 = ax.text(0, -60, "aa", fontsize=size); sw = h_of(p1)[1] - h_of(p2)[1]; p1.remove(); p2.remove()
        cx, cy = x, y
        for tok in text.split():
            met = mark and is_slot(tok); t = ax.text(cx, cy, tok, fontsize=size, va="top", ha="left", zorder=3, color=MET_ORANGE if met else color, fontweight="bold" if met else "normal"); ww = h_of(t)[1]
            if cx + ww > x + width and cx > x: cy -= lh; cx = x; t.set_position((cx, cy)); ww = h_of(t)[1]
            cx += ww + sw
        return cy - lh
    def box(x, top, w, bot, fill=BOX): ax.add_patch(FancyBboxPatch((x, bot), w, top - bot, boxstyle="round,pad=0.2,rounding_size=0.6", facecolor=fill, edgecolor=EDGE, linewidth=0.8, zorder=1))
    def header(y, text): t = ax.text(M, y, text, fontsize=BODY, fontweight="bold", color=INK, va="top", zorder=3); return y - h_of(t)[0] - 0.8
    def subhead(x, y, text): t = ax.text(x, y, text, fontsize=BODY, fontweight="bold", color=BLUE, va="top", zorder=3); return y - h_of(t)[0] - 0.5
    FULL = 100 - 2 * M
    # ---- (a)
    y = header(99.6, "(a)  Generation: one archetypal context template from the anchor submission (Claude Opus 4.5)")
    top = y; ys = subhead(M + PAD, top - PAD, "METANYM TABLE"); ncol = len(TABLE[0]); x0 = M + PAD
    fs = lambda r: BODY - 0.3
    def tw(s, size, bold):                                       # rendered width of a string, in axis units
        pr = ax.text(0, -60, s, fontsize=size, fontweight="bold" if bold else "normal"); w_ = h_of(pr)[1]; pr.remove(); return w_
    need = [max(tw(TABLE[r][c].replace("[", "").replace("]", ""), fs(r), r == 0 or c == 0) for r in range(len(TABLE))) for c in range(ncol)]
    gap = (FULL - 2 * PAD - sum(need)) / (ncol - 1); assert gap > 0.3, f"metanym table too wide for the page: {sum(need):.1f} of {FULL - 2 * PAD:.1f} units"
    xs = [x0 + sum(need[:c]) + c * gap for c in range(ncol)]
    probe = ax.text(0, -60, "Ag", fontsize=BODY - 0.3); lh = h_of(probe)[0] * 1.2; probe.remove(); yy = ys
    for r, row in enumerate(TABLE):
        for c, cell in enumerate(row):
            ax.text(xs[c], yy, cell.replace("[", "").replace("]", ""), fontsize=fs(r), va="top", ha="left", color=MET_ORANGE if c == 0 and r > 0 else INK, fontweight="bold" if r == 0 or c == 0 else "normal", zorder=3)
        yy -= lh
        if r == 0: ax.plot([x0, M + FULL - PAD], [yy + 0.3, yy + 0.3], color=EDGE, lw=0.6, zorder=2)
    box(M, top, FULL, yy - PAD + lh * 0.3); y = yy - PAD - 0.8 + lh * 0.3
    top = y; ys = subhead(M + PAD, top - PAD, "INSTANTIATED CONTEXT TEMPLATE — BACTERIAL CHEMOTAXIS"); ya = flow(M + PAD, ys, FULL - 2 * PAD, FA); bot = ya - PAD + 0.4; box(M, top, FULL, bot); y = bot - 0.8
    top = y; ys2 = subhead(M + PAD, top - PAD, "IDIOMATIC REWRITE"); yb2 = flow(M + PAD, ys2, FULL - 2 * PAD, FB, mark=False); bot = yb2 - PAD + 0.4; box(M, top, FULL, bot); y = bot - 1.8
    # ---- (b): full-width instantiation, then three judges with their complete justifications
    y = header(y, "(b)  Evaluation — factual correctness (Gemini 2.5 Flash submission)")
    top = y; ys = subhead(M + PAD, top - PAD, "INSTANTIATED CONTEXT TEMPLATE — ECOSYSTEM MANAGEMENT"); ya = flow(M + PAD, ys, FULL - 2 * PAD, FORM_A); bot = ya - PAD + 0.4; box(M, top, FULL, bot, fill=EVAL_BOX); y = bot - 1.0
    NAMEW = 12.0
    PICK = ["opus-4.5", "3.1-pro", "sonnet-4"]                     # three judges, both vendors of the council
    for name, rating, just in [j for k in PICK for j in JUDGES if j[0] == k]:
        top = y; ax.text(M + PAD, top - PAD, DISPLAY.get(name, name), fontsize=BODY, fontweight="bold", color=INK, va="top", zorder=3)
        ax.text(M + PAD, top - PAD - 3.2, f"{rating}/10", fontsize=BODY + 1.5, fontweight="bold", color=ORANGE, va="top", zorder=3)
        shown = re.sub(r"\s+", " ", just.strip().strip('"“”')); shown = re.sub(r"[Ff]orm \(a\)", "[instantiation]", shown); shown = re.sub(r"[Ff]orm \(b\)", "[idiomatic rewrite]", shown)
        yj = flow(M + NAMEW, top - PAD, FULL - NAMEW - PAD, "“" + shown + "”", size=BODY, color=INK2, mark=False)
        bot = min(yj, top - PAD - 6.0) - PAD + 0.4; box(M, top, FULL, bot, fill=EVAL_BOX); y = bot - 0.8
    bot_left = y; yj = y
    return fig, min(bot_left, yj)
H = 8.0
for _ in range(12):
    fig, y_end = render(H); used = (100 - y_end) / 100 * H - 0.02
    if abs(used - H) < 0.03: break
    plt.close(fig); H = used
fig.savefig(OUT, dpi=300, facecolor=SURFACE); print("wrote", OUT, f"{W:.1f} x {H:.2f} in")
