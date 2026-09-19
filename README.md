# The Metanym Game

**Paper:** *The Metanym Game: An LLM Benchmark Without Ground Truth That Rises With the Models It
Measures* — [arXiv:2606.21008](https://arxiv.org/abs/2606.21008) v3 (DOI
[10.48550/arXiv.2606.21008](https://doi.org/10.48550/arXiv.2606.21008)), September 2026. **Author:** David Nordfors (david.nordfors@archetypes.ai).

This repository is the public record of the paper: the manuscript, the arXiv source, the build, and the
reproduction package. Everything behind the paper is in `reproduce/`, as it was produced: the prompts as
sent, every submission the twelve models generated, every rating every judge gave with its justification
and the record of the API call, every raw GPQA reply. One command re-derives every number, table and
figure; a second checks that the records form one chain (see `reproduce/README.md`, *Check the chain
yourself*).

## Layout

```
paper/
  metanym_game.md             the manuscript — Markdown source of truth
  appendices/A–G              A estimators, B prompts, C worked evaluation, D GPQA audit,
                              E constructs, F the three runs apart and pooled, G anchoring
  metanym_game.pdf            the built paper (arXiv v3)
figures/                      the paper's figures, drawn by reproduce/scripts/
build/
  build_paper.py              markdown -> paper.tex -> PDF, in the conference style under build/style/
  style/                      iclr2027_conference.{sty,bst,tex}, natbib, fancyhdr — official, untouched
submission-arxiv/             the arXiv v3 source as generated: paper.tex, style files, figures, the tarball
reproduce/
  reproduce.sh                regenerates every exhibit; each step labelled with the table or figure it makes
  scripts/verify_chain.py     checks the records from prompt to table against one another
  DATA_MANIFEST.md            data provenance and the result -> script map
  SHA256SUMS                  every input file; its own SHA-256 is the digest printed in the paper
  data/, prompts/, submissions/, scripts/, figures/
archive/
  arxiv-v2/                   the extended earlier version (arXiv v2, August 2026; run 1 alone), kept
                              whole with its own README, manuscript, appendices, PDF and arXiv source
```

## Reproduce

```bash
conda env create -f reproduce/environment.yml && conda activate metanym-game
cd reproduce && python3 scripts/verify_chain.py && bash reproduce.sh
```

## Build the paper

```bash
python3 build/build_paper.py --arxiv     # paper/metanym_game.pdf, and the bundle + source tarball in submission-arxiv/
python3 build/build_paper.py             # the anonymised conference build: PDF and bundle, written outside this tree
```

Requires `pandoc` and `tectonic`. The anonymised build fails loudly if the main text runs past the 9-page
limit or if an author name, repository URL or arXiv id survives into the PDF.

## The versions

v3 (this tree) pools the three full runs of the game — one factorisation over all three runs' factual
scores, each player's three portfolios graded — and is the current version. v2, in
`archive/arxiv-v2/`, is the extended treatment of run 1 alone; it carries detail the conference length
dropped and is kept for that reason. The reproduction package serves both: the run-1 sections of
`reproduce.sh` are v2's numbers, the pooled steps at its end are v3's.

## License & citation

Code (`build/build_paper.py`, `reproduce/`) under **MIT**; paper text and figures under **CC BY 4.0**;
the ICLR style files keep their own terms. See [`LICENSE`](LICENSE). To cite, use
[`CITATION.cff`](CITATION.cff) (GitHub's "Cite this repository").
