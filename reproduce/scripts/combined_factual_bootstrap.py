#!/usr/bin/env python3
"""95% joint bootstrap interval for the combined factual rating 1/2(E^F + G^F).

The §4.8 figure's horizontal bars. The earlier convention — averaging the endpoints of the
E^F and G^F component intervals — is not a valid interval for the mean of two correlated
quantities; this script replaces it with the A.5 joint resample: one draw of the 55
(submission, archetype) atoms per replicate recomputes the full factual factorisation —
E^F with its in-replicate anchoring f/f_a, G^F likewise — and 1/2(E^F+G^F) is formed on
that one resample, so the components' covariance is captured automatically. Percentiles of
the replicates are the interval. Twelve-evaluator basis, matching §4.2/§4.8 (the selection
evidence; §4.8 precedes the council deliberately).

The anchor's combined value is 7 by calibration in every replicate (both halves anchored to
itself), so its interval is degenerate at 7 — the figure's "x exact, no horizontal bar".
Inert-band models inherit the §4.2 interval conventions (see the dagger note there).

Writes data/combined_factual_bootstrap.csv. Deterministic (fixed seed).
Run: RUNS_GEN=... RUNS_SWEEP=... python scripts/combined_factual_bootstrap.py
"""
from pathlib import Path

import numpy as np

from build_paper1_tables import components, load, run_dirs, scoring_atoms

SEED = 20260816
B = 1000


def main():
    GA, targets = load(run_dirs())
    atoms = scoring_atoms(targets)
    comp = components(GA, targets, atoms)
    models = sorted(set(comp["EF"]) | set(comp["GF"]))

    def combined(c):
        out = {}
        for m in models:
            ef, gf = c["EF"].get(m), c["GF"].get(m)
            if ef is not None and gf is not None and ef == ef and gf == gf:
                out[m] = (ef + gf) / 2
        return out

    point = combined(comp)
    rng = np.random.default_rng(SEED)
    acc = {m: [] for m in models}
    n = len(atoms)
    for _ in range(B):
        draw = [atoms[i] for i in rng.integers(0, n, n)]
        for m, v in combined(components(GA, targets, draw)).items():
            acc[m].append(v)

    out = Path(__file__).resolve().parent.parent / "data" / "combined_factual_bootstrap.csv"
    lines = ["model,combined,lo95,hi95"]
    print(f"{'model':24}{'1/2(EF+GF)':>12}   95% joint CI")
    for m in sorted(point, key=lambda m: -point[m]):
        lo, hi = np.percentile(acc[m], [2.5, 97.5])
        print(f"{m:24}{point[m]:>12.2f}   [{lo:.2f}, {hi:.2f}]")
        lines.append(f"{m},{point[m]:.4f},{lo:.4f},{hi:.4f}")
    out.write_text("\n".join(lines) + "\n")
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
