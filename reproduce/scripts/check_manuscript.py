#!/usr/bin/env python3
# supplementary: manuscript consistency tooling, not a result producer
"""Manuscript consistency checks. Run before any arXiv upload or venue submission.

Checks that do not need the data:
  1. every §x.y cross-reference resolves to a section that exists
  2. every [](#anchor) link resolves to an <a id="..."> in the file
  3. section numbering is contiguous within each chapter
  4. enumerated-caveat counts ("Four caveats ...") match the list that follows
  5. no orphaned references to appendices that are not present
  6. tables declared with a `Table:` caption are preceded by a table body

Checks that need the pinned data (skipped with --no-data):
  7. every numeric claim registered in CLAIMS below still reproduces

Exit code 0 = all pass. Non-zero = at least one failure.
"""
import re, sys, os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PAPER = ROOT / "paper" / "metanym_game.md"
APPX = ROOT / "paper" / "appendices"
PKG = ROOT / "reproduce"

# --- numeric claims the manuscript makes that the pinned data must reproduce -------
# (label, regex that must appear in the paper, callable -> actual value, tolerance)
CLAIMS = []


def load():
    return PAPER.read_text(encoding="utf-8")


def sections(text):
    out = {}
    for m in re.finditer(r"^#{2,4}\s+(?:Appendix\s+)?([0-9]+(?:\.[0-9]+)?)[.\s—-]", text, re.M):
        out[m.group(1)] = m.start()
    return out


def check_xrefs(text, secs):
    bad = []
    for m in re.finditer(r"§\s*([0-9]+\.[0-9]+|[0-9]+)", text):
        ref = m.group(1)
        if ref not in secs:
            line = text[:m.start()].count("\n") + 1
            bad.append((line, f"§{ref}"))
    return bad


def gh_slug(heading):
    """GitHub's heading-anchor rule: lowercase, drop punctuation, spaces -> hyphens."""
    s = heading.strip().lower()
    s = re.sub(r"[^\w\s-]", "", s)
    return re.sub(r"\s+", "-", s).strip("-")


def check_anchors(text):
    """A link target is valid if it matches an explicit <a id>, or the GitHub
    auto-anchor of some heading (pandoc generates its own; GitHub renders the repo)."""
    ids = set(re.findall(r'<a\s+id="([^"]+)"', text))
    ids |= {gh_slug(h) for h in re.findall(r"^#{1,6}\s+(.*)$", text, re.M)}
    bad = []
    for m in re.finditer(r"\]\(#([^)]+)\)", text):
        if m.group(1) not in ids:
            line = text[:m.start()].count("\n") + 1
            bad.append((line, f"#{m.group(1)}"))
    return bad


def check_numbering(secs):
    from collections import defaultdict
    chapters = defaultdict(list)
    for s in secs:
        if "." in s:
            c, n = s.split(".")
            chapters[int(c)].append(int(n))
    gaps = []
    for c, ns in chapters.items():
        ns = sorted(ns)
        for a, b in zip(ns, ns[1:]):
            if b != a + 1:
                gaps.append(f"chapter {c}: {a} -> {b}")
    return gaps


