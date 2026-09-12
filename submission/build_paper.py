#!/usr/bin/env python3
r"""Build submission/paper.tex + paper.pdf from paper/metanym_game_iclr27.md in the ICLR 2027 style.

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
SUB = ROOT / "submission"
MD = ROOT / "paper" / "metanym_game_iclr27.md"
APPENDIX_DIR = ROOT / "paper" / "appendices"
PAGE_LIMIT = int(sys.argv[sys.argv.index("--limit") + 1]) if "--limit" in sys.argv else 9

# Figure widths as a fraction of the text width, keyed by file stem (KeyError = unlisted figure).
FIGURE_WIDTHS = {"council_evaluation_pc1": 0.36, "total_validation": 0.46, "total_validation_simple": 0.32, "anchoring_resolution": 0.6, "runs_panel": 1.0}

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
    c = c.replace("](../submission/figures/", "](figures/")
    c = re.sub(r'<a id="([^"]+)"></a>', r"[]{#\1}", c)  # survives pandoc as \label
    (SUB / "_paper_combined.md").write_text(c)
    return title, c


# ------------------------------------------------------------------ 2. guard
def guard(text: str) -> None:
    hits = [g for g in ANONYMITY_GUARDS if g.lower() in text.lower()]
    assert not hits, f"double-blind violation — these strings appear in the build: {hits}"


# ----------------------------------------------------------------- 4. postfix
def unicode_fixes(body: str) -> str:
    # The ICLR style uses the 8-bit Times fonts; map the symbols the manuscript uses.
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
        ncols = len(re.findall(r"[lrc]", cols))
        rows = [r for r in rest.split("\\\\") if "&" in r]
        cells = [[c.strip() for c in r.split("&")] for r in rows]
        maxlen = [max(len(c[i]) for c in cells if len(c) > i) for i in range(ncols)]
        widest_row = max(sum(len(c) for c in row) for row in cells)
        prose = max(maxlen) > 60
        wide = (not prose) and (ncols >= 6 or ("ballast" in (cap or "")) or ("cos(G,E)" in rest) or widest_row > 90)
        if prose:  # prose cells: paragraph columns, widths by content, never scaled
            total = sum(maxlen)
            cols = "".join(">{\\raggedright\\arraybackslash}p{%.2f\\linewidth}" % (0.98 * m / total)
                           for m in maxlen)
        tab = "\\begin{tabular}{" + cols + "}\n" + rest + "\n\\end{tabular}"
        if wide:
            tab = "\\resizebox{\\linewidth}{!}{" + tab + "}"
        out = "\\begin{table}[htb]\n"
        if cap:
            out += "\\caption{" + cap.strip() + "}\n" + (label + "\n" if label else "")
        out += "\\begin{center}" + ("\\footnotesize" if prose else "\\small") + "\n" + tab + "\n\\end{center}\n\\end{table}"
        return out

    n = len(pat.findall(body))
    body = pat.sub(one, body)
    assert "\\begin{longtable}" not in body, "a longtable survived conversion"
    print(f"{n} tables converted to floats")
    return body



# ------------------------------------------------ heat tables (YlGnBu, as in the arXiv build)
_YLGNBU = [(255,255,217),(237,248,177),(199,233,180),(127,205,187),(65,182,196),(29,145,192),(34,94,168),(37,52,148),(8,29,88)]
def _cellcolor(v, vmin, vmax):
    t = min(max((v - vmin) / (vmax - vmin), 0.0), 1.0) * (len(_YLGNBU) - 1)
    i = min(int(t), len(_YLGNBU) - 2); f = t - i
    r, g, b = (round(_YLGNBU[i][k] + f * (_YLGNBU[i + 1][k] - _YLGNBU[i][k])) for k in range(3))
    fg = "000000" if (0.299 * r + 0.587 * g + 0.114 * b) / 255 > 0.55 else "FFFFFF"
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
    return re.sub(r"\\caption\{(.*?)\}\n(?:\\label\{[^}]*\}\n)?\\begin\{center\}\\small\n(?:\\resizebox\{\\linewidth\}\{!\}\{)?(\\begin\{tabular\}.*?\\end\{tabular\})", one, body, flags=re.S)

def postfix(body: str) -> str:
    body = tables_to_floats(body)
    body = heat_tables(body)
    body = body.replace("\\pandocbounded{\\includegraphics[keepaspectratio]{",
                        "\\includegraphics[width=\\linewidth]{")
    def fig(m):
        name = Path(m.group(1)).stem
        return "\\includegraphics[width=%.2f\\linewidth]{%s}" % (FIGURE_WIDTHS[name], m.group(1))
    body = re.sub(r"\\includegraphics(?:\[.*?\])?\{([^}]+)\}", fig, body, flags=re.S)
    body = body.replace("\\begin{figure}\n", "\\begin{figure}[t]\n")
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
    assert "phantomsection\\label{tab-" not in body and "phantomsection\\label{fig-" not in body, "a float label was not moved into its float"
    assert "\\appendix" in body, "appendix marker lost"
    body = body.replace("\\begin{verbatim}", "\\begin{lstlisting}").replace("\\end{verbatim}", "\\end{lstlisting}")
    body = body.replace("\\_", "\\_\\allowbreak{}")
    return unicode_fixes(body)


PREAMBLE = r"""\documentclass{article}
\usepackage{iclr2027_conference,times}
\usepackage{hyperref}
\usepackage{url}
\usepackage{amsmath,amssymb}
\usepackage{graphicx}
\usepackage{booktabs,longtable,array,calc}
\usepackage{xcolor}
\usepackage{colortbl}
\usepackage{float}
\usepackage{listings}
\lstset{breaklines=true,breakatwhitespace=false,basicstyle=\ttfamily\scriptsize,columns=fullflexible,keepspaces=true,extendedchars=true}
\providecommand{\tightlist}{\setlength{\itemsep}{0pt}\setlength{\parskip}{0pt}}
\providecommand{\pandocbounded}[1]{#1}
\providecommand{\real}[1]{#1}
\graphicspath{{./}{figures/}}
%\iclrfinalcopy % Uncomment for camera-ready version, but NOT for submission.
"""


# --------------------------------------------------------------- 5. assemble
def main() -> None:
    title, combined = combine()
    guard(combined)
    pandoc = subprocess.run(
        ["pandoc", "-f", "markdown+pipe_tables+tex_math_dollars+raw_tex", "-t", "latex",
         "--wrap=none", "--columns=4000", "--top-level-division=section", "--shift-heading-level-by=-1", "--no-highlight",
         str(SUB / "_paper_combined.md")],
        check=True, capture_output=True, text=True).stdout
    body = postfix(pandoc)
    body = re.sub(r"(\\(?:sub)*section)\{\d+(?:\.\d+)* ", r"\1{", body)  # drop hand-typed numbers
    body = body.replace("\\section{Abstract}\\label{abstract}", "\\begin{abstract}", 1)
    assert "\\section{Introduction}" in body, "no Introduction section after the abstract"
    body = body.replace("\\section{Introduction}", "\\end{abstract}\n\\section{Introduction}", 1)
    tex = (PREAMBLE + "\\title{" + title + "}\n\\author{Anonymous}\n\\begin{document}\n\\maketitle\n"
           + body + "\n\\end{document}\n")
    # attach the end-of-main-text label to the conclusion's last paragraph, so its page is the page that paragraph ends on
    assert "\n\n\\subsection*{AI use statement}" in tex
    tex = tex.replace("\n\n\\subsection*{AI use statement}", "\\label{endmain}\n\n\\subsection*{AI use statement}", 1)
    i = tex.index("\\appendix")
    tex = tex[:i] + tex[i:].replace("\\begin{table}[htb]", "\\begin{table}[H]").replace("\\begin{figure}[t]", "\\begin{figure}[H]")
    guard(tex)
    (SUB / "paper.tex").write_text(tex)

    r = subprocess.run(["tectonic", "-k", "--keep-logs", "-Z", "search-path=style", "-Z", "search-path=.", "paper.tex"],
                       cwd=SUB, capture_output=True, text=True)
    log = (SUB / "paper.log").read_text() if (SUB / "paper.log").exists() else r.stderr
    if r.returncode != 0:
        print(r.stderr[-4000:])
        raise SystemExit("tectonic failed")
    aux = (SUB / "paper.aux").read_text()
    m = re.search(r"\\newlabel\{endmain\}\{\{[^}]*\}\{(\d+)\}", aux)
    assert m, "endmain label not found in paper.aux — the AI use statement heading was not emitted"
    end_page = int(m.group(1))
    overfull = len(re.findall(r"Overfull \\hbox", log))
    print(f"paper.pdf built. Main text ends on page {end_page} (limit {PAGE_LIMIT}); "
          f"{overfull} overfull hboxes; {len(re.findall(r'LaTeX Warning: Reference', log))} unresolved refs.")
    if end_page > PAGE_LIMIT:
        raise SystemExit(f"OVER THE PAGE LIMIT: main text runs to page {end_page}, limit is {PAGE_LIMIT}")


if __name__ == "__main__":
    main()
