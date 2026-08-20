#!/usr/bin/env python3
"""Canonical reproduction of the Paper-1 (submitted) rating tables, from raw run data.

ONE authoritative script for the numbers in the submitted manuscript
(`papers/v3/paper1_v2/paper1_v2.6.md`). It recomputes every component from the anchor-7
run + the anchor sweep {5,6,7,8} and prints, to the paper's displayed precision:

  * Criterion A  : evaluator factual competence E^F (anchored), generator factuality G^F
  * Criterion B  : per-axis criterion reliability rho_{s,axis}  (the anchor-sweep consistency)
  * Per-criterion: generator quality G (reliability-weighted) and evaluator reliability E,
                   per non-factual axis, plus their anchored cosine cos(G,E)
  * Council      : the criterion-reliability column of the council table
  * Breakdown    : the four anchored components G^F, G^C, E^F, E^C  (per model)
  * Leaderboard  : total T = 1/4(G^F+G^C+E^F+E^C), with E = 1/2(E^F+E^C), G = 1/2(G^F+G^C)

The three exhibits of paper section 4.6 -- the per-axis anchor-sweep consistency table, the
per-criterion G-vs-E table with its cos(G,E) footer, and the council table's criterion-reliability
column -- are all emitted here, from the one RHO/rho_bar computation, so they cannot drift apart.
The point estimates are also written to data/section_4_4_criterion_b.csv (see DATA_MANIFEST.md).

Every evaluator quantity here is **leave-self-out**: an evaluator's ratings of its own portfolio
are collected in the runs but never enter its own reliability (A.2.b), and the two submissions that
returned a sixth archetype contribute their first five only (SCORED_ARCHETYPES). Criterion A is the
one deliberate exception: its matrix keeps a self-entry, set to the anchor value (A5).

Key estimator choices (these reproduce the *submitted* numbers; see paper Appendix A):
  * E^F  : leading left singular vector of the row-centred per-PC factual matrix (anchor 7,
           self/missing = 7), clipped >=0, anchored as 7 f_s / f_anchor.            (A5-A7,A12)
  * G^F  : full-panel, per-PC, leave-self-out mean of the 1-10 factual scores of a generator,
           weighted by each evaluator's competence E^F  (the "G^F-prime" of A8-A9).  (A8-A9)
  * E^C  : collapsed 4-axis anchor-sweep consistency rho_bar, anchored 7 rho_bar/rho_bar_a. (A10-A12)
  * G^C  : council leave-self-out mean of the five non-factual generation axes, with each
           council member's vote on each axis WEIGHTED BY ITS PER-AXIS RELIABILITY rho_{t,axis}
           (the submitted reliability weighting), averaged over the five axes.        (A1, sec 4.4)
  * G,E,T: the symmetric 2x2 of {maker,judge} x {factual,criterion}, anchor pinned at 7. (A13-A14)

Point estimates only (fast, deterministic at T=0). 95% CIs are produced by the per-component
bootstrap scripts (criterion_a/criterion_b/generation_factuality_validation/bootstrap_total);
this script is the single place the *point* tables are assembled with the reliability weighting.

`components()` below computes the four anchored components from a multiset of (submission,
archetype) scoring atoms, and `totals()` assembles T from them; `bootstrap_total.py` imports both
and calls them once per resample, so the point estimate it reports is this script's, by
construction, rather than a second implementation of the same estimator.

Env: RUNS_GEN (anchor-7 run), RUNS_SWEEP (parent of probe_K_anchor{5,6,8}). See DATA_MANIFEST.md.
Run: RUNS_GEN=... RUNS_SWEEP=... python scripts/build_paper1_tables.py
"""
from __future__ import annotations
import json, re, os, glob, statistics as st, sys
from pathlib import Path
import numpy as np
from decimal import Decimal, ROUND_HALF_UP

r2 = lambda x: float(Decimal(str(x)).quantize(Decimal("0.01"), ROUND_HALF_UP))
r1 = lambda x: float(Decimal(str(x)).quantize(Decimal("0.1"), ROUND_HALF_UP))
JR = re.compile(r"```json\s*\n(.*?)\n```", re.DOTALL)

