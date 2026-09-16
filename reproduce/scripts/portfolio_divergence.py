#!/usr/bin/env python3
"""§6 (ICLR version) — where the regeneration runs 2 and 3 part, and what returns after they part.
Reads the raw generator portfolios of runs 2 and 3 (data/regenerations/portfolios_run{2,3}/<model>_off_T0_r1.md; same
prompt, temperature 0, reasoning off, two hours apart; run 1's portfolios were not preserved) and reports, per model:
  * the number of words the two portfolios share before the first differing word, and the words at the fork;
  * the archetypes (by title) of run 2 that recur in run 3 after the fork;
and over the archetypes a model kept by title: templates verbatim vs rewritten, text similarity, slot names kept,
domains kept, and metanyms identical where a domain and a slot were both kept.
Normalisation: lower-case, punctuation stripped, leading "the " dropped. No API calls."""
import re, glob, difflib, statistics as st
from pathlib import Path
PKG = Path(__file__).resolve().parent.parent
RUNS = {2: PKG / "data/regenerations/portfolios_run2", 3: PKG / "data/regenerations/portfolios_run3"}
norm = lambda t: re.sub(r"^the ", "", re.sub(r"[^a-z ]", "", t.lower()).strip())
HEAD = re.compile(r"^##+\s*Archetype(?:al context)?(?: Proposal)?\s*\d*\s*[:—-]?\s*(.+)$", re.M)
def parse(s):
    """title -> (template text, domains, {slot: {domain: metanym}})"""
    out = {}
    for p in re.split(r"^##+\s*Archetype(?:al context)?(?: Proposal)?\s*\d*\s*[:—-]?\s*", s, flags=re.M)[1:]:
        title = norm(p.splitlines()[0].strip("* #"))
        m = re.search(r"(?:context[- ]template|^#+\s*\d?\.?\s*template)\**:?\s*\n+(.+?)(?=\n#+|\n\*\*Metanym|\nMetanym)", p, re.S | re.I | re.M)
        template = m.group(1).strip() if m else ""
        rows = [l for l in p.splitlines() if l.startswith("|")]
        doms, table = [], {}
        if len(rows) >= 3:
            hdr = [c.strip() for c in rows[0].strip("|").split("|")]; doms = [norm(h) for h in hdr[1:]]
            for l in rows[2:]:
                cells = [c.strip() for c in l.strip("|").split("|")]
                if len(cells) == len(hdr):
                    table[re.sub(r"[^A-Z_ ]", "", cells[0].upper()).strip()] = {d: norm(v) for d, v in zip(doms, cells[1:])}
        if title and (template or table): out[title] = (template, doms, table)
    return out
text = {r: {Path(f).name.split("_off")[0]: open(f).read() for f in sorted(glob.glob(str(d / "*.md")))} for r, d in RUNS.items()}
models = sorted(set(text[2]) & set(text[3]))
print(f"portfolios read: {len(models)} models x 2 runs")
print("\nwhere runs 2 and 3 part (words shared before the first differing word; the fork; archetypes of run 2 recurring in run 3 after the fork):")
after_k = after_n = 0
for m in models:
    a, b = text[2][m], text[3][m]; wa, wb = a.split(), b.split(); k = 0
    while k < min(len(wa), len(wb)) and wa[k] == wb[k]: k += 1
    if k == len(wa) == len(wb):
        print(f"  {m:20} identical ({len(wa)} words)"); continue
    ta = [norm(t.strip('* #')) for t in HEAD.findall(a)]; tb = {norm(t.strip('* #')) for t in HEAD.findall(b)}
    n_before = len(HEAD.findall(" ".join(wa[:k])))  # archetype headings fully inside the shared prefix
    rest = ta[n_before:]; kept = [t for t in rest if t in tb]; after_k += len(kept); after_n += len(rest)
    print(f"  {m:20} {k:5} words shared; fork: {' '.join(wa[k:k+3])!r} vs {' '.join(wb[k:k+3])!r}; archetypes after the fork recurring: {len(kept)}/{len(rest)}")
print(f"  total: {after_k} of {after_n} archetypes recur after the fork (models whose runs part)")
tw = lambda t: set(re.findall(r"[a-z]+", t.lower()))
rows = []
for m in models:
    A, B = parse(text[2][m]), parse(text[3][m])
    for t in sorted(set(A) & set(B)):
        ta, da, Ta = A[t]; tb, db, Tb = B[t]
        same = tot = 0
        for d in set(da) & set(db):
            for s in set(Ta) & set(Tb): tot += 1; same += Ta[s].get(d) == Tb[s].get(d)
        rows.append(dict(m=m, t=t, verbatim=(ta == tb), ratio=difflib.SequenceMatcher(None, ta, tb).ratio(),
                         dk=len(set(da) & set(db)), dn=max(len(da), len(db)), sk=len(set(Ta) & set(Tb)), sn=max(len(Ta), len(Tb)), same=same, tot=tot))
n_all = sum(len(parse(text[2][m])) for m in models)
print(f"\narchetypes kept by title, run 2 -> run 3: {len(rows)} of {n_all}")
verb = [r for r in rows if r["verbatim"]]; rw = [r for r in rows if not r["verbatim"]]
print(f"  template verbatim: {len(verb)} ({', '.join(sorted({r['m'] for r in verb}))}); rewritten: {len(rw)}")
S = lambda rs, a, b: f"{sum(r[a] for r in rs)} of {sum(r[b] for r in rs)}"
print(f"  rewritten templates: median text similarity (difflib ratio) {st.median(r['ratio'] for r in rw):.2f}; slot names kept {S(rw,'sk','sn')}; domains kept {S(rw,'dk','dn')}; metanyms identical where domain and slot both kept {S(rw,'same','tot')}")
print(f"  all kept archetypes: slot names kept {S(rows,'sk','sn')}; domains kept {S(rows,'dk','dn')}; metanyms identical where both kept {S(rows,'same','tot')}")
print("\nper archetype (model, title, template verbatim, similarity, domains kept, slots kept, metanyms identical):")
for r in rows: print(f"  {r['m']:20} {r['t'][:40]:40} {'verbatim' if r['verbatim'] else 'rewritten':9} {r['ratio']:.2f}  {r['dk']}/{r['dn']}  {r['sk']}/{r['sn']}  {r['same']}/{r['tot']}")
