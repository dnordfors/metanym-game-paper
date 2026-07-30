#!/usr/bin/env python3
"""N-way generation-robustness comparison across independent benchmark runs.

Usage:
    python compare_runs.py --sweep <run1_sweep_dir> <eval_dir_run1> <eval_dir_run2> [<eval_dir_run3> ...]

For each anchor-7 evaluation directory it rebuilds the leaderboard (reliability weights from the
shared --sweep, since the evaluators are unchanged), then reports per-model total T across all
runs with mean / SD / range (the run-to-run resampling error bar), council membership per run and
whether it is identical across all runs, and the pairwise Pearson + Spearman matrices.
"""
import sys, subprocess, re, os, itertools
from pathlib import Path
import numpy as np

HERE = Path(__file__).resolve().parent
args = sys.argv[1:]
sweep = args[args.index("--sweep") + 1]
evals = [a for i, a in enumerate(args) if a != "--sweep" and (i == 0 or args[i-1] != "--sweep")]

def leaderboard(runs_gen):
    env = {**os.environ, "RUNS_GEN": str(runs_gen), "RUNS_SWEEP": str(sweep)}
    out = subprocess.run([sys.executable, str(HERE / "build_paper1_tables.py")],
                         env=env, capture_output=True, text=True).stdout
    lb = {}
    for m in re.finditer(r'^\s*\d+\s+(\S+)\s+(yes|--)\s+([\d.]+)\s+([\d.]+)\s+([\d.]+)\s*$', out, re.M):
        lb[m.group(1)] = {"council": m.group(2) == "yes", "T": float(m.group(3))}
    if not lb:
        sys.exit(f"could not parse leaderboard for {runs_gen}")
    return lb

def spearman(a, b):
    ra, rb = np.argsort(np.argsort(a)), np.argsort(np.argsort(b))
    return float(np.corrcoef(ra, rb)[0, 1])

LBs = [leaderboard(e) for e in evals]
models = [m for m in LBs[0] if all(m in lb for lb in LBs)]
nrun = len(LBs)
print(f"\n=============  N={nrun} generation robustness  =============")
print(f"{'model':22}" + "".join(f"  T{i+1:>5}" for i in range(nrun)) + f"  {'mean':>6} {'SD':>5} {'range':>6}  seats")
order = sorted(models, key=lambda m: -np.mean([lb[m]['T'] for lb in LBs]))
for m in order:
    Ts = np.array([lb[m]['T'] for lb in LBs])
    seats = "".join("C" if lb[m]['council'] else "·" for lb in LBs)
    print(f"{m:22}" + "".join(f"  {t:6.2f}" for t in Ts)
          + f"  {Ts.mean():6.2f} {Ts.std(ddof=1):5.2f} {Ts.max()-Ts.min():6.2f}  {seats}")

councils = [frozenset(m for m in models if lb[m]['council']) for lb in LBs]
print(f"\ncouncil identical across all {nrun} runs: {len(set(councils)) == 1}")
if len(set(councils)) == 1:
    print(f"  seats: {sorted(councils[0])}")
sd = np.array([np.std([lb[m]['T'] for lb in LBs], ddof=1) for m in models])
print(f"per-model run-to-run SD of T: mean {sd.mean():.2f}, max {sd.max():.2f}")

print("\npairwise Pearson / Spearman of total ratings:")
for i, j in itertools.combinations(range(nrun), 2):
    a = [LBs[i][m]['T'] for m in models]; b = [LBs[j][m]['T'] for m in models]
    print(f"  run{i+1} vs run{j+1}:  Pearson {np.corrcoef(a, b)[0,1]:.3f}   Spearman {spearman(a, b):.3f}")
