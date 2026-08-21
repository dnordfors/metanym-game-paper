# `data/` — pinned evaluation data

This directory is complete and self-contained: `../reproduce.sh` runs against it with no downloads,
no credentials and no API calls. `reproduce.sh` sets the environment variables that point at these
directories itself, so there is nothing to configure.

Provenance, per-directory file counts, and which files are inputs versus regenerated outputs are all
in [`../DATA_MANIFEST.md`](../DATA_MANIFEST.md).

Layout in brief:

```
probe_J_20260529T005230Z/            un-anchored run, all twelve participants — §4.1 baseline
probe_K_20260529T014133Z/            run 1, anchor 7 — the published leaderboard
probe_K_anchor5_20260529T030442Z/    anchor sweep (§5.7)
probe_K_anchor6_20260529T032518Z/
probe_K_anchor8_20260529T033755Z/
regenerations/                       runs 2 and 3, the §4.9 regeneration robustness check
gpqa_runs/                           raw self-administered GPQA Diamond responses (Appendix D)
*.csv                                provided tables, plus those written by reproduce.sh
```

Each evaluation file is `eval_<evaluator>_x_<target>.json`, holding that evaluator's per-parallel-context
`factual_per_pc` ratings and per-archetype non-factual axis ratings for that target's portfolio, with
the matching `.md` transcript alongside.
