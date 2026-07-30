#!/usr/bin/env python3
"""Regenerate the Appendix C and D sections of submission/paper.tex from paper/appendices/.

paper.tex is pandoc output whose preamble was then hand-tuned (fonts loaded by path,
longtable font and centring, custom column types). Regenerating the whole file would
discard that, so this script converts only the two appendix bodies and their stub
descriptions and splices them in, leaving the preamble and the manuscript untouched.

    python3 submission/splice_appendices.py        # rewrites submission/paper.tex in place
    python3 submission/splice_appendices.py -o /tmp/paper.tex

Then build with either engine (both produce the same page count):
    cd submission && tectonic -X compile paper.tex --outdir out
    cd submission && xelatex paper.tex && xelatex paper.tex
"""
import argparse
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TEX = ROOT / "submission" / "paper.tex"
MANUSCRIPT = ROOT / "paper" / "metanym_game.md"
APPENDICES = {
    "C": ROOT / "paper" / "appendices" / "C_anchor_submission.md",
    "D": ROOT / "paper" / "appendices" / "D_council_evaluation_gemini-2.5-flash.md",
}

# Anchors delimiting what we replace. Each appendix contributes a stub (heading +
# one description paragraph, from the manuscript) followed by the appendix body.
# We key on \label{}, which both pandoc 2.x (\hypertarget wrapper) and 3.x (bare
# \subsubsection) emit, so the script stays runnable against its own output.
C_STUB = "appendix-c.-anchor-reference-submission"
C_BODY = "appendix-c.-anchor-reference-submission-claude-opus-4.5"
D_STUB = "appendix-d.-council-evaluation-of-a-target-submission"
D_BODY = "appendix-d.-council-evaluation-of-a-target-submission-gemini-2.5-flash"
AVAIL = "data-and-code-availability"
REFS = "references"
END = r"\end{document}"

# --columns must exceed the widest source table line, or pandoc emits fixed column
# widths that are too narrow for the [SLOT] names and overlap the next column (the
# defect visible in the pre-2026-07 PDFs).
PANDOC = ["pandoc", "-t", "latex", "--wrap=none", "--columns=400"]

# The metanym tables are 6 columns of unequal need: one long slot name, then five
# domain terms. Auto-width (l) columns overrun the text block, so set them
# explicitly. The slot column is sized from its own longest entry, because names
# like ALLOCATION_STRATEGY offer no break point and would otherwise print over the
# next column; the domain cells take what is left and wrap freely.
WIDE_TABLE = "@{}llllll@{}"
TOTAL_WIDTH = 0.895  # \linewidth less the six columns' \tabcolsep
EM_PER_CHAR = 0.0145  # width of one upper-case character, as a fraction of \linewidth
MAX_SLOT_WIDTH = 0.30

# Each appendix body holds exactly one table, and both are numbered exhibits of the
# paper. Their captions and labels live here rather than in paper.tex because this
# script overwrites the bodies wholesale: anything added to paper.tex by hand is lost
# on the next run. The markdown source carries the matching HTML anchor and link.
TABLE_EXHIBITS = {
    "C": (
        "The anchor portfolio's metanym table for its first archetype — ten slots "
        "instantiated across five domains.",
        "tab:anchor-metanym",
    ),
    "D": (
        "The target portfolio's metanym table for its first archetype — fifteen slots "
        "instantiated across five domains.",
        "tab:target-metanym",
    ),
}


def pandoc(*args, stdin=None):
    proc = subprocess.run(PANDOC + list(args), input=stdin, capture_output=True, text=True)
    if proc.returncode:
        sys.exit(f"pandoc failed: {proc.stderr}")
    return proc.stdout.rstrip("\n")


def size_metanym_tables(latex):
    while WIDE_TABLE in latex:
        start = latex.index(WIDE_TABLE)
        body = latex[start : latex.index(r"\end{longtable}", start)]
        slots = [
            line.split("&")[0].strip().replace("\\", "").replace("{", "").replace("}", "")
            for line in body.split("\n")
            if "&" in line and line.rstrip().endswith("\\\\")
        ]
        longest = max((len(s) for s in slots), default=10)
        slot = min(MAX_SLOT_WIDTH, max(0.13, round(longest * EM_PER_CHAR, 4)))
        domain = round((TOTAL_WIDTH - slot) / 5, 4)
        cols = [rf">{{\raggedright\arraybackslash}}p{{{slot}\linewidth}}"]
        cols += [rf">{{\raggedright\arraybackslash}}p{{{domain}\linewidth}}"] * 5
        spec = "@{}\n  " + "\n  ".join(cols) + "@{}"
        print(f"  table: longest slot {longest} chars -> slot {slot}, domains {domain}")
        latex = latex[:start] + spec + latex[start + len(WIDE_TABLE) :]
    return latex


def caption_table(markdown, caption):
    """Give the body's one table a pandoc caption, before conversion.

    Captioning in markdown rather than patching the LaTeX afterwards is what gets the
    \\endfirsthead/\\endhead pair a captioned longtable needs; pandoc writes it for us.
    """
    lines = markdown.split("\n")
    rows = [i for i, l in enumerate(lines) if l.startswith("|")]
    if not rows or rows != list(range(rows[0], rows[-1] + 1)):
        sys.exit("expected exactly one contiguous table in the appendix body")
    lines[rows[-1] + 1 : rows[-1] + 1] = ["", f"Table: {caption}"]
    return "\n".join(lines)


