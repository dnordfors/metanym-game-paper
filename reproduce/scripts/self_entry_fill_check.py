#!/usr/bin/env python3
"""Appendix A.2 (ICLR version) — robustness of the factual SVD to the self-entry convention. The published matrix fills an
evaluator's own cells (and any missing cell) with the anchor value 7 (A5). This check refills them with the evaluator's own row
mean, so they vanish under row-centering, recomputes the pooled components, and reports: ranking by E^F, the largest change in a
loading, and Pearson r of the total T with GPQA under both fills. No API calls. Prints the comparison; asserts the manuscript's
three claims (same ranking; loadings within 0.04; r moved by less than 0.01)."""
import sys, csv, inspect, numpy as np
from pathlib import Path
HERE = Path(__file__).resolve().parent; PKG = HERE.parent; sys.path.insert(0, str(HERE))
import pooled_components as PC
src = inspect.getsource(PC.components)
src = src.replace("F = np.full((len(panel), len(cols)), 7.0)", "F = np.full((len(panel), len(cols)), np.nan)")
src = src.replace("    rowmean = F.mean(1); Fc = F - rowmean[:, None]", "    F = np.where(np.isnan(F), np.nanmean(F, 1)[:, None], F); rowmean = F.mean(1); Fc = F - rowmean[:, None]")
assert "nanmean" in src; ns = dict(PC.__dict__); exec(src.replace("def components(", "def components_rowmean("), ns)
GAs = PC.load_runs([1, 2, 3]); graded = PC.graded_targets(GAs); atoms = PC.scoring_atoms(GAs, graded)
A = PC.components(GAs, graded, atoms, PC.MODELS); B = ns["components_rowmean"](GAs, graded, atoms, PC.MODELS)
rows = lambda p: [r for r in csv.DictReader(l for l in open(p) if not l.lstrip('"').startswith("#"))]
gpqa = {r["model"]: float(r["gpqa_diamond_accuracy"]) for r in rows(PKG / "data/gpqa_selfadministered.csv")}
def T(c, m): return np.mean([c["GF"][m], c["GC"][m], c["EF"][m], c["EC"][m]])
ms = [m for m in PC.MODELS if m in gpqa]; ra, rb = (np.corrcoef([T(c, m) for m in ms], [gpqa[m] for m in ms])[0, 1] for c in (A, B))
rank = lambda c: sorted(ms, key=lambda m: -c["EF"][m]); dload = max(abs(A["EFload"][m] - B["EFload"][m]) for m in ms)
print(f"{'model':22s} {'E^F fill 7':>10s} {'E^F row-mean':>13s} {'load 7':>7s} {'load rm':>8s}")
for m in rank(A): print(f"{m:22s} {A['EF'][m]:10.2f} {B['EF'][m]:13.2f} {A['EFload'][m]:7.3f} {B['EFload'][m]:8.3f}")
print(f"E^F ranking identical: {rank(A) == rank(B)}; largest loading change {dload:.3f}; T vs GPQA r = {ra:.3f} (fill 7) vs {rb:.3f} (row mean)")
assert rank(A) == rank(B) and dload <= 0.04 and abs(ra - rb) < 0.01, "the A.2 robustness sentence no longer holds"