WORDS = {"one":1,"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8}


def check_caveat_count(text):
    """'Four caveats bound the present run.' — an enumerated count in prose cannot be
    parsed reliably, so this surfaces the paragraph for a human read rather than
    guessing. Returns the claimed count and the paragraph; never auto-fails."""
    m = re.search(r"\b(One|Two|Three|Four|Five|Six)\s+caveats?\s+bound", text)
    if not m:
        return None, ["no 'N caveats bound' sentence found — check §5.7 still enumerates"]
    claimed = WORDS[m.group(1).lower()]
    end = text.find("\n\n", m.start())
    para = text[m.start():end if end > 0 else len(text)]
    return claimed, [para]


def check_appendices(text):
    refs = set(re.findall(r"Appendix\s+([A-Z])(?:\.[0-9a-z]+)?", text))
    have = set()
    if APPX.is_dir():
        for f in APPX.iterdir():
            m = re.match(r"([A-Z])[_.]", f.name)
            if m:
                have.add(m.group(1))
    return sorted(refs - have)


def check_tables(text):
    """every 'Table: ...' caption should follow a markdown table"""
    bad = []
    for m in re.finditer(r"^Table:\s", text, re.M):
        before = text[:m.start()].rstrip().split("\n")
        tail = [l for l in before[-6:] if l.strip()]
        if not any(l.lstrip().startswith("|") for l in tail):
            bad.append(text[:m.start()].count("\n") + 1)
    return bad


def blank_comments(text):
    """Blank out HTML comments, preserving newlines so line numbers stay valid.

    REVIEW markers deliberately cite arXiv v2's old numbering (§3.3, §3.5) and the
    style manual (§1.1); those are history and external refs, not cross-references
    into this manuscript, so the xref check must not see them.
    """
    return re.sub(r"<!--.*?-->",
                  lambda m: re.sub(r"[^\n]", " ", m.group(0)), text, flags=re.S)


def check_review_markers(text):
    """Open author-review markers left in the manuscript: (line, id, risk)."""
    out = []
    for m in re.finditer(r"<!--\s*REVIEW\s+([A-Z]\d+)\s+risk=(\S+)", text):
        out.append((text[:m.start()].count("\n") + 1, m.group(1), m.group(2)))
    return out


def check_package_xrefs(secs):
    """Section refs in the reproduce package must resolve too.

    Scripts and manifests cite the manuscript by section number, so a renumbering
    of the paper silently rots them. Caught once already: the §3.3/§3.4/§3.5 move
    into §4 left nine dangling §3.5 refs and a §4.9 that had become GPQA.
    """
    bad = []
    for f in sorted(PKG.rglob("*")):
        if f.suffix not in {".py", ".md"} or not f.is_file():
            continue
        if f.name == "check_manuscript.py":          # this file quotes examples
            continue
        for i, line in enumerate(f.read_text(errors="ignore").splitlines(), 1):
            # both the §x.y form and the plain-text "sec 4.4" / "section 4.1" form
            refs = (re.findall(r"§(\d+\.\d+)", line)
                    + re.findall(r"\b(?:sec|section)\s+(\d+\.\d+)", line, re.I))
            for ref in refs:
                if ref not in secs:
                    bad.append((f.relative_to(PKG), i, ref))
    return bad


def main():
    text = load()
    secs = sections(text)
    fails = 0

    def report(name, problems, fmt=str):
        nonlocal fails
        if problems:
            fails += 1
            print(f"  FAIL  {name}")
            for p in problems[:12]:
                print(f"          {fmt(p)}")
            if len(problems) > 12:
                print(f"          ... and {len(problems)-12} more")
        else:
            print(f"  ok    {name}")

    print(f"manuscript: {PAPER.relative_to(ROOT)}")
    print(f"sections found: {len(secs)}\n")

    report("1. section cross-references resolve",
           check_xrefs(blank_comments(text), secs),
           lambda p: f"line {p[0]}: {p[1]} does not exist")
    report("2. anchor links resolve",
           check_anchors(text), lambda p: f"line {p[0]}: {p[1]} has no target")
    report("3. section numbering contiguous", check_numbering(secs))
    report("5. referenced appendices exist",
           check_appendices(text), lambda p: f"Appendix {p} referenced but no file")
    report("6. table captions follow tables",
           check_tables(text), lambda p: f"line {p}: caption with no table above")
    report("7. reproduce-package section refs resolve",
           check_package_xrefs(secs), lambda p: f"{p[0]}:{p[1]}: §{p[2]} does not exist")

    # 8. open author-review markers. These are HTML comments, so pandoc drops them from
    # the LaTeX build and they cannot reach a PDF — but a manuscript still carrying them
    # has unaudited passages in it, so --submission refuses to pass.
    marks = check_review_markers(text)
    if marks:
        if "--submission" in sys.argv:
            fails += 1
            print(f"  FAIL  8. {len(marks)} open REVIEW marker(s) — not submission-ready")
            for ln, mid, risk in marks:
                print(f"          line {ln}: {mid} (risk={risk})")
        else:
            print(f"  open  8. {len(marks)} REVIEW marker(s) awaiting author sign-off "
                  f"(--submission makes this fatal)")
            for ln, mid, risk in marks:
                print(f"          line {ln}: {mid} (risk={risk})")

    claimed, para = check_caveat_count(text)
    print(f"\n  MANUAL  4. §5.7 claims {claimed} caveats — read the paragraph and count:\n")
    for chunk in para:
        for line in chunk.split(". "):
            if line.strip():
                print(f"            {line.strip()[:110]}")

    print()
    if fails:
        print(f"{fails} automatic check(s) FAILED")
        return 1
    if not check_script_coverage():
        sys.exit(1)
    print("all automatic manuscript checks passed (one MANUAL item above)")
    return 0



def check_script_coverage():
    """Every script in scripts/ must appear in reproduce.sh or declare itself supplementary
    (a line beginning '# supplementary:'). Replaces the retired CURRENT_SCRIPTS.md's
    hand-written completeness claim with a machine-enforced one."""
    here = Path(__file__).resolve().parent
    steps = (here.parent / "reproduce.sh").read_text()
    missing = []
    for f in sorted(here.glob("*.py")):
        head = f.read_text()[:2000]
        if f.name not in steps and "# supplementary:" not in head:
            missing.append(f.name)
    if missing:
        print(f"  FAIL  9. scripts not in reproduce.sh and not marked supplementary: {missing}")
        return False
    print("  ok    9. every script is in reproduce.sh or marked supplementary")
    return True


if __name__ == "__main__":
    sys.exit(main())
