# Data manifest

Provenance and contents of everything in `data/`. This directory is **self-contained**: a clean
checkout runs `reproduce.sh` with no downloads, no credentials and no API calls. Paths below are
relative to `reproduce/`.

For *which script produces which exhibit*, read `reproduce.sh` — that is the single map, and it is
verified by being run. This file only records where the inputs came from.

## Upstream source

Every evaluation run here is pinned from the API-probe experiment of 28–29 May 2026 in the private working
repository. Portfolios were generated and cross-evaluated through an API gateway fronting the vendors' endpoints
(each envelope carries the vendor's model version string and token counts) at temperature 0 with
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
| `data/probe_J_20260529T005230Z/` | un-anchored run, all twelve participants (no calibration anchor) | §4.1 | 144 / 144 + `run_info.json` + `leaderboard_lso.json` |
| `data/probe_K_20260529T014133Z/` | run 1, anchor 7 — the **published** leaderboard | §4.2–§4.9 | 134 / 132 |
| `data/probe_K_anchor5_20260529T030442Z/` | anchor sweep, anchor 5 | §4.2, §5.7 | 135 / 132 |
| `data/probe_K_anchor6_20260529T032518Z/` | anchor sweep, anchor 6 | §4.2, §5.7 | 133 / 132 |
| `data/probe_K_anchor8_20260529T033755Z/` | anchor sweep, anchor 8 | §4.2, §5.7 | 135 / 132 |
| `data/regenerations/probe_K_anchor7_20260619T015828Z/` | run 2 — independent regeneration | §4.9 | 133 / 132 |
| `data/regenerations/probe_K_anchor7_20260619T040659Z/` | run 3 — independent regeneration | §4.9 | 133 / 132 |
| `data/portfolios_run1/` | run 1 — the twelve raw generator portfolios the canonical run evaluated (`<model>_off_T0_r1.md`, verbatim as generated; the matching `.json` is the gateway envelope: the response, model version and token counts). The anchor and the two ballast files in `submissions/` are copies of three of them | §4 | 12 / 12 |
| `data/regenerations/portfolios_run2/` | run 2 — the twelve raw generator portfolios (`<model>_off_T0_r1.md`; same prompt, T = 0, reasoning off) | §6 (ICLR) | 12 |
| `data/regenerations/portfolios_run3/` | run 3 — the twelve raw generator portfolios, two hours after run 2 | §6 (ICLR) | 12 |
| `prompts/` | the prompts as sent: `generator.md` (Appendix B.1), `evaluator_calibrated.md` (Appendix B.2, every anchored run and the thinking-vs-play evaluation), `evaluator.md` (the un-anchored form of §4.1) | Appendix B | 3 |
| `data/thinking_vs_play/20260916T023717Z/gen/` | thinking-vs-play (2026-09-16, official Anthropic/OpenAI APIs): the eight portfolios (`<player>.md`; `.reasoning.md` = the vendor's thinking summary; `.json` = envelope + raw response + request) | §6 (ICLR) | 8 |
| `data/thinking_vs_play/20260916T023717Z/eval/` | thinking-vs-play: the 64 evaluations (`eval_<judge>_x_<target>.*`) with the calibrated evaluator prompt (`data/thinking_vs_play/evaluator_calibrated.md`), anchor = claude-opus-4.5's run-1 portfolio pinned at 7, ballasts = the two ballast submissions | §6 (ICLR) | 64 |

Run 1's log records a 5,373-character evaluator template; `prompts/evaluator_calibrated.md` has 5,512 characters and is
the revision the anchor sweep (anchors 5, 6, 8, from two hours later) and both regenerations record. Run 1 was made with an
earlier revision of the same prompt that was not kept; Appendix B prints the shipped one. `scripts/verify_chain.py` expects
exactly this discrepancy and no other.

Paths recorded in the run logs and `run_info.json` files are rewritten to package-relative paths (`data/…`, `prompts/…`),
all of which resolve inside this directory; nothing else in a record is altered.

Anchor 7 serves double duty: it is both the production run and the anchor-7 point of the sweep
(`anchor_sweep_leaderboard.py` matches it by the `probe_K_2*` prefix). The JSON counts exceed the
132 ordered pairs by the run's own metadata/config files.

`reproduce.sh` locates these through three environment variables it sets itself —
`RUNS_GEN` (run 1), `RUNS_SWEEP` and `RUNS` (the `data/` parent holding all four anchors) — so no
manual environment setup is required.

## Provided tables

| File | Contents |
|---|---|
| `data/gpqa_selfadministered.csv` | GPQA Diamond, self-administered on the same 12-model roster under the council protocol (T=0, reasoning off), `accuracy = n_correct/198`. The independent measure the §4.8 figure correlates against. |
| `data/external_benchmarks.csv` | Published external scores for the 12-model roster, published external scores kept for reference; not read by `reproduce.sh`. |
| `data/our_metrics.csv` | E^F_svd and G^F_svd at anchor 7 with bootstrap 95% CIs, as a convenience snapshot of the headline metrics. |

## Written by `reproduce.sh`

These are **outputs**, committed so a reader can diff them against a fresh run:

| File | Written by |
|---|---|
| `data/criterion_a_ef_gf.csv` | `scripts/generation_factuality_validation.py` (anchored E^F + G^F) |
| `data/total_rating_twelvebasis.csv` | `scripts/build_paper1_tables.py`: total T + council seats on the **twelve-participant basis** of §4.2–§4.4 — the basis the council was selected on; §4.7 compares it with the official council basis (Spearman 0.986, MAD 0.12) and Appendix D.1 re-runs the GPQA coupling on it. Not the published leaderboard (that is `data/total_rating_council.csv`, below). The §4.9 step drives the same script once per regeneration run; only run 1 writes this file. |
| `data/total_rating_twelvebasis_bootstrap.csv` | `scripts/bootstrap_total.py` (the same totals with their 95% joint-bootstrap interval, A.5), from run 1. The `total` column is `build_paper1_tables.py`'s, computed by the same imported code, so the two CSVs agree exactly. Same run-1-only guard. |
| `data/section_4_4_criterion_b.csv` | `scripts/build_paper1_tables.py` (all three §4.4 exhibits in one long-format file: the per-axis anchor-sweep consistencies of exhibit (i), the per-criterion G/E pairs and cosines of exhibit (ii), and the criterion-reliability column of the council table, exhibit (iii)). Values are unrounded, so the file is the machine-checkable source behind the rounded cells printed in the paper. Same run-1-only guard as the leaderboard. |
| `data/section_4_1_unanchored.csv` | `scripts/section_4_1_unanchored.py` (un-anchored LSO means and 95% CIs for the §4.1 leaderboard) |
| `figures/total_validation.png` | `scripts/plot_total_validation.py` (the §4.8 figure, T vs GPQA) |
| `figures/anchoring_resolution.png` | `scripts/plot_anchoring_resolution.py` (the §4.2 figure) |
| `figures/council_evaluation_pc1.png` | `scripts/plot_council_evaluation.py` (the §3.2 exhibit, verbatim from Appendix C) |
| `figures/council_evaluation_pc1_all.png` | `scripts/plot_council_evaluation.py --all-judges` — the same exhibit with all five judges, no ghost row | Figure 2 (arXiv v3) |
| `figures/ballast_heatmap.png` | `scripts/plot_ballast_heatmap.py` (the §4.6 exhibit) |
| *(stdout only)* | `scripts/ballast_sizing.py` — the §4.6 ballast-sizing table. Convenes all seven possible contests per candidate ballast and reports range, $\sigma_1/\sigma_2$, seat spread, fidelity to the §4.2 values, and the fraction of bootstrap resamples in which the §4.5 guards hold. Its printed reference row reproduces §4.2's $\sigma_1/\sigma_2$ (2.57 → 2.6) and is the check that the round's matrix is built the same way as the bootstrap's. |
| *(stdout only)* | `scripts/spectral_gap_checks.py` — the ICLR version's Appendix A.6 spectral-gap check: per run, $\sigma_1/\sigma_2$, $\sigma_1$ against the 95th-percentile noise edge of a per-evaluator permutation null (1.57× in run 1, 1.29× in run 3), whether $\sigma_2$ also exceeds its edge, and the bootstrap stability of $u_1$. Same matrix as `ballast_sizing.py`'s twelve-evaluator reference. |
| *(stdout only)* | `scripts/consensus_limits.py` — the §5.7 departure-from-consensus curve and the §5.7 cross-council spread. Imports its matrix builder from `ballast_sizing.py`, so both obey the leave-self-out rule above. |
| *(stdout only)* | `scripts/check_manuscript.py` — manuscript consistency: section cross-references, anchor links, section numbering, referenced appendices, table captions. Run it before any arXiv upload or venue submission. |

## Ballast submissions

`submissions/` carries the anchor portfolio and the two portfolios §4.6 pins as ballast — the two
lowest-rated submissions of the canonical run, by the participants' own factual ratings:

| file | model | participants' mean factual rating |
|---|---|---:|
| `submissions/anchor_claude-opus-4.5.md` | claude-opus-4.5 (the anchor; first archetype in full, both forms) | — |
| `submissions/ballast_gpt-4o-mini.md` | gpt-4o-mini | 4.99 |
| `submissions/ballast_gpt-4.1-nano.md` | gpt-4.1-nano | 5.38 |
| `submissions/council_evaluation_gemini-2.5-flash.md` | the complete council evaluation of gemini-2.5-flash's portfolio, run 1 (every judge's rating and justification, the administrator's synthesis); the source of the council-evaluation exhibits (`plot_council_evaluation*.py`, `plot_game_example.py`); the extended paper prints it as Appendix C | — |

They are generation output of the probe_I stage that fed run 1, reproduced verbatim. Nothing in
`reproduce.sh` reads them — the pinned evaluations already encode how the participants graded them —
but a contest under §4.5 needs the text, because the contestant grades them.

Re-running `reproduce.sh` rewrites the CSVs byte-identically — the bootstrap draws from a
fixed seed, so its interval columns do not move between runs. The PNGs are not byte-reproducible:
what it plots is identical, but text is rasterised slightly differently by different font stacks, so
roughly 2% of their pixels change — the labels and tick numbers, not the data. Diff the CSVs, and
compare the figures by eye.

## Not included

- **Level-1 re-generation tooling.** `reproduce.sh` is deterministic re-analysis of the pinned
  outputs. Re-querying the models to produce a *new* run (a fresh N, non-deterministic, costs
  budget) is a separate activity; that tooling lives with the upstream experiment in the working
  repo, not in this package.
- **The validated archetype database.** Not read by any script here; it lives upstream at
  `projects/completed/council-of-peers-benchmark-2/data/archetype_db/archetypes.json`.

## data/gpqa_runs/ and data/total_rating_council.csv
- `gpqa_runs/gpqa_20260613T173827Z/`: the raw self-administered GPQA Diamond run — per model, `responses.json` with all 198 records (raw response text, key letter, stored verdict). Source: the working repository's GPQA administration of 13 June 2026 (Appendix D.2). Audited by `scripts/gpqa_audit.py` (Appendix D).
- `total_rating_council.csv`: the §4.7 council-basis **official leaderboard** (the table in the paper and in the README) (T + per-contest A.5 bootstrap CIs + components). Produced by papers/v3/experiments/29_council_only_leaderboard/council_basis_tables.py (seed 20260816); package-side producer pending (REVIEW A8).

## data/total_rating_twelve.csv, total_rating_runs.csv, ec_svd_twelve.csv
Appendix D.1's comparison substrates: bootstrap-basis components, per-run council-basis
totals, and the declined per-axis-SVD E^C. Produced by
papers/v3/experiments/29_council_only_leaderboard/council_basis_tables.py and
papers/v3/experiments/27_svd_vs_consistency_per_axis/ec_from_svd.py (package-side producer
pending, tracked in REVIEW A8). Consumed by scripts/t_gpqa_ladder.py.

## data/total_rating_council_replicates.csv, slope_band_full.csv
The per-model T bootstrap replicate distributions (A.5 per-contest resample; anchor = point
mass at 7 by construction) and the scheme-C pointwise band. Produced by
papers/v3/experiments/29_council_only_leaderboard/council_basis_tables.py and
scripts/slope_full_bootstrap.py; consumed by Appendix D.1's measurement-error sensitivity.

## Pooled three runs — the official (ICLR 2027 version) ratings

The ICLR 2027 version of the paper (`metanym-game-paper-iclr27/`) pools the three full runs: one row-centred SVD over the
column-stacked factual matrices of runs 1–3 (12 × 805), G^C over each player's three portfolios, E^C from run 1's anchor
sweep (the only sweep). `scripts/pooled_components.py` holds the estimators and, run on run 1 alone, reproduces the run-1
tables above (asserted in its `__main__`). All outputs below are deterministic (seed 20260816 unless stated).

| Artifact | Producer / meaning | Paper (ICLR version) |
|---|---|---|
| `data/total_rating_council_pooled123.csv` | `scripts/pooled_council_tables.py` — council-basis official leaderboard on the pooled corpus, per-round A.5 bootstrap CI (B=1000) | §4.4 leaderboard, Fig. 2, Appendix D |
| `data/total_rating_council_replicates_pooled123.csv` | same — per-model T replicates | Appendix D.1 propagation |
| `data/total_rating_twelve_pooled123.csv` | same — twelve-evaluator components, pooled | §4.4 bases check, D.1 |
| `data/total_rating_council_pooled12.csv`, `data/total_rating_twelve_pooled12.csv` | same with `RUNS=1,2 B=0` — runs 1 and 2 pooled | Appendix F panel |
| `data/criterion_a_pooled123.csv` | `scripts/pooled_criterion_a.py` — E^F loading, anchored E^F, G^F with atom-bootstrap CIs | Appendix A.2 table; §3.4, §4.2 |
| *(stdout)* | `scripts/pooled_ladder.py` — D.1 ladder, compounds, regimes, bases (Fisher + BCa) on the pooled CSVs | §4.5, Appendix D.1 |
| `data/slope_band_full_pooled123.csv` | `scripts/pooled_slope_full_bootstrap.py` — slope/r under propagated measurement error | Appendix D.1 |
| *(stdout)* | `scripts/pooled_ballast_sizing.py`, `scripts/pooled_ballast_table.py` — A.6 sizing and per-seat table on the pooled corpus | Appendix A.6 |
| `data/alignment_cosine_pooled123.csv`, `data/g_vs_e_pooled123.csv` | `scripts/pooled_vendor_alignment.py` — same-vendor robustness (stdout), G-vs-E per criterion, anchored cosine + CI | §4.2, §4.3, Appendix A.5 |
| *(stdout)* | `scripts/pooled_spectral_gap_checks.py` — per-run and pooled σ₁/σ₂, permutation null, u₁ stability | Appendix A.6, F |
| `data/per_run_components.csv` | `scripts/per_run_components.py` — four quarters per run (E^C from run 1's sweep) + run-to-run agreement | Appendix F table, §4.6 |
| *(stdout)* | `scripts/per_run_contests.py` — per-run contests: contestant E^F vs twelve-basis, contest gaps | §4.6, Appendix F |
| `figures/runs_panel.png` | `scripts/plot_runs_panel.py` — three runs apart + pooled, against GPQA | Appendix F figure |
| `figures/total_validation_simple_pooled123.png` | `scripts/plot_total_validation_simple_pooled.py` — pooled T vs GPQA (copied to the ICLR folder as `total_validation_simple.png`) | Fig. 2 |
| *(stdout)* | `scripts/archetype_recurrence.py` — archetype titles and domains from the evaluation transcripts: titles kept verbatim between runs, titles shared across models, models offering a resource-allocation archetype, domains used by five or more models | §6 hypothesis paragraph |
| *(stdout)* | `scripts/portfolio_divergence.py` — runs 2 and 3 raw portfolios: words shared before the first differing word, the fork, archetypes returning after it; over kept archetypes, templates verbatim vs rewritten, text similarity, slot names, domains and metanyms kept | §6 (ICLR) |
| *(stdout)* | `scripts/compression_ratio_all.py` — words per template, metanym set and Form (a) instantiation over every archetype in the run 2 and 3 portfolios; the instantiation / metanym-set ratio (limit of the compression factor) and the factor at five contexts | §6 (ICLR) |
| *(stdout)* | `scripts/thinking_vs_play.py` — thinking vs play: factual means per player, on-minus-off per model with a judge-and-archetype bootstrap, judge agreement, what the thinking texts contain | §6 (ICLR) |
| *(stdout)* | `scripts/compression_ratio.py` — words of the anchor's first archetype: template, metanym table, the five rewrites; compression factor at five contexts and per added context | §6 hypothesis paragraph |
| *(stdout)* | `scripts/self_entry_fill_check.py` — the pooled factual SVD with self-entries filled by the evaluator's row mean instead of the anchor value: same $E^{F}$ ranking, loadings within 0.04, $T$–GPQA $r$ moved by less than 0.01 | Appendix A.2 (ICLR version) |
| `data/baseline_aggregators.csv` | `scripts/baseline_aggregators.py` — Pearson/Spearman with GPQA of the un-anchored plain mean (§4.1 pass), the anchored plain mean (run 1, anchor at 7) and the official pooled $T$ | §4.5 (ICLR version): 0.77, 0.93, 0.98 |
| *(stdout)* | `scripts/gpqa_reply_lengths.py` — words per GPQA reply per model, bare-letter replies | §6 (ICLR) |
| `figures/council_evaluation_pc1_wide.png` | `scripts/plot_council_evaluation_wide.py` — the same exhibit in landscape for the ICLR text width | Figure 1 (ICLR version) |
| `figures/council_evaluation_pc1_compact.png` | `scripts/plot_council_evaluation_compact.py` — the instantiation and the clause each of the five judges singles out | Figure 1 (ICLR version) until 2026-09-17; the full exhibit is its Appendix C |
| `figures/game_example.png` | `scripts/plot_game_example.py` — (a) the anchor submission's first archetype (template, metanym table, first domain as instantiation and idiomatic rewrite, from `submissions/anchor_claude-opus-4.5.md`); (b) the Appendix C instantiation with three judges' complete justifications | Figure 1 (ICLR version, from 2026-09-17), one page |
| `figures/game_generation.png` | `scripts/plot_game_example.py --panel a` — the same generation material with the context template, full page | Figure 1 (arXiv v3) |
| `figures/game_evaluation.png` | `scripts/plot_game_example.py --panel b` — the same evaluation with the idiomatic rewrite, the administrator's summary and all five judges, full page | not used in a paper (the arXiv version takes the council exhibit below) |
