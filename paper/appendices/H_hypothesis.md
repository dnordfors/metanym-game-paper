# H. The argument behind the hypothesis

Nothing in this appendix tests the hypothesis of §6. It sets out the argument step by step, marks each step as a cited result, a measurement on the released data, or the hypothesis itself, and ends with what would refute it. Every number comes from a script in the released package.

<a id="fig-gpqa-scatter-h"></a>

![The agreement the hypothesis is offered for, reproduced from Figure 2: the official total $T$ (council basis, three runs pooled) against self-administered GPQA Diamond accuracy, twelve models; Pearson $r = 0.98$ (95% BCa CI [0.95, 0.99]), Spearman $\rho = 0.96$. Filled markers are council seats, open markers non-council, the star the anchor at $T = 7$ by calibration.](../submission/figures/total_validation_simple.png)

<a id="fig-mechanism"></a>

![A hypothesis for the 0.98: the metanym game reproduces the way the model organises its knowledge, and GPQA runs on that organisation. An archetype ($\alpha$, $\beta$, $\gamma$) is held once; each domain adds only its metanym set (the slices), about an eighth of the instantiation it yields. GPQA: archetype and domain are given; the model derives the instantiation and selects the matching candidate. The game: nothing is given; the model selects the archetype and domains that best satisfy the criteria and writes them out.](../submission/figures/mechanism_sketch.png)

## H.1 The chain

1. **Cited.** Training a language model is compression. Predicting text is compressing it (Shannon, 1951); a trained model is a general-purpose compressor (Delétang et al., 2024).
2. **Cited.** Training selects what is compressed, by construction of the objective. The loss is taken on held-out text, so an abstraction earns its place only by predicting instantiations the model has not seen, and the abstractions that recur most across the corpus earn the most. A situation structure that appears in biology, economics and stories alike is one.
3. **Cited.** Compression generalises. The shortest description keeps a recurring pattern once, as an abstraction, and reuses it (Rissanen, 1978); that is a concept.
4. **Cited.** A concept is a frame with open slots. Minsky's (1974) frames are stereotyped situations with terminals that instances fill; the context template of §2 is such a frame, written in words.
5. **Cited.** An analogy is a shared relational structure with different particulars (Gentner, 1983). The archetypal context is that shared structure.
6. **Hypothesis.** A language model holds its knowledge as archetypal contexts, each instantiated in the topic domains where it applies. The template is the abstraction; the metanym set is what the abstraction leaves out, the topic domain; the two reconstruct the instantiation exactly.
7. **Measured (H.2).** The metanym form is strong compression. About 3 for a template with five parallel contexts and about 8 for each further one, growing with every domain a template serves — the order of the compression a trained model achieves on text, in words rather than bits. The factor grows because the template has open slots: a memorised string compresses only its exact repeats, a frame compresses every new instance that fits it, and no instantiation here repeats another. This is the abstracting kind of compression, the kind held-out loss rewards; a representation this compressive is what training would find.
8. **Hypothesis.** The game measures the mechanism directly. Nothing is given; the model selects the archetype and the domains that best satisfy the prompt's criteria, factual truth among them, and writes them out.
9. **Hypothesis (H.4 is the observation).** GPQA measures the mechanism's use. The archetype and the domain are given by the question; the model derives the instantiation and selects the candidate that matches it. The two tests agree because they exercise one operation from opposite ends: GPQA fixes the store position and selects among four strings, the game selects the store position and fixes the output form.
10. **Hypothesis (H.3 is the signature).** Corollary: retrieval, not construction. In the game the models retrieve templates and metanym sets that training already compressed, which is why they play well with no reasoning channel and why a model rewrites its portfolios between runs but keeps its archetypes.
11. **Established.** What the data establish is narrower. The factual pair reaches 0.94 with GPQA and the two subjective quarters lift it to 0.98 (§4.5, Appendix D.1). The hypothesis is consistent with the general factor of Ilić and Gignac (2024), and more specific.

## H.2 The compression of the metanym form

Measured on the anchor submission's first archetype, the one archetype shipped in full (`scripts/compression_ratio.py`). The template is 120 words; the metanym table 84 words for five parallel contexts, 17 per context; the five instantiations (Form a, the form the template and metanym set reconstruct exactly) average 130 words. With $n$ contexts the factor is $130n/(120+17n)$:

| contexts | 5 | 10 | 20 | 50 | limit |
|---|--:|--:|--:|--:|--:|
| factor | 3.2 | 4.5 | 5.7 | 6.9 | 7.8 |

Table: Literal compression of the metanym form against the number of parallel contexts per template, from the anchor's first archetype (120-word template, 17 words of metanyms per context, 130-word instantiations).

The asymptote is the ratio of an instantiation to its metanym set, and it is reached only when a template is amortised over dozens of domains, which is the situation inside a model rather than inside a five-context game. The count is in words, and metanyms are the high-entropy tokens, so the factor in bits is lower; the bit-level factor is measurable with an open-weights model and is not measured here. Templates in the released portfolios run 80 to 120 words with 10 to 15 slots, so the asymptote varies by archetype within the same range. It is a lower limit in one further sense: a metanym set is itself a frame with slots, so the topic domain compresses by the same rule, and the factors multiply down the hierarchy.