MODELS = ["claude-opus-4.1", "claude-opus-4.5", "claude-opus-4.0", "claude-sonnet-4",
          "gemini-3.1-pro", "gemini-2.5-flash", "gpt-4.1-2025-04-14", "gpt-4.1-mini",
          "gpt-4.1-nano", "gpt-4o", "gpt-4o-2024-08-06", "gpt-4o-mini"]
FK = {"gpt-4.1-2025-04-14": "gpt-41-2025-04-14", "gpt-4.1-mini": "gpt-41-mini", "gpt-4.1-nano": "gpt-41-nano"}
fk = lambda m: FK.get(m, m)
NF4 = ("beauty", "intelligence", "instantiation_distinctness", "impressive_length")
AXES5 = ("beauty", "intel", "distinct", "length", "struct")          # the five non-factual axes
AXKEY = {"beauty": "beauty", "intel": "intelligence", "distinct": "instantiation_distinctness",
         "length": "impressive_length"}                              # struct handled via per-portfolio sd
COUNCIL = ["claude-opus-4.1", "claude-opus-4.5", "claude-opus-4.0", "gemini-3.1-pro", "gemini-2.5-flash"]
AM = "claude-opus-4.5"          # anchor model: reference portfolio, pinned to 7; ungraded as generator
# Row order of the paper's per-criterion G-vs-E table (sec 4.4): anchor first, then by family.
GE_ORDER = ["claude-opus-4.5", "claude-opus-4.1", "claude-opus-4.0", "claude-sonnet-4",
            "gemini-3.1-pro", "gemini-2.5-flash", "gpt-4.1-mini", "gpt-4.1-2025-04-14",
            "gpt-4.1-nano", "gpt-4o-2024-08-06", "gpt-4o", "gpt-4o-mini"]
NF4KEY = ("beauty", "intel", "distinct", "length")     # the four per-archetype non-factual axes
# Archetypes 1..5 only. Two submissions (gemini-2.5-flash, gpt-4.1-mini) carry a sixth
# archetype; its five parallel contexts are excluded so the panel stays balanced at 25
# contexts per portfolio -- 11 x 25 = 275 columns in the Criterion-A factual matrix --
# which is the same archetype set the criterion components below are built over.
SCORED_ARCHETYPES = 5


def run_dirs():
    gen, sweep = os.environ.get("RUNS_GEN"), os.environ.get("RUNS_SWEEP")
    if not (gen and sweep):
        sys.exit("set RUNS_GEN (anchor-7 run) and RUNS_SWEEP (parent of probe_K_anchor{5,6,8}); see DATA_MANIFEST.md")
    D = {7: gen}
    for a in (5, 6, 8):
        ds = sorted(glob.glob(str(Path(sweep) / f"probe_K_anchor{a}_*")))
        D[a] = max(ds, key=lambda d: len(glob.glob(d + "/eval_*_x_*.json")))
    return D


def parse(d, ev, tg):
    fp = Path(d) / f"eval_{fk(ev)}_x_{fk(tg)}.json"
    if not fp.exists():
        return None
    try:
        node = json.loads(JR.search(json.load(open(fp))["Messages"][0]["Message"]["Content"]).group(1))
        node = node["scores"][list(node["scores"])[0]]
        sd = node.get("structural_diversity")
        sd = float(sd) if isinstance(sd, (int, float)) else None
        arch = {ai: {"fact": list(a.get("factual_per_pc") or []),
                     "six": [a[k] for k in NF4 if isinstance(a.get(k), (int, float))],
                     "nf4": [a[k] for k in NF4 if isinstance(a.get(k), (int, float))]}
                for ai, a in enumerate(node["archetypal_contexts"], 1)}
        for rec in arch.values():                # the collapsed 4-axis score of A11, cached: it
            rec["nf4mean"] = st.mean(rec["nf4"]) if rec["nf4"] else None   # is re-read every replicate
        return {"arch": arch, "sd": sd}
    except Exception:
        return None


def pear(x, y):
    x, y = np.asarray(x, float), np.asarray(y, float)
    m = ~(np.isnan(x) | np.isnan(y)); x, y = x[m], y[m]
    if len(x) < 3 or x.std() < 1e-9 or y.std() < 1e-9:
        return np.nan
    return float(((x - x.mean()) * (y - y.mean())).mean() / (x.std() * y.std()))


