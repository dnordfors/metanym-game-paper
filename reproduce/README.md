# Reproducing *The Metanym Game*

This directory regenerates every numerical result in the paper from the pinned evaluation data in
`data/`. The theory it implements is written out in the paper's **Appendix A (Rating estimators)**,
equations A1–A15; each script's docstring quotes the section it computes and the numbered formula it
implements. No external answer key is used anywhere.

## Run it

```bash
conda env create -f environment.yml && conda activate metanym-game
bash reproduce.sh
```

Deterministic, no API calls, well under a minute. See the root [`README.md`](../README.md) for
options, and use `PYTHON=/path/to/python bash reproduce.sh` to pick a different interpreter.

## Where things are documented

- **[`reproduce.sh`](reproduce.sh)** — the map. Every step is labelled with the paper exhibit it
  produces, so it answers "where did this number come from?" and cannot drift from what actually
  runs, because running it is the verification.
- **[`CURRENT_SCRIPTS.md`](CURRENT_SCRIPTS.md)** — a readable index of the same twelve steps, with
  the equation each one implements.
- **[`DATA_MANIFEST.md`](DATA_MANIFEST.md)** — provenance and contents of every input.

## The experiment being re-analysed

```
generate ─▶ evaluate (anchor sweep) ─▶ score
portfolios   per-axis ratings,          factual competence, criterion
             anchors 5,6,7,8            competence, council, total leaderboard
```

1. **Generate** — each model produces a portfolio (5 archetypal templates, each instantiated as 5
   parallel contexts) at temperature 0, no reasoning, no tools.
2. **Evaluate** — every model scores every portfolio, **including its own**, on the six-axis
   rubric against the fixed anchor reference, repeated at anchor values 5, 6, 7 and 8. The
   self-pairs are shipped in `data/` for completeness but are excluded at scoring time: every
   rating in step 3 is **leave-self-out**.
3. **Score** — the scripts here turn that evaluation tensor into the paper's ratings.

Steps 1 and 2 were run once and their outputs pinned into `data/`; `reproduce.sh` is step 3 only.

## What each rating means

One line each; full definitions in Appendix A.

- **G** generation rating, **I** instantiation rating — council leave-self-out means on the anchored scale.
- **f** factual competence — leading left singular vector of the evaluators' row-centred graded rating matrix, no answer key (cf. Dawid & Skene 1979; Parisi et al. 2014).
- **ρ̄** criterion competence (anchor-shift consistency) — mean pairwise Pearson of the collapsed non-factual score across anchors 5, 6, 7, 8, computed leave-self-out over archetypes 1–5: 50 (submission, archetype) units for a graded evaluator, 55 for the anchor, whose own portfolio is the reference rather than a graded submission.
- **council** — the evaluators that are both factually competent and anchor-stable; they issue the official ratings.
- **E^F, E^C, E, T** — the evaluator indices (factual competence, criterion competence), their mean, and the total, all on the scale where the anchor model scores 7.

All confidence intervals reported by these scripts are 95% percentile bootstrap intervals as
defined in Appendix A.
