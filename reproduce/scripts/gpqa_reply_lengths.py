#!/usr/bin/env python3
"""§6 (ICLR version) — how the models answered GPQA with the reasoning channel off: words per reply
(median, min, max) and the number of bare-letter replies (< 15 words), per model, from the shipped records."""
import json, glob, statistics as st, os
from pathlib import Path
root = sorted(glob.glob(str(Path(__file__).resolve().parent.parent / "data/gpqa_runs/gpqa_*")))[0]
print(f"{'model':22}{'median words':>13}{'min':>6}{'max':>7}{'bare-letter replies':>21}{'n':>5}")
tot = 0; bare_tot = 0
for m in sorted(glob.glob(f"{root}/*")):
    if not os.path.isdir(m): continue
    R = json.load(open(f"{m}/responses.json")); w = [len((r["raw_text"] or "").split()) for r in R]
    bare = sum(1 for x in w if x < 15); tot += len(w); bare_tot += bare
    print(f"{m.split('/')[-1]:22}{st.median(w):>13.0f}{min(w):>6}{max(w):>7}{bare:>21}{len(w):>5}")
print(f"bare-letter replies in all: {bare_tot} of {tot}")