## H.3 The retrieval signature: the runs part on one word, and the archetypes return

At temperature 0 the decoder takes the highest-scoring token at each position. Serving is not bit-exact from call to call, and where two candidates score almost equally a difference below rounding decides between them; from that token on the text is generated anew. Runs 2 and 3 were made two hours apart from the same prompt at temperature 0, and the raw portfolios of both are shipped (`data/regenerations/portfolios_run2/`, `portfolios_run3/`; `scripts/portfolio_divergence.py`). Run 1's portfolios were not preserved, so the three-week pair is read from the evaluation transcripts, which copy the headings (`scripts/archetype_recurrence.py`).

**Where the runs part.** Gemini 2.5 Flash returned the same 9,099 words. The other eleven models part inside the first template sentence, after 3 to 93 shared words, on one word: *risks* against *faces*, *that detect* against *to detect*, *activates* against *encounters*. Everything after the fork, two to eight thousand words, is generated anew. After the fork, 22 of 42 archetypes return by title; in the four models that keep the most, Claude Opus 4.0, GPT-4.1, Gemini 3.1 Pro and GPT-4o, 14 of 17.

| Model | Words shared | The fork (run 2 / run 3) | Archetypes returning after it |
|---|---:|---|---:|
| claude-opus-4.0 | 23 | *activated [UNIT] recruits* / *[UNIT] that receives* | 4 / 4 |
| claude-opus-4.1 | 14 | *activates a [DETECTOR]* / *encounters a [DETECTOR]* | 1 / 4 |
| claude-opus-4.5 | 40 | *that detect changes* / *to detect changes* | 2 / 5 |
| claude-sonnet-4 | 15 | *[ORGANIZATION]. Each* / *[ORGANIZATION] while* | 2 / 4 |
| gemini-2.5-flash | 9,099 | identical | 6 / 6 |
| gemini-3.1-pro | 93 | *risks [CONSEQUENCE]* / *faces [CONSEQUENCE]* | 3 / 4 |
| gpt-4.1 | 75 | first table cell: *Biological Organism* / *Genetics* | 4 / 5 |
| gpt-4.1-mini | 3 | *[Resource Flow* / *Resource Flow* | 1 / 5 |
| gpt-4.1-nano | 14 | *based on [INFORMATION]* / *by a [DECISION-MAKER]* | 1 / 3 |
| gpt-4o | 23 | *[CRITERIA] to ensure* / *[STRATEGY] to ensure* | 3 / 4 |
| gpt-4o-2024-08-06 | 23 | *[CRITERIA] to ensure* / *balancing [CONSTRAINT]* | 1 / 4 |
| gpt-4o-mini | 26 | *relative importance of* / *value of each* | 0 / 0 |

Table: Where the raw portfolios of runs 2 and 3 part (same prompt, temperature 0, two hours apart), and how many of run 2's archetypes after the fork return in run 3 by title. gpt-4o-mini's run 2 portfolio holds one archetype, the one the fork falls in.

**What returns and what does not.** Of the 37 archetypes a model kept by title, 30 templates are rewritten, with a median text similarity of 0.19; half the slot names are kept (199 of 387), a third of the domains (53 of 150), and where a domain and a slot are both kept the metanym is the same in 221 of 388 cells. Seven templates return verbatim: Gemini 2.5 Flash's six, and one GPT-4.1 template returned word for word with all five domains replaced, the fork falling on the first cell of its metanym table.

**The reading.** The perturbation acts in literal space: the first near-degenerate logits after the prompt decide the wording, and from there the context template and the metanym sets are written anew. What returns is the archetype, in a different literal representation. This is what one archetype in latent space with many projections in literal space predicts. A stored text would return verbatim or not at all; Gemini 2.5 Flash's identical portfolio is the one case that does not separate the two. Between run 1 and run 2, three weeks apart, 20 of 50 titles recur.

**Across models, the same concepts recur, across vendors.** Seven of the eleven graded models, from all three vendors, offer a resource-allocation archetype (title containing "allocation"). Six domains are used by five or more models: urban planning, social media, corporate structure, the climate system, software development, biological evolution. Of 81 distinct titles, 14 are used by more than one model.

**The caveat.** Recurrence is strongest inside a vendor: 11 of the 14 shared titles are shared within one vendor only, the two Opus models sharing cascade amplification, phase transition, competitive exclusion and boundary maintenance word for word, and the GPT-4o family sharing resource allocation, conflict resolution and growth and development. Shared training data explains within-vendor recurrence as well as shared representation does. The cross-vendor recurrence is the evidence. A second reading of the recurrence is a strong prior over topics under this prompt; the test that separates it from a stored structure is the fifth prediction of H.5.

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
5. **Recurrence under a changed prompt.** With the two worked examples of the generation prompt replaced, the same archetypes should return, rewritten as in H.3. A refutation: recurrence that vanishes with the examples, which would put the archetypes in the prompt and not in the model.
