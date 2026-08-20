#!/usr/bin/env python3
"""Build submission/paper.tex + paper.pdf from paper/metanym_game.md and the appendices.

Pipeline (all deterministic):
  1. combine  — manuscript body + appendices A–D (stubs replaced by full text),
                figure paths re-pointed to submission/figures, REVIEW comments dropped
  2. pandoc   — markdown -> latex fragment (--wrap=none; computed table widths)
  3. postfix  — LTcaptype shim, breakable underscores and \\texttt paths,
                \\RaggedRight table columns (hyphenation on)
  4. tables   — every longtable becomes an unbreakable [H] float; the numeric tables
                are re-set as YlGnBu heat tables (the arXiv-v1 style, heattables.py);
                the metanym tables get a no-wrap slot column; the leaderboard gets a
                page of its own
  5. assemble — preamble.tex + body + \\end{document}; compile with tectonic

Run from the repo root:  python3 submission/build_paper.py
The preamble lives in submission/preamble.tex (hand-tuned; never regenerated).
"""
import io
import re
import subprocess
import sys
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parent.parent
SUB = ROOT / "submission"
MD = ROOT / "paper" / "metanym_game.md"
APPENDICES = ["A_rating_estimators.md", "B_generation_and_evaluation_prompts.md",
              "C_council_evaluation_gemini-2.5-flash.md", "D_gpqa_audit.md"]
try:
    from matplotlib import colormaps
    cmap = colormaps["YlGnBu"]
except ImportError:
    from matplotlib import cm
    cmap = cm.get_cmap("YlGnBu")

# ---------------------------------------------------------------- 1. combine
def combine():
    md = MD.read_text()
    i = md.find("## Appendices")
    parts = [md[:i], "## Appendices\n"]
    for f in APPENDICES:
        t = (ROOT / "paper" / "appendices" / f).read_text()
        t = re.sub(r"<!--.*?-->\s*", "", t, flags=re.S)
        t = re.sub(r"^(#+)", r"#\1", t, flags=re.M)
        parts.append(t.strip() + "\n")
    c = "\n".join(parts)
    c = c.replace("](../reproduce/figures/", "](figures/")
    c = c.replace("](../submission/figures/", "](figures/")
    c = re.sub(r"<!-- REVIEW.*?-->\s*", "", c, flags=re.S)
    (SUB / "_paper_combined.md").write_text(c)
    return c

# ---------------------------------------------------------------- 3. postfix
def postfix(body):
    body = body.replace("\\def\\LTcaptype{none}", "\\relax")
    body = body.replace("\\_", "\\_\\allowbreak{}")
    body = body.replace(">{\\raggedright\\arraybackslash}",
                        ">{\\RaggedRight\\arraybackslash\\hspace{0pt}}")
    body = body.replace("★", "\\(\\star\\)")
    def tt(m):
        inner = m.group(1)
        if "/" in inner:
            inner = inner.replace("/", "/\\allowbreak{}")
        return "\\texttt{" + inner + "}"
    return re.sub(r"\\texttt\{([^{}]*(?:\{[^{}]*\}[^{}]*)*)\}", tt, body)

# ------------------------------------------------- 4. heat-table helpers (v1)
def cellcolor(v, vmin, vmax):
    t = float(np.clip((v - vmin) / (vmax - vmin), 0.0, 1.0))
    r, g, b, _ = cmap(t)
    bg = "%02X%02X%02X" % (int(r * 255), int(g * 255), int(b * 255))
    fg = "000000" if (0.299 * r + 0.587 * g + 0.114 * b) > 0.55 else "FFFFFF"
    return bg, fg

def datacell(v, vmin, vmax, fmt="{:.2f}"):
    if v is None:
        return r"\cellcolor[HTML]{EEEEEE}\textcolor[HTML]{777777}{n/a}"
    bg, fg = cellcolor(v, vmin, vmax)
    return r"\cellcolor[HTML]{%s}\textcolor[HTML]{%s}{%s}" % (bg, fg, fmt.format(v))

def num(x):
    x = x.strip().replace("**", "").replace("†", "")
    return None if x.lower() in ("n/a", "na", "—", "-", "") else float(x)

