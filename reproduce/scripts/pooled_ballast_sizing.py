#!/usr/bin/env python3
"""Appendix A.6 ballast sizing on the POOLED factual corpus (mirrors ballast_sizing.py; same measure())."""
import os, sys, collections, statistics as st
from pathlib import Path
import numpy as np
PKG = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PKG / "scripts")); os.chdir(PKG)
import ballast_sizing as BS
from ballast_sizing import build, ef, COUNCIL, MODELS, SEP_LO, SEP_HI, SPREAD_FLOOR
runs = [int(x) for x in os.environ.get("RUNS", "1,2,3").split(",")]
DIRS = {1: "data/probe_K_20260529T014133Z", 2: "data/regenerations/probe_K_anchor7_20260619T015828Z", 3: "data/regenerations/probe_K_anchor7_20260619T040659Z"}
Rs, bys, targets = [], [], set(); off = 0
for r in runs:
    R, by, t = build(DIRS[r]); Rs.append(R); bys.append({k: [i + off for i in v] for k, v in by.items()}); off += R.shape[1]; targets |= set(t)
R = np.concatenate(Rs, axis=1); by = {}
for b in bys:
    for k, v in b.items(): by.setdefault(k, []).extend(v)
targets = [m for m in MODELS if m in targets]
B = int(os.environ.get("B", 600))
council_t = [m for m in COUNCIL if m in targets]; contestants = [m for m in MODELS if m not in COUNCIL]
pool = sorted([m for m in targets if m not in COUNCIL], key=lambda t: float(np.nanmean(R[:, by[t]])))
ref, sep_ref = ef(R, list(range(R.shape[1])), MODELS)
rng = np.random.default_rng(20260811); rs = lambda idx: rng.choice(idx, len(idx), replace=True)
print(f"A.6 ballast sizing on pooled runs {runs}: {R.shape[1]} columns, B={B}")
print(f"reference: twelve-evaluator sigma1/sigma2 = {sep_ref:.2f}, council E^F spread = {max(ref[m] for m in COUNCIL)-min(ref[m] for m in COUNCIL):.2f}")
print(f"ballast candidates, poorest first: {', '.join(pool)}\n")
print(f"{'ballast':10}{'rng(mean)':>11}{'rng(max)':>10}{'sigma1/sigma2':>22}{'spread':>9}{'fidelity':>10}{'guards':>9}   rotations")
dem = {}
for n, label in ((0, "none"), (1, "one"), (2, "two"), (3, "three")):
    b = pool[:n]
    mvm, mvx, sep, sp, fid, lows = BS.measure(R, by, council_t, b, contestants, ref)
    acc = [BS.measure(R, by, council_t, b, contestants, ref, rs) for _ in range(B)]
    lo, hi = np.percentile([a[2] for a in acc], [2.5, 97.5])
    hold = sum(1 for a in acc if SEP_LO <= a[2] <= SEP_HI and a[3] > SPREAD_FLOOR) / B
    print(f"{label:10}{mvm:>11.2f}{mvx:>10.2f}{f'{sep:5.2f} [{lo:4.2f}, {hi:4.2f}]':>22}{sp:>9.2f}{fid:>10.2f}" + (f"{hold:>9.2f}" if n else f"{'--':>9}") + f"   rotate-out->{len(set(lows))}")
    dem[label] = lows
print("\nrotation target per contestant:")
for label, lows in dem.items():
    tally = collections.Counter(lows); print(f"  {label:6} {len(tally)} distinct  |  " + ", ".join(f"{s} x{k}" for s, k in tally.most_common()))
