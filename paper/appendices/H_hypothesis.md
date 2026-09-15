# H. A hypothesis for the metanym game–GPQA correlation

Nothing in this appendix tests the hypothesis of §6. It sets out the argument step by step, marks each step as a cited result, a measurement on the released data, or the hypothesis itself, and ends with what would refute it. Every number comes from a script in the released package.

<a id="fig-gpqa-scatter-h"></a>

![The agreement the hypothesis is offered for, reproduced from Figure 2: the official total $T$ (council basis, three runs pooled) against self-administered GPQA Diamond accuracy, twelve models; Pearson $r = 0.98$ (95% BCa CI [0.95, 0.99]), Spearman $\rho = 0.96$. Filled markers are council seats, open markers non-council, the star the anchor at $T = 7$ by calibration.](../submission/figures/total_validation_simple.png)

<a id="fig-mechanism"></a>

![A hypothesis for the 0.98: the metanym game reproduces the way the model organises its knowledge, and GPQA runs on that organisation. An archetype ($\alpha$, $\beta$) is held once; each domain adds only its metanym set (the slices), about a fifth of the instantiation it yields. GPQA: archetype and domain are given; the model derives the instantiation and selects the matching candidate. The game: nothing is given; the model selects the archetype and domains that best satisfy the criteria and writes them out.](../submission/figures/mechanism_sketch.png)

## H.1 The chain

1. **Cited.** Training a language model is compression. Predicting text is compressing it (Shannon, 1951); a trained model is a general-purpose compressor (Delétang et al., 2024).
2. **Cited.** Training selects what is compressed, by construction of the objective. The loss is taken on held-out text, so an abstraction earns its place only by predicting instantiations the model has not seen, and the abstractions that recur most across the corpus earn the most. A situation structure that appears in biology, economics and stories alike is one.
3. **Cited.** Compression generalises. The shortest description keeps a recurring pattern once, as an abstraction, and reuses it (Rissanen, 1978); that is a concept.
4. **Cited.** A concept is a frame with open slots. Minsky's (1974) frames are stereotyped situations with terminals that instances fill; the context template of §2 is such a frame, written in words.
5. **Cited.** An analogy is a shared relational structure with different particulars (Gentner, 1983). The archetypal context is that shared structure.
6. **Hypothesis.** A language model holds its knowledge as archetypal contexts, each instantiated in the topic domains where it applies. The template is the abstraction; the metanym set is what the abstraction leaves out, the topic domain; the two reconstruct the instantiation exactly.
7. **Measured.** In the metanym game an instantiation is between two and a half and eleven times the size of its metanym set. That hints at a compression rate at scale of the same order of magnitude as has been measured for language models, about ten (Delétang et al., 2024), and above gzip's three. The factor grows with the domains because the template has open slots: a memorised string compresses only its exact repeats, a frame compresses every new instance that fits it.
8. **Hypothesis.** A form this compressive qualifies as a learning mechanism for a language model.
9. **Hypothesis.** The game measures the mechanism directly. Nothing is given; the model selects the archetype and the domains that best satisfy the prompt's criteria, factual truth among them, and writes them out.
10. **Hypothesis (with the observation).** GPQA measures the mechanism's use. The archetype and the domain are given by the question; the model derives the instantiation and selects the candidate that matches it. With the reasoning channel off, 99.5% of the GPQA replies derive the answer and then pick the candidate that matches it. The two tests agree because they exercise one operation from opposite ends: GPQA fixes the store position and selects among four strings, the game selects the store position and fixes the output form.
11. **Hypothesis (H.2 is the signature).** Corollary: retrieval, not construction. In the game the models retrieve templates and metanym sets that training already compressed, which is why they play well with no reasoning channel and why a model rewrites its portfolios between runs but keeps its archetypes.
12. **Established.** What the data establish is narrower. The factual pair reaches 0.94 with GPQA and the two subjective quarters lift it to 0.98 (§4.5, Appendix D.1). The hypothesis is consistent with the general factor of Ilić and Gignac (2024), and more specific.

## H.2 The retrieval signature in the released transcripts

The archetype titles and parallel-context domains of every graded portfolio in the three runs, as the evaluation transcripts record them (`scripts/archetype_recurrence.py`; the raw portfolios are not shipped, the transcripts copy their headings).

**Within a model, the archetypes persist while the texts change.** Eleven of twelve portfolios differ between runs (§4.6). Between the two runs made two hours apart, 34 of 48 archetype titles recur verbatim; between run 1 and run 2, three weeks apart, 20 of 50. Gemini 2.5 Flash produced the same five titles in all three runs; Claude Opus 4.0 kept four or five of five. The models rewrite; they do not reinvent. This is what one archetype in latent space with many projections in literal space predicts, and what a stored text would not.

**Across models, the same concepts recur, across vendors.** Seven of the eleven graded models, from all three vendors, offer a resource-allocation archetype (title containing "allocation"). Six domains are used by five or more models: urban planning, social media, corporate structure, the climate system, software development, biological evolution. Of 81 distinct titles, 14 are used by more than one model.

**The caveat.** Recurrence is strongest inside a vendor: 11 of the 14 shared titles are shared within one vendor only, the two Opus models sharing cascade amplification, phase transition, competitive exclusion and boundary maintenance word for word, and the GPT-4o family sharing resource allocation, conflict resolution and growth and development. Shared training data explains within-vendor recurrence as well as shared representation does. The cross-vendor recurrence is the evidence.

## H.3 Predictions, and what would refute the hypothesis

1. **Domain-matched agreement.** A model's factual score on parallel contexts in a field tracks its GPQA accuracy in that field. GPQA Diamond carries subject labels, and the released evaluations carry each parallel context's domain, so the test needs no new run. A refutation: the field-by-field agreement is no higher than the agreement across fields.
2. **Separability in latent space.** Archetype and topic domain are separable in a model's latent space: the same archetype recoverable from parallel contexts in unrelated domains, and the domain from unrelated archetypes. A refutation: representations that separate by domain only.
3. **Retrieval over construction.** Reasoning should add little to generation in the game, where templates and metanym sets are retrieved, and may still help judging, where the task is to catch a broken substitution. A refutation: a reasoning budget that raises generation ratings as much as it raises judging.
4. **The bit-level factor.** Given its template and metanym set, an instantiation's per-token loss under an open-weights model should fall far below its loss given nothing, and by more for archetypes that recur across many domains. A refutation: no such gap, or a gap that does not grow with the number of domains.
