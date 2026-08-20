#!/usr/bin/env python3
"""Slope and correlation under FULL uncertainty propagation (Appendix D.1).

Three nested uncertainty schemes for the T-vs-GPQA fit, each 95% percentile intervals:

  A. sampling only      — classical pairs bootstrap of the 12 point estimates;
  B. measurement only   — the 12 models fixed; each replicate draws every model's T from
                          its empirical A.5 bootstrap replicate distribution
                          (data/total_rating_council_replicates.csv; the anchor's is a
                          point mass at 7 by construction) and its GPQA accuracy from
                          Binomial(198, p-hat)/198;
  C. both               — resample the 12 models with replacement AND draw each included
                          model's coordinates as in B. The honest total-uncertainty
                          interval for slope and r.

Scheme C modestly OVERSTATES total uncertainty (the observed scatter already contains one
realization of each point's measurement noise; jittering observed values adds a second) —
it is a labeled-conservative bound, reported in Appendix D.1 as sensitivity. The FIGURE
retains the classical confidence band by convention. Writes data/slope_band_full.csv (the
scheme-C pointwise band) for reference. Deterministic seed.
"""
import csv
from pathlib import Path

import numpy as np
from scipy.stats import pearsonr

DATA = Path(__file__).resolve().parent.parent / "data"
SEED = 20260817
B2 = 10000


def rd(name):
    return list(csv.DictReader([l for l in (DATA / name).read_text().splitlines()
                                if not l.lstrip().lstrip('"').startswith("#")]))


council = {r["model"]: r for r in rd("total_rating_council.csv")}
gpqa = {r["model"]: r for r in rd("gpqa_selfadministered.csv")}
reps_rows = rd("total_rating_council_replicates.csv")
reps = {r["model"]: np.array([float(r[k]) for k in r
                              if k.startswith("r") and r[k] not in ("", None)])
        for r in reps_rows}
MS = [m for m in council if m in gpqa and m in reps]
n = len(MS)
X = np.array([float(council[m]["T"]) for m in MS])
P = np.array([float(gpqa[m]["gpqa_diamond_accuracy"]) / 100 for m in MS])
NQ = np.array([float(gpqa[m]["n_total"]) for m in MS])
Y = P * 100
minB = min(len(reps[m]) for m in MS)
R = np.stack([reps[m][:minB] for m in MS])   # n_models x common replicate count


def fit(x, y):
    b, a = np.polyfit(x, y, 1)
    return b, a, pearsonr(x, y).statistic


b0, a0, r0 = fit(X, Y)
rng = np.random.default_rng(SEED)
grid = np.linspace(X.min() - 0.25, X.max() + 0.25, 60)


def run(scheme):
    slopes, rs, lines = [], [], []
    for _ in range(B2):
        idx = rng.integers(0, n, n) if scheme in ("A", "C") else np.arange(n)
        if scheme in ("B", "C"):
            x = np.array([R[i][rng.integers(0, R.shape[1])] for i in idx])
            y = rng.binomial(NQ[idx].astype(int), P[idx]) / NQ[idx] * 100
        else:
            x, y = X[idx], Y[idx]
        if x.std() < 1e-9 or y.std() < 1e-9:
            continue
        b, a, r = fit(x, y)
        slopes.append(b)
        rs.append(r)
        if scheme == "C":
            lines.append(b * grid + a)
    return np.array(slopes), np.array(rs), (np.array(lines) if lines else None)


print(f"point estimates: slope = {b0:.2f} GPQA-pts per T-unit, r = {r0:.3f}, n = {n}")
print(f"{'scheme':44}{'slope 95%':>16}{'r 95%':>16}")
bands = None
for scheme, label in (("A", "A sampling only (pairs bootstrap)"),
                      ("B", "B measurement only (T replicates + binomial)"),
                      ("C", "C both (the honest total interval)")):
    slopes, rs, lines = run(scheme)
    slo, shi = np.percentile(slopes, [2.5, 97.5])
    rlo, rhi = np.percentile(rs, [2.5, 97.5])
    print(f"{label:44}[{slo:5.2f}, {shi:5.2f}] [{rlo:.2f}, {rhi:.2f}]")
    if scheme == "C":
        bands = np.percentile(lines, [2.5, 97.5], axis=0)

out = DATA / "slope_band_full.csv"
lines_out = ["# pointwise 95% band of the fitted line under the two-level bootstrap (scheme C:",
             "#   models resampled with replacement + per-model measurement draws from the",
             f"#   T replicate distributions and GPQA binomials). seed {SEED}, B={B2}.",
             "# produced by scripts/slope_full_bootstrap.py; drawn by plot_total_validation.py",
             "x,lo95,hi95"]
for x, lo, hi in zip(grid, bands[0], bands[1]):
    lines_out.append(f"{x:.4f},{lo:.4f},{hi:.4f}")
out.write_text("\n".join(lines_out) + "\n")
print(f"wrote {out}")
