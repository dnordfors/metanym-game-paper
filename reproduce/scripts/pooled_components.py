#!/usr/bin/env python3
"""Pooled estimators: the four anchored components over a POOLED corpus of runs.

Principled pooling (sub-project README, boundary condition 1):
  * factual matrix = column-stack of the runs' factual scores; ONE row-centred SVD gives E^F (left
    vector) and the consensus item ratings behind G^F (right vector), read exactly as in
    build_paper1_tables.components() (A5-A9);
  * G^C = reliability-weighted council mean over each player's (run, archetype) atoms (A12b);
  * E^C and the per-axis reliabilities rho come from run 1's anchor sweep only -- the only sweep,
    all four anchors on the same texts (A10-A12) -- over the run-1 atoms of the draw.
The scoring atom is (run, submission, archetype); a bootstrap draw of atoms drives every component.

With runs=[run1] this reproduces the published numbers exactly (validation in __main__).
Imports the shipped loader and constants; nothing in the package is modified.
"""
import os, sys, statistics as st
from pathlib import Path
import numpy as np

PKG = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PKG / "scripts"))
import build_paper1_tables as B   # noqa: E402

MODELS, COUNCIL, AM, AXES5, NF4KEY, SCORED = B.MODELS, B.COUNCIL, B.AM, B.AXES5, B.NF4KEY, B.SCORED_ARCHETYPES
RUN_DIRS = {1: PKG / "data/probe_K_20260529T014133Z",
            2: PKG / "data/regenerations/probe_K_anchor7_20260619T015828Z",
            3: PKG / "data/regenerations/probe_K_anchor7_20260619T040659Z"}
SWEEP_DIRS = {a: max(sorted((PKG / "data").glob(f"probe_K_anchor{a}_*")),
                     key=lambda d: len(list(d.glob("eval_*_x_*.json")))) for a in (5, 6, 8)}
pear, meanpw = B.pear, B.meanpw


def load_runs(runs):
    """{run: {anchor: {(ev, tg): record}}}: anchor 7 per run; anchors 5/6/8 (run-1 texts) under run 1."""
    GAs = {}
    for r in runs:
        GAs[r] = {7: {(e, t): B.parse(RUN_DIRS[r], e, t) for e in MODELS for t in MODELS if e != t}}
        if r == 1:
            for a in (5, 6, 8):
                GAs[r][a] = {(e, t): B.parse(SWEEP_DIRS[a], e, t) for e in MODELS for t in MODELS if e != t}
    return GAs


def graded_targets(GAs):
    return [m for m in MODELS if any(GAs[r][7].get((e, m)) for r in GAs for e in MODELS)]


def scoring_atoms(GAs, graded):
    return [(r, t, ai) for r in GAs for t in graded for ai in range(1, SCORED + 1)]