def meanpw(R4):
    ps = [pear(R4[i], R4[j]) for i in range(4) for j in range(i + 1, 4)]
    ps = [p for p in ps if p == p]
    return st.mean(ps) if ps else np.nan


def load(D=None):
    """Parse every (evaluator, target) record at each swept anchor; return (GA, targets)."""
    D = D or run_dirs()
    GA = {a: {(e, t): parse(D[a], e, t) for e in MODELS for t in MODELS} for a in (5, 6, 7, 8)}
    targets = [m for m in MODELS if any(GA[7].get((e, m)) for e in MODELS)]
    return GA, targets


def scoring_atoms(targets):
    """The (submission, archetype) scoring atoms of A.5: the 11 graded portfolios x 5 archetypes."""
    return [(t, ai) for t in targets for ai in range(1, SCORED_ARCHETYPES + 1)]


def components(GA, targets, atoms, diagnostics=False):
    """The four anchored components G^F, G^C, E^F, E^C over a multiset of scoring atoms.

    `atoms` is a list of (submission, archetype) pairs, repeats allowed: passing
    scoring_atoms(targets) gives the published point estimates, passing a resample gives the
    bootstrap replicate of A.5. Each atom carries the parallel contexts inside it, so the atoms
    induce the factual matrix columns (A5-A7), the 55-unit vectors of rho_bar (A11), and the
    per-submission means G^C averages (A12b). The per-portfolio structural-diversity axis has one
    unit per portfolio, so its rho is taken over the distinct submissions the atoms carry.
    Returns the dict of per-model components plus the per-axis tables the paper's §4.4 rows need.

    `diagnostics=True` additionally computes the factual anchor-sweep consistency RHOF -- the
    `factual` column of the §4.4 per-axis table. It is a diagnostic only (factual is gated by f,
    not by consistency) and it is the most expensive rho in the file, one unit per parallel
    context rather than per archetype, so the bootstrap callers leave it off.
    """
    G7 = GA[7]

    # ---- E^F (Criterion A): per-PC factual SVD, anchored 7 f/f_a ----------------------------
    R = {(e, t): (G7[(e, t)]["arch"] if G7.get((e, t)) else None) for e in MODELS for t in MODELS if e != t}
    cols, seen = [], set()                       # one column per (atom, pc) context
    for n, (tg, ai) in enumerate(atoms):
        for ev in MODELS:
            a = R.get((ev, tg))
            if not a or ai not in a:
                continue
            for pi in range(len(a[ai]["fact"])):
                c = (n, pi)
                if c not in seen:
                    seen.add(c); cols.append((n, tg, pi))
    cidx = {(n, pi): i for i, (n, _tg, pi) in enumerate(cols)}
    mi = {m: i for i, m in enumerate(MODELS)}
    F = np.full((len(MODELS), len(cols)), 7.0)
    for n, (tg, ai) in enumerate(atoms):
        for ev in MODELS:
            a = R.get((ev, tg))
            if not a or ai not in a:
                continue
            for pi, v in enumerate(a[ai]["fact"]):
                F[mi[ev], cidx[(n, pi)]] = float(v)
    rowmean = F.mean(1)
    Fc = F - rowmean[:, None]
    U, S, Vt = np.linalg.svd(Fc, full_matrices=False)
    f = U[:, 0]; v = Vt[0, :]; s1 = S[0]
    if f.sum() < 0:
        f = -f; v = -v
    if pear(v, Fc.mean(0)) < 0:
        v = -v
    fpos = np.clip(f, 0, None)
    EFload = dict(zip(MODELS, fpos))
    fa = EFload[AM]                                                   # the anchor's own loading
    EF = {m: (7 * EFload[m] / fa if fa > 0 else float("nan")) for m in MODELS}   # anchored E^F (A12)
    # A8-A9 SVD-consensus generator rating r_hat = C + kappa * v, averaged per generator
    W = fpos.sum()
    C = float((fpos * rowmean).sum() / W)
    kap = float(s1 * (fpos * f).sum() / W)
    rhat = C + kap * v
    gen_of = np.array([c[1] for c in cols])

    # Canonical G^F = the SVD right-vector consensus rating (A8-A9); the paper's published value.
    GF = {AM: 7.0}
    for g in targets:
        if g == AM:
            continue
        mine = rhat[gen_of == g]                 # the columns this generator contributed
        GF[g] = float(mine.mean()) if mine.size else float("nan")

    # ---- per-axis reliability rho_{ev,axis} (Criterion B, A10) over the anchor sweep ----------
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
    portfolios = list(dict.fromkeys(t for t, _ai in atoms))     # one unit per distinct submission
    for ax in AXES5:
        units = [(t,) for t in portfolios] if ax == "struct" else list(atoms)
        for ev in MODELS:
            A = np.full((4, len(units)), np.nan)
            for k, anc in enumerate((5, 6, 7, 8)):
                for j, u in enumerate(units):
                    t = u[0]
                    if ev == t:                  # leave-self-out: an evaluator's ratings of its
                        continue                 # own portfolio never enter its own reliability
                    A[k, j] = axis_val(GA[anc].get((ev, t)), (None if ax == "struct" else u[1]), ax)
            RHO[ax][ev] = meanpw(A)

    # ---- factual anchor-sweep consistency (diagnostic column of the §4.4 per-axis table) --------
    RHOF = {}
    if diagnostics:
        for ev in MODELS:
            units = []
            for (t, ai) in atoms:
                if ev == t:
                    continue
                npi = max((len(GA[a][(ev, t)]["arch"][ai]["fact"])
                           for a in (5, 6, 7, 8)
                           if GA[a].get((ev, t)) and ai in GA[a][(ev, t)]["arch"]), default=0)
                units += [(t, ai, pi) for pi in range(npi)]
            A = np.full((4, len(units)), np.nan)
            for k, anc in enumerate((5, 6, 7, 8)):
                for j, (t, ai, pi) in enumerate(units):
                    rec = GA[anc].get((ev, t))
                    if rec and ai in rec["arch"] and pi < len(rec["arch"][ai]["fact"]):
                        A[k, j] = rec["arch"][ai]["fact"][pi]
            RHOF[ev] = meanpw(A) if len(units) >= 3 else np.nan

    # ---- E^C (Criterion B): collapsed 4-axis rho_bar, anchored 7 rho_bar/rho_bar_a (A11-A12) --
    rb = {}
    for ev in MODELS:
        A = np.full((4, len(atoms)), np.nan)
        for k, anc in enumerate((5, 6, 7, 8)):
            for j, (t, ai) in enumerate(atoms):
                if ev == t:
                    continue
                rec = GA[anc].get((ev, t))
                if rec and ai in rec["arch"] and rec["arch"][ai]["nf4mean"] is not None:
                    A[k, j] = rec["arch"][ai]["nf4mean"]
        rb[ev] = meanpw(A)
    ra = rb[AM]                                                       # the anchor's own rho_bar
    EC = {m: (7 * rb[m] / ra if ra == ra and ra > 0 else float("nan")) for m in MODELS}

    # ---- per-criterion E (anchored per-axis) and reliability-weighted generator quality G ------
    def Eaxis(ax):
        raA = RHO[ax][AM]
        e = {m: (7 * RHO[ax][m] / raA if RHO[ax][m] == RHO[ax][m] and raA else np.nan) for m in MODELS}
        e[AM] = 7.0
        return e
    Eax = {ax: Eaxis(ax) for ax in AXES5}

    atoms_of = {}                                # the archetypes each submission contributes
    for tg, ai in atoms:
        atoms_of.setdefault(tg, []).append(ai)

    def gen_axis(s, axis, weighted):
        num = den = 0.0
        for t in COUNCIL:
            if t == s:
                continue
            rec = G7.get((t, s))
            if not rec:
                continue
            if axis == "struct":
                v = rec["sd"]                    # one score per portfolio, not per atom
            else:
                vs = [axis_val(rec, ai, axis) for ai in atoms_of.get(s, [])]
                vs = [x for x in vs if x is not None]
                v = st.mean(vs) if vs else None
            if v is None:
                continue
            w = max(RHO[axis][t], 0.0) if weighted else 1.0
            num += w * v
            den += w
        return num / den if den > 0 else None
    Gax = {ax: {} for ax in AXES5}
    for ax in AXES5:
        for s in MODELS:
            Gax[ax][s] = 7.0 if s == AM else gen_axis(s, ax, weighted=True)

    # G^C = mean over the five reliability-weighted per-axis generator scores
    GC = {}
    for s in MODELS:
        if s == AM:
            GC[s] = 7.0; continue
        vals = [Gax[ax][s] for ax in AXES5 if Gax[ax].get(s) is not None]
        GC[s] = st.mean(vals) if len(vals) == 5 else float("nan")

    return dict(GF=GF, GC=GC, EF=EF, EC=EC, Gax=Gax, Eax=Eax,
                RHO=RHO, RHOF=RHOF, RB=rb, EFload=EFload)


