# Proposed revision — cite BenchBench in §5.4 and §4.7

**Status: proposed, not applied.** Nothing in `paper/` or `submission/` has been changed. This
file argues for one added citation and gives the exact text to insert if the argument is
accepted. Landing it means a new arXiv version — see [What it costs](#what-it-costs) before
deciding.

Section references (§4.7, §5.4, …) are to `paper/metanym_game.md` (v2 numbering, August 2026), and paths are relative to
this package. This package, inside `archetypal-contexts`, is the only copy —
[`../../docs/PUBLICATION_PACKAGE.md`](../../docs/PUBLICATION_PACKAGE.md). The standalone
`~/python/BOLD/metanym-game-paper` repo, and `github.com/dnordfors/metanym-game-paper` behind
it, are a carbon copy of it: never edit them directly, they are re-synced from here. **Which
means this file travels to the public repo with the rest of the package** — it is written to be
readable by anyone who finds it there.

Raised from the sibling `metanym-co-website/docs/PRIOR_ART.md`, which lists neighbours this
paper does not currently cite. This is the one worth the revision; the rest of that list is
optional.

## The reference

> Zheng, Y., Luo, H., Lin, Z., Liu, W., & Tuan, L. A. (2026). BenchBench: Benchmarking
> automated benchmark generation. arXiv:2603.20807. Submitted 21 March 2026.

A three-stage pipeline that evaluates language models as benchmark **designers** rather than as
answerers: extract domain cards from seed benchmarks, have designer models generate
quota-controlled suites, then validate the generated items with a multi-model answerer panel —
exact/numeric/symbolic verifiers where possible, rubric-guided judging otherwise. Nine variants
across computer science, mathematics, medicine and theory-of-mind reasoning; 16.7K items
generated, ~15K retained, ~152K graded model–item responses.

Its headline finding: **benchmark-design ability is only moderately correlated with answer-time
strength, Spearman ρ ≈ 0.37.** The authors conclude that design is a distinct meta-capability.

## Why it belongs in the paper

**1. It is independent corroboration of §4.7's central claim, from people with no stake in it.**

§4.7 reports that generation and evaluation do not coincide — Gemini 3.1 Pro is the participants'
strongest factual judge yet a middling generator; Sonnet-4 generates near the top yet does not
clear the evaluator bar. §5.1 makes that separation load-bearing: it is why the council can pick
judges rather than only rank makers.

As the paper stands, a reader can read the dissociation as an artefact of this instrument — of
the anchored 1–10 rating, of the SVD, of twelve closed-weight models from three providers. That
reading is available because there is nothing else in the paper to compare it against.
BenchBench closes it. Different items, different task, different scoring machinery, different
authors, same dissociation. It converts the finding from *a result of ours* into *a result two
independent instruments agree on*, which is a categorically stronger thing to have, and it costs
one sentence.

**2. The structural parallel is striking and worth naming.**

BenchBench's central object is a **designer–answerer matrix**: models on one axis as producers
of items, models on the other as responders to them. That is the same object as the paper's
two-sided ratings matrix (§4.2) — generators on one axis, evaluators on the other — arrived at
independently, from a different starting question. Two groups reaching for the same matrix is
evidence that the making/judging separation is a real feature of the problem rather than a
modelling choice.

**3. Distinguishing it strengthens the self-containment claim rather than weakening it.**

BenchBench is *not* key-free. It starts from seed benchmarks, and it validates generated items
with verifiers where they exist and rubric-guided judging where they do not. So it establishes
the dissociation while still depending on external truth — which is exactly the contrast §5.4
draws for everything else in the field. Citing it therefore does double duty: it corroborates
the finding *and* supplies one more instance of the pattern that prior work is either a good
test that needs a key, or key-free but aimed elsewhere.

This is why the citation belongs in §5.4 rather than only in the reference list: the point is
not "here is a related paper", it is "the separation this benchmark is built on has been found
twice, by different means".

## Where it goes

Three insertions. The first is the substantive one; the second is a cross-reference; the third
is the reference entry.

### (a) §5.4 — Where this sits (the peer-evaluation paragraph)

Currently one paragraph. Add a second. Present text:

> Making and judging factual truth are different abilities, and the council measures both and
> keeps them apart (§4.3). A benchmark that scored only generation would miss judging
> competence — the very thing the council gate selects on — so it is the separation, not just
> the rating, that lets the panel pick judges rather than only rank makers.

Insert after it:

> The separation is not peculiar to this instrument. BenchBench (Zheng et al. 2026) evaluates
> language models as benchmark *designers* and reports design ability correlating only
> moderately with answer-time strength, Spearman $\rho \approx 0.37$, concluding that design is
> a distinct meta-capability. That is the same dissociation on different items, under a
> different scoring procedure, from independent authors — and it is reached through a
> designer–answerer matrix structurally analogous to the two-sided ratings matrix of §4.3.
> BenchBench is not key-free, however: it seeds from existing benchmarks and validates
> generated items with verifiers or rubric-guided judging, so it establishes the separation
> while still resting on external truth. The finding replicates; the self-containment does not
> come with it.

Rationale for the last two sentences: without them the citation reads as conceding that
somebody else did this first. With them it lands as corroboration plus one more instance of the
§5.4 pattern.

### (b) §4.7 — Total rating and the official leaderboard

Optional, and only if §5.4's paragraph is judged too far from the evidence it corroborates.
Target: the "Generation and evaluation do not coincide" reading at the end of §4.7 (the three Opus
models are middling factual judges; gemini-3.1-pro, the strongest judge, generates mid-pack).

Append: `Independent evidence for this separation is discussed in §5.4.`

Recommendation: do this one. It is four words of cross-reference and it puts the corroboration
where the sceptical reader meets the claim.

### (c) References → *Generation vs evaluation*

The subsection currently runs 42–44 and is the last before the appendices, so the new entry is
45 and no renumbering is needed anywhere.

> 45. Zheng, Y., Luo, H., Lin, Z., Liu, W., & Tuan, L. A. (2026). BenchBench: Benchmarking
>     automated benchmark generation. *arXiv preprint.* arXiv:2603.20807.

## What it costs

This is the part that makes it a decision rather than an edit.

1. **Two files, by hand.** The manuscript prose exists twice: `paper/metanym_game.md` and
   `submission/paper.tex`. `paper.tex` is pandoc output whose preamble was hand-tuned, and
   `splice_appendices.py` regenerates *only* the Appendix C and D bodies — the manuscript body
   is never regenerated. Both files must be edited, and they must be kept identical in
   substance. Note the notation difference: `\rho` in the `.tex`, `$\rho$` in the `.md`.
2. **Rebuild the PDF.** `cd submission && tectonic -X compile paper.tex`, then copy to
   `paper/metanym_game.pdf` — the tracked copy readers see. Adding a paragraph to §5.4 and one
   reference is likely to reflow the reference list across a page boundary; check the tail of
   the PDF, not just the section.
3. **Regenerate the arXiv bundle** (`submission/metanym_game_arxiv.tar.gz`).
4. **Re-run `reproduce.sh` before sharing.** `../docs/PUBLICATION_PACKAGE.md` rule: the package
   is shared only after a green reproduce from a clean checkout. A prose-only change does not
   touch any number, but the rule is the rule and running it is cheap — no model calls.
5. **Re-sync the carbon copy and push it.** `~/python/BOLD/metanym-game-paper` →
   `github.com/dnordfors/metanym-game-paper`, which is public.
6. **Tag the shared state** per the versioning rule, and submit a new arXiv version.
   arXiv:2606.21008 becomes v2 — public and permanent, and the listing shows the revision. A
   one-citation revision is an ordinary and unremarkable reason for a v2, but it is not
   invisible.
7. **`CITATION.cff`** needs no change — the citation is to this work, not from it.

If a v2 is going to happen anyway for other reasons, this rides along for nearly nothing. If it
is not, the question is whether one corroborating citation justifies a version bump on its own.
Argument that it does: the making/judging dissociation is the paper's most contestable empirical
claim, and this is the only external support for it currently in existence.