def components(GAs, graded, atoms, panel, ec_atoms=None):
    """G^F, G^C, E^F, E^C for `panel` (the evaluators) over the pooled atoms of `graded`."""
    sweep_run = 1 if 1 in GAs else None
    mi = {m: i for i, m in enumerate(panel)}

    # ---- E^F and consensus ratings: one SVD over all (atom, pc) columns ------------------------
    cols, seen = [], set()
    for n, (r, tg, ai) in enumerate(atoms):
        for ev in panel:
            rec = GAs[r][7].get((ev, tg)) if ev != tg else None
            if not rec or ai not in rec["arch"]:
                continue
            for pi in range(len(rec["arch"][ai]["fact"])):
                if (n, pi) not in seen:
                    seen.add((n, pi)); cols.append((n, tg, pi))
    cidx = {(n, pi): i for i, (n, _t, pi) in enumerate(cols)}
    F = np.full((len(panel), len(cols)), 7.0)
    for n, (r, tg, ai) in enumerate(atoms):
        for ev in panel:
            rec = GAs[r][7].get((ev, tg)) if ev != tg else None
            if not rec or ai not in rec["arch"]:
                continue
            for pi, v in enumerate(rec["arch"][ai]["fact"]):
                F[mi[ev], cidx[(n, pi)]] = float(v)
    rowmean = F.mean(1); Fc = F - rowmean[:, None]
    U, S, Vt = np.linalg.svd(Fc, full_matrices=False)
    f, v, s1 = U[:, 0], Vt[0, :], S[0]
    if f.sum() < 0:
        f, v = -f, -v
    if pear(v, Fc.mean(0)) < 0:
        v = -v
    fpos = np.clip(f, 0, None)
    EFload = dict(zip(panel, fpos)); fa = EFload.get(AM, 0.0)   # anchor off the panel: E^F undefined
    EF = {m: (7 * EFload[m] / fa if fa > 0 else float("nan")) for m in panel}
    W = fpos.sum(); C = float((fpos * rowmean).sum() / W); kap = float(s1 * (fpos * f).sum() / W)
    rhat = C + kap * v
    gen_of = np.array([c[1] for c in cols])
    GF = {AM: 7.0}
    for g in graded:
        if g != AM:
            mine = rhat[gen_of == g]; GF[g] = float(mine.mean()) if mine.size else float("nan")
    gap = float(S[0] / S[1]) if len(S) > 1 and S[1] > 0 else float("inf")

    # ---- reliabilities rho and E^C: run-1 sweep over the run-1 atoms of the draw ---------------
    GA1 = GAs.get(sweep_run, {a: {} for a in (5, 6, 7, 8)})   # no run 1 in the pool: rho/E^C undefined (NaN)
    atoms1 = [(t, ai) for (r, t, ai) in (ec_atoms if ec_atoms is not None else atoms) if r == sweep_run]

    def axis_val(rec, ai, axis):
        if rec is None:
            return None
        if axis == "struct":
            return rec["sd"]
        a = rec["arch"].get(ai)
        if not a or len(a["six"]) != 4:
            return None
        return a["six"][("beauty", "intel", "distinct", "length").index(axis)]
    RHO = {ax: {} for ax in AXES5}
    portfolios = list(dict.fromkeys(t for t, _ in atoms1))
    for ax in AXES5:
        units = [(t,) for t in portfolios] if ax == "struct" else list(atoms1)
        for ev in panel:
            A = np.full((4, len(units)), np.nan)
            for k, anc in enumerate((5, 6, 7, 8)):
                for j, u in enumerate(units):
                    if ev == u[0]:
                        continue
                    A[k, j] = axis_val(GA1[anc].get((ev, u[0])), (None if ax == "struct" else u[1]), ax)
            RHO[ax][ev] = meanpw(A)
    rb = {}
    for ev in panel:
        A = np.full((4, len(atoms1)), np.nan)
        for k, anc in enumerate((5, 6, 7, 8)):
            for j, (t, ai) in enumerate(atoms1):
                if ev == t:
                    continue
                rec = GA1[anc].get((ev, t))
                if rec and ai in rec["arch"] and rec["arch"][ai]["nf4mean"] is not None:
                    A[k, j] = rec["arch"][ai]["nf4mean"]
        rb[ev] = meanpw(A)
    ra = rb.get(AM, float('nan'))
    EC = {m: (7 * rb[m] / ra if ra == ra and ra > 0 else float("nan")) for m in panel}
    Eax = {}
    for ax in AXES5:
        raA = RHO[ax].get(AM)
        e = {m: (7 * RHO[ax][m] / raA if RHO[ax][m] == RHO[ax][m] and raA else np.nan) for m in panel}
        if AM in panel:
            e[AM] = 7.0
        Eax[ax] = e

    # ---- G^C: reliability-weighted council mean over each player's pooled atoms ----------------
    atoms_of = {}
    for r, tg, ai in atoms:
        atoms_of.setdefault(tg, []).append((r, ai))
    seats = [t for t in COUNCIL if t in panel]

    def gen_axis(s, axis):
        num = den = 0.0
        for t in seats:
            if t == s:
                continue
            if axis == "struct":
                vs = [GAs[r][7][(t, s)]["sd"] for r in dict.fromkeys(r for r, _ in atoms_of.get(s, []))
                      if GAs[r][7].get((t, s)) and GAs[r][7][(t, s)]["sd"] is not None]
            else:
                vs = [axis_val(GAs[r][7].get((t, s)), ai, axis) for r, ai in atoms_of.get(s, [])]
                vs = [x for x in vs if x is not None]
            if not vs:
                continue
            w = max(RHO[axis][t], 0.0)
            num += w * st.mean(vs); den += w
        return num / den if den > 0 else None
    Gax = {ax: {s: (7.0 if s == AM else gen_axis(s, ax)) for s in panel} for ax in AXES5}
    GC = {}
    for s in panel:
        if s == AM:
            GC[s] = 7.0; continue
        vals = [Gax[ax][s] for ax in AXES5 if Gax[ax].get(s) is not None]
        GC[s] = st.mean(vals) if len(vals) == 5 else float("nan")
    return dict(GF=GF, GC=GC, EF=EF, EC=EC, Gax=Gax, Eax=Eax, RHO=RHO, RB=rb, EFload=EFload,
                gap=gap, ncols=len(cols), sigma=S[:4].tolist())