def label_table(latex, label):
    """Label that caption, and resolve the body's link to it into a numbered reference.

    pandoc renders the markdown link [text](#anchor) as \\hyperref[anchor]{text} and
    drops the <a id> that anchor pointed at, so the reference is rewritten to name the
    table number and hang off the \\label instead.
    """
    latex, n = re.subn(
        r"(\\caption\{(?:[^{}]|\{[^{}]*\})*\})(\\tabularnewline)",
        rf"\1\\label{{{label}}}\2",
        latex,
        count=1,
    )
    if n != 1:
        sys.exit(rf"expected one longtable \caption to label {label}, found {n}")
    anchor = re.escape(label.replace(":", "-"))
    latex, n = re.subn(
        rf"\\hyperref\[{anchor}\]\{{([^{{}}]*)\}}", rf"\1 (Table~\\ref{{{label}}})", latex
    )
    if n != 1:
        sys.exit(f"expected one markdown link to #{label.replace(':', '-')}, found {n}")
    return latex


def section(manuscript_lines, heading):
    """The named "## " section of the manuscript, up to the next one."""
    i = manuscript_lines.index(heading)
    j = next(k for k in range(i + 1, len(manuscript_lines)) if manuscript_lines[k].startswith("## "))
    return [l for l in manuscript_lines[i:j]]


def stub_description(manuscript_lines, heading):
    i = manuscript_lines.index(heading)
    j = i + 1
    while not manuscript_lines[j].strip():
        j += 1
    return pandoc(stdin=manuscript_lines[j])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("-o", "--out", type=Path, default=TEX)
    args = ap.parse_args()

    lines = TEX.read_text().split("\n")
    manuscript = MANUSCRIPT.read_text().split("\n")

    def heading(label):
        """Line index at which the sectioning block carrying \\label{label} begins."""
        hits = [
            i
            for i, l in enumerate(lines)
            for m in re.finditer(r"\\label\{([^}]*)\}", l)
            if m.group(1) == label
        ]
        if len(hits) != 1:
            sys.exit(f"expected exactly one \\label{{{label}}} in paper.tex, found {len(hits)}")
        i = hits[0]
        # pandoc 2.x opens the block with a \hypertarget on the preceding line
        return i - 1 if i and lines[i - 1].startswith(r"\hypertarget{") else i

    def description(block_start):
        """Line index of the one-paragraph stub description following a heading block."""
        i = block_start
        while r"\label{" not in lines[i]:
            i += 1
        i += 1
        while not lines[i].strip():
            i += 1
        return i

    c_stub, c_body = heading(C_STUB), heading(C_BODY)
    d_stub, d_body = heading(D_STUB), heading(D_BODY)
    end = next(i for i, l in enumerate(lines) if l.startswith(END))
    if not c_stub < c_body < d_stub < d_body < end:
        sys.exit("appendix anchors are out of order; paper.tex structure has changed")
    c_desc, d_desc = description(c_stub), description(d_stub)

    bodies = {}
    for k, p in APPENDICES.items():
        caption, label = TABLE_EXHIBITS[k]
        body = pandoc("--shift-heading-level-by=2",
                      stdin=caption_table(p.read_text(), caption))
        bodies[k] = label_table(size_metanym_tables(body), label)
    stubs = {
        "C": stub_description(manuscript, "### Appendix C. Anchor (reference) submission"),
        "D": stub_description(manuscript, "### Appendix D. Council evaluation of a target submission"),
    }

    avail, refs = heading(AVAIL), heading(REFS)
    if not avail < refs < c_stub:
        sys.exit("availability/references anchors are out of order")
    avail_latex = pandoc(stdin="\n".join(section(manuscript, "## Data and code availability")))

    # Splice back to front so the earlier indices stay valid.
    lines[d_body:end] = bodies["D"].split("\n") + [""]
    lines[d_desc : d_desc + 1] = stubs["D"].split("\n")
    lines[c_body:d_stub] = bodies["C"].split("\n") + [""]
    lines[c_desc : c_desc + 1] = stubs["C"].split("\n")
    lines[avail:refs] = avail_latex.split("\n") + [""]
    out = "\n".join(lines)

    # pandoc marks uncaptioned longtables \LTcaptype{none}; longtable then bumps a
    # counter of that name, which the 2.x-era preamble never had to define.
    if r"\LTcaptype{none}" in out and r"\newcounter{none}" not in out:
        out = out.replace(
            r"\usepackage{longtable,booktabs}",
            "\\usepackage{longtable,booktabs}\n"
            "% pandoc marks uncaptioned longtables \\LTcaptype{none}; give it a counter to bump\n"
            "\\newcounter{none}",
            1,
        )
    if r"\real{" in out and "{calc}" not in out:
        sys.exit(r"pandoc emitted \real{} but the preamble lacks calc; check --columns")

    args.out.write_text(out)
    print(f"wrote {args.out} ({len(out.splitlines())} lines)")


if __name__ == "__main__":
    main()
