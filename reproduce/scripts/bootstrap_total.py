#!/usr/bin/env python3
"""95% joint bootstrap interval for the symmetric total T (Appendix A.5; T itself is A14).

Appendix A.5 prescribes the method, verbatim:

    "The evaluation rating E and the total T are **not** obtained by combining the component
     intervals with an analytic (independent-variance) formula. ... Instead E and T are
     bootstrapped **jointly**, resampling on the coarsest shared grid so a single draw serves all
     three free-generation components: the **(submission, archetype) atom**. The 55 atoms are
     resampled with replacement once per replicate; each atom carries the parallel contexts inside
     it, so the resampled atoms *induce* both the factual rating columns of f (A5-A7) and the
     55-unit vectors of rho_bar (A11), while G averages over the resampled atoms of each
     submission. Every component -- including the anchor's f_a and rho_bar_a
     (the council is held at its selected membership, as A.5 states) -- is recomputed on that one resample, T is formed, and the percentiles of the T
     replicates give the interval; the joint resample captures the inter-component covariance
     automatically."

and, for every interval in the paper: "the rating's resampling unit is drawn with replacement, the
rating is recomputed, and the 2.5th and 97.5th percentiles of the replicates form the interval
(~10^3-10^4 replicates)."

This script does exactly that. One draw of the 55 (submission, archetype) atoms per replicate
drives every component at once -- the factual matrix columns and hence f, including the anchor's
own f_a; the 55-unit collapsed vectors and hence rho_bar, including the anchor's own rho_bar_a;
and the per-submission means G^C averages -- T = 1/4(G^F+G^C+E^F+E^C) is re-formed on that one
resample, and the 2.5/97.5 percentiles of the T replicates are the interval. B=1000 replicates at
a fixed seed, so repeated runs are byte-identical.

One departure from the wording above, stated rather than hidden: the **council is held at its
selected membership** (we condition on selection) rather than re-selected per replicate. The A.3
gate is itself defined by a bootstrap CI on f, so re-selecting within a replicate would require a
nested bootstrap; and the council is a fixed roster everywhere else in this package, including in
build_paper1_tables.py, which owns the published point estimates. Everything else A.5 names --
f_a, rho_bar_a and every component -- is recomputed on the resample.

The point estimates are not recomputed here. build_paper1_tables.py, the canonical producer of the
published tables, exposes components() and totals(); this script calls them for the point estimate
and again on every resample, so the T column below is that script's T by construction rather than
a second implementation of the same estimator.

Env: RUNS_GEN (anchor-7 run), RUNS_SWEEP (parent of probe_K_anchor{5,6,8}). See DATA_MANIFEST.md.
Run: RUNS_GEN=... RUNS_SWEEP=... python scripts/bootstrap_total.py
"""
from __future__ import annotations
from pathlib import Path
import numpy as np

from build_paper1_tables import (MODELS, SCORED_ARCHETYPES, r2, run_dirs, load,
                                 scoring_atoms, components, totals)

SEED = 20260606     # fixed: the CSV this writes is byte-identical between runs
B = 1000            # replicates (A.5: ~10^3-10^4)


def main():
    D = run_dirs()
    GA, targets = load(D)
    atoms = scoring_atoms(targets)          # 11 submissions x SCORED_ARCHETYPES archetypes
    rows = totals(components(GA, targets, atoms))       # the published point estimates

    rng = np.random.default_rng(SEED)
    n = len(atoms)
    acc = {d["m"]: [] for d in rows}
    for _ in range(B):
        draw = [atoms[i] for i in rng.integers(0, n, n)]
        for d in totals(components(GA, targets, draw)):
            if d["m"] in acc:
                acc[d["m"]].append(d["T"])
    ci = {m: (float(np.percentile(v, 2.5)), float(np.percentile(v, 97.5))) if len(v) > 20
          else (float("nan"), float("nan")) for m, v in acc.items()}

    print(f"Total rating T = 1/4(G^F+G^C+E^F+E^C) with a 95% joint bootstrap CI over the "
          f"{n} (submission, archetype) atoms")
    print(f"B={B} replicates, seed={SEED}, archetypes 1-{SCORED_ARCHETYPES}; council held at its "
          f"selected membership (A.5, A.3)")
    print(f"{'#':>2} {'model':22}{'council':>8}{'T':>7}   95% CI          replicates")
    for i, d in enumerate(rows, 1):
        lo, hi = ci[d["m"]]
        print(f"{i:>2} {d['m']:22}{('yes' if d['council'] else '--'):>8}{r2(d['T']):>7}"
              f"   [{lo:.2f}, {hi:.2f}]{len(acc[d['m']]):>14}")
    missing = [m for m in MODELS if m not in acc]
    if missing:
        print("no complete set of four components:", ", ".join(missing))

    # Only the published anchor-7 run owns this file, exactly as for the leaderboard CSV: any
    # other run dir (a §4.9 regeneration, say) may be analysed without overwriting the release.
    if Path(D[7]).name.startswith("probe_K_2"):
        out = Path(__file__).resolve().parent.parent / "data" / "total_rating_bootstrap.csv"
        with open(out, "w") as fh:
            fh.write("model,total,total_lo,total_hi,council\n")
            for d in rows:
                lo, hi = ci[d["m"]]
                fh.write(f"{d['m']},{r2(d['T'])},{r2(lo)},{r2(hi)},"
                         f"{'yes' if d['council'] else 'no'}\n")
        print("wrote", out)


if __name__ == "__main__":
    main()