def clean(s):
    return (s.replace("**", "").replace("★", r"$\star$").replace("⎯", "")
             .strip().replace("_", r"\_"))

def clean_math(s):
    return s.replace("**", "").replace("★", r"$\star$").strip()

def split_val_ci(s):
    m = re.match(r"([-\d.]+)\s*(\[.*\])?", s.strip().replace("**", ""))
    return float(m.group(1)), (m.group(2) or "")

def md_rows(combined, anchor, pred):
    lines = combined.splitlines()
    s = next(i for i, l in enumerate(lines) if anchor in l)
    out = []
    for l in lines[s:]:
        if not l.startswith("|"):
            if out:
                break
            continue
        c = [x.strip() for x in l.strip("|").split("|")]
        if pred(c):
            out.append(c)
        elif out:
            if all(x and set(x) <= set("⎯—-–: ") for x in c):
                continue
            break
    return out

def wrap(caption, body):
    return ("\\begin{table}[H]\n\\centering\n\\caption{%s}\n\\par\\nobreak\\smallskip\n"
            "{\\tablefont\\footnotesize\\setlength{\\tabcolsep}{0pt}"
            "\\renewcommand{\\arraystretch}{1.5}\n%s\n}\n\\end{table}" % (caption, body))

def wrap_page(caption, body, heading="Final leaderboard"):
    return ("\\clearpage\n\\begingroup\\centering\\null\\vfill\n"
            "{\\tablefont\\LARGE\\bfseries %s\\par}\\smallskip\n"
            "\\captionof{table}{%s}\\par\\medskip\n"
            "{\\tablefont\\normalsize\\setlength{\\tabcolsep}{0pt}"
            "\\renewcommand{\\arraystretch}{1.7}\n%s\\par}\n"
            "\\vfill\\endgroup\\clearpage" % (heading, caption, body))

def replace_longtable(tex, marker, newblock):
    pat = re.compile(r"(?:\{\\relax % do not increment counter\n)?"
                     r"\\begin\{longtable\}.*?\\end\{longtable\}\n?\}?", re.S)
    n = [0]
    def repl(m):
        if marker in m.group(0) and n[0] == 0:
            n[0] += 1
            return newblock
        return m.group(0)
    tex2 = pat.sub(repl, tex)
    assert n[0] == 1, f"no longtable matched marker {marker!r}"
    return tex2

# ------------------------------------------------------------ heated tables
def build_consistency(md):
    rows = md_rows(md, "| Evaluator | factual | beauty",
                   lambda c: len(c) == 7 and any(ch.isalpha() for ch in c[0]) and "Evaluator" not in c[0])
    axes = ["factual", "beauty", "intel", "distinct", "length", "struct"]
    hdr = (r"\multicolumn{1}{l}{\textbf{Evaluator}} & "
           + " & ".join(r"\multicolumn{1}{c}{\textbf{%s}}" % a for a in axes) + r"\\")
    L = [r"\begin{tabular}{B H!{\vrule width 1pt} H H H H H}", r"\toprule", hdr, r"\midrule"]
    for i, r in enumerate(rows):
        L.append(clean(r[0]) + " & " + " & ".join(datacell(num(x), 0.0, 1.0) for x in r[1:]) + r"\\")
    L += [r"\bottomrule", r"\end{tabular}"]
    return wrap("Anchor-sweep consistency, per evaluator and axis.", "\n".join(L))

