#!/usr/bin/env python3
"""Appendix H.2 (ICLR version) — the literal compression of the metanym form, averaged over every archetype in the shipped
raw portfolios of runs 2 and 3 (data/regenerations/portfolios_run{2,3}/). For each archetype whose template, metanym table
and five Form (a) instantiations parse: words in the template, in each domain's metanym set (its column of the table), and
in each Form (a) instantiation. Reports the instantiation / metanym-set ratio (the limit of the compression factor
n·F/(T + n·M) as domains n grow), the factor at the five contexts of one game, and the per-model ratios. Word = a run of
letters/digits (hyphens and apostrophes inside a word kept). No API calls."""
import re, glob, statistics as st
from pathlib import Path
PKG = Path(__file__).resolve().parent.parent
W = lambda s: len(re.findall(r"[A-Za-z0-9][A-Za-z0-9'’\-]*", s))
recs = []
for run in (2, 3):
    for f in sorted(glob.glob(str(PKG / f"data/regenerations/portfolios_run{run}/*.md"))):
        m = Path(f).name.split("_off")[0]; s = open(f).read()
        for p in re.split(r"^##+\s*Archetype(?:al context)?(?: Proposal)?\s*\d*\s*[:—-]?\s*", s, flags=re.M)[1:]:
            t = re.search(r"(?:context[- ]template|^#+\s*\d?\.?\s*template)\**:?\s*\n+(.+?)(?=\n#+|\n\*\*Metanym|\nMetanym)", p, re.S | re.I | re.M)
            rows = [l for l in p.splitlines() if l.startswith("|")]
            if not t or len(rows) < 3: continue
            hdr = [c.strip() for c in rows[0].strip("|").split("|")]; nd = len(hdr) - 1; sets = [0] * nd
            for l in rows[2:]:
                cells = [c.strip() for c in l.strip("|").split("|")]
                if len(cells) == len(hdr):
                    for i, v in enumerate(cells[1:]): sets[i] += W(v)
            forms = [W(x) for x in re.findall(r"\*\*Form \(a\)\**:?\**:?[ \t]*\n?\s*(.+?)(?=\n\s*\n|\n\*\*Form|\n#)", p, re.S | re.I)]
            if nd >= 5 and len(forms) >= 5 and all(sets[:5]):
                recs.append((m, run, W(t.group(1)), sets[:5], forms[:5]))
T = [r[2] for r in recs]; M = [x for r in recs for x in r[3]]; F = [x for r in recs for x in r[4]]
ratio = [st.mean(r[4]) / st.mean(r[3]) for r in recs]
print(f"archetypes measured: {len(recs)} from {len({r[0] for r in recs})} models, runs 2 and 3")
print(f"words — template: mean {st.mean(T):.0f} (range {min(T)}–{max(T)}); metanym set per domain: mean {st.mean(M):.1f}; Form (a) instantiation: mean {st.mean(F):.0f}")
print(f"instantiation / metanym set per archetype: mean {st.mean(ratio):.1f}, median {st.median(ratio):.1f}, range {min(ratio):.1f}–{max(ratio):.1f}  (the limit of the compression factor as domains are added)")
print(f"compression factor at the five contexts of one game, 5F/(T+5M) on the means: {5*st.mean(F)/(st.mean(T)+5*st.mean(M)):.2f}")
by = {}
for r, q in zip(recs, ratio): by.setdefault(r[0], []).append(q)
print("per model, mean instantiation / metanym set: " + ", ".join(f"{m} {st.mean(v):.1f}" for m, v in sorted(by.items())))
