#!/usr/bin/env python3
"""Appendix A competence table on the pooled corpus, twelve-evaluator basis: E^F loading, anchored E^F,
G^F, each with the A.5 atom-bootstrap 95% interval. Env: RUNS, B (1000), SEED."""
import os, sys
from pathlib import Path
import numpy as np
sys.path.insert(0, str(Path(__file__).resolve().parent))
import pooled_components as PC
from pooled_components import MODELS, AM
runs = [int(x) for x in os.environ.get("RUNS", "1,2,3").split(",")]; B = int(os.environ.get("B", 1000))
tag = "pooled" + "".join(map(str, runs)); OUT = Path(__file__).resolve().parent.parent / "data"
GAs = PC.load_runs(runs); graded = PC.graded_targets(GAs); atoms = PC.scoring_atoms(GAs, graded)
pt = PC.components(GAs, graded, atoms, MODELS)
rng = np.random.default_rng(int(os.environ.get("SEED", 20260816))); acc = {m: {"load": [], "EF": [], "GF": []} for m in MODELS}
n = len(atoms)
for _ in range(B):
    c = PC.components(GAs, graded, [atoms[i] for i in rng.integers(0, n, n)], MODELS)
    for m in MODELS:
        acc[m]["load"].append(c["EFload"][m]); acc[m]["EF"].append(c["EF"][m]); acc[m]["GF"].append(c["GF"].get(m, np.nan))
pc = lambda v: np.nanpercentile(v, [2.5, 97.5])
lines = [f"# Appendix A competence table, pooled runs {runs}, twelve-evaluator basis; atom bootstrap B={B}; sigma1/sigma2={pt['gap']:.4f}",
         "# produced by scripts/pooled_criterion_a.py",
         "model,EF_loading,EF_loading_lo95,EF_loading_hi95,EF,EF_lo95,EF_hi95,GF,GF_lo95,GF_hi95"]
print(f"{'model':22}{'loading':>9}{'CI':>16}{'E^F':>7}{'CI':>16}{'G^F':>7}{'CI':>16}")
for m in sorted(MODELS, key=lambda m: -pt["EFload"][m]):
    l = pc(acc[m]["load"]); e = pc(acc[m]["EF"]); g = pc(acc[m]["GF"]); gf = pt["GF"].get(m, np.nan)
    lines.append(f"{m},{pt['EFload'][m]:.4f},{l[0]:.4f},{l[1]:.4f},{pt['EF'][m]:.4f},{e[0]:.4f},{e[1]:.4f},{gf:.4f},{g[0]:.4f},{g[1]:.4f}")
    print(f"{m:22}{pt['EFload'][m]:>9.2f}{f'[{l[0]:.2f}, {l[1]:.2f}]':>16}{pt['EF'][m]:>7.2f}{f'[{e[0]:.2f}, {e[1]:.2f}]':>16}{gf:>7.2f}{f'[{g[0]:.2f}, {g[1]:.2f}]':>16}")
(OUT / f"criterion_a_{tag}.csv").write_text("\n".join(lines) + "\n"); print("wrote", OUT / f"criterion_a_{tag}.csv")