def build_GE(md):
    rows = md_rows(md, "| ★ claude-opus-4.5 | 7.0",
                   lambda c: len(c) == 11 and any(ch.isalpha() for ch in c[0]) and "Model" not in c[0])
    data = [r for r in rows if "cos" not in r[0].lower()]
    cosrow = next((r for r in rows if "cos" in r[0].lower()), None)
    crit = ["beauty", "intel", "distinct", "length", "struct"]
    top = (r"\multicolumn{1}{l}{} & "
           + " & ".join(r"\multicolumn{2}{c}{\textbf{%s}}" % c for c in crit) + r"\\")
    sub = (r"\multicolumn{1}{l}{\textbf{Model}} & "
           + " & ".join([r"\multicolumn{1}{c}{$G$} & \multicolumn{1}{c}{$E$}"] * 5) + r"\\")
    L = [r"\begin{tabular}{B HH" + "!{\\vrule width 1pt}HH" * 4 + r"}",
         r"\toprule", top, sub, r"\midrule"]
    for r in data:
        L.append(clean(r[0]) + " & "
                 + " & ".join(datacell(num(x), 0.0, 10.0, "{:.1f}") for x in r[1:]) + r"\\")
    if cosrow:
        cells = [x.strip().replace("**", "") for x in cosrow[1:]]
        cos = [cells[i] for i in (0, 2, 4, 6, 8)]
        cis = [cells[i] for i in (1, 3, 5, 7, 9)]
        L.append(r"\midrule")
        L.append(r"\textbf{cos(G,E)} & "
                 + " & ".join(r"\multicolumn{2}{c}{\textbf{%s}}" % c for c in cos) + r"\\")
        L.append(r"{\footnotesize 95\% CI} & "
                 + " & ".join(r"\multicolumn{2}{c}{\footnotesize %s}" % c for c in cis) + r"\\")
    L += [r"\bottomrule", r"\end{tabular}"]
    return wrap("Per-criterion generator quality (G) vs evaluator reliability (E).", "\n".join(L))

def build_leaderboard(md):
    rows = md_rows(md, "| Rank | Model | Council | **$T$",
                   lambda c: len(c) == 6 and c[0].strip().isdigit())
    cs = (r"{>{\centering\arraybackslash}m{1.0cm} B >{\centering\arraybackslash}m{1.6cm}"
          r"!{\vrule width 1pt} >{\centering\arraybackslash}m{1.5cm} >{\centering\arraybackslash}m{2.4cm} "
          r">{\centering\arraybackslash}m{1.5cm} >{\centering\arraybackslash}m{1.5cm}}")
    hdr = (r"\multicolumn{1}{c}{\textbf{Rank}} & \multicolumn{1}{l}{\textbf{Model}} & "
           r"\multicolumn{1}{c}{\textbf{Council}} & \multicolumn{1}{c}{\textbf{$T$}} & "
           r"\multicolumn{1}{c}{\textbf{95\% CI}} & \multicolumn{1}{c}{\textbf{$E$}} & "
           r"\multicolumn{1}{c}{\textbf{$G$}}\\")
    L = [r"\begin{tabular}" + cs, r"\toprule", hdr, r"\midrule"]
    prev = "council"
    for rank, model, council, tcell, e, g in rows:
        cl = "council" if "council" in council else "--"
        if prev == "council" and cl != "council":
            L.append(r"\midrule[\heavyrulewidth]")
        prev = cl
        tval, tci = split_val_ci(tcell)
        L.append(clean(rank) + " & " + clean(model) + " & " + cl + " & "
                 + datacell(tval, 0, 10) + " & " + tci + " & "
                 + datacell(num(e), 0, 10) + " & " + datacell(num(g), 0, 10) + r"\\")
    L += [r"\bottomrule", r"\end{tabular}"]
    cap = (r"Total rating \(T\) (95\% CI) with its evaluator (\(E\)) and generator (\(G\)) "
           r"halves; all twelve models ranked, council seats marked. The anchor "
           r"(claude-opus-4.5) is 7 by construction.")
    return wrap_page(cap, "\n".join(L))

def build_breakdown(md):
    rows = md_rows(md, "| Rank | Model | Council? | $G^{F}$",
                   lambda c: len(c) == 7 and c[0].strip().isdigit())
    top = (r"\multicolumn{3}{l}{} & \multicolumn{2}{c}{\textbf{generation}} & "
           r"\multicolumn{2}{c}{\textbf{evaluation}}\\")
    sub = (r"\multicolumn{1}{l}{\textbf{\#}} & \multicolumn{1}{l}{\textbf{Model}} & "
           r"\multicolumn{1}{l}{\textbf{Council}} & \multicolumn{1}{c}{$G^{F}$} & \multicolumn{1}{c}{$G^{C}$} & "
           r"\multicolumn{1}{c}{$E^{F}$} & \multicolumn{1}{c}{$E^{C}$}\\")
    L = [r"\begin{tabular}{>{\centering\arraybackslash}m{0.6cm} B >{\centering\arraybackslash}m{1.3cm} "
         r"HH!{\vrule width 1pt}HH}", r"\toprule", top, sub, r"\midrule"]
    prev = "council"
    for rank, model, council, gf, gc, ef, ec in rows:
        cl = "council" if "council" in council else "--"
        if prev == "council" and cl != "council":
            L.append(r"\midrule[\heavyrulewidth]")
        prev = cl
        cells = [datacell(num(x), 0, 10) for x in (gf, gc, ef, ec)]
        L.append(clean(rank) + " & " + clean(model) + " & " + cl + " & " + " & ".join(cells) + r"\\")
    L += [r"\bottomrule", r"\end{tabular}"]
    return wrap(r"Competence breakdown --- the four anchored components behind each model's "
                r"evaluator (\(E\)) and generator (\(G\)) scores.", "\n".join(L))

