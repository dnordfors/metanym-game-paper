#!/usr/bin/env python3
"""Pooled corpus, twelve-evaluator basis: (a) same-vendor robustness of the G^F ordering (§4.2) — G^F
recomputed with each vendor's judges removed, Spearman against the full panel; (b) per-criterion G vs E
table with the anchored cosine (A.4/A15) and its atom-bootstrap 95% CI. Env: RUNS, B (1000 for the cosine CI)."""
import os, sys
from pathlib import Path
import numpy as np
from scipy.stats import spearmanr
sys.path.insert(0, str(Path(__file__).resolve().parent))
import pooled_components as PC
from pooled_components import MODELS, AM, AXES5, COUNCIL
B_ = PC.B
runs = [int(x) for x in os.environ.get("RUNS", "1,2,3").split(",")]; B = int(os.environ.get("B", 1000))
tag = "pooled" + "".join(map(str, runs)); OUT = Path(__file__).resolve().parent.parent / "data"
GAs = PC.load_runs(runs); graded = PC.graded_targets(GAs); atoms = PC.scoring_atoms(GAs, graded)
full = PC.components(GAs, graded, atoms, MODELS)
VENDOR = {"Anthropic": [m for m in MODELS if m.startswith("claude")], "Google": [m for m in MODELS if m.startswith("gemini")], "OpenAI": [m for m in MODELS if m.startswith("gpt")]}
gens = [g for g in graded if g != AM]
print(f"same-vendor robustness, pooled runs {runs} (G^F ordering of {len(gens)} generators vs full panel):")
for v, ms in VENDOR.items():
    panel = [m for m in MODELS if m not in ms]
    c = PC.components(GAs, graded, atoms, panel)
    a = [full["GF"][g] for g in gens]; b = [c["GF"].get(g, np.nan) for g in gens]
    ok = [i for i in range(len(gens)) if b[i] == b[i]]
    print(f"  without {v:9} judges ({len(panel)} left): Spearman {spearmanr([a[i] for i in ok],[b[i] for i in ok])[0]:.2f}  (n={len(ok)})  gap {c['gap']:.2f}")
print(f"\nper-criterion G vs E, pooled {tag} (E from the run-1 sweep):")
cos = {ax: B_.cos_anchored([full["Gax"][ax][m] for m in MODELS if full["Gax"][ax].get(m) is not None], [full["Eax"][ax][m] for m in MODELS if full["Gax"][ax].get(m) is not None]) for ax in AXES5}
print(f"{'model':22}" + "".join(f"{ax+' G':>10}{ax+' E':>10}" for ax in AXES5))
for m in B_.GE_ORDER:
    print(f"{m:22}" + "".join(f"{(full['Gax'][ax].get(m) if full['Gax'][ax].get(m) is not None else float('nan')):>10.1f}{full['Eax'][ax][m]:>10.1f}" for ax in AXES5))
print(f"{'cos(G,E)':22}" + "".join(f"{cos[ax]:>10.2f}{'':>10}" for ax in AXES5))
if B:
    rng = np.random.default_rng(20260816); n = len(atoms); acc = {ax: [] for ax in AXES5}
    for _ in range(B):
        c = PC.components(GAs, graded, [atoms[i] for i in rng.integers(0, n, n)], MODELS)
        for ax in AXES5:
            ms = [m for m in MODELS if c["Gax"][ax].get(m) is not None]
            acc[ax].append(B_.cos_anchored([c["Gax"][ax][m] for m in ms], [c["Eax"][ax][m] for m in ms]))
    print(f"\ncos(G,E) 95% CI (B={B}):")
    lines = [f"# per-criterion G vs E and anchored cosine, pooled runs {runs}, twelve basis; cosine CI by atom bootstrap B={B}", "# produced by scripts/pooled_vendor_alignment.py", "axis,cos,cos_lo95,cos_hi95"]
    for ax in AXES5:
        lo, hi = np.nanpercentile(acc[ax], [2.5, 97.5]); print(f"  {ax:9} {cos[ax]:.2f} [{lo:.2f}, {hi:.2f}]"); lines.append(f"{ax},{cos[ax]:.4f},{lo:.4f},{hi:.4f}")
    (OUT / f"alignment_cosine_{tag}.csv").write_text("\n".join(lines) + "\n")
    lines = [f"# per-criterion G (pooled, reliability-weighted council mean) and E (run-1 sweep), runs {runs}", "# produced by scripts/pooled_vendor_alignment.py", "model," + ",".join(f"{ax}_G,{ax}_E" for ax in AXES5)]
    for m in B_.GE_ORDER:
        lines.append(m + "," + ",".join(f"{(full['Gax'][ax].get(m) if full['Gax'][ax].get(m) is not None else float('nan')):.4f},{full['Eax'][ax][m]:.4f}" for ax in AXES5))
    (OUT / f"g_vs_e_{tag}.csv").write_text("\n".join(lines) + "\n")