def T_of(comp, m):
    vals = [comp["GF"].get(m), comp["GC"].get(m), comp["EF"].get(m), comp["EC"].get(m)]
    if any(v is None or v != v for v in vals):
        return None, vals
    return sum(vals) / 4, vals


def ballast_of(GAs, graded, n=2):
    """Two lowest-rated non-council submissions by the twelve-panel pooled factual mean."""
    def fm(t):
        vs = [float(x) for r in GAs for ev in MODELS if ev != t
              for rec in [GAs[r][7].get((ev, t))] if rec
              for a in rec["arch"].values() for x in (a["fact"] or [])]
        return st.mean(vs) if vs else float("nan")
    return sorted([t for t in graded if t not in COUNCIL], key=fm)[:n]


def council_rounds(GAs, graded):
    """(panel, graded) per model under the council basis: seats share a round, contestants get their own."""
    ballast = ballast_of(GAs, graded)
    cg = [t for t in graded if t in COUNCIL] + [b for b in ballast if b not in COUNCIL]
    rounds = {m: (list(COUNCIL), list(cg)) for m in COUNCIL}
    for m in [x for x in MODELS if x not in COUNCIL]:
        rounds[m] = (COUNCIL + [m], cg + ([m] if m not in cg else []))
    return rounds, ballast


if __name__ == "__main__":
    import csv
    GAs = load_runs([1]); graded = graded_targets(GAs)
    rd = lambda p: {r["model"]: r for r in csv.DictReader([l for l in open(p) if not l.startswith("#")])}
    pub12 = rd(PKG / "data/total_rating_twelve.csv"); pubC = rd(PKG / "data/total_rating_council.csv")
    comp = components(GAs, graded, scoring_atoms(GAs, graded), MODELS)
    worst = 0.0
    for m in MODELS:
        T, parts = T_of(comp, m)
        if T is None:
            continue
        for k, v in zip(("T", "GF", "GC", "EF", "EC"), [T] + parts):
            worst = max(worst, abs(v - float(pub12[m][k])))
    print(f"twelve basis, run 1: max |pooled - published| = {worst:.5f}  (columns {comp['ncols']}, gap {comp['gap']:.3f})")
    rounds, ballast = council_rounds(GAs, graded); print("ballast:", ballast); worst = 0.0
    for m, (panel, g) in rounds.items():
        c = components(GAs, g, scoring_atoms(GAs, g), panel); T, parts = T_of(c, m)
        for k, v in zip(("T", "GF", "GC", "EF", "EC"), [T] + parts):
            worst = max(worst, abs(v - float(pubC[m][k])))
    print(f"council basis, run 1: max |pooled - published| = {worst:.5f}")
