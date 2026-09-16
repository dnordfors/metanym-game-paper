# H. A hypothesis for the metanym game–GPQA correlation

Nothing in this appendix tests the hypothesis of §6. It sets out the argument step by step, marks each step as a cited result, a measurement on the released data, or the hypothesis itself, and ends with what would refute it. Every number comes from a script in the released package.

<a id="fig-gpqa-scatter-h"></a>

![The agreement the hypothesis is offered for, reproduced from Figure 2: the official total $T$ (council basis, three runs pooled) against self-administered GPQA Diamond accuracy, twelve models; Pearson $r = 0.98$ (95% BCa CI [0.95, 0.99]), Spearman $\rho = 0.96$. Filled markers are council seats, open markers non-council, the star the anchor at $T = 7$ by calibration.](../submission/figures/total_validation_simple.png)

<a id="fig-mechanism"></a>

![A hypothesis for the 0.98: the metanym game reproduces the way the model organises its knowledge, and GPQA runs on that organisation. An archetype ($\alpha$, $\beta$) is held once; each domain adds only its metanym set (the slices), about a fifth of the instantiation it yields. GPQA: archetype and domain are given; the model derives the instantiation and selects the matching candidate. The game: nothing is given; the model selects the archetype and domains that best satisfy the criteria and writes them out.](../submission/figures/mechanism_sketch.png)

## H.1 The chain

1. **Cited.** Training a language model is compression. Predicting text is compressing it (Shannon, 1951); a trained model is a general-purpose compressor (Delétang et al., 2024).
2. **Cited.** Analogy is semantic compression. An analogy is a shared relational structure with different particulars (Gentner, 1983).
3. **Postulated.** The archetypal context is a semantic structure in the latent space. A context template is a literal representation of the archetypal context. The metanym sets are the particulars that, when inserted into the slots of the template, instantiate into parallel contexts, analogous metaphors.
4. **Hypothesis.** A language model holds its knowledge as archetypal contexts, each instantiated in the topic domains where it applies. The template is the abstraction, the metanym set is the topic domain, and the two reconstruct the instantiation exactly.
5. **Measured.** In the metanym game an instantiation is between two and a half and eleven times the size of its metanym set, so each domain is added for a fraction of the text it yields. That is compression of the same order as has been measured for language models, about ten (Delétang et al., 2024), and above gzip's three. A memorised string compresses only its exact repeats; a frame compresses every new instance that fits it.
6. **Hypothesis.** A form this compressive qualifies as a learning mechanism for a language model.
7. **Hypothesis.** The Metanym Game and GPQA run the same mechanism from opposite ends:
    - GPQA sets the archetype and the domain in the prompt, with four candidate answers where only one is true. In 99.5% of the responses the model first derives the solution and then identifies the truthful candidate.
    - The Metanym Game sets no archetype or domain; the prompt merely shares rating criteria, emphasizing truthfulness; the model selects an archetype and a set of domains to score the highest rating.

If the hypothesis is correct, it explains why models play the Metanym Game so well without reasoning at T=0, a task few humans would attempt without long reflection. Because it is actually not creative, the semantic response to the prompt is ready to be extracted. If so, adding reasoning will not improve the result much.

**A test.** We played four models each as two players, with the reasoning channel off at temperature 0 and on, through the official APIs: Claude Sonnet 4.6, Claude Haiku 4.5, GPT-5.6 Terra and GPT-5.6 Luna. Each played the generation prompt once and judged, with the benchmark's evaluator prompt and anchor, the six players that were neither itself nor its kin, plus the two ballasts. The thinking model does not build templates in its thinking. It writes them once, in the answer, the same way the non-thinking model does. If templates were constructed by reasoning, the thinking would be full of drafting and revising. It is not. What the thinking does contain is a list of archetypes, by name, and a choice among them. That is selection over things the model already has, which is what retrieval from a store looks like. The ratings agree: thinking changed the factual score by less than a point for every model, and by nothing that clears the interval for any of them.

| Model | Reasoning off | Reasoning on | On minus off, 95% interval |
|---|---:|---:|---|
| Claude Haiku 4.5 | 5.99 | 5.31 | −0.67 [−1.83, +0.42] |
| GPT-5.6 Luna | 7.63 | 7.81 | +0.18 [−0.08, +0.47] |
| Claude Sonnet 4.6 | 7.00 | 7.31 | +0.31 [−0.09, +0.76] |
| GPT-5.6 Terra | 7.01 | 7.55 | +0.54 [−0.17, +1.31] |

Table: Factual rating with the reasoning channel off and on, six judges each, anchor at 7; bootstrap over judges and archetypes, percentile 95% intervals. One portfolio per cell; the vendors return summaries of the thinking, not the trace.

On GPQA the reasoning channel does matter: Anthropic reports Claude Opus 4 and Claude Sonnet 4 at 74.9 and 70.0 without extended thinking and 79.6 and 75.4 with it (Anthropic, 2025), and our reasoning-off administration reads 71.2 and 72.2 for the same models (Appendix D). That is the split the hypothesis predicts: GPQA is the mechanism's use, a derivation, which reasoning helps (Sprague et al., 2025); the game is the mechanism, a retrieval, which reasoning does not.

**Two consequences.** If the hypothesis is correct, the agreement is domain-matched: a model's factual score on parallel contexts in a field tracks its GPQA accuracy in that field, and GPQA's subject labels together with the domains of the released evaluations allow the test without a new run; field-by-field agreement no higher than agreement across fields would refute it. And archetype and topic domain are separable in the model's latent space: the same archetype is recoverable from its parallel contexts in unrelated domains, and the domain from unrelated archetypes; representations that separate by domain only would refute it.

What the data establish is narrower: the factual pair reaches 0.94 with GPQA and the two subjective quarters lift it to 0.98 (§4.5, Appendix D.1).
 