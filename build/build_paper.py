#!/usr/bin/env python3
r"""Build paper/metanym_game_iclr27.pdf from paper/metanym_game_iclr27.md in the ICLR 2027 style (or, with --arxiv, the arXiv v3
version: paper/metanym_game_arxiv_v3.pdf). The submission bundle — the generated paper.tex, the style files and the figures it uses —
is written to submission-iclr/ (or submission-arxiv/, plus the source tarball); build/ holds this script and the style files, figures/
the figure sources; neither submission directory ever holds the paper itself.

Provenance: adapted from ../metanym-game-paper/submission/build_paper.py (arXiv pipeline); the
ICLR style files in submission/style/ are the official iclr-2027-style-files.zip, untouched.

Pipeline (deterministic):
  1. combine   — manuscript + appendices (stub links replaced by the files' content, headings
                 demoted one level), every <comment: …> block dropped, figure paths re-pointed
  2. guard     — anonymity assertions on the combined text (author name, repo URL, arXiv id)
  3. pandoc    — markdown → LaTeX fragment (--wrap=none, wide --columns so pipe tables keep
                 plain l/r/c columns), sections numbered by the style
  4. postfix   — longtables → [t] table floats (caption above, per the ICLR template), wide
                 tables scaled to the text width, figures width=\linewidth, the three statements
                 as unnumbered subsections, References unnumbered, \appendix before the appendix
  5. assemble  — ICLR preamble + body; compile with tectonic; read the main-text page count from
                 the .aux and fail loudly if it exceeds the limit

Run from the repo root:  python3 submission/build_paper.py [--limit 9]
"""
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BUILD = ROOT / "build"; STYLE = BUILD / "style"; FIGS = ROOT / "figures"
MD = ROOT / "paper" / "metanym_game_iclr27.md"
APPENDIX_DIR = ROOT / "paper" / "appendices"
ARXIV = "--arxiv" in sys.argv   # arXiv v3 mode: author block, preprint header, no anonymity guard, no page limit, larger figures
PAGE_LIMIT = int(sys.argv[sys.argv.index("--limit") + 1]) if "--limit" in sys.argv else (999 if ARXIV else 9)
ARXIV_ID = "2606.21008"; ARXIV_AUTHOR = r"David Nordfors \\ \texttt{david.nordfors@archetypes.ai}"
ARXIV_REPO = "https://github.com/dnordfors/metanym-game-paper"
ARXIV_FIGURE_WIDTHS = {"total_validation_simple": 0.55, "mechanism_sketch": 0.92}   # unpaired, larger
ARXIV_FIGURE_SWAPS = {"council_evaluation_pc1_compact.png": "council_evaluation_pc1_wide.png"}
ARXIV_DROP_SECTIONS = ("Ethics statement",)

# Figure widths as a fraction of the text width, keyed by file stem (KeyError = unlisted figure).
FIGURE_WIDTHS = {"game_example": 1.0, "council_evaluation_pc1": 1.0, "council_evaluation_pc1_wide": 1.0, "council_evaluation_pc1_compact": 1.0, "total_validation": 0.46, "total_validation_simple": 0.32, "anchoring_resolution": 0.6, "runs_panel": 1.0, "mechanism_sketch": 1.0}

# Strings that must not survive into a double-blind submission.
ANONYMITY_GUARDS = ["Nordfors", "dnordfors", "archetypes.ai", "2606.21008", "github.com/dnordfors"]


# ---------------------------------------------------------------- 1. combine
def combine() -> str:
    md = MD.read_text()
    md = re.sub(r"<comment:.*?>\s*", "", md, flags=re.S)
    assert "<comment:" not in md, "an unclosed <comment: block survived stripping"
    # title line → \title; the style prints the anonymous author block itself
    m = re.match(r"# (.+)\n", md)
    assert m, "manuscript must start with a level-1 title line"
    title = m.group(1)
    md = md[m.end():]
    # appendix stubs: "→ [`appendices/X.md`](appendices/X.md) — …" lines, in order
    i = md.find("## Appendices")
    assert i >= 0, "manuscript must contain a '## Appendices' section with stub links"
    head, stubs = md[:i], md[i:]
    files = re.findall(r"\]\(appendices/([^)]+\.md)\)", stubs)
    assert files, "no appendix stub links found"
    parts = [head, "\n```{=latex}\n\\endgroup\n\\clearpage\n\\appendix\n```\n"]
    for f in files:
        t = (APPENDIX_DIR / f).read_text()
        t = re.sub(r"<comment:.*?>\s*", "", t, flags=re.S)
        assert "<comment:" not in t, f"unclosed <comment: block in {f}"
        # '# X. Title' → '## Title' (letters come from \appendix); demote the rest one level
        t = re.sub(r"^# [A-Z]\. ", "## ", t, count=1, flags=re.M)
        t = re.sub(r"^(##+) [A-Z]\.\d+ ", r"#\1 ", t, flags=re.M)
        parts.append(t.strip() + "\n")
    c = "\n".join(parts)
    c = c.replace("](../figures/", "](figures/")
    c = re.sub(r'<a id="([^"]+)"></a>', r"[]{#\1}", c)  # survives pandoc as \label
    (BUILD / "_paper_combined.md").write_text(c)
    return title, c


# ------------------------------------------------------------------ 2. guard
def guard(text: str) -> None:
    if ARXIV: return
    hits = [g for g in ANONYMITY_GUARDS if g.lower() in text.lower()]
    assert not hits, f"double-blind violation — these strings appear in the build: {hits}"


# ----------------------------------------------------------------- 4. postfix
def unicode_fixes(body: str) -> str:
    """The ICLR style uses the 8-bit Times fonts; map the symbols the manuscript uses. Inside verbatim blocks (the prompts of
    Appendix B, printed as sent) the same symbols go through listings' escape, so the page shows the symbol itself and the
    printed prompt carries no LaTeX macro."""
    parts = re.split(r"(\\begin\{lstlisting\}.*?\\end\{lstlisting\})", body, flags=re.S)   # verbatim was renamed to lstlisting above
    return "".join(_unicode_verbatim(p) if p.startswith("\\begin{lstlisting}") else _unicode_prose(p) for p in parts)

def _unicode_verbatim(block: str) -> str:
    for u, tex in {"≤": "\\le", "≥": "\\ge", "→": "\\rightarrow", "×": "\\times", "≈": "\\approx"}.items():
        block = block.replace(u, "(*@\\ensuremath{" + tex + "}@*)")
    for u, plain in {"—": "--", "–": "-", "“": '"', "”": '"', "‘": "'", "’": "'", "…": "...", "−": "-"}.items():
        block = block.replace(u, plain)
    left = sorted({ch for ch in block if ord(ch) > 127}); assert not left, f"unmapped non-ASCII characters in a verbatim block: {left}"
    return block

def _unicode_prose(body: str) -> str:
    for u, tex in {
        "★": r"\ensuremath{\star}", "†": r"\ensuremath{\dagger}", "≈": r"\ensuremath{\approx}",
        "≥": r"\ensuremath{\ge}", "≤": r"\ensuremath{\le}", "×": r"\ensuremath{\times}",
        "→": r"\ensuremath{\rightarrow}", "●": r"\ensuremath{\bullet}", "ρ": r"\ensuremath{\rho}",
        "σ": r"\ensuremath{\sigma}", "Δ": r"\ensuremath{\Delta}", "−": r"\ensuremath{-}",
        "§": r"\S{}", "…": r"\ldots{}", "—": "---", "–": "--", "ć": r"\'{c}", "ä": r"\"{a}", "é": r"\'{e}",
        "ć": r"\'{c}", "“": "``", "”": "''", "‘": "`", "’": "'",
    }.items():
        body = body.replace(u, tex)
    left = sorted({ch for ch in body if ord(ch) > 127})
    assert not left, f"unmapped non-ASCII characters remain: {left}"
    return body


def tables_to_floats(body: str) -> str:
    """pandoc longtable → table float with the caption above, scaled to the text width when wide."""
    pat = re.compile(
        r"\\begin\{longtable\}\[\]\{(?P<cols>.*?)\}\n"
        r"(?:\\caption\{(?P<cap>.*?)\}\\tabularnewline\n)?"
        r"(?P<rest>.*?)\\end\{longtable\}", re.S)

    def one(m):
        cols, cap, rest = m.group("cols"), m.group("cap"), m.group("rest")
        label = ""
        if cap:
            lm = re.search(r"\\label\{([^}]+)\}", cap)
            if lm:
                label = lm.group(0)
                cap = cap.replace(label, "")
        # keep the first header block only; drop the repeated head and the foot markers
        rest = re.sub(r"\\endfirsthead\n.*?\\endhead\n", "", rest, flags=re.S)
        rest = rest.replace("\\bottomrule\\noalign{}\n\\endlastfoot\n", "")
        assert "\\end" not in rest, "unexpected longtable structure: " + rest[:200]
        rest = rest.strip() + "\n\\bottomrule"
        ncols = cols.count("p{") or len(re.findall(r"[lrc]", cols))   # pandoc emits p{} columns for wrapped tables
        content = lambda r: bool(re.sub(r"\\[A-Za-z]+(\{[^}]*\})*", "", r).strip())   # text left once LaTeX commands are removed
        rows = [r for r in rest.split("\\\\") if "&" in r or (ncols == 1 and content(r))]   # one-column tables have no &
        cells = [[c.strip() for c in r.split("&")] for r in rows]
        maxlen = [max(len(c[i]) for c in cells if len(c) > i) for i in range(ncols)]
        widest_row = max(sum(len(c) for c in row) for row in cells)
        prose = max(maxlen) > 60
        wide = (not prose) and ((ncols >= 6 and widest_row > 60) or ("ballast" in (cap or "")) or ("cos(G,E)" in rest) or widest_row > 90)   # a short many-column table is not scaled up
        if prose:  # prose cells: paragraph columns, widths by content, never scaled
            total = sum(maxlen)
            cols = "".join(">{\\raggedright\\arraybackslash}p{%.2f\\linewidth}" % (0.92 * m / total)   # leaves room for the column padding
                           for m in maxlen)
        tab = "\\begin{tabular}{" + cols + "}\n" + rest + "\n\\end{tabular}"
        if wide:
            tab = "\\shrinktowidth{" + tab + "}"   # shrinks a table wider than the text block; never enlarges a narrow one
        out = "\\begin{table}[htb]\n"
        if cap:
            out += "\\caption{" + cap.strip() + "}\n" + (label + "\n" if label else "")
        out += "\\begin{center}" + ("\\footnotesize" if prose else "\\small") + "\n" + tab + "\n\\end{center}\n\\end{table}"
        return out

    n = len(pat.findall(body))
    body = pat.sub(one, body)
    assert "\\begin{longtable}" not in body, "a longtable survived conversion"
    print(f"{n} tables converted to floats")
    return merge_table_parts(body)


def pair_figures(body: str, left: str, right: str, wl: float, wr: float) -> str:
    """Fold two consecutive single-image figures (by file stem) into one figure with two side-by-side minipages, each
    keeping its own caption, number and label (captions wrap to the minipage width, i.e. sit under their image)."""
    fig = lambda stem: (r"\\begin\{figure\}\[t\]\n\\centering\n\\pandocbounded\{\\includegraphics\[width=[\d.]+\\linewidth\]\{figures/"
                        + stem + r"\.png\}\}\n\\caption\{([^\n]*)\}\n\\label\{([^}]+)\}\n\\end\{figure\}\n")
    m = re.search(fig(left) + r"\n" + fig(right), body)
    assert m, "pair_figures: the two figures are not consecutive: %s, %s" % (left, right)
    cl, ll, cr, lr = m.groups()
    mp = lambda w, stem, cap, lab: ("\\begin{minipage}[t]{%.2f\\linewidth}\\centering\n\\includegraphics[width=\\linewidth]{figures/%s.png}\n"
                                    "\\caption{%s}\\label{%s}\n\\end{minipage}" % (w, stem, cap, lab))
    return body[:m.start()] + "\\begin{figure}[t]\n\\centering\n" + mp(wl, left, cl, ll) + "\\hfill\n" + mp(wr, right, cr, lr) + "\n\\end{figure}\n" + body[m.end():]


def merge_table_parts(body: str) -> str:
    """A table whose caption is exactly PARTBTABLE is folded into the float before it as part (b);
    that float's own tabular gets the label (a). One float, one caption, one table number."""
    marker = "\\caption{PARTBTABLE}\n"
    while marker in body:
        i = body.index(marker)
        start_b = body.rfind("\\begin{table}[htb]\n", 0, i)
        end_b = body.index("\\end{table}", i) + len("\\end{table}")
        part_b = body[start_b:end_b]
        m = re.search(r"\\begin\{center\}(\\footnotesize|\\small)\n(.*?)\n\\end\{center\}", part_b, flags=re.S)
        size_b, tab_b = m.group(1), m.group(2)
        prev_end = body.rfind("\\end{table}", 0, start_b) + len("\\end{table}")
        prev_start = body.rfind("\\begin{table}[htb]\n", 0, prev_end)
        part_a = body[prev_start:prev_end]
        # parts are stacked with a small gap and no (a)/(b) labels: the caption names them and the reader sees which is which
        between = body[prev_end:start_b].strip()          # a paragraph written between the parts stays with them, above the next part
        lead = ("\\begin{flushleft}" + size_b + " " + between + "\\end{flushleft}\n") if between else ""
        part_a2 = part_a.replace("\\end{center}\n\\end{table}", "\\end{center}\n\\vspace{4pt}" + lead + "\\begin{center}" + size_b + "\n" + tab_b + "\n\\end{center}\n\\end{table}")
        body = body[:prev_start] + part_a2 + body[end_b:]
        print("merged a part-(b) table into the float before it")
    return body



# ------------------------------------------------ heat tables (YlGnBu, as in the arXiv build)
_YLGNBU = [(255,255,217),(237,248,177),(199,233,180),(127,205,187),(65,182,196),(29,145,192),(34,94,168),(37,52,148),(8,29,88)]
def _cellcolor(v, vmin, vmax):
    t = min(max((v - vmin) / (vmax - vmin), 0.0), 1.0) * (len(_YLGNBU) - 1)
    i = min(int(t), len(_YLGNBU) - 2); f = t - i
    r, g, b = (round(_YLGNBU[i][k] + f * (_YLGNBU[i + 1][k] - _YLGNBU[i][k])) for k in range(3))
    fg = "1A1A1A" if (0.299 * r + 0.587 * g + 0.114 * b) / 255 > 0.55 else "EEF3F8"   # off-white with a hint of the cell blue, near-black on light cells: softer than pure white and black
    return "%02X%02X%02X" % (r, g, b), fg

# caption substring -> (vmin, vmax); every numeric cell of a matching table is coloured by its leading number
HEAT = {"Final leaderboard": (0.0, 10.0), "Anchor-sweep consistency": (0.0, 1.0),
        "Per-criterion generator quality": (0.0, 10.0), "by contest composition": (0.0, 10.0), "aggregation ladder": (0.0, 1.0),
        "on the full roster and on the leading eight": (0.0, 1.0),
        "three full re-runs": [(0.0, 10.0), (0.0, 10.0), (0.0, 10.0), (0.0, 1.0)],          # T1, T2, T3 on the rubric; SD in rating points
        "two instruments side by side": [(0.0, 10.0), (0.0, 100.0)],                       # T anchored 1-10; GPQA accuracy in %
        "Evaluator factual competence": [(0.0, 1.0), (0.0, 10.0), None, (0.0, 10.0), None]}  # loading; anchored; CI; G^F; CI
_NUM = re.compile(r"^\s*(?:\\textbf\{)?(-?\d+(?:\.\d+)?)")

def heat_cell(cell, vmin, vmax):
    m = _NUM.match(cell)
    if not m or "%" in cell and vmax == 10.0:
        return cell
    v = float(m.group(1))
    if vmax == 10.0 and v > 10.0:   # a rank or a count in a rating table: leave it
        return cell
    bg, fg = _cellcolor(v, vmin, vmax)
    return "\\cellcolor[HTML]{%s}\\textcolor[HTML]{%s}{%s}" % (bg, fg, cell.strip())

def heat_tables(body):
    def one(m):
        cap, tab = m.group(1), m.group(2)
        rng = next((r for k, r in HEAT.items() if k in cap), None)
        if not rng:
            return m.group(0)
        lines = tab.split("\n"); out = []; header = True
        for ln in lines:
            if "\\midrule" in ln: header = False
            if header or "&" not in ln:
                out.append(ln); continue
            cells = ln.split("&"); tail = ""
            if cells[-1].rstrip().endswith("\\\\"):
                cells[-1] = cells[-1].rstrip()[:-2]; tail = " \\\\"
            first = cells[0]
            vm = rng if "SD" not in lines[1] else rng
            ranges = rng if isinstance(rng, list) else [rng] * (len(cells) - 1)
            assert len(ranges) >= len(cells) - 1, ("per-column ranges do not cover the table", cap[:40])
            out.append(first + "&" + "&".join(c if r is None else heat_cell(c, *r) for c, r in zip(cells[1:], ranges)) + tail)
        return m.group(0).replace(tab, "\n".join(out))
    return re.sub(r"\\caption\{(.*?)\}\n(?:\\label\{[^}]*\}\n)?\\begin\{center\}\\small\n(?:\\shrinktowidth\{)?(\\begin\{tabular\}.*?\\end\{tabular\})", one, body, flags=re.S)

def postfix(body: str) -> str:
    body = tables_to_floats(body)
    body = heat_tables(body)
    body = body.replace("\\pandocbounded{\\includegraphics[keepaspectratio]{",
                        "\\includegraphics[width=\\linewidth]{")
    def fig(m):
        name = Path(m.group(1)).stem
        w = {**FIGURE_WIDTHS, **(ARXIV_FIGURE_WIDTHS if ARXIV else {})}[name]
        return "\\includegraphics[width=%.2f\\linewidth]{%s}" % (w, m.group(1))
    body = re.sub(r"\\includegraphics(?:\[.*?\])?\{([^}]+)\}", fig, body, flags=re.S)
    body = body.replace("\\begin{figure}\n", "\\begin{figure}[t]\n")
    body = re.sub(r"\\begin\{figure\}\[t\](\n\\centering\n(?:\\pandocbounded\{)?\\includegraphics\[[^\]]*\]\{figures/game_example\.png)", r"\\begin{figure}[p]\1", body)   # Figure 1: its own page
    body = re.sub(r"(\\includegraphics\[[^\]]*\]\{figures/game_example\.png\}\}?)\n(\\caption\{)", r"\1\n\\vspace{-14pt}\n\2", body)   # Figure 1: caption tight under the exhibit
    for s in ("AI use statement", "Ethics statement", "Reproducibility statement"):
        body = re.sub(r"\\section\{" + s + r"\}\\label\{[^}]*\}", r"\\subsection*{" + s + "}", body)
    body = re.sub(r"\\section\{References\}\\label\{[^}]*\}",
                  r"\\section*{References}\n\\begingroup\\small\\setlength{\\parindent}{-1.5em}"
                  r"\\setlength{\\leftskip}{1.5em}", body)
    # move the pandoc span-labels that precede a float into the float, after its caption
    body = re.sub(r"\\protect\\phantomsection\\label\{(tab-[^}]+)\}\{\}\n\n(\\begin\{table\}\[htb\]\n\\caption\{.*?\}\n)",
                  r"\2\\label{\1}\n", body, flags=re.S)
    body = re.sub(r"\\protect\\phantomsection\\label\{(fig-[^}]+)\}\{\}\n\n(\\begin\{figure\}.*?\\caption\{.*?\}(?:\\label\{[^}]*\})?\n)",
                  r"\2\\label{\1}\n", body, flags=re.S)
    for _m in re.finditer(r"\\protect\\phantomsection\\label\{(tab-|fig-)[^}]+\}", body):
        raise SystemExit("a float label was not moved into its float: " + body[_m.start():_m.start() + 400].replace("\n", " | "))
    if not ARXIV: body = pair_figures(body, "total_validation_simple", "mechanism_sketch", 0.36, 0.62)  # §4.5: plot beside the sketch
    assert "\\appendix" in body, "appendix marker lost"
    body = body.replace("\\begin{verbatim}", "\\begin{lstlisting}").replace("\\end{verbatim}", "\\end{lstlisting}")
    body = body.replace("\\_", "\\_\\allowbreak{}")
    return unicode_fixes(body)


PREAMBLE = r"""\documentclass{article}
\usepackage[T1]{fontenc}   % tectonic (XeTeX) defaults to TU, under which Times (ptm) has no shapes and the text falls back to Latin Modern without bold
\usepackage{iclr2027_conference,times}
\usepackage{hyperref}
\usepackage{url}
\usepackage{amsmath,amssymb}
\usepackage{graphicx}
\usepackage{booktabs,longtable,array,calc}
\newsavebox{\shrinkbox}\newcommand{\shrinktowidth}[1]{\sbox{\shrinkbox}{#1}\ifdim\wd\shrinkbox>\linewidth\resizebox{\linewidth}{!}{\usebox{\shrinkbox}}\else\usebox{\shrinkbox}\fi}
\usepackage{xcolor}
\usepackage{colortbl}
\usepackage{float}
\usepackage{listings}
\lstset{breaklines=true,breakatwhitespace=false,basicstyle=\ttfamily\scriptsize,columns=fullflexible,keepspaces=true,extendedchars=true,escapeinside={(*@}{@*)}}
\providecommand{\tightlist}{\setlength{\itemsep}{0pt}\setlength{\parskip}{0pt}}
\providecommand{\pandocbounded}[1]{#1}
\providecommand{\real}[1]{#1}
\graphicspath{{./}{figures/}}
%\iclrfinalcopy % Uncomment for camera-ready version, but NOT for submission.
"""


# --------------------------------------------------------------- 5. assemble
def arxiv_edits(md: str) -> str:
    for s in ARXIV_DROP_SECTIONS:
        i = md.index("\n## " + s); j = md.index("\n## ", i + 1); md = md[:i] + md[j:]
    md = md.replace("(anonymised repository, supplementary material)", "(%s, `reproduce/`)" % ARXIV_REPO)
    for a, b_ in ARXIV_FIGURE_SWAPS.items(): md = md.replace(a, b_)
    return md

def prune_uncited_references(md: str) -> str:
    """Drop reference entries that the text being built never cites (surname within 40 characters of the year), and say so.
    A version that drops a section (arXiv drops the Ethics statement) thereby drops the references cited only there."""
    i = md.index("\n## References\n"); j = md.index("\n## ", i + 1) if "\n## " in md[i + 1:] else len(md)
    head, refs, tail = md[:i], md[i:j], md[j:]
    body = head + tail; kept, dropped = [], []
    for para in refs.split("\n\n"):
        m = re.match(r"([A-Za-zÀ-ž'\-]+)[^\n]*?\((\d{4})\)", para.strip())
        if m and not re.search(re.escape(m.group(1)) + r"[^\n]{0,40}" + m.group(2), body): dropped.append(f"{m.group(1)} ({m.group(2)})"); continue
        kept.append(para)
    if dropped: print("references not cited in this version, dropped from its list:", ", ".join(dropped))
    return head + "\n\n".join(kept) + tail

def main() -> None:
    title, combined = combine()
    if ARXIV:
        combined = arxiv_edits(combined); (BUILD / "_paper_combined.md").write_text(combined)
    combined = prune_uncited_references(combined); (BUILD / "_paper_combined.md").write_text(combined)
    guard(combined)
    pandoc = subprocess.run(
        ["pandoc", "-f", "markdown+pipe_tables+tex_math_dollars+raw_tex", "-t", "latex",
         "--wrap=none", "--columns=4000", "--top-level-division=section", "--shift-heading-level-by=-1", "--no-highlight",
         str(BUILD / "_paper_combined.md")],
        check=True, capture_output=True, text=True).stdout
    body = postfix(pandoc)
    body = re.sub(r"(\\(?:sub)*section)\{\d+(?:\.\d+)* ", r"\1{", body)  # drop hand-typed numbers
    body = body.replace("\\section{Abstract}\\label{abstract}", "\\begin{abstract}", 1)
    assert "\\section{Introduction}" in body, "no Introduction section after the abstract"
    body = body.replace("\\section{Introduction}", "\\end{abstract}\n\\section{Introduction}", 1)
    if ARXIV:
        tex = (PREAMBLE.replace("%\\iclrfinalcopy", "\\iclrfinalcopy") + "\\title{" + title + "}\n\\author{" + ARXIV_AUTHOR + "}\n\\begin{document}\n\\maketitle\n"
               + "\\lhead{Preprint. arXiv:" + ARXIV_ID + " v3, September 2026.}\n" + body + "\n\\end{document}\n")
    else:
        tex = (PREAMBLE + "\\title{" + title + "}\n\\author{Anonymous}\n\\begin{document}\n\\maketitle\n"
               + body + "\n\\end{document}\n")
    # attach the end-of-main-text label to the conclusion's last paragraph, so its page is the page that paragraph ends on
    assert "\n\n\\subsection*{AI use statement}" in tex
    tex = tex.replace("\n\n\\subsection*{AI use statement}", "\\label{endmain}\n\n\\subsection*{AI use statement}", 1)
    i = tex.index("\\appendix")
    tex = tex[:i] + tex[i:].replace("\\begin{table}[htb]", "\\begin{table}[H]").replace("\\begin{figure}[t]", "\\begin{figure}[H]")
    guard(tex)
    import shutil
    OUT = ROOT / ("submission-arxiv" if ARXIV else "submission-iclr")
    OUT.mkdir(exist_ok=True); (OUT / "figures").mkdir(exist_ok=True)
    for f in STYLE.glob("*.sty"): shutil.copy(f, OUT / f.name)
    for name in set(re.findall(r"\\includegraphics\[[^\]]*\]\{figures/([^}]+)\}", tex)): shutil.copy(FIGS / name, OUT / "figures" / name)
    (OUT / "paper.tex").write_text(tex)

    r = subprocess.run(["tectonic", "-k", "--keep-logs", "-Z", "search-path=.", "paper.tex"],
                       cwd=OUT, capture_output=True, text=True)
    log = (OUT / "paper.log").read_text() if (OUT / "paper.log").exists() else r.stderr
    if r.returncode != 0:
        print(r.stderr[-4000:])
        raise SystemExit("tectonic failed")
    aux = (OUT / "paper.aux").read_text()
    m = re.search(r"\\newlabel\{endmain\}\{\{[^}]*\}\{(\d+)\}", aux)
    assert m, "endmain label not found in paper.aux — the AI use statement heading was not emitted"
    end_page = int(m.group(1))
    overfull = len(re.findall(r"Overfull \\hbox", log))
    print(f"paper.pdf built. Main text ends on page {end_page} (limit {PAGE_LIMIT}); "
          f"{overfull} overfull hboxes; {len(re.findall(r'LaTeX Warning: Reference', log))} unresolved refs.")
    if end_page > PAGE_LIMIT:
        raise SystemExit(f"OVER THE PAGE LIMIT: main text runs to page {end_page}, limit is {PAGE_LIMIT}")
    FINAL = ROOT / "paper" / ("metanym_game_arxiv_v3.pdf" if ARXIV else "metanym_game_iclr27.pdf"); shutil.move(str(OUT / "paper.pdf"), str(FINAL)); print(f"PDF: {FINAL}")
    if ARXIV:
        import tarfile
        with tarfile.open(OUT / "metanym_game_v3_arxiv.tar.gz", "w:gz") as tar:
            for f in ["paper.tex"] + [p.name for p in OUT.glob("*.sty")]: tar.add(OUT / f, arcname=f)
            tar.add(OUT / "figures", arcname="figures")
        print(f"arXiv sources: {OUT / 'metanym_game_v3_arxiv.tar.gz'}")


if __name__ == "__main__":
    main()
