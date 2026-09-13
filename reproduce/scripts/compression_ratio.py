#!/usr/bin/env python3
"""§6 (ICLR version) — the literal-space compression of the metanym form, measured on the anchor submission's first
archetype (submissions/anchor_claude-opus-4.5.md, the one archetype shipped in full): words of the five idiomatic
rewrites (Form b) against the words of the context template plus the metanym table; and the marginal factor, words of
one rewrite against one metanym set. Words = maximal runs of letters, digits, apostrophes and hyphens."""
import re
from pathlib import Path
s = (Path(__file__).resolve().parent.parent / "submissions/anchor_claude-opus-4.5.md").read_text()
sec = s[s.index("## Archetype Proposal"):s.index("## The remaining four archetypes")]
template = sec[sec.index("### Context-template"):sec.index("### Metanym table")].split("\n", 1)[1].strip()
table = sec[sec.index("### Metanym table"):sec.index("### Bacterial Chemotaxis")]
rows = [l for l in table.splitlines() if l.startswith("|") and not set(l) <= set("|-: ")][1:]   # slot rows, header dropped
fa = re.findall(r"\*\*Instantiation \(Form a\):\*\*\s*\n(.+?)\n", sec); fb = re.findall(r"\*\*Idiomatic rewrite \(Form b\):\*\*\s*\n(.+?)\n", sec)
w = lambda t: len(re.findall(r"[A-Za-z0-9'’-]+", t))
tw, sets, n = w(template), sum(w(r) for r in rows), len(fb)
print(f"anchor, first archetype: template {tw} words; metanym table {sets} words for {n} contexts ({sets/n:.0f} per context)")
print(f"Form b rewrites: {[w(x) for x in fb]} words (mean {sum(w(x) for x in fb)/n:.0f}); Form a instantiations: {[w(x) for x in fa]}")
print(f"factor at {n} contexts: Form b {sum(w(x) for x in fb)/(tw+sets):.1f}, Form a {sum(w(x) for x in fa)/(tw+sets):.1f}")
print(f"marginal factor per added context (rewrite words / metanym-set words): Form b {sum(w(x) for x in fb)/sets:.1f}, Form a {sum(w(x) for x in fa)/sets:.1f}")
