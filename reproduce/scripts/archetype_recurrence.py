#!/usr/bin/env python3
"""§6 (ICLR version) — do the models retrieve archetypes rather than build them? Reads the archetype titles and
parallel-context domains as the evaluation transcripts (eval_*_x_*.md) record them for every graded portfolio in the
three runs (raw portfolios are not shipped; the transcripts copy their headings), and reports:
  * persistence: archetype titles kept verbatim by the same model between runs (run 1 -> 2, three weeks apart; 2 -> 3, two hours apart);
  * recurrence across models: titles used by more than one model; models offering a resource-allocation archetype
    (title containing "allocation"), and the vendors they span; domains used by five or more models.
Normalisation: lower-case, punctuation stripped, leading "the " dropped. No API calls."""
import re, glob, collections
from pathlib import Path
PKG = Path(__file__).resolve().parent.parent
RUNS = {1: PKG / "data/probe_K_20260529T014133Z", 2: PKG / "data/regenerations/probe_K_anchor7_20260619T015828Z", 3: PKG / "data/regenerations/probe_K_anchor7_20260619T040659Z"}
title_re = re.compile(r"^###\s*Archetypal context\s*(\d+)\s*[:—-]\s*(.+?)\s*$", re.M)
pc_re = re.compile(r"^-\s*PC\s*(\d+)\s*\(([^)]+)\)", re.M)
PLACEHOLDER = ("(missing)", "missing", "n/a", "(none)")
norm = lambda t: re.sub(r"^the ", "", re.sub(r"[^a-z ]", "", t.lower()).strip())
port = {}
for run, d in RUNS.items():
    for f in sorted(glob.glob(str(d / "eval_*_x_*.md"))):
        tg = re.match(r".*/eval_(.+)_x_(.+)\.md", f).group(2)
        s = open(f).read(); ts = [t for _, t in title_re.findall(s)][:5]
        if len(ts) == 5 and (run, tg) not in port:
            port[(run, tg)] = ([t for t in ts if t.lower() not in PLACEHOLDER], [p for _, p in pc_re.findall(s)])
models = sorted({tg for _, tg in port}); vendor = lambda m: "Anthropic" if m.startswith("claude") else "Google" if m.startswith("gemini") else "OpenAI"
print(f"portfolios read: {len(port)} ({len(models)} graded models x {len(RUNS)} runs)")
print("\npersistence of archetype titles (kept verbatim / comparable slots):")
tot = {(1, 2): [0, 0], (2, 3): [0, 0]}
for m in models:
    sets = {r: {norm(t) for t in port[(r, m)][0]} for r in RUNS if (r, m) in port}
    cells = []
    for a, b in tot:
        if a in sets and b in sets:
            k, n = len(sets[a] & sets[b]), min(len(sets[a]), len(sets[b])); tot[(a, b)][0] += k; tot[(a, b)][1] += n; cells.append(f"{a}->{b}: {k}/{n}")
    print(f"  {m:22} " + "   ".join(cells))
for (a, b), (k, n) in tot.items(): print(f"  total run {a} -> run {b}: {k} of {n} titles recur verbatim")
by_title = collections.defaultdict(set)
for (r, m), (ts, _) in port.items():
    for t in ts: by_title[norm(t)].add(m)
print(f"\ndistinct titles: {len(by_title)}; used by more than one model: {sum(1 for v in by_title.values() if len(v) > 1)}")
ra = {m for (r, m), (ts, _) in port.items() if any("allocation" in norm(t) for t in ts)}
print(f"models offering a resource-allocation archetype (title contains 'allocation'): {len(ra)} of {len(models)}, vendors {sorted({vendor(m) for m in ra})}: {sorted(ra)}")
dom = collections.defaultdict(set)
for (r, m), (_, ds) in port.items():
    for d in ds: dom[norm(d)].add(m)
print("domains used by five or more models:", [(d, len(v)) for d, v in sorted(dom.items(), key=lambda kv: -len(kv[1])) if len(v) >= 5])
