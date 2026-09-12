#!/usr/bin/env python3
"""Appendix (runs apart): the four anchored components per run, twelve-evaluator basis — factual quarters and G^C on
the run's own atoms, E^C from run 1's sweep — beside the pooled values; each run's spectral gap; run-to-run agreement
of the regenerated three quarters vs the full T. Writes data/per_run_components.csv."""
import sys, csv, itertools, statistics as st
from pathlib import Path
import numpy as np
from scipy.stats import pearsonr, spearmanr
sys.path.insert(0, str(Path(__file__).resolve().parent))
import pooled_components as PC
from pooled_components import MODELS, COUNCIL
OUT = Path(__file__).resolve().parent.parent / "data"
GAs = PC.load_runs([1, 2, 3]); graded = PC.graded_targets(GAs); allatoms = PC.scoring_atoms(GAs, graded)
ec_atoms = [a for a in allatoms if a[0] == 1]
res = {r: PC.components(GAs, graded, [a for a in allatoms if a[0] == r], MODELS, ec_atoms=ec_atoms) for r in (1, 2, 3)}
res["pooled"] = PC.components(GAs, graded, allatoms, MODELS)
Q = ("GF", "GC", "EF", "EC")
lines = ["# four anchored components per run (twelve-evaluator basis; E^C from the run-1 sweep in every run) and pooled", "# produced by pooled-three-runs/scripts/per_run_components.py", "run,sigma1_sigma2,model,GF,GC,EF,EC,T"]
for k, c in res.items():
    for m in MODELS:
        T, v = PC.T_of(c, m)
        if T is not None:
            lines.append(f"{k},{c['gap']:.4f},{m}," + ",".join(f"{x:.4f}" for x in v) + f",{T:.4f}")
(OUT / "per_run_components.csv").write_text("\n".join(lines) + "\n")
print("spectral gap: " + "  ".join(f"{k}: {c['gap']:.2f}" for k, c in res.items()))
print(f"\n{'model':22}" + "".join(f"{'E^F r'+str(r):>8}" for r in (1,2,3)) + f"{'pooled':>8}   " + "".join(f"{'T r'+str(r):>7}" for r in (1,2,3)) + f"{'pooled':>8}")
for m in sorted(MODELS, key=lambda m: -res["pooled"]["EF"][m]):
    print(f"{m:22}" + "".join(f"{res[r]['EF'][m]:8.2f}" for r in (1,2,3)) + f"{res['pooled']['EF'][m]:8.2f}   " + "".join(f"{(PC.T_of(res[r], m)[0] or float('nan')):7.2f}" for r in (1,2,3)) + f"{(PC.T_of(res['pooled'], m)[0] or float('nan')):8.2f}" + ("   *" if m in COUNCIL else ""))
ms = [m for m in MODELS if all(PC.T_of(res[r], m)[0] is not None for r in (1,2,3))]
print(f"\nrun-to-run agreement over {len(ms)} models (Pearson / Spearman):")
for lab, f in (("E^F alone", lambda c, m: c["EF"][m]), ("regenerated three quarters", lambda c, m: (c["GF"][m]+c["GC"][m]+c["EF"][m])/3), ("full T", lambda c, m: PC.T_of(c, m)[0])):
    cells = []
    for i, j in itertools.combinations((1,2,3), 2):
        a = [f(res[i], m) for m in ms]; b = [f(res[j], m) for m in ms]
        cells.append(f"{i}v{j} {pearsonr(a,b)[0]:.2f}/{spearmanr(a,b)[0]:.2f}")
    print(f"  {lab:28} " + "   ".join(cells))
