#!/usr/bin/env python3
"""§4.5 (ICLR version) / Appendix D.1 — do the estimators earn their place? The same ratings aggregated the plain way, against
GPQA Diamond: (1) the un-anchored pass of §4.1 (probe_J), every portfolio's leave-self-out mean over all axes and judges;
(2) the anchored pass at the production anchor (probe_K, run 1), the same plain mean, the anchor itself at 7 by calibration;
(3) the official pooled total T (SVD factual quarters + consistency-weighted criterion quarters). Pearson r and Spearman rho
with the self-administered GPQA accuracies of data/gpqa_selfadministered.csv. Writes data/baseline_aggregators.csv."""
import sys, csv, numpy as np
from pathlib import Path
from scipy.stats import spearmanr
HERE = Path(__file__).resolve().parent; PKG = HERE.parent; sys.path.insert(0, str(HERE))
import plot_anchoring_resolution as PAR
rows = lambda p: [r for r in csv.DictReader(l for l in open(p) if not l.lstrip('"').startswith("#"))]
gpqa = {r["model"]: float(r["gpqa_diamond_accuracy"]) for r in rows(PKG / "data/gpqa_selfadministered.csv")}
rng = np.random.default_rng(0)
J = PAR.lso_stats(PAR.load_cells(PKG / "data/probe_J_20260529T005230Z"), PAR.MODELS, rng)
K = PAR.lso_stats(PAR.load_cells(PKG / "data/probe_K_20260529T014133Z"), [m for m in PAR.MODELS if m != PAR.ANCHOR], rng)
agg = {"un-anchored plain mean (sec 4.1 pass)": {m: J[m][0] for m in PAR.MODELS},
       "anchored plain mean (run 1; anchor at 7)": {**{m: K[m][0] for m in K}, PAR.ANCHOR: 7.0},
       "official total T (pooled, council basis)": {r["model"]: float(r["T"]) for r in rows(PKG / "data/total_rating_council_pooled123.csv")}}
out = []
for label, d in agg.items():
    ms = [m for m in PAR.MODELS if m in d and m in gpqa]; x = np.array([d[m] for m in ms]); y = np.array([gpqa[m] for m in ms])
    r, rho = np.corrcoef(x, y)[0, 1], spearmanr(x, y)[0]; out.append((label, len(ms), r, rho)); print(f"{label:>44}: n={len(ms)}  Pearson r = {r:.2f}  Spearman rho = {rho:.2f}")
with open(PKG / "data/baseline_aggregators.csv", "w") as fh:
    w = csv.writer(fh); w.writerow(["aggregator", "n", "pearson_r", "spearman_rho"]); [w.writerow([a, n, f"{r:.3f}", f"{s:.3f}"]) for a, n, r, s in out]
assert out[0][2] < out[1][2] < out[2][2], "the ladder plain -> anchored -> T is not monotone; the manuscript sentence no longer holds"
