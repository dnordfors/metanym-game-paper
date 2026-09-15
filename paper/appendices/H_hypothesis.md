# H. A hypothesis for the metanym game–GPQA correlation

Nothing in this appendix tests the hypothesis of §6. It sets out the argument step by step, marks each step as a cited result, a measurement on the released data, or the hypothesis itself, and ends with what would refute it. Every number comes from a script in the released package.

<a id="fig-gpqa-scatter-h"></a>

![The agreement the hypothesis is offered for, reproduced from Figure 2: the official total $T$ (council basis, three runs pooled) against self-administered GPQA Diamond accuracy, twelve models; Pearson $r = 0.98$ (95% BCa CI [0.95, 0.99]), Spearman $\rho = 0.96$. Filled markers are council seats, open markers non-council, the star the anchor at $T = 7$ by calibration.](../submission/figures/total_validation_simple.png)

<a id="fig-mechanism"></a>

![A hypothesis for the 0.98: the metanym game reproduces the way the model organises its knowledge, and GPQA runs on that organisation. An archetype ($\alpha$, $\beta$) is held once; each domain adds only its metanym set (the slices), about a fifth of the instantiation it yields. GPQA: archetype and domain are given; the model derives the instantiation and selects the matching candidate. The game: nothing is given; the model selects the archetype and domains that best satisfy the criteria and writes them out.](../submission/figures/mechanism_sketch.png)

## H.1 The chain

1. **Cited.** Training a language model is compression. Predicting text is compressing it (Shannon, 1951); a trained model is a general-purpose compressor (Delétang et al., 2024).
2. **Cited.** Analogy is semantic compression. An analogy is a shared relational structure with different particulars (Gentner, 1983).
3. The archetypal context is a semantic structure in the latent space. A context template is a literal representation of the archetypal context. The metanym sets are the particulars that, when inserted into the slots of the template, instantiate into parallel contexts, analogous metaphors.
4. **Hypothesis.** A language model holds its knowledge as archetypal contexts, each instantiated in the topic domains where it applies. The template is the abstraction, the metanym set is the topic domain, and the two reconstruct the instantiation exactly.
5. **Measured.** In the metanym game an instantiation is between two and a half and eleven times the size of its metanym set, so each domain is added for a fraction of the text it yields. That is compression of the same order as has been measured for language models, about ten (Delétang et al., 2024), and above gzip's three. A memorised string compresses only its exact repeats; a frame compresses every new instance that fits it.
6. **Hypothesis.** A form this compressive qualifies as a learning mechanism for a language model.
7. **Hypothesis.** The game measures the mechanism directly. Nothing is given; the model selects the archetype and the domains that best satisfy the prompt's criteria, factual truth among them, and writes them out.
8. **Hypothesis, with a measurement.** GPQA measures the mechanism's use. The archetype and the domain are given by the question; the model derives the instantiation and selects the candidate that matches it, which is what 99.5% of the replies do with the reasoning channel off. The two tests run one operation from opposite ends: GPQA gives the archetype and the domain and asks for the instantiation; the game asks for the archetype and the domains and gets the instantiations.
9. **Hypothesis, with a measurement.** Corollary: retrieval, not construction. In the game the models retrieve templates and metanym sets that training already compressed, which is why they play well with no reasoning channel. The signature: eleven of twelve portfolios differ between runs, yet most archetype titles recur verbatim between the two runs made two hours apart, and two in five between runs three weeks apart.
10. **Established.** What the data establish is narrower. The factual pair reaches 0.94 with GPQA and the two subjective quarters lift it to 0.98 (§4.5, Appendix D.1). The hypothesis is consistent with the general factor of Ilić and Gignac (2024), and more specific.

## H.2 Predictions, and what would refute the hypothesis

1. **Domain-matched agreement.** A model's factual score on parallel contexts in a field tracks its GPQA accuracy in that field. GPQA Diamond carries subject labels, and the released evaluations carry each parallel context's domain, so the test needs no new run. A refutation: the field-by-field agreement is no higher than the agreement across fields.
2. **Separability in latent space.** Archetype and topic domain are separable in a model's latent space: the same archetype recoverable from parallel contexts in unrelated domains, and the domain from unrelated archetypes. A refutation: representations that separate by domain only.
3. **Retrieval over construction.** Reasoning should add little to generation in the game, where templates and metanym sets are retrieved, and may still help judging, where the task is to catch a broken substitution. A refutation: a reasoning budget that raises generation ratings as much as it raises judging.
4. **The bit-level factor.** Given its template and metanym set, an instantiation's per-token loss under an open-weights model should fall far below its loss given nothing, and by more for archetypes that recur across many domains. A refutation: no such gap, or a gap that does not grow with the number of domains.