def build_critA(md):
    rows = md_rows(md, "| Model | $E^{F}$ loading",
                   lambda c: len(c) == 6 and "Model" not in c[0] and "---" not in c[0]
                   and any(ch.isalnum() for ch in c[0]))
    cs = (r"{B >{\centering\arraybackslash}m{1.5cm} >{\centering\arraybackslash}m{1.6cm} "
          r">{\centering\arraybackslash}m{1.8cm}!{\vrule width 1pt} "
          r">{\centering\arraybackslash}m{1.1cm} >{\centering\arraybackslash}m{1.8cm}}")
    hdr = (r"\multicolumn{1}{l}{\textbf{Model}} & "
           r"\multicolumn{1}{c}{\textbf{\shortstack{$E^{F}$\\loading}}} & "
           r"\multicolumn{1}{c}{\textbf{\shortstack{$E^{F}$\\anchored}}} & "
           r"\multicolumn{1}{c}{\textbf{95\% CI}} & "
           r"\multicolumn{1}{c}{\textbf{$G^{F}$}} & \multicolumn{1}{c}{\textbf{95\% CI}}\\")
    L = [r"\begin{tabular}" + cs, r"\toprule", hdr, r"\midrule"]
    for model, load, anch, eci, gf, gci in rows:
        dag = r"$\dagger$" if "†" in anch else ""
        L.append(clean(model) + " & " + datacell(num(load), 0, 1) + " & "
                 + datacell(num(anch), 0, 10) + dag + " & " + clean(eci) + " & "
                 + datacell(num(gf), 0, 10) + " & " + clean(gci) + r"\\")
    L += [r"\bottomrule", r"\end{tabular}"]
    return wrap("Evaluator factual competence and generator factuality (key-free SVD).", "\n".join(L))

def build_vendor(md):
    rows = md_rows(md, "| Evaluator set | Spearman",
                   lambda c: len(c) == 4 and "Evaluator set" not in c[0] and "---" not in c[0] and c[0].strip())
    cs = (r"{>{\raggedright\arraybackslash}m{3.7cm} >{\centering\arraybackslash}m{2.0cm} "
          r">{\centering\arraybackslash}m{2.6cm} >{\centering\arraybackslash}m{2.2cm}}")
    hdr = (r"\multicolumn{1}{l}{\textbf{Evaluator set}} & "
           r"\multicolumn{1}{c}{\textbf{\shortstack{Spearman\\vs full}}} & "
           r"\multicolumn{1}{c}{\textbf{\shortstack{Claude\\generators}}} & "
           r"\multicolumn{1}{c}{\textbf{\shortstack{GPT-4o\\family}}}\\")
    L = [r"\begin{tabular}" + cs, r"\toprule", hdr, r"\addlinespace[2pt]\midrule"]
    for panel, sp, cla, gpt in rows:
        L.append(clean_math(panel) + " & " + datacell(num(sp), 0, 1) + " & "
                 + clean_math(cla) + " & " + clean_math(gpt) + r"\\")
    L += [r"\bottomrule", r"\end{tabular}"]
    return wrap("Same-vendor robustness of the factual ordering.", "\n".join(L))

def build_council(md):
    rows = md_rows(md, "| Council member | Factual competence",
                   lambda c: len(c) == 3 and "Council member" not in c[0] and "---" not in c[0])
    cs = (r"{B >{\centering\arraybackslash}m{1.2cm} >{\centering\arraybackslash}m{2.0cm}!{\vrule width 1pt} "
          r">{\centering\arraybackslash}m{1.2cm} >{\centering\arraybackslash}m{2.0cm}}")
    hdr = (r"\multicolumn{1}{l}{\textbf{Council member}} & \multicolumn{2}{c}{\textbf{Factual competence}} & "
           r"\multicolumn{2}{c}{\textbf{Rating consistency}}\\")
    sub = (r"\multicolumn{1}{l}{} & \multicolumn{1}{c}{} & \multicolumn{1}{c}{95\% CI} & "
           r"\multicolumn{1}{c}{} & \multicolumn{1}{c}{95\% CI}\\")
    L = [r"\begin{tabular}" + cs, r"\toprule", hdr, sub, r"\midrule"]
    for member, fac, crit in rows:
        fv, fci = split_val_ci(fac)
        cv, cci = split_val_ci(crit)
        L.append(clean(member) + " & " + datacell(fv, 0, 0.6) + " & " + clean(fci)
                 + " & " + datacell(cv, 0, 1) + " & " + clean(cci) + r"\\")
    L += [r"\bottomrule", r"\end{tabular}"]
    return wrap("The initial council --- the five reliable evaluators.", "\n".join(L))

def build_gpqa_side(md):
    rows = md_rows(md, "| Model | $T$ | GPQA",
                   lambda c: len(c) == 3 and "Model" not in c[0] and "---" not in c[0] and c[0].strip())
    cs = (r"{B >{\centering\arraybackslash}m{1.8cm} >{\centering\arraybackslash}m{2.6cm}}")
    hdr = (r"\multicolumn{1}{l}{\textbf{Model}} & \multicolumn{1}{c}{\textbf{$T$}} & "
           r"\multicolumn{1}{c}{\textbf{GPQA Diamond (\%)}}\\")
    L = [r"\begin{tabular}" + cs, r"\toprule", hdr, r"\midrule"]
    for model, t, q in rows:
        L.append(clean(model) + " & " + datacell(num(t), 0, 10) + " & "
                 + datacell(num(q), 0, 100, "{:.1f}") + r"\\")
    L += [r"\bottomrule", r"\end{tabular}"]
    return wrap(r"The two instruments side by side --- the key-free total rating \(T\) "
                r"(§4.7) and self-administered GPQA Diamond accuracy (voids counted as "
                r"wrong), sorted by \(T\).", "\n".join(L))

def build_reruns(md):
    rows = md_rows(md, "| Model | $T_1$",
                   lambda c: len(c) == 5 and "Model" not in c[0] and "---" not in c[0] and c[0].strip())
    cs = (r"{B >{\centering\arraybackslash}m{1.35cm} >{\centering\arraybackslash}m{1.35cm} "
          r">{\centering\arraybackslash}m{1.35cm}!{\vrule width 1pt} >{\centering\arraybackslash}m{1.35cm}}")
    hdr = (r"\multicolumn{1}{l}{\textbf{Model}} & \multicolumn{1}{c}{\textbf{$T_1$}} & "
           r"\multicolumn{1}{c}{\textbf{$T_2$}} & \multicolumn{1}{c}{\textbf{$T_3$}} & "
           r"\multicolumn{1}{c}{\textbf{SD}}\\")
    L = [r"\begin{tabular}" + cs, r"\toprule", hdr, r"\midrule"]
    for model, t1, t2, t3, sd in rows:
        L.append(clean(model) + " & " + " & ".join(datacell(num(x), 0, 10) for x in (t1, t2, t3))
                 + " & " + datacell(num(sd), 0, 1) + r"\\")
    L += [r"\bottomrule", r"\end{tabular}"]
    return wrap(r"Total rating \(T\) across three full re-runs (run 1 = the bootstrap "
                r"generation, re-analysed on the council basis; runs 2--3 the same day), "
                r"all on the council basis of §4.7.", "\n".join(L))

