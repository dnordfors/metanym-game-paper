# Script index

A readable index of what [`reproduce.sh`](reproduce.sh) runs, and which paper number each step
produces. `reproduce.sh` is the authoritative map — this file mirrors it for reading. Every script
in `scripts/` is listed below; the package ships nothing else, so there is no question of which
file is current.

## The pipeline

| Paper result | Script | Produces |
|---|---|---|
| §4.1 un-anchored LSO leaderboard, consecutive gaps, and the leading-eight / trailing-four division | `section_4_1_unanchored.py` | leave-self-out means + 95% CIs from `data/probe_J_*`; bootstrap P(pair holds) for adjacent ranks and the 32 cross-division pairs; writes `data/section_4_1_unanchored.csv`; asserts the manuscript floors (max upper gap ≤ 0.17, adjacent P 0.53–0.75, cross-division min P ≥ 0.79) |
| §4.6 symmetric total **T**, the four components, and Tables 11/12 | `build_paper1_tables.py` | T = ¼(G^F+G^C+E^F+E^C) (A14); G^C is **reliability-weighted** (A12b); reproduces the published leaderboard exactly |
| §4.4 all three exhibits — per-axis ρ, per-criterion G vs E with cos(G,E), and the council reliability column | `build_paper1_tables.py` | prints the three tables and writes `data/section_4_4_criterion_b.csv` (unrounded). Everything is **leave-self-out** over archetypes 1–5, and every intermediate is carried unrounded to a single round-half-up at print time |
| §4.6 the 95% interval on **T** | `bootstrap_total.py` | joint percentile bootstrap over the 55 (submission, archetype) atoms (A.5): one draw per replicate recomputes every component, the anchor's own f_a and ρ̄_a included, and T is re-formed. Point estimates are `build_paper1_tables.py`'s — it imports that script's `components()`/`totals()` rather than re-implementing them |
| §4.3 Criterion A — evaluator factual competence **E^F** (Table 6) | `generation_factuality_validation.py` | graded **soft**-SVD left-vector loading (0.58/0.55/0.36/…) + anchored E^F (A5–A7, A12); reproduces Table 6 exactly |
| §4.7 Fig 1 headline ½(E^F+G^F) vs GPQA (r=0.92) | `plot_average_validation.py` | the combined-r 0.92 figure (one canonical source for the headline) |
| §4.3 — generator factual competence **G^F_svd** (spectral) | `generator_factual_competence.py` | SVD right-vector loading per generator (A8–A9) |
| §4.3 — subjective **G^F** vs spectral validation (r≈0.96) | `generation_factuality_validation.py` | full-panel competence-weighted G^F vs G^F_svd |
| §4.4 Criterion B — criterion competence **E^C** (anchor-shift), and the council table's 95% CI | `criterion_b_stability.py` | per-axis ρ (A10) + collapsed ρ̄ (A11), anchored E^C (A12), leave-self-out over archetypes 1–5, plus the percentile bootstrap. Point estimates are `build_paper1_tables.py`'s and are asserted equal to it at the end of the run, so the two cannot drift |
| §4.4 alignment footer **cos(G,E)** (5 non-factual axes) | `alignment_cosine.py` | anchored cosine (A15) + bootstrap CIs; imports `build_paper1_tables.py`'s `components()`/`cos_axes()` for both the point value and each replicate, so G is the reliability-weighted council mean (A12b) on one code path |
| §4.3 same-vendor robustness (leave-one-vendor-out) | `vendor_robustness.py` | graded G^F factual ordering under per-vendor judge removal (Spearman vs full) |
| §5.7 anchor-sweep robustness of the official leaderboard (N=4 non-semantic perturbation) | `anchor_sweep_leaderboard.py` | §4.4 rating recomputed per anchor 5/6/7/8; pairwise Spearman 0.90–0.96 (mean 0.94), rank range ≤1 above the trailing four |
| §4.3/§5.6 graded-vs-binarised SVD comparison (same matrix) | `graded_vs_binary_svd.py` | binary thresholds t∈{4,5,6}: Spearman vs graded 0.78–0.90; fifth council seat flips Flash↔Sonnet-4 with t |
| §4.8 robustness to regeneration (N=3): T1/T2/T3, run-to-run SD, council identity, pairwise Pearson/Spearman | `compare_runs.py <run1> <run2> <run3> --sweep data` | compares the 3 anchor-7 regenerations (run1 = bootstrap; runs 2-3 in `data/regenerations/`); reproduces §4.8 exactly |

All scripts use the **graded** 1–10 SVD (no thresholding), matching Appendix A.2.a
(equations A1–A15).

**`reproduce.sh` runs all of these in order and is the proven bridge** — it regenerates every exhibit
from `data/` (pinned from experiment `papers/v3/experiments/17_bold_api_probe`), so the paper↔data
links are verified by execution, not asserted. Three scripts also emit small CSVs — two of them what
Fig 1 consumes: `generation_factuality_validation.py` → `data/criterion_a_ef_gf.csv` (anchored E^F +
G^F); `build_paper1_tables.py` → `data/total_rating_leaderboard.csv`; and `bootstrap_total.py` →
`data/total_rating_bootstrap.csv` (the same totals with their 95% intervals). Run `bash reproduce.sh`.

## Inputs

Provenance and contents of every input: see [`DATA_MANIFEST.md`](DATA_MANIFEST.md). The scripts read
`RUNS_GEN` (the anchor-7 run) and/or `RUNS_SWEEP` (the `data/` parent holding anchors 5/6/7/8);
`reproduce.sh` sets both, so running it needs no environment setup.

Earlier drafts also carried binary-verdict and un-weighted-mean variants of these estimators as
cross-checks. They disagreed with the published graded, reliability-weighted results and are not part
of the release; they remain in the working repo's experiment history.
