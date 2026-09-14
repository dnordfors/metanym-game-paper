# H. The argument behind the hypothesis

Nothing in this appendix tests the hypothesis of §6. It sets out the argument step by step, marks each step as a cited result, a measurement on the released data, or the hypothesis itself, and ends with what would refute it. Every number comes from a script in the released package.

<a id="fig-gpqa-scatter-h"></a>

![The agreement the hypothesis is offered for, reproduced from Figure 2: the official total $T$ (council basis, three runs pooled) against self-administered GPQA Diamond accuracy, twelve models; Pearson $r = 0.98$ (95% BCa CI [0.95, 0.99]), Spearman $\rho = 0.96$. Filled markers are council seats, open markers non-council, the star the anchor at $T = 7$ by calibration.](../submission/figures/total_validation_simple.png)

## H.1 The chain

1. **Training a language model is compression** (cited). Predicting text is compressing it (Shannon, 1951); a trained model is a general-purpose compressor (Delétang et al., 2024).
2. **Training selects what is compressed** (cited, by construction of the objective). The loss is taken on held-out text, so an abstraction earns its place only by predicting instantiations the model has not seen, and the abstractions that recur most across the corpus earn the most. A situation structure that appears in biology, economics and stories alike is one.
3. **Compression generalises** (cited). The shortest description keeps a recurring pattern once, as an abstraction, and reuses it (Rissanen, 1978); that is a concept.
4. **A concept is a frame with open slots** (cited). Minsky's (1974) frames are stereotyped situations with terminals that instances fill; the context template of §2 is such a frame, written in words.
5. **An analogy is a shared relational structure with different particulars** (cited; Gentner, 1983). The archetypal context is that shared structure.
6. **Hypothesis.** A language model holds its knowledge as archetypal contexts, each instantiated in the topic domains where it applies. The template is the abstraction; the metanym set is what the abstraction leaves out, the topic domain; the two reconstruct the instantiation exactly.
7. **The metanym form is strong compression** (measured, H.2). About 3 for a template with five parallel contexts and about 8 for each further one, growing with every domain a template serves — the order of the compression a trained model achieves on text, in words rather than bits. The factor grows because the template has open slots: a memorised string compresses only its exact repeats, a frame compresses every new instance that fits it, and no instantiation here repeats another. This is the abstracting kind of compression, the kind held-out loss rewards; a representation this compressive is what training would find.
8. **The game measures the mechanism directly** (hypothesis). Nothing is given; the model selects the archetype and the domains that best satisfy the prompt's criteria, factual truth among them, and writes them out.
9. **GPQA measures the mechanism's use** (hypothesis, with H.4 as the observation). The archetype and the domain are given by the question; the model derives the instantiation and selects the candidate that matches it. The two tests agree because they exercise one operation from opposite ends: GPQA fixes the store position and selects among four strings, the game selects the store position and fixes the output form.
10. **Corollary: retrieval, not construction** (hypothesis, with H.3 as the signature). In the game the models retrieve templates and metanym sets that training already compressed, which is why they play well with no reasoning channel and why a model rewrites its portfolios between runs but keeps its archetypes.
11. **What the data establish is narrower.** The factual pair reaches 0.94 with GPQA and the two subjective quarters lift it to 0.98 (§4.5, Appendix D.1). The hypothesis is consistent with the general factor of Ilić and Gignac (2024), and more specific.

## H.2 The compression of the metanym form

Measured on the anchor submission's first archetype, the one archetype shipped in full (`scripts/compression_ratio.py`). The template is 120 words; the metanym table 84 words for five parallel contexts, 17 per context; the five instantiations (Form a, the form the template and metanym set reconstruct exactly) average 130 words. With $n$ contexts the factor is $130n/(120+17n)$:

| contexts | 5 | 10 | 20 | 50 | limit |
|---|--:|--:|--:|--:|--:|
| factor | 3.2 | 4.5 | 5.7 | 6.9 | 7.8 |

Table: Literal compression of the metanym form against the number of parallel contexts per template, from the anchor's first archetype (120-word template, 17 words of metanyms per context, 130-word instantiations).

