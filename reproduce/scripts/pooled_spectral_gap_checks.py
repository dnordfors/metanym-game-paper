#!/usr/bin/env python3
"""POOLED variant (sub-project pooled-three-runs): adds the pooled matrices to the per-run checks.
Appendix A.6 (ICLR version) — spectral-gap checks on the factual rating matrix, per run.

Produces: for each anchored run, sigma1/sigma2; sigma1 relative to the 95th-percentile noise edge of a
per-evaluator permutation null (each evaluator's ratings shuffled across the 275 columns; shared structure
destroyed, marginals kept); whether sigma2 also exceeds its noise edge (a second, contrasting pattern of
judgement); and the bootstrap stability of the leading direction u1 (sign-aligned and top-2-Procrustes-aligned,
as in A.5). Printed figures quoted in the paper: sigma1/edge = 1.57 (run 1) and 1.29 (run 3).

Matrix per Appendix A.2: rows = 12 evaluators, columns = 11 graded portfolios x 25 parallel contexts (first five
archetypes), entries = the 1-10 factual rating used directly; self-entries and entries whose grading call did not
return (file missing or unparseable) = the anchor value 7; rows centred. Deterministic (seed 20260911), no API.
Provenance: promoted 2026-09-11 from projects/active/metanym-game-paper-iclr27/scripts/spectral_gap_checks.py;
run-directory conventions as in ballast_sizing.py. Env: none required (paths relative to reproduce/).
"""

import json, re, sys
from pathlib import Path
import numpy as np
DATA = Path(__file__).resolve().parent.parent / "data"
RUNS = {"run1 (probe_K 20260529)": DATA / "probe_K_20260529T014133Z",
        "run2 (20260619 015828)": DATA / "regenerations" / "probe_K_anchor7_20260619T015828Z",
        "run3 (20260619 040659)": DATA / "regenerations" / "probe_K_anchor7_20260619T040659Z"}
RUNS["pooled runs 1+2"] = [RUNS["run1 (probe_K 20260529)"], RUNS["run2 (20260619 015828)"]]
RUNS["pooled runs 1+2+3"] = [RUNS["run1 (probe_K 20260529)"], RUNS["run2 (20260619 015828)"], RUNS["run3 (20260619 040659)"]]
M = ["claude-opus-4.1","claude-opus-4.5","claude-opus-4.0","claude-sonnet-4","gemini-3.1-pro","gemini-2.5-flash",
     "gpt-4.1-2025-04-14","gpt-4.1-mini","gpt-4.1-nano","gpt-4o","gpt-4o-2024-08-06","gpt-4o-mini"]
ANCHOR = "claude-opus-4.5"
FK = {"gpt-4.1-2025-04-14":"gpt-41-2025-04-14","gpt-4.1-mini":"gpt-41-mini","gpt-4.1-nano":"gpt-41-nano"}
fk = lambda m: FK.get(m, m)
JR = re.compile(r"```json\s*\n(.*?)\n```", re.DOTALL)
UNPARSEABLE = []

def ratings(run, e, t):
    fp = run / f"eval_{fk(e)}_x_{fk(t)}.json"
    if not fp.exists(): return None
    try:
        n = json.loads(JR.search(json.load(open(fp))["Messages"][0]["Message"]["Content"]).group(1))
        n = n["scores"][list(n["scores"])[0]]
    except (json.JSONDecodeError, AttributeError, KeyError) as err:
        UNPARSEABLE.append((e, t, type(err).__name__)); return None   # documented convention (A.2): entry set to the anchor value 7
    out = {}
    for ai, a in enumerate(n["archetypal_contexts"][:5], 1):
        for k, v in enumerate(a.get("factual_per_pc") or []):
            out[(ai, k)] = float(v)
    return out

def build(run):
    targets = [t for t in M if t != ANCHOR]
    cols = [(t, ai, k) for t in targets for ai in range(1, 6) for k in range(5)]
    F = np.full((len(M), len(cols)), 7.0)
    missing = 0
    for i, e in enumerate(M):
        for t in targets:
            if e == t: continue
            d = ratings(run, e, t)
            if d is None: missing += 1; continue
            for j, (tt, ai, k) in enumerate(cols):
                if tt == t and (ai, k) in d: F[i, j] = d[(ai, k)]
    assert F.shape == (12, 275), F.shape
    return F, missing

