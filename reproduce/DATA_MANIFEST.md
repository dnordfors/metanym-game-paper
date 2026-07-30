# Data manifest

Provenance and contents of everything in `data/`. This directory is **self-contained**: a clean
checkout runs `reproduce.sh` with no downloads, no credentials and no API calls. Paths below are
relative to `reproduce/`.

For *which script produces which exhibit*, read `reproduce.sh` — that is the single map, and it is
verified by being run. This file only records where the inputs came from.

## Upstream source

Every evaluation run here is pinned from experiment
`papers/v3/experiments/17_bold_api_probe` in the private `archetypal-contexts` working repo.
Portfolios were generated and cross-evaluated through the BOLD gateway at temperature 0 with
reasoning disabled; each model evaluates every portfolio on the six-axis rubric against a fixed
anchor reference. The run therefore contains **self-evaluation files** (`eval_X_x_X.json`) as
well as cross-evaluations, and they are shipped here unmodified. No rating in the paper uses
them: every estimator in `scripts/` is leave-self-out and drops the self-pair before scoring.

## Evaluation runs

Each run directory holds one `eval_<evaluator>_x_<target>.json` per ordered model pair, plus the
matching `.md` transcript. The JSON carries the per-parallel-context `factual_per_pc` ratings and
the per-archetype non-factual axis ratings. Counts below are `json` / `md` files.

| Directory | Role | Paper | Files |
|---|---|---|---|
| `data/probe_J_20260529T005230Z/` | un-anchored full-panel run (no calibration anchor) | §4.1 | 144 / 144 + `run_info.json` + `leaderboard_lso.json` |
| `data/probe_K_20260529T014133Z/` | run 1, anchor 7 — the **published** leaderboard | §4.3–§4.7 | 134 / 132 |
| `data/probe_K_anchor5_20260529T030442Z/` | anchor sweep, anchor 5 | §4.3, §5.7 | 135 / 132 |
| `data/probe_K_anchor6_20260529T032518Z/` | anchor sweep, anchor 6 | §4.3, §5.7 | 133 / 132 |
| `data/probe_K_anchor8_20260529T033755Z/` | anchor sweep, anchor 8 | §4.3, §5.7 | 135 / 132 |
| `data/regenerations/probe_K_anchor7_20260619T015828Z/` | run 2 — independent regeneration | §4.8 | 133 / 132 |
| `data/regenerations/probe_K_anchor7_20260619T040659Z/` | run 3 — independent regeneration | §4.8 | 133 / 132 |

Anchor 7 serves double duty: it is both the production run and the anchor-7 point of the sweep
(`anchor_sweep_leaderboard.py` matches it by the `probe_K_2*` prefix). The JSON counts exceed the
132 ordered pairs by the run's own metadata/config files.

`reproduce.sh` locates these through three environment variables it sets itself —
`RUNS_GEN` (run 1), `RUNS_SWEEP` and `RUNS` (the `data/` parent holding all four anchors) — so no
manual environment setup is required.

## Provided tables

| File | Contents |
|---|---|
| `data/gpqa_selfadministered.csv` | GPQA Diamond, self-administered on the same 12-model roster under the council protocol (T=0, reasoning off), `accuracy = n_correct/198`. The independent measure Figure 1 correlates against (§4.7). |
| `data/external_benchmarks.csv` | Published external scores for the 12-model roster, the substrate for the §4.3 / §5.3 external-validation discussion. |
| `data/our_metrics.csv` | E^F_svd and G^F_svd at anchor 7 with bootstrap 95% CIs, as a convenience snapshot of the headline metrics. |

## Written by `reproduce.sh`

These are **outputs**, committed so a reader can diff them against a fresh run:

| File | Written by |
|---|---|
| `data/criterion_a_ef_gf.csv` | `scripts/generation_factuality_validation.py` (anchored E^F + G^F) |
| `data/total_rating_leaderboard.csv` | `scripts/build_paper1_tables.py` (total T + council seats), from run 1 — the published leaderboard. The §4.8 step drives the same script once per regeneration run; only run 1 writes this file. |
| `data/total_rating_bootstrap.csv` | `scripts/bootstrap_total.py` (the same totals with their 95% joint-bootstrap interval, A.5), from run 1. The `total` column is `build_paper1_tables.py`'s, computed by the same imported code, so the two CSVs agree exactly. Same run-1-only guard. |
| `data/section_4_4_criterion_b.csv` | `scripts/build_paper1_tables.py` (all three §4.4 exhibits in one long-format file: the per-axis anchor-shift consistencies of exhibit (i), the per-criterion G/E pairs and cosines of exhibit (ii), and the criterion-reliability column of the council table, exhibit (iii)). Values are unrounded, so the file is the machine-checkable source behind the rounded cells printed in the paper. Same run-1-only guard as the leaderboard. |
| `data/section_4_1_unanchored.csv` | `scripts/section_4_1_unanchored.py` (un-anchored LSO means and 95% CIs for the §4.1 leaderboard) |
| `figures/average_validation.png` | `scripts/plot_average_validation.py` (paper Figure 1) |

Re-running `reproduce.sh` rewrites the CSVs byte-identically — the bootstrap draws from a
fixed seed, so its interval columns do not move between runs. The PNG is not byte-reproducible:
what it plots is identical, but text is rasterised slightly differently by different font stacks, so
roughly 2% of its pixels change — the labels and tick numbers, not the data. Diff the CSVs, and
compare the figure by eye.

## Not included

- **Level-1 re-generation tooling.** `reproduce.sh` is deterministic re-analysis of the pinned
  outputs. Re-querying the models to produce a *new* run (a fresh N, non-deterministic, costs
  budget) is a separate activity; that tooling lives with the upstream experiment in the working
  repo, not in this package.
- **Raw generated portfolios** beyond the `.md` transcripts already inside each run directory.
  The appendices in `paper/appendices/` carry the portfolios the paper actually exhibits.
- **The validated archetype database.** Not read by any script here; it lives upstream at
  `projects/completed/council-of-peers-benchmark-2/data/archetype_db/archetypes.json`.