The asymptote is the ratio of an instantiation to its metanym set, and it is reached only when a template is amortised over dozens of domains, which is the situation inside a model rather than inside a five-context game. The count is in words, and metanyms are the high-entropy tokens, so the factor in bits is lower; the bit-level factor is measurable with an open-weights model and is not measured here. Templates in the released portfolios run 80 to 120 words with 10 to 15 slots, so the asymptote varies by archetype within the same range. It is a lower limit in one further sense: a metanym set is itself a frame with slots, so the topic domain compresses by the same rule, and the factors multiply down the hierarchy.

## H.3 The retrieval signature in the released transcripts

The archetype titles and parallel-context domains of every graded portfolio in the three runs, as the evaluation transcripts record them (`scripts/archetype_recurrence.py`; the raw portfolios are not shipped, the transcripts copy their headings).

**Within a model, the archetypes persist while the texts change.** Eleven of twelve portfolios differ between runs (§4.6). Between the two runs made two hours apart, 34 of 48 archetype titles recur verbatim; between run 1 and run 2, three weeks apart, 20 of 50. Gemini 2.5 Flash produced the same five titles in all three runs; Claude Opus 4.0 kept four or five of five. The models rewrite; they do not reinvent. This is what one archetype in latent space with many projections in literal space predicts, and what a stored text would not.

**Across models, the same concepts recur, across vendors.** Seven of the eleven graded models, from all three vendors, offer a resource-allocation archetype (title containing "allocation"). Six domains are used by five or more models: urban planning, social media, corporate structure, the climate system, software development, biological evolution. Of 81 distinct titles, 14 are used by more than one model.

**The caveat.** Recurrence is strongest inside a vendor: 11 of the 14 shared titles are shared within one vendor only, the two Opus models sharing cascade amplification, phase transition, competitive exclusion and boundary maintenance word for word, and the GPT-4o family sharing resource allocation, conflict resolution and growth and development. Shared training data explains within-vendor recurrence as well as shared representation does. The cross-vendor recurrence is the evidence.

## H.4 How GPQA was answered

With the reasoning channel off and temperature zero, no model answered with a bare letter (`scripts/gpqa_reply_lengths.py`):

| model | median words | replies under 15 words |
|---|--:|--:|
| claude-opus-4.0 / 4.1 / 4.5 | 221 / 242 / 288 | 2 / 2 / 0 |
| claude-sonnet-4 | 260 | 0 |
| gemini-2.5-flash / 3.1-pro | 546 / 374 | 0 / 2 |
| gpt-4.1 / mini / nano | 180 / 328 / 287 | 5 / 0 / 0 |
| gpt-4o / 2024-08-06 / mini | 196 / 191 / 230 | 1 / 1 / 0 |

Table: Words per GPQA reply with the reasoning channel off, and replies under fifteen words, per model (198 items each).

Thirteen replies of 2,376 are under fifteen words, most of them truncations. Every model wrote a derivation and ended it with the answer line, as the prompt allowed (Appendix D.2). In the derivations the model states the relation the question turns on in the question's domain and then tests the candidates against it: an instantiation written out, then a match — the sequence step 9 describes. "Reasoning off" removes the hidden channel; the visible derivation remains, and the question of whether a hidden channel would change play is open (§6, Scope).

## H.5 Predictions, and what would refute the hypothesis

1. **Domain-matched agreement.** A model's factual score on parallel contexts in a field tracks its GPQA accuracy in that field. GPQA Diamond carries subject labels, and the released evaluations carry each parallel context's domain, so the test needs no new run. A refutation: the field-by-field agreement is no higher than the agreement across fields.
2. **Separability in latent space.** Archetype and topic domain are separable in a model's latent space: the same archetype recoverable from parallel contexts in unrelated domains, and the domain from unrelated archetypes. A refutation: representations that separate by domain only.
3. **Retrieval over construction.** Reasoning should add little to generation in the game, where templates and metanym sets are retrieved, and may still help judging, where the task is to catch a broken substitution. A refutation: a reasoning budget that raises generation ratings as much as it raises judging.
4. **The bit-level factor.** Given its template and metanym set, an instantiation's per-token loss under an open-weights model should fall far below its loss given nothing, and by more for archetypes that recur across many domains. A refutation: no such gap, or a gap that does not grow with the number of domains.
