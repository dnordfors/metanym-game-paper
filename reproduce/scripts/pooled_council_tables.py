#!/usr/bin/env python3
"""Council-basis official tables on the POOLED corpus (mirrors council_basis_tables.py).

Writes to the sub-project's data/ with the package's CSV schemas, suffixed by the pooled set:
  total_rating_council_<tag>.csv, total_rating_council_replicates_<tag>.csv, total_rating_twelve_<tag>.csv
Env: RUNS (default "1,2,3"), B (default 1000; 0 = point estimates only), SEED (20260816).
"""
import os, sys, csv, statistics as st
from pathlib import Path
import numpy as np
sys.path.insert(0, str(Path(__file__).resolve().parent))
import pooled_components as PC
from pooled_components import MODELS, COUNCIL, AM

runs = [int(x) for x in os.environ.get("RUNS", "1,2,3").split(",")]
B_REP = int(os.environ.get("B", 1000)); SEED = int(os.environ.get("SEED", 20260816))
tag = "pooled" + "".join(map(str, runs))
OUT = Path(__file__).resolve().parent.parent / "data"; OUT.mkdir(exist_ok=True)

GAs = PC.load_runs(runs); graded = PC.graded_targets(GAs)
rounds, ballast = PC.council_rounds(GAs, graded)
rng = np.random.default_rng(SEED)
rows, ci, reps = {}, {}, {}

def boot(panel, g, rated):
    atoms = PC.scoring_atoms(GAs, g); n = len(atoms); acc = {m: [] for m in rated}
    for _ in range(B_REP):
        draw = [atoms[i] for i in rng.integers(0, n, n)]
        c = PC.components(GAs, g, draw, panel)
        for m in rated:
            T, _ = PC.T_of(c, m)
            if T is not None:
                acc[m].append(T)
    return acc

# seats round (one bootstrap serves the five seats), then one round per contestant
panel, g = rounds[AM]
seats = PC.components(GAs, g, PC.scoring_atoms(GAs, g), panel)
for m in COUNCIL:
    rows[m] = PC.T_of(seats, m)
seats_gap = seats["gap"]
if B_REP:
    acc = boot(panel, g, COUNCIL)
    for m, v in acc.items():
        if len(v) > 20:
            ci[m] = (np.percentile(v, 2.5), np.percentile(v, 97.5)); reps[m] = v
gaps = {}
for m in [x for x in MODELS if x not in COUNCIL]:
    panel, g = rounds[m]
    c = PC.components(GAs, g, PC.scoring_atoms(GAs, g), panel); rows[m] = PC.T_of(c, m); gaps[m] = c["gap"]
    if B_REP:
        acc = boot(panel, g, [m])
        if len(acc[m]) > 20:
            ci[m] = (np.percentile(acc[m], 2.5), np.percentile(acc[m], 97.5)); reps[m] = acc[m]

hdr = [f"# council-basis official leaderboard on the pooled corpus, runs {runs}: T = 1/4(GF+GC+EF+EC), per-round A.5 bootstrap CI",
       f"# produced by scripts/pooled_council_tables.py (seed {SEED}, B={B_REP}); ballast {ballast}",
       "model,council,T,T_lo95,T_hi95,GF,GC,EF,EC"]
order = sorted([m for m in rows if rows[m][0] is not None], key=lambda m: -rows[m][0])
for m in order:
    T, (GF, GC, EF, EC) = rows[m]; lo, hi = ci.get(m, (float("nan"),) * 2)
    hdr.append(f"{m},{'yes' if m in COUNCIL else 'no'},{T:.4f},{lo:.4f},{hi:.4f},{GF:.4f},{GC:.4f},{EF:.4f},{EC:.4f}")
(OUT / f"total_rating_council_{tag}.csv").write_text("\n".join(hdr) + "\n")
if B_REP:
    lines = [f"# per-model T bootstrap replicates (council basis, pooled runs {runs}; seed {SEED}, B={B_REP})",
             "# produced by scripts/pooled_council_tables.py",
             "model," + ",".join(f"r{i}" for i in range(B_REP))]
    for m in sorted(reps):
        v = list(reps[m]) + [""] * (B_REP - len(reps[m]))
        lines.append(m + "," + ",".join(f"{x:.4f}" if x != "" else "" for x in v))
    (OUT / f"total_rating_council_replicates_{tag}.csv").write_text("\n".join(lines) + "\n")
pub = PC.components(GAs, graded, PC.scoring_atoms(GAs, graded), MODELS)
lines = [f"# twelve-evaluator components on the pooled corpus, runs {runs}; sigma1/sigma2 = {pub['gap']:.4f}",
         "# produced by scripts/pooled_council_tables.py", "model,T,GF,GC,EF,EC"]
for m in MODELS:
    T, (GF, GC, EF, EC) = PC.T_of(pub, m)
    if T is not None:
        lines.append(f"{m},{T:.4f},{GF:.4f},{GC:.4f},{EF:.4f},{EC:.4f}")
(OUT / f"total_rating_twelve_{tag}.csv").write_text("\n".join(lines) + "\n")

print(f"runs {runs}: ballast {ballast}; twelve-basis gap {pub['gap']:.2f} ({pub['ncols']} columns); seats-round gap {seats_gap:.2f}")
print(f"{'#':>2} {'model':22}{'seat':>5}{'T':>7}  {'95% CI':16}{'GF':>6}{'GC':>6}{'EF':>6}{'EC':>6}{'gap':>6}")
for i, m in enumerate(order, 1):
    T, (GF, GC, EF, EC) = rows[m]; lo, hi = ci.get(m, (float('nan'),) * 2)
    print(f"{i:>2} {m:22}{('*' if m in COUNCIL else ''):>5}{T:>7.2f}  [{lo:.2f}, {hi:.2f}]  {GF:>6.2f}{GC:>6.2f}{EF:>6.2f}{EC:>6.2f}{gaps.get(m, seats_gap):>6.2f}")
print("wrote", OUT / f"total_rating_council_{tag}.csv")
