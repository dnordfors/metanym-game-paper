#!/usr/bin/env python3
"""Anchored-cosine alignment of generation vs evaluation, per criterion (§4.4 footer).

For each criterion the table pairs the generator quality G with the evaluator reliability E
across the panel, both anchored so the anchor model reads 7, and reports their **anchored
cosine** -- the cosine of the two vectors after subtracting the anchor point (7,7). Because the
anchor sits at 7 on both axes by construction, the anchored cosine measures how the panel's
deviations-from-anchor in making line up with its deviations-from-anchor in judging.
(Appendix A.6, eq A15.)

  Covers the five non-factual criteria (factual competence is Criterion A's separate measure).
  G : per-axis council leave-self-out generation mean at anchor 7, each council member's vote
      weighted by its own per-axis reliability max(rho_{t,x},0) (A12b); anchor pinned 7.
  E : per-axis criterion reliability E^C_a = 7 rho_{s,x}/rho_{a,x} (A.2.b/A10, A12).
  cos(G,E)_x = <G_x-7, E_x-7> / (||G_x-7|| ||E_x-7||)   over the panel.   (A15)

Both G and E are formed from UNROUNDED rho and unrounded per-axis means: the paper rounds once,
at print time. The point estimate is `build_paper1_tables.py`'s -- this script imports that
script's `components()` and `cos_axes()` rather than re-implementing the estimator, exactly as
`bootstrap_total.py` does, so the cosine printed here and the cos(G,E) footer row of the §4.4
table are the same number by construction. What this script adds is the interval.

CI: percentile bootstrap over the 55 (submission, archetype) atoms (A.5), recomputing
G, E and the cosine on each resample.

Env: RUNS_GEN (anchor-7 run), RUNS_SWEEP (dir holding anchor 5/6/7/8).
Run: RUNS_GEN=... RUNS_SWEEP=... python scripts/alignment_cosine.py
"""
from __future__ import annotations
import numpy as np

from build_paper1_tables import (AXES5, r2, run_dirs, load, scoring_atoms, components, cos_axes)

SEED = 20260606
B = 1000            # replicates (A.5: ~10^3-10^4)

# Self-check: the cos(G,E) footer row of the §4.4 table, to the precision the paper prints.
TABLE = {"beauty": 0.91, "intel": 0.90, "distinct": 0.89, "length": 0.84, "struct": 0.87}


def main():
    GA, targets = load(run_dirs())
    atoms = scoring_atoms(targets)
    point = cos_axes(components(GA, targets, atoms))

    rng = np.random.default_rng(SEED)
    n = len(atoms)
    boots = {ax: [] for ax in AXES5}
    for _ in range(B):
        draw = [atoms[i] for i in rng.integers(0, n, n)]
        rep = cos_axes(components(GA, targets, draw))
        for ax in AXES5:
            if rep[ax] == rep[ax]:
                boots[ax].append(rep[ax])

    print(f"anchored cosine cos(G,E) per criterion (A15), with a 95% percentile bootstrap over "
          f"the {n} (submission, archetype) atoms of A.5")
    print(f"B={B} replicates, seed={SEED}; G is the reliability-weighted council mean (A12b)")
    print(f"{'criterion':10}{'cos(G,E)':>10}{'95% CI':>16}{'table':>8}{'match':>8}")
    for ax in AXES5:
        lo, hi = ((np.percentile(boots[ax], 2.5), np.percentile(boots[ax], 97.5))
                  if len(boots[ax]) > 20 else (np.nan, np.nan))
        p, t = point[ax], TABLE[ax]
        ok = "  ok" if r2(p) == t else f"  d={p - t:+.2f}"
        print(f"{ax:10}{p:>10.3f}   [{r2(lo):.2f}, {r2(hi):.2f}]{t:>8.2f}{ok:>8}")


if __name__ == "__main__":
    main()
