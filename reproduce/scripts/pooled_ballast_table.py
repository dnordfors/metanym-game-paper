#!/usr/bin/env python3
"""Appendix A.6 table on the pooled corpus: each seat's anchored E^F by contest composition (0-3 ballast blocks,
mean over the seven contestants) beside the twelve-evaluator pooled reference; mean |delta| at two blocks."""
import os, sys, statistics as st
from pathlib import Path
import numpy as np
PKG = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PKG / "scripts")); os.chdir(PKG)
from ballast_sizing import build, ef, COUNCIL, MODELS
DIRS = {1: "data/probe_K_20260529T014133Z", 2: "data/regenerations/probe_K_anchor7_20260619T015828Z", 3: "data/regenerations/probe_K_anchor7_20260619T040659Z"}
runs = [int(x) for x in os.environ.get("RUNS", "1,2,3").split(",")]
Rs, by, off, targets = [], {}, 0, set()
for r in runs:
    R, b, t = build(DIRS[r]); Rs.append(R); targets |= set(t)
    for k, v in b.items(): by.setdefault(k, []).extend(i + off for i in v)
    off += R.shape[1]
R = np.concatenate(Rs, axis=1); targets = [m for m in MODELS if m in targets]
council_t = [m for m in COUNCIL if m in targets]; contestants = [m for m in MODELS if m not in COUNCIL]
pool = sorted([m for m in targets if m not in COUNCIL], key=lambda t: float(np.nanmean(R[:, by[t]])))
ref, _ = ef(R, list(range(R.shape[1])), MODELS)
C = lambda ts: [i for t in ts for i in by[t]]
tab = {s: [] for s in COUNCIL}; lows = {}
for n in range(4):
    base = council_t + [b for b in pool[:n] if b not in council_t]; lows[n] = []
    per = {s: [] for s in COUNCIL}
    for c in contestants:
        v, _ = ef(R, C(base + ([c] if c not in base else [])), COUNCIL + [c])
        for s in COUNCIL: per[s].append(v[s])
        lows[n].append(min(COUNCIL, key=lambda m: v[m]))
    for s in COUNCIL: tab[s].append(st.mean(per[s]))
print(f"pooled runs {runs}; ballast order {pool[:3]}")
print(f"{'seat':20}{'council alone':>15}{'+1':>8}{'+2':>8}{'+3':>8}{'all 12':>8}")
for s in sorted(COUNCIL, key=lambda s: -ref[s]):
    print(f"{s:20}" + "".join(f"{x:8.2f}" for x in tab[s]) + f"{ref[s]:8.2f}")
d2 = st.mean(abs(tab[s][2] - ref[s]) for s in COUNCIL); print(f"mean |delta| at two blocks (seat means): {d2:.2f}; lowest seat per contest at two blocks: {lows[2]}")
