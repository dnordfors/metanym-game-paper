# The Metanym Game — ICLR 2027 version

**Paper:** *The Metanym Game: An LLM Benchmark Without Ground Truth That Rises With the Models It
Measures* — the ICLR 2027 conference version, which is the official version of the paper.
**Author:** David Nordfors (david.nordfors@archetypes.ai). The extended earlier treatment is
[arXiv:2606.21008 v2](https://arxiv.org/abs/2606.21008) (DOI
[10.48550/arXiv.2606.21008](https://doi.org/10.48550/arXiv.2606.21008)); it reports the first of
the three runs alone, and this version supersedes it.

This repository is the public record of the paper: the manuscript, its ICLR submission bundle, and
the reproduction package. Every number, table and figure recomputes from `reproduce/` — pinned
evaluation runs, raw GPQA records, analysis scripts, one-command `reproduce.sh`; deterministic, no
API calls.

> **Review status.** While the paper is under double-blind review this repository must not be
> linked from the submission; reviewers receive an anonymised copy.

## Layout

```
paper/
  metanym_game_iclr27.md      the manuscript — Markdown source of truth
  appendices/A–G              the appendix (A estimators, B prompts, C worked evaluation,
                              D GPQA audit, E constructs, F the three runs apart and pooled, G anchoring)
  metanym_game_iclr27.pdf     the built paper
figures/                      the paper's figures, produced by reproduce/scripts/
build/
  build_paper.py              markdown -> paper.tex (+ the PDF into paper/) in the official ICLR 2027 style
  style/                      iclr2027_conference.{sty,bst,tex}, natbib, fancyhdr — official, untouched
submission-iclr/              the ICLR bundle as generated: paper.tex, style files, the figures it uses
submission-arxiv/             the arXiv bundle as generated (build_paper.py --arxiv): the same plus the source tarball
reproduce/
  reproduce.sh                regenerates every exhibit; each step labelled with the table or figure it makes
  DATA_MANIFEST.md            data provenance and the result -> script map
  data/, scripts/, figures/   the pinned runs, the analysis scripts, the figures they draw
```

## Reproduce

```bash
conda env create -f reproduce/environment.yml && conda activate metanym-game
cd reproduce && bash reproduce.sh
```

## Build the paper

```bash
python3 build/build_paper.py             # writes paper/metanym_game_iclr27.pdf and the bundle in submission-iclr/
python3 build/build_paper.py --arxiv     # writes paper/metanym_game_arxiv_v3.pdf and the bundle + tarball in submission-arxiv/
```

Requires `pandoc` and `tectonic`. The build fails loudly if the main text runs past ICLR's 9-page
limit or if an author name, repository URL or arXiv id survives into the PDF while `\iclrfinalcopy`
is off. Uncomment `\iclrfinalcopy` in the preamble (in `build_paper.py`) for the camera-ready.

## How this differs from the extended arXiv version

The official ratings pool the three full runs of the game — one factorisation over all three runs'
factual scores, each player's three portfolios graded — where arXiv v2 reports run 1 alone; the
runs apart, and why they are pooled, are Appendix F. The main text is compressed to 9 pages: the
estimator definitions, the per-axis consistency table, the per-criterion generation–evaluation
table, the ballast sizing and the GPQA audit are in the appendix. §5 adds EigenBench (Chang et al.,
ICLR 2026) to the related work, and the abstract's priority claim is narrowed to what the two-sided
factorisation adds.

## License & citation

Code (`build/build_paper.py`, `reproduce/`) under **MIT**; paper text and figures under
**CC BY 4.0**; the ICLR style files keep their own terms. See [`LICENSE`](LICENSE). To cite, use
[`CITATION.cff`](CITATION.cff) (GitHub's "Cite this repository").