def cos_anchored(g, e):
    g = np.asarray(g, float) - 7; e = np.asarray(e, float) - 7
    m = ~(np.isnan(g) | np.isnan(e)); g, e = g[m], e[m]
    if len(g) < 3 or np.linalg.norm(g) < 1e-9 or np.linalg.norm(e) < 1e-9:
        return np.nan
    return float(g @ e / (np.linalg.norm(g) * np.linalg.norm(e)))


def cos_axes(comp):
    """The cos(G,E) footer of the §4.4 per-criterion table, from UNROUNDED G and E (A15)."""
    Gax, Eax = comp["Gax"], comp["Eax"]
    out = {}
    for ax in AXES5:
        ms = [m for m in MODELS if Gax[ax].get(m) is not None
              and Gax[ax][m] == Gax[ax][m] and Eax[ax][m] == Eax[ax][m]]
        out[ax] = cos_anchored([Gax[ax][m] for m in ms], [Eax[ax][m] for m in ms])
    return out


def totals(comp):
    """Assemble the symmetric total (A13-A14) per model, best first; drop incomplete models."""
    GF, GC, EF, EC = comp["GF"], comp["GC"], comp["EF"], comp["EC"]
    rows = []
    for s in MODELS:
        if s not in GF or any(v != v for v in (GF[s], GC[s], EF[s], EC[s])):
            continue
        G = (GF[s] + GC[s]) / 2
        E = (EF[s] + EC[s]) / 2
        T = (GF[s] + GC[s] + EF[s] + EC[s]) / 4
        rows.append(dict(m=s, GF=GF[s], GC=GC[s], EF=EF[s], EC=EC[s], G=G, E=E, T=T,
                         council=(s in COUNCIL)))
    rows.sort(key=lambda d: -d["T"])
    return rows