def build_ballast(md):
    rows = md_rows(md, "| Seat | council alone",
                   lambda c: len(c) == 6 and "Seat" not in c[0] and "---" not in c[0] and c[0].strip())
    cols = ["council alone", "+1 ballast", "+2 ballast", "+3 ballast", r"all 12 (§4.2)"]
    cs = (r"{B >{\centering\arraybackslash}m{1.55cm} >{\centering\arraybackslash}m{1.45cm}"
          r"!{\vrule width 1.2pt} >{\centering\arraybackslash}m{1.45cm}!{\vrule width 1.2pt} "
          r">{\centering\arraybackslash}m{1.45cm} >{\centering\arraybackslash}m{1.6cm}}")
    hdr = (r"\multicolumn{1}{l}{\textbf{Seat}} & "
           + " & ".join(r"\multicolumn{1}{c}{\textbf{\shortstack{%s}}}" % c.replace(" ", r"\\")
                        for c in cols) + r"\\")
    L = [r"\begin{tabular}" + cs, r"\toprule", hdr, r"\midrule"]
    for r in rows:
        L.append(clean(r[0]) + " & "
                 + " & ".join(datacell(num(x), 0, 10) for x in r[1:]) + r"\\")
    L += [r"\bottomrule", r"\end{tabular}"]
    cap = (r"Each seat's anchored \(E^{F}\) by contest composition --- 0--3 ballast blocks "
           r"(mean over the seven possible contestants) beside the reference from all 12 "
           r"participants (§4.2). Council alone, the column is scrambled; from two ballast "
           r"on, the contest reproduces the reference (mean \(|\Delta|\) 0.33 over the seven "
           r"contests, and the same seat is lowest in all seven). The ruled column is the "
           r"protocol's configuration. Values from \texttt{scripts/ballast\_sizing.py} via "
           r"\texttt{scripts/plot\_ballast\_heatmap.py}.")
    return wrap(cap, "\n".join(L))

# ---------------------------------------------- metanym tables (no-wrap slots)
def metanym_table(block):
    """Re-set a 6-column metanym longtable: natural no-wrap slot column,
    domains share the rest; footnotesize, unbreakable [H] float."""
    capm = re.search(r"\\caption\{(.*?)\}\\tabularnewline", block, re.S)
    caption = capm.group(1) if capm else None
    body_part = block.split("\\endlastfoot", 1)[1]
    rows = [l for l in body_part.splitlines()
            if "&" in l and "\\end{longtable}" not in l]
    hdrm = re.findall(r"\\begin\{minipage\}[^\n]*\n(.*?)\n\\end\{minipage\}", block, re.S)
    headers = [h.strip() for h in hdrm[:6]] or None
    def slotlen(r):
        c = r.split("&")[0]
        c = c.replace("\\_\\allowbreak{}", "_").replace("\\allowbreak{}", "")
        c = c.replace("\\_", "_").replace("\\", "").replace("{", "").replace("}", "")
        return len(c.strip())
    slot_chars = max((slotlen(r) for r in rows), default=12)
    slotw = f"{slot_chars * 5.3 + 3:.0f}pt"
    dom = r">{\RaggedRight\arraybackslash\hspace{0pt}}p{\dimexpr(\linewidth-%s-12\tabcolsep)/5\relax}" % slotw
    cs = "{>{\\arraybackslash}p{%s} %s}" % (slotw, " ".join([dom] * 5))
    L = [r"\begin{tabular}" + cs, r"\toprule"]
    if headers:
        L.append(r"\multicolumn{1}{l}{\textbf{%s}} & " % headers[0]
                 + " & ".join(r"\textbf{%s}" % h for h in headers[1:]) + r"\\")
        L.append(r"\midrule")
    L += rows
    L += [r"\bottomrule", r"\end{tabular}"]
    inner = ("{\\tablefont\\scriptsize\\setlength{\\tabcolsep}{3pt}"
             "\\renewcommand{\\arraystretch}{1.3}\n" + "\n".join(L) + "\n}")
    if caption:
        return ("\\begin{table}[H]\n\\centering\n\\caption{%s}\n\\par\\nobreak\\smallskip\n%s\n\\end{table}"
                % (caption, inner))
    return "\\begin{center}\n" + inner + "\n\\end{center}"

