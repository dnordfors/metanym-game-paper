"""Per-run contests (runs apart), two ballast blocks: with two ballast, is a contestant's contest-basis E^F higher than its
twelve-basis E^F on the same run, and does it outrank a seat it should not?"""
import sys, os, statistics as st
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import numpy as np
from ballast_sizing import build, ef, COUNCIL, MODELS, ANCHOR
from pathlib import Path
RUNS = {"run1": Path("data/probe_K_20260529T014133Z"),
        "run2": Path("data/regenerations/probe_K_anchor7_20260619T015828Z"),
        "run3": Path("data/regenerations/probe_K_anchor7_20260619T040659Z")}
B = int(os.environ.get("B", 300))
for name, run in RUNS.items():
    R, by, targets = build(run)
    council_t = [m for m in COUNCIL if m in targets]
    contestants = [m for m in MODELS if m not in COUNCIL]
    pool = sorted([m for m in targets if m not in COUNCIL], key=lambda t: float(np.nanmean(R[:, by[t]])))
    ballast = pool[:2]
    ref, sep12 = ef(R, list(range(R.shape[1])), MODELS)
    rng = np.random.default_rng(20260912)
    print(f"\n{name}: twelve-basis sigma1/sigma2={sep12:.2f}; ballast={ballast}")
    print(f"{'contestant':22}{'E^F contest':>12}{'95% CI':>16}{'E^F twelve':>11}{'diff':>7}{'s1/s2':>7}{'spread':>8}{'low seat':>9}  outranks seats (contest / twelve)")
    for c in contestants:
        base = council_t + [b for b in ballast if b not in council_t]
        cols_t = base + ([c] if c not in base else [])
        cols = [i for t in cols_t for i in by[t]]
        v, sep = ef(R, cols, COUNCIL + [c])
        seats = {m: v[m] for m in COUNCIL}
        spread = max(seats.values()) - min(seats.values())
        boots = []
        for _ in range(B):
            rc = [i for t in cols_t for i in rng.choice(by[t], len(by[t]), replace=True)]
            vb, _ = ef(R, rc, COUNCIL + [c]); boots.append(vb[c])
        lo, hi = np.nanpercentile(boots, [2.5, 97.5])
        n_c = sum(v[c] > seats[m] for m in COUNCIL); n_12 = sum(ref[c] > ref[m] for m in COUNCIL)
        print(f"{c:22}{v[c]:>12.2f}{f'[{lo:.2f}, {hi:.2f}]':>16}{ref[c]:>11.2f}{v[c]-ref[c]:>7.2f}{sep:>7.2f}{spread:>8.2f}{min(seats.values()):>9.2f}  {n_c} / {n_12}")