def write_section_4_4_csv(path, comp, cos, order_i, order_ii):
    """Machine-checkable dump of the three §4.4 exhibits, unrounded (the paper rounds at print)."""
    RHO, RHOF, RB, Gax, Eax = comp["RHO"], comp["RHOF"], comp["RB"], comp["Gax"], comp["Eax"]
    num = lambda v: "" if v is None or v != v else f"{v:.6f}"
    with open(path, "w") as fh:
        fh.write("exhibit,model,axis,value\n")
        for m in order_i:                                       # exhibit (i): per-axis rho
            fh.write(f"per_axis_rho,{m},factual,{num(RHOF.get(m))}\n")
            for ax in AXES5:
                fh.write(f"per_axis_rho,{m},{ax},{num(RHO[ax].get(m))}\n")
        for m in order_ii:                                      # exhibit (ii): G and E per axis
            for ax in AXES5:
                fh.write(f"generator_G,{m},{ax},{num(Gax[ax].get(m))}\n")
                fh.write(f"evaluator_E,{m},{ax},{num(Eax[ax].get(m))}\n")
        for ax in AXES5:
            fh.write(f"alignment_cos,-,{ax},{num(cos[ax])}\n")
        for m in order_i:                                       # exhibit (iii): the council column
            fh.write(f"collapsed_rho,{m},-,{num(RB.get(m))}\n")
            fh.write(f"factual_loading,{m},-,{num(comp['EFload'].get(m))}\n")


