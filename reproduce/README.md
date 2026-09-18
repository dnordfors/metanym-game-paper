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

Deterministic, no API calls, about a minute. See the root [`README.md`](../README.md) for
options, and use `PYTHON=/path/to/python bash reproduce.sh` to pick a different interpreter.

## Check the chain yourself

Everything between the prompts and the numbers is in this directory, and each link can be checked without
trusting the others. In the order the experiment ran:

| link | what is here | how to check it |
|---|---|---|
| prompts as sent | `prompts/generator.md`, `prompts/evaluator_calibrated.md` (anchored), `prompts/evaluator.md` (un-anchored); printed verbatim in Appendix B | every run's `run_info.json` names its prompt and records its length |
| generated portfolios | `data/portfolios_run1/` (the canonical run, with each call's API envelope), `data/regenerations/portfolios_run{2,3}/`; twelve per run | open any file; the ballast files in `submissions/` are byte-copies of two of run 1's |
| evaluations | one `eval_<judge>_x_<target>.json` (ratings + API envelope: model version string, token counts, finish reason) and `.md` (the judge's justification, verbatim) per ordered pair, for the un-anchored pass, anchor 7 (run 1), anchors 5/6/8 and runs 2–3: 936 calls | `scripts/verify_chain.py` checks each envelope is a completed call whose token count fits its transcript, and that the archetype titles a judge names are those of the target's portfolio file |
| GPQA | `data/gpqa_runs/…/<model>/responses.json`, 198 raw replies per model | re-scored by `scripts/verify_chain.py` and audited by `scripts/gpqa_audit.py` (Appendix D) |
| numbers | every CSV the paper's tables use | `bash reproduce.sh` rewrites them byte-identically from the evaluation JSONs; each step is labelled with its exhibit |
| bytes | `SHA256SUMS` over every input file; its own SHA-256 is the package digest printed in the paper | `python3 scripts/verify_chain.py` (standard library, seconds) |

```bash
python3 scripts/verify_chain.py    # links 1–7: prompts, portfolios, evaluations, GPQA, checksums
bash reproduce.sh                  # link 8: the numbers
```

Two records outside this package fix its dates: arXiv:2606.21008 v1 (June 2026) and v2 (August 2026) report these numbers, and the public repository's history at github.com/dnordfors/metanym-game-paper has carried the evaluation files since 30 July 2026, timestamped by the host.

## Where things are documented

- **[`reproduce.sh`](reproduce.sh)** — the map. Every step is labelled with the paper exhibit it
  produces, so it answers "where did this number come from?" and cannot drift from what actually
  runs, because running it is the verification.
- **[`DATA_MANIFEST.md`](DATA_MANIFEST.md)** — provenance and contents of every input, including the one recorded discrepancy (run 1's evaluator prompt revision).

## The experiment being re-analysed

```
generate ─▶ evaluate (anchor sweep) ─▶ score
portfolios   per-axis ratings,          peer centrality, rating
             anchors 5,6,7,8            consistency, council, total leaderboard
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

- **G^C** criterion generation rating — council leave-self-out mean over the five non-factual axes, each judge's vote weighted by its own rating consistency on that axis, on the anchored scale.
- **f** factual competence (peer centrality) — leading left singular vector of the evaluators' row-centred graded rating matrix, no answer key (cf. Dawid & Skene 1979; Parisi et al. 2014); its right vector, aggregated per generator, is **G^F**.
- **r̄** rating consistency (the anchor sweep) — mean pairwise Pearson of the collapsed non-factual score across anchors 5, 6, 7, 8, computed leave-self-out over archetypes 1–5: 50 (submission, archetype) units for a graded evaluator, 55 for the anchor, whose own portfolio is the reference rather than a graded submission.
- **council** — the evaluators that are both factually competent and rating-consistent; they issue the official ratings, each model rated in its own contest (council + ballast + the model itself).
- **E^F, E^C, E, G, T** — the evaluator indices (factual competence, rating consistency), their mean E, the generation mean G = ½(G^F+G^C), and the total T = ¼(G^F+G^C+E^F+E^C), all on the scale where the anchor model scores 7.

All confidence intervals reported by these scripts are 95% percentile bootstrap intervals as
defined in Appendix A.

## Pooled three runs (ICLR 2027 version)

The conference version pools the three full runs; its numbers come from the `scripts/pooled_*.py`, `per_run_*.py` and `plot_runs_panel.py` steps at the end of `reproduce.sh` (see the last section of `DATA_MANIFEST.md`). The arXiv v2 numbers are the run-1 numbers of the sections above.