def fix_metanym_tables(tex):
    pat = re.compile(r"(?:\{\\relax % do not increment counter\n)?"
                     r"\\begin\{longtable\}.*?\\end\{longtable\}\n?\}?", re.S)
    n = [0]
    def repl(m):
        block = m.group(0)
        first_cells = re.search(r"\\endlastfoot\s*\n([A-Z\\_{}]+) &", block)
        if first_cells and ("NAVIGATOR" in block or "INTERDEPENDENCY" in block
                            or "PERTURBATION" in block or "\\{SLOT" in block
                            or re.search(r"\\endlastfoot\s*\n[A-Z]{4,}", block)):
            n[0] += 1
            return metanym_table(block)
        return block
    tex2 = pat.sub(repl, tex)
    return tex2, n[0]

# ------------------------------------- remaining longtables -> [H] tabulars
def unbreak_rest(tex):
    pat = re.compile(r"(?:\{\\relax % do not increment counter\n)?"
                     r"\\begin\{longtable\}(\[\])?\{(.*?)\}\n(.*?)\\end\{longtable\}\n?\}?", re.S)
    n = [0]
    def repl(m):
        spec, inner = m.group(2), m.group(3)
        capm = re.search(r"\\caption\{(.*?)\}\\tabularnewline", inner, re.S)
        caption = capm.group(1) if capm else None
        if "\\endlastfoot" not in inner:
            return m.group(0)
        if "\\endfirsthead" in inner:
            head_part = inner.split("\\endfirsthead", 1)[0]
        else:
            head_part = inner.split("\\endhead", 1)[0]
        body = inner.split("\\endlastfoot", 1)[1]
        head = head_part
        if capm:
            head = head.replace(capm.group(0), "")
        head = head.replace("\\noalign{}", "")
        body = body.replace("\\noalign{}", "")
        n[0] += 1
        tab = ("\\begin{tabular}{" + spec + "}\n" + head.strip() + "\n"
               + body.strip() + "\n\\end{tabular}")
        inner_block = ("{\\tablefont\\small\\setlength{\\tabcolsep}{4pt}\n" + tab + "\n}")
        if caption:
            return ("\\begin{table}[H]\n\\centering\n\\caption{%s}\n\\par\\nobreak\\smallskip\n%s\n\\end{table}"
                    % (caption, inner_block))
        return "\\begin{center}\n" + inner_block + "\n\\end{center}"
    return pat.sub(repl, tex), n[0]

# -------------------------------------------------------------------- main
def main():
    md = combine()
    subprocess.run(["/opt/homebrew/bin/pandoc", "_paper_combined.md", "-f", "markdown", "-t", "latex",
                    "--wrap=none", "-o", "_body.tex"], cwd=SUB, check=True)
    body = (SUB / "_body.tex").read_text()
    body = postfix(body)

    # heat the numeric tables (marker = a distinctive cell/caption substring)
    body = replace_longtable(body, "Anchor-sweep consistency, per evaluator and axis", build_consistency(md))
    body = replace_longtable(body, "Per-criterion generator quality", build_GE(md))
    body = replace_longtable(body, "Final leaderboard --- total rating", build_leaderboard(md))
    for marker, builder in [
        ("Competence breakdown --- the four anchored components", build_breakdown),
        ("Evaluator factual competence and generator factuality (key-free SVD)", build_critA),
        ("Same-vendor robustness of the factual ordering", build_vendor),
        ("The initial council --- the five reliable evaluators", build_council),
        ("The two instruments side by side", build_gpqa_side),
        ("across three full re-runs", build_reruns),
        ("by contest composition", build_ballast),
    ]:
        body = replace_longtable(body, marker, builder(md))

    body, nm = fix_metanym_tables(body)
    body, nr = unbreak_rest(body)
    print(f"tables: heated 10, metanym-set {nm}, unbroken {nr}")

    tex = (SUB / "preamble.tex").read_text() + body + "\n\\end{document}\n"
    (SUB / "paper.tex").write_text(tex)
    r = subprocess.run(["/opt/homebrew/bin/tectonic", "-X", "compile", "paper.tex"], cwd=SUB,
                       capture_output=True, text=True)
    over = re.findall(r"Overfull \\hbox \(([\d.]+)pt", r.stderr)
    errs = [l for l in r.stderr.splitlines() if l.startswith("error")]
    print("errors:", errs or "none")
    print("overfull:", sorted(set(float(x) for x in over), reverse=True)[:6] or "none")
    if errs:
        sys.exit(1)

if __name__ == "__main__":
    main()