def build_any(run):
    if isinstance(run, list):
        parts = [build(r) for r in run]
        return np.concatenate([f for f, _ in parts], axis=1), sum(m for _, m in parts)
    return build(run)

def svd_c(F):
    Fc = F - F.mean(1, keepdims=True)
    U, S, Vt = np.linalg.svd(Fc, full_matrices=False)
    u = U[:, 0]; u = u if u.sum() > 0 else -u
    return S, u, U[:, 1]

rng = np.random.default_rng(20260911); B = 1000
for name, run in RUNS.items():
    F, missing = build_any(run)
    S, u1, u2 = svd_c(F)
    ratio = S[0] / S[1]; share = S[0]**2 / (S**2).sum()
    # 1. permutation null: per-row shuffle across columns
    null = []
    for _ in range(B):
        Fp = np.array([rng.permutation(row) for row in F]); null.append(svd_c(Fp)[0][0])
    null = np.array(null); edge95 = np.percentile(null, 95); edge_ratio = S[0] / edge95
    p = (null >= S[0]).mean()
    # also: is sigma2 above the null edge? (a second genuinely shared/contrast pattern)
    null2 = []
    for _ in range(300):
        Fp = np.array([rng.permutation(row) for row in F]); null2.append(svd_c(Fp)[0][1])
    # 2. bootstrap stability of u1
    corr_simple, corr_proc = [], []
    for _ in range(B):
        idx = rng.integers(0, F.shape[1], F.shape[1]); Fb = F[:, idx] - F[:, idx].mean(1, keepdims=True)
        Ub, Sb, _ = np.linalg.svd(Fb, full_matrices=False)
        ub = Ub[:, 0]; ub = ub if ub @ u1 > 0 else -ub; corr_simple.append(ub @ u1 / (np.linalg.norm(ub) * np.linalg.norm(u1)))
        A = np.stack([u1, u2], 1); Bm = Ub[:, :2]                       # Procrustes: align the top-2 subspace
        W, _, Zt = np.linalg.svd(Bm.T @ A); Q = W @ Zt; ua = (Bm @ Q)[:, 0]; ua = ua if ua @ u1 > 0 else -ua
        corr_proc.append(ua @ u1 / (np.linalg.norm(ua) * np.linalg.norm(u1)))
    pos = [M[i] for i in np.argsort(-u2) if u2[i] > 0.15]; neg = [M[i] for i in np.argsort(u2) if u2[i] < -0.15]
    print(f"\n=== {name}   (evaluator-target entries set to 7 — file missing or unparseable: {missing}; unparseable: {[(e,t) for e,t,_ in UNPARSEABLE]})"); UNPARSEABLE.clear()
    print(f"sigma1/sigma2 = {ratio:.2f}   sigma1^2 share of centred variance = {share:.3f}   top-5 sigmas: {np.round(S[:5],1)}")
    print(f"permutation null (per-row shuffle, B={B}): sigma1 95th pct = {edge95:.1f}, real sigma1 = {S[0]:.1f} -> sigma1/edge = {edge_ratio:.2f}, p = {p:.3f}")
    print(f"  sigma2 real = {S[1]:.1f} vs null sigma2 95th pct = {np.percentile(null2,95):.1f}  -> second pattern {'ABOVE' if S[1] > np.percentile(null2,95) else 'within'} noise")
    print(f"u1 stability over column bootstrap: corr with full-sample u1 — sign-aligned median {np.median(corr_simple):.3f} (5th pct {np.percentile(corr_simple,5):.3f}); Procrustes-aligned median {np.median(corr_proc):.3f} (5th pct {np.percentile(corr_proc,5):.3f})")
    print(f"u1 loadings (competence): " + ", ".join(f"{M[i]}={u1[i]:+.2f}" for i in np.argsort(-u1)))
    print(f"u2 sign pattern: + {pos} | - {neg}")