def main():
    D = run_dirs()
    GA, targets = load(D)
    comp = components(GA, targets, scoring_atoms(targets), diagnostics=True)
    Gax, Eax, RHO, RHOF, RB = comp["Gax"], comp["Eax"], comp["RHO"], comp["RHOF"], comp["RB"]
    cos = cos_axes(comp)
    rows = totals(comp)

    # §4.4 exhibit (i) is ordered by each evaluator's mean over the four per-archetype non-factual
    # axes -- the same four (A11) collapses -- so the ordering and the council gate agree on what
    # "reliable" means. Ties are impossible at this precision; NaN sorts last.
    key = lambda m: -st.mean([RHO[ax][m] for ax in NF4KEY if RHO[ax][m] == RHO[ax][m]] or [-9])
    order_i = sorted(MODELS, key=key)
    order_ii = [m for m in GE_ORDER if m in MODELS]

    # ---- emit leaderboard (model, total, council) as CSV for downstream figures (Fig 1) ----
    # Only the published anchor-7 run owns this file (probe_K_2*; the §4.9 regenerations are
    # probe_K_anchor7_*, the same naming anchor_sweep_leaderboard.py relies on). compare_runs.py
    # drives this script once per regeneration and reads our stdout, so those passes must leave
    # the published leaderboard on disk untouched. The §4.4 CSV carries the same guard.
    if Path(D[7]).name.startswith("probe_K_2"):
        dd = Path(__file__).resolve().parent.parent / "data"
        with open(dd / "total_rating_leaderboard.csv", "w") as fh:
            fh.write("model,total,council\n")
            for d in rows:
                fh.write(f"{d['m']},{r2(d['T'])},{'yes' if d['council'] else 'no'}\n")
        write_section_4_4_csv(dd / "section_4_4_criterion_b.csv", comp, cos, order_i, order_ii)

    # ---- print the submitted tables -----------------------------------------------------------
    print("=== Final leaderboard (sec 4.7): T = 1/4(G^F+G^C+E^F+E^C);  E = 1/2(E^F+E^C),  G = 1/2(G^F+G^C) ===")
    print(f"{'#':>2} {'model':22}{'council':>8}{'T':>7}{'E':>7}{'G':>7}")
    for i, d in enumerate(rows, 1):
        print(f"{i:>2} {d['m']:22}{('yes' if d['council'] else '--'):>8}{r2(d['T']):>7}{r2(d['E']):>7}{r2(d['G']):>7}")

    print("\n=== Competence breakdown (sec 4.7): the four anchored components ===")
    print(f"{'model':22}{'G^F':>7}{'G^C':>7}{'E^F':>7}{'E^C':>7}")
    for d in rows:
        print(f"{d['m']:22}{r2(d['GF']):>7}{r2(d['GC']):>7}{r2(d['EF']):>7}{r2(d['EC']):>7}")

    print("\n=== sec 4.4 exhibit (i): anchor-sweep consistency rho, per evaluator and axis (A10) ===")
    print(f"{'evaluator':22}{'factual':>9}" + "".join(f"{ax:>9}" for ax in AXES5))
    for m in order_i:
        vals = [RHOF.get(m)] + [RHO[ax].get(m) for ax in AXES5]
        print(f"{m:22}" + "".join(f"{(r2(v) if v is not None and v == v else 'n/a'):>9}" for v in vals))

    print("\n=== sec 4.4 exhibit (ii): generator quality G (reliability-weighted, A12b) vs evaluator reliability E ===")
    print(f"{'model':22}" + "".join(f"{ax+' G':>9}{ax+' E':>9}" for ax in AXES5))
    for s in order_ii:
        cells = ""
        for ax in AXES5:
            g = Gax[ax].get(s); e = Eax[ax].get(s)
            cells += f"{(r1(g) if g is not None and g == g else 'na'):>9}{(r1(e) if e == e else 'na'):>9}"
        print(f"{s:22}{cells}")
    print(f"{'cos(G,E)':22}" + "".join(f"{r2(cos[ax]):>9}{'':>9}" for ax in AXES5))

    print("\n=== sec 4.4 exhibit (iii): the council -- factual competence loading and criterion reliability ===")
    print("(95% CIs: generation_factuality_validation.py for the loading, criterion_b_stability.py for rho_bar)")
    print(f"{'council member':22}{'loading':>9}{'rho_bar':>9}")
    for m in sorted(COUNCIL, key=lambda z: -comp["EFload"][z]):
        print(f"{m:22}{r2(comp['EFload'][m]):>9}{r2(RB[m]):>9}")


if __name__ == "__main__":
    main()
