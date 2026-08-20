#!/usr/bin/env python3
"""Appendix D.1 — every number, recomputed from the shipped CSVs.

Inputs (all in data/): total_rating_council.csv (official council-basis components),
total_rating_twelve.csv (bootstrap-basis components), total_rating_runs.csv (council-basis
T per regeneration run), ec_svd_twelve.csv (the declined per-axis-SVD E^C variant),
gpqa_selfadministered.csv, external_benchmarks.csv.

Prints, in D.1's order: the aggregation ladder (quarters, halves, factual pair, T) with
Pearson/Spearman and Fisher-z + BCa 95% intervals; the subjective-quarters-by-estimator
comparison; the leave-one-out and best-pair compounds; the full-roster vs leading-eight
regime inversion (with the within-Anthropic rank agreement); the basis comparison; the
per-run regeneration correlations; the anchor-exclusion checks; and D.4's public-vs-self
agreement on the sourceable models. Asserts the headline values so a drifted input fails
loudly rather than printing stale prose.
"""
import csv
import sys
from pathlib import Path

import numpy as np
from scipy.stats import bootstrap, pearsonr, spearmanr

DATA = Path(__file__).resolve().parent.parent / "data"


def rd(name):
    return list(csv.DictReader([l for l in (DATA / name).read_text().splitlines()
                                if not l.lstrip().lstrip('"').startswith("#")]))


council = {r["model"]: r for r in rd("total_rating_council.csv")}
twelve = {r["model"]: r for r in rd("total_rating_twelve.csv")}
runs = {r["model"]: r for r in rd("total_rating_runs.csv")}
ecsvd = {r["model"]: float(r["EC_svd"]) for r in rd("ec_svd_twelve.csv")}
gpqa = {r["model"]: float(r["gpqa_diamond_accuracy"]) for r in rd("gpqa_selfadministered.csv")}
ext = {r["model"]: r["gpqa_diamond"] for r in rd("external_benchmarks.csv")}

MS = [m for m in council if m in gpqa]
G = np.array([gpqa[m] for m in MS])
ANCHOR = "claude-opus-4.5"
LEAD8 = [m for m in MS if float(council[m]["T"]) >= 4.4]
rng = np.random.default_rng(20260816)


def q(basis, m, k):
    return float(basis[m][k])


def series(f, basis=council, ms=MS):
    return np.array([f(basis, m) for m in ms])


def fisher(r, n):
    z, se = np.arctanh(r), 1 / np.sqrt(n - 3)
    return np.tanh(z - 1.96 * se), np.tanh(z + 1.96 * se)


def bca(v, g):
    res = bootstrap((v, g), lambda x, y: pearsonr(x, y).statistic, paired=True,
                    vectorized=False, n_resamples=10000, method="BCa",
                    confidence_level=0.95, random_state=rng)
    return res.confidence_interval.low, res.confidence_interval.high


def row(name, v, g=G, ci=True):
    r = pearsonr(v, g).statistic
    rho = spearmanr(v, g).correlation
    if ci:
        flo, fhi = fisher(r, len(v))
        blo, bhi = bca(v, g)
        print(f"{name:38} r={r:.2f}  rho={rho:.2f}  Fisher[{flo:.2f},{fhi:.2f}]  BCa[{blo:.2f},{bhi:.2f}]")
    else:
        print(f"{name:38} r={r:.2f}  rho={rho:.2f}")
    return r


LADDER = [("E^C alone", lambda b, m: q(b, m, "EC")),
          ("G^F alone", lambda b, m: q(b, m, "GF")),
          ("E^F alone", lambda b, m: q(b, m, "EF")),
          ("G^C alone", lambda b, m: q(b, m, "GC")),
          ("G half", lambda b, m: (q(b, m, "GF") + q(b, m, "GC")) / 2),
          ("E half", lambda b, m: (q(b, m, "EF") + q(b, m, "EC")) / 2),
          ("factual pair", lambda b, m: (q(b, m, "GF") + q(b, m, "EF")) / 2),
          ("T", lambda b, m: float(b[m]["T"]))]

print("— D.1 aggregation ladder (council basis, n=12) —")
rs = {}
for name, f in LADDER:
    rs[name] = row(name, series(f))
assert round(rs["T"], 2) == 0.97 and round(rs["G^C alone"], 2) == 0.92, "headline drift"

print("\n— subjective quarters by estimator —")
row("G^C (official)", series(lambda b, m: q(b, m, "GC")), ci=False)
row("E^C (official)", series(lambda b, m: q(b, m, "EC")), ci=False)
row("E^C_svd (declined; twelve basis)", np.array([ecsvd[m] for m in MS]), ci=False)

print("\n— compounds: leave-one-out and best pair —")
row("1/3(GF+GC+EF)  (drop E^C)", series(lambda b, m: (q(b, m, "GF") + q(b, m, "GC") + q(b, m, "EF")) / 3), ci=False)
row("1/2(GC+EF)", series(lambda b, m: (q(b, m, "GC") + q(b, m, "EF")) / 2), ci=False)

print(f"\n— regime inversion (leading eight = {len(LEAD8)} models) —")
G8 = np.array([gpqa[m] for m in LEAD8])
for name, f in (("G^F", lambda b, m: q(b, m, "GF")), ("G^C", lambda b, m: q(b, m, "GC")),
                ("E^F", lambda b, m: q(b, m, "EF")), ("E^C", lambda b, m: q(b, m, "EC")),
                ("T", lambda b, m: float(b[m]["T"]))):
    v8 = series(f, ms=LEAD8)
    print(f"{name:38} leading-8 r={pearsonr(v8, G8).statistic:.2f}  rho={spearmanr(v8, G8).correlation:.2f}")
anth = [m for m in MS if "claude" in m]
va = series(lambda b, m: float(b[m]["T"]), ms=anth)
ga = np.array([gpqa[m] for m in anth])
print(f"{'within-Anthropic (n=4), T':38} rho={spearmanr(va, ga).correlation:.2f}")
trail = [m for m in MS if m not in LEAD8]
vt = series(lambda b, m: float(b[m]["T"]), ms=trail)
gt = np.array([gpqa[m] for m in trail])
print(f"{'trailing four (n=4), T':38} r={pearsonr(vt, gt).statistic:.2f}")

print("\n— basis comparison (council vs twelve-evaluator) —")
tw_ms = [m for m in MS if m in twelve]
for name, f in LADDER:
    rc = pearsonr(series(f, council, tw_ms), np.array([gpqa[m] for m in tw_ms])).statistic
    rt = pearsonr(series(f, twelve, tw_ms), np.array([gpqa[m] for m in tw_ms])).statistic
    print(f"{name:38} council {rc:.3f}   twelve {rt:.3f}")

print("\n— regeneration (council basis) —")
run_ms = [m for m in MS if m in runs]
for i in (1, 2, 3):
    v = np.array([float(runs[m][f"T_run{i}"]) for m in run_ms])
    g = np.array([gpqa[m] for m in run_ms])
    ex = [j for j, m in enumerate(run_ms) if m != ANCHOR]
    print(f"run {i}: r={pearsonr(v, g).statistic:.2f}  rho={spearmanr(v, g).correlation:.2f}  "
          f"(excl. anchor r={pearsonr(v[ex], g[ex]).statistic:.2f})")

print("\n— anchor exclusion (run 1, official) —")
ex = [i for i, m in enumerate(MS) if m != ANCHOR]
vT = series(lambda b, m: float(b[m]["T"]))
print(f"T vs GPQA excl. anchor: r={pearsonr(vT[ex], G[ex]).statistic:.3f}")

print("\n— D.4: public vs self-administered (sourceable models) —")
src = [m for m in MS if ext.get(m)]
a = np.array([float(ext[m]) for m in src])
b = np.array([gpqa[m] for m in src])
print(f"n={len(src)}: r={pearsonr(a, b).statistic:.2f}  rho={spearmanr(a, b).correlation:.2f}")

print("\nE.1 ladder: all values recomputed from shipped CSVs; headline assertions passed")
