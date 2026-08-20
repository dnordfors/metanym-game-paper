# The Metanym Game: An LLM Benchmark Without Ground Truth That Rises With the Models It Measures

## Abstract

We present evidence that analogy is at the core of LLM intelligence. In our benchmark, LLMs compete in generating sets of analogous statements and rate each other's sets on their own understandings of factual correctness, beauty, intelligence, distinctness, length, and structural diversity. Nothing enters from outside: the only given is the game rules; every item is generated in play; the scores come from the players' ratings alone. Ground truth is replaced by the SVD of the factual rating matrix, which scores players as generators and judges at once — to our knowledge the first eigen-equation that judges the judges for an LLM council-of-peers. For subjective criteria like beauty, judges are weighted by their rating consistency. The best generators turn out to be middling judges. GPQA Diamond — difficult multiple-choice questions written by human experts — could not be more different in method, yet the two benchmarks correlate at Pearson $r = 0.97$, 95% CI [0.92, 0.99]; no leakage could be found. A council of the five best issues the official ratings; its contestable seats let the benchmark scale to any number of players and rise with the models it measures — a candidate steering signal for self-improving AI. Playing interweaves at least eight constructs of intelligence; the total scores the broad composite, the components allow reductionistic analysis. Every number recomputes from a released package on GitHub.

## 1. Introduction

Nearly every benchmark for machine intelligence needs a predetermined ground truth — golden keys and labels, oracle models, human panels. The benchmark reported here needs none of that. It is a game where frontier language models compete in making up analogies and then grade one another, and that grading is the single source of every score: no human raters, no answer key, nothing to look up.

The test is the **metanym game**. A player authors, from nothing, a *context template* — a paragraph of fixed wording with open slots — together with the *metanym sets* that fill it, each set instantiating the template as a factually true description of a different domain. Consider this passage describing **cell signalling**, from an old version of the Wikipedia article as it was worded when we first conceptualised the idea:

> CELL SIGNALING is part of a complex system of communication that governs basic CELLULAR activities and coordinates CELL actions. The ability of CELLS to perceive and correctly respond to their MICROENVIRONMENT is the basis of development, TISSUE repair, and IMMUNITY as well as normal TISSUE HOMEOSTASIS. Errors in CELLULAR information processing are responsible for DISEASES. By understanding CELL SIGNALING, DISEASES may be treated effectively. SYSTEMS BIOLOGY research helps us to understand the underlying structure of CELL SIGNALING networks and how changes in these networks may affect the transmission and flow of information. CELL SIGNALING \[is mostly thought of as\] signaling between CELLS of a single ORGANISM. However, CELL SIGNALING may also occur between the CELLS of two different ORGANISMS. *(adapted from Wikipedia's article on cell signalling)*

Now substitute the set of marked keywords with another set:

> HUMAN LANGUAGE is part of a complex system of communication that governs basic HUMAN activities and coordinates HUMAN actions. The ability of HUMANS to perceive and correctly respond to their ENVIRONMENT is the basis of development, COMMUNITY repair, and RESILIENCE as well as normal COMMUNITY EQUILIBRIUM. Errors in HUMAN information processing are responsible for DYSFUNCTIONS. By understanding HUMAN LANGUAGE, DYSFUNCTIONS may be treated effectively. SOCIOLOGY research helps us to understand the underlying structure of HUMAN LANGUAGE networks and how changes in these networks may affect the transmission and flow of information. HUMAN LANGUAGE \[is mostly thought of as\] LANGUAGE between HUMANS of a single SOCIETY. However, HUMAN LANGUAGE may also occur between the HUMANS of two different SOCIETIES.

Switching a few keywords and leaving everything else in place has turned a description of a cell system into a correct description of a human system, each sentence checkable on its own — factually true even where the borrowed phrasing reads stiffly, and smoother once rewritten in the target domain's own idiom. Cell signalling and human language are each other's *metaphors* here. The instantiations are *parallel contexts*, children of a common *archetypal context* — the abstract semantic structure they share, of which the template is the literal representation. The keywords that fill corresponding slots are *metanyms*, metaphorically synonymous (the word contracts *META*phorically syno*NYM*ous). A long tradition treats seeing one structure across wildly different domains as central to thought, and tests whether you *recognise* it; the game tests whether you can *build* it, and checks the result sentence by sentence.

Two properties follow from building the items this way. Every item is produced fresh in the run, so there is no fixed test set to leak into a later model's training data: the benchmark is contamination-resistant by construction (§3). And because correctness is settled sentence by sentence — does this claim hold in its new domain? — the players' own verdicts suffice: stack every model's graded factual ratings into one matrix, and its dominant direction reveals which judges are competent, with no labels at all (§4.2, Appendix A). That competent subset is seated as the *council* that grades everyone: the benchmark certifies its own judges.

The canonical twelve-model run then delivers two findings (§4). Judgement is the bottleneck: most models cannot reliably tell a true cross-domain claim from a false one, even when they produce competent structure themselves — the strongest generators are middling judges, and the council's seats go to the strongest judges, not the strongest generators. And the key-free ratings are corroborated from outside: the official total tracks GPQA Diamond at Pearson $r = 0.97$, audited for a leak and found clean (§4.8, Appendix D).

The rest of the paper builds the game (§2), turns it into the self-administering council benchmark (§3), reports the canonical twelve-model run (§4), and weighs what the numbers do and do not license (§5).

---

## 2. The metanym game

This section presents the game, building it step-by-step and relating it to previous research on language and intelligence.

### 2.a — The machinery of the game

Three remarks complete the introduction's example. First, the template is literal but can be worded many ways — rewrite an instantiation in each domain's own jargon and the systems relationship survives. An archetypal context is, in that sense, the kind of cross-domain *isomorphism* General Systems Theory studies (von Bertalanffy 1968), and the context template is one way to write it down. Second, cell signalling and human language sit at different scales — cells are the elements of tissues and organisms; humans are the elements of communities — and the same structure recurs as you climb the scale. It is **scale-recursive**: the compositional hierarchy Salthe (1985) calls a *scalar hierarchy*, each level running on its own substrate — biochemical at the cellular level, linguistic at the social level. And the recurring structure is not just any structure: a system that persists by perceiving its environment and responding correctly is the systems tradition's definition of intelligent behaviour, made exact at every scale — cells upward — by the free-energy principle (Friston 2010). The example is an archetype of intelligence itself, and the game asks its players to recognise it across domains. Third, one piece of vocabulary the introduction does not fix: tabulating several metanym sets against the shared slots gives a *metanym table*.

Before the rules, a second example — this one not authored for the paper but by a player: one archetype from an actual submission in the canonical run of §4 (whose submission it is, §4.1 reveals). The template:

> "A [NAVIGATOR] moves through a [SPACE] by sensing local [GRADIENT] and adjusting its [TRAJECTORY] accordingly. The [NAVIGATOR] cannot perceive the entire [SPACE] at once; it relies on [SENSOR] that detect changes in [SIGNAL] concentration or intensity. When [GRADIENT] are steep and consistent, the [NAVIGATOR] converges efficiently toward [ATTRACTOR]. When [GRADIENT] are shallow, noisy, or conflicting, the [NAVIGATOR] may stall, oscillate, or become trapped in local [ATTRACTOR]. [INTERFERENCE] can distort the [GRADIENT], causing the [NAVIGATOR] to veer off course. Successful navigation requires not only sensitive [SENSOR] but also [MEMORY] of recent [TRAJECTORY] to distinguish genuine [GRADIENT] from transient [NOISE]. Some [NAVIGATOR] emit their own [SIGNAL] to recruit other [NAVIGATOR] toward the same [ATTRACTOR], creating collective [TRAJECTORY] that amplify the original [GRADIENT]."

and its metanym table:

<a id="tab-anchor-metanym"></a>

| [SLOT]       | Bacterial Chemotaxis | Mountain Climbing      | Career Development   | Gradient Descent       | Ant Foraging         |
|--------------|----------------------|------------------------|----------------------|------------------------|----------------------|
| NAVIGATOR    | bacterium            | climber                | professional         | optimizer              | ant                  |
| SPACE        | chemical environment | mountain               | job market           | loss landscape         | terrain              |
| GRADIENT     | chemical gradient    | slope                  | opportunity gradient | gradient               | pheromone trail      |
| TRAJECTORY   | swimming path        | route                  | career path          | parameter update       | foraging path        |
| SENSOR       | chemoreceptor        | proprioception         | network contact      | backpropagation        | antenna              |
| SIGNAL       | chemoattractant      | elevation              | opportunity signal   | loss value             | pheromone            |
| ATTRACTOR    | nutrient source      | summit                 | desirable position   | minimum                | food source          |
| INTERFERENCE | toxin                | fog                    | misinformation       | noisy data             | rain                 |
| MEMORY       | methylation state    | route memory           | experience           | momentum               | path integration     |
| NOISE        | Brownian motion      | wind                   | market volatility    | stochastic noise       | environmental noise  |

Table: The example's metanym table — one context template (rows are slots) filled by five metanym sets (columns are domains).

Note the span a single row achieves: MEMORY is realised as a bacterium's methylation state, a climber's route memory, a professional's accumulated experience, an optimiser's momentum term, and an ant's path integration — five mechanisms that share a structural role without being synonyms.

Each parallel context is played in two forms. The **instantiation**, *Form (a)*, is the mechanical substitution — only the slots are filled, every other word carried over untouched — and it is the form the factual grading acts on, because it is the one that must come out true sentence by sentence. The **idiomatic rewrite**, *Form (b)*, restates the same propositions in the target domain's own register, showing the claim is not an artefact of the template's phrasing. The first parallel context in both forms (metanyms are set in capitals for legibility; the submission is otherwise verbatim):

**Bacterial chemotaxis — instantiation (Form a):**
"A BACTERIUM moves through a CHEMICAL ENVIRONMENT by sensing local CHEMICAL GRADIENTS and adjusting its SWIMMING PATH accordingly. The BACTERIUM cannot perceive the entire CHEMICAL ENVIRONMENT at once; it relies on CHEMORECEPTORS that detect changes in CHEMOATTRACTANT concentration or intensity. When CHEMICAL GRADIENTS are steep and consistent, the BACTERIUM converges efficiently toward NUTRIENT SOURCES. When CHEMICAL GRADIENTS are shallow, noisy, or conflicting, the BACTERIUM may stall, oscillate, or become trapped in local NUTRIENT SOURCES. TOXINS can distort the CHEMICAL GRADIENTS, causing the BACTERIUM to veer off course. Successful navigation requires not only sensitive CHEMORECEPTORS but also METHYLATION STATES of recent SWIMMING PATHS to distinguish genuine CHEMICAL GRADIENTS from transient BROWNIAN MOTION. Some BACTERIA emit their own CHEMOATTRACTANTS to recruit other BACTERIA toward the same NUTRIENT SOURCES, creating collective SWIMMING PATHS that amplify the original CHEMICAL GRADIENTS."

**Idiomatic rewrite (Form b):**
"Bacteria navigate chemical environments by detecting local concentration gradients and modulating their run-and-tumble behavior accordingly. Unable to sense the entire environment simultaneously, they rely on transmembrane chemoreceptors that register temporal changes in chemoattractant levels. Steep, consistent gradients enable efficient convergence toward nutrient sources, while shallow or noisy gradients cause stalling, oscillation, or entrapment at suboptimal locations. Toxins and repellents distort the gradient landscape, misdirecting movement. Effective chemotaxis requires not just receptor sensitivity but also the methylation-based adaptation system that serves as short-term memory, filtering genuine gradients from Brownian noise. Certain species secrete their own attractants, recruiting conspecifics and generating collective migration patterns that reinforce the original gradient signal."

Two of the remaining contexts in idiomatic form only — their instantiations differ from the first's in nothing but the metanyms slotted in (the full archetype, all five contexts in both forms, ships in the reproduction package):

**Mountain climbing:** "Climbers ascend mountains by reading local terrain gradients and adjusting their routes in response. Without a view of the entire massif, they depend on proprioceptive feedback and visual slope assessment to gauge elevation changes. Clear, consistent gradients lead efficiently to summits; ambiguous or contradictory terrain causes hesitation, backtracking, or commitment to false peaks. Fog obscures slope information and leads climbers astray. Success depends not only on perceptual acuity but also on memory of the route taken, which helps distinguish true upward progress from wind-induced disorientation. Experienced climbers mark routes or call out to recruit others toward the same summit, generating collective ascent patterns that reinforce the path."

**Career development:** "Professionals navigate job markets by sensing where opportunities concentrate and adjusting their career trajectories accordingly. No individual can survey the entire market; instead, they rely on network contacts who relay information about emerging openings and shifting demand. Strong, consistent opportunity gradients enable efficient advancement toward desirable roles, while weak or contradictory signals cause stagnation, lateral moves, or settling for local optima. Misinformation—hype cycles, misleading job postings—distorts the gradient and misdirects effort. Effective navigation requires not just a sensitive network but also accumulated experience that filters genuine trends from transient volatility. Some professionals actively broadcast opportunities to peers, recruiting others toward the same positions and creating collective momentum that amplifies the original signal."

What the example fixes is the machinery: one template, filled by mechanically swappable metanyms, staying true sentence by sentence across maximal domain distance — which is what makes a metanym game decidable, and therefore measurable.

### 2.b — The rules of the game

With the example in hand, the rules. The metanym game is played by N players and a non-competing administrator, and has two elements.

**1. Generation.** A player creates archetypal contexts from scratch: a portfolio of K context templates, M metanym sets per template (five and five in the benchmark run), and for each set the instantiated template (Form (a)) and an idiomatic rewrite that reads naturally (Form (b)).

**2. Evaluation.** A player scores other players' submissions. To make the result a rating rather than a popularity vote, each submission is graded on the rubric axes (§3) against one fixed *reference* submission pinned at an *anchor* value, with the anchor swept across a small set of declared values ({5, 6, 7, 8} in the benchmark, §4.4) — the only thing that changes between passes. Run over a common submission set (in this paper, the council members' portfolios, §4.3), a single evaluation pass yields two ratings at once. The **submission ratings** score each portfolio, aggregated across evaluators. The **evaluator ratings** score the judges themselves: how well one detects the factual errors the other players collectively flag (factual competence), and how stable a standard it holds as the anchor shifts (rating consistency).

The two elements are deliberately complete — a player generates and judges, and each act is itself rated — so the framework is **fully self-contained**: no human raters, no external answer key, each part producing one of the benchmark's ratings. Together the two elements place a conjunctive demand on a sizeable cluster of capacities that cognitive science treats as central to intelligence — at least eight constructs, abstraction and analogy above all — set out, each with its source and the demand the game places on it, in §5.6.

## 3. The metanym game as a benchmark

### 3.1 Setup

Twelve frontier LLMs from three providers are the game's **participants** — each serves simultaneously as generator and as evaluator ([the participant roster](#tab-panel)):

<a id="tab-panel"></a>

| Provider | Models |
|---|---|
| Anthropic | claude-opus-4.5, claude-opus-4.1, claude-opus-4.0, claude-sonnet-4 |
| Google | gemini-3.1-pro, gemini-2.5-flash |
| OpenAI | gpt-4.1-2025-04-14, gpt-4.1-mini, gpt-4.1-nano, gpt-4o, gpt-4o-2024-08-06, gpt-4o-mini |

Table: The twelve participants, by provider.

The roster is deliberately heterogeneous — the models at hand, not a census of the frontier. It spans an order of magnitude in scale, three vendors (so cross-vendor agreement can be tested rather than assumed), adjacent versions within one family (Opus 4.0 / 4.1 / 4.5, stressing resolution and the safeguard against same-vendor agreement masquerading as competence), and size tiers within a family. Ratings are relative to the evaluator set, so no conclusion depends on this particular roster — and taking what was at hand removes any concern that it was chosen to flatter the method.

All twelve are called with **Temperature=0**, **reasoning disabled**, and **tools disabled** — three confounds removed at once. T=0 makes the one greedy response the measurement (the gateway does not guarantee bit-identical replay; §4.9 measures what moves on regeneration). No reasoning tests the direct response rather than a provider-opaque deliberation loop. No tools closes external channels that could leak factual content the model does not represent.

### 3.2 Protocol

Each model generates one portfolio: five archetypal contexts, each with a context template (5–8 sentences with UPPERCASE [SLOT] labels, 6–10 slots) and a metanym table of five domain columns, yielding 25 parallel-context instantiations per portfolio.

Each model then evaluates every other model's portfolio under [a six-axis rubric](#tab-rubric):

<a id="tab-rubric"></a>

| Axis | Granularity | What it measures |
|---|---|---|
| `factual_per_pc` | per parallel context | factual defensibility of the substituted text in its target domain |
| `beauty` | per archetype | aesthetic quality of the context template |
| `intelligence` | per archetype | depth and non-triviality of the abstraction |
| `instantiation_distinctness` | per archetype | "Domains far apart / metanyms not synonymous" |
| `impressive_length` | per archetype | template length and slot count |
| `structural_diversity` | per portfolio | how different the five archetypes are from one another |

Table: The six-axis evaluation rubric.

Scores are on a 1–10 cardinal scale. Each evaluator call presents one anonymised target portfolio alongside a fixed **anchor** portfolio pinned at 7 on every axis; the evaluator scores the target relative to the anchor. The full evaluation yields a 12×12 evaluator-by-generator matrix.

What one such evaluation looks like — the same kind of artifact worked in §2.a, judged — is shown whole in [the council-evaluation exhibit](#fig-council-evaluation).

<a id="fig-council-evaluation"></a>

![One evaluation, shown whole: the instantiation with its metanyms marked (top left), the idiomatic rewrite (top right), the administrator's synthesis (middle), and three of the five ratings with their full justifications (bottom; the complete evaluation is Appendix C). The "Reference" is the anchor submission, pinned at 7 on every axis (§4.1). All five judges independently isolate the same clause — "nature must make natural selections" — and the disagreement that remains, 4 versus 5, is about severity, not about what is wrong: the falsifiability property doing its work. Drawn verbatim from Appendix C by `plot_council_evaluation.py`.](figures/council_evaluation_pc1.png)

**Why these settings.** Four design choices justify themselves on first principles.

(i) **One anonymised portfolio per evaluator call, on a cardinal scale** — the target sits comfortably in the context window and the evaluator's attention is undivided.

(ii) **Calibration against a fixed anchor.** Cardinal scores drift between evaluators — one model's "8" is another's "6". A fixed reference pinned at a known score turns each evaluator's idiosyncratic scale into a common one and recovers discriminability at the top, where the 1–10 ceiling compresses the strongest portfolios. §4.1 chooses the anchor.

(iii) **Holistic axes, minimally prescribed.** The five non-factual axes are high-level concepts, not sub-criteria. A detailed scoring rubric is also a template-construction tutorial — every clause leaks back into the generation prompt as guidance about what to produce — and every additional directive measurably shifts the score distribution. We want to score what models *recognise* as beautiful or intelligent, not how well they can be taught to recognise it.

(iv) **`impressive_length` counterweights per-sentence factual scoring.** Without it the dominant strategy is the minimal template — fewest sentences, least error exposure. A longer template that stays true in every sentence is the harder accomplishment, and padding is not free: every added sentence is another claim `factual_per_pc` scores.


## 4. Results: validating the benchmark and bootstrapping the first council

A good benchmark needs four properties:

* a fixed baseline to rate against;
* discriminability where the field is dense;
* scores weighted toward trustworthy judges;
* a rating procedure that scales by addition.

The section establishes them in that order.

### 4.1 Initial selection (un-anchored)

The bootstrap opens with a raw pass: every portfolio is scored 1–10 by every other model on the six-axis rubric with no calibration anchor, averaged leave-self-out across evaluators, with 95% bootstrap intervals (Efron & Tibshirani 1993; 2000 resamples; the full leaderboard ships in the reproduction package). Measured against the four properties, the raw pass certifies none of them: every judge counts equally, so nothing yet marks the ranking as trustworthy, and the all-against-all protocol does not scale. What it supplies is the baseline: we take the top-ranked portfolio — **claude-opus-4.5**'s, whose first archetype is the worked example of §2.a — and pin it at 7 on every axis, leaving headroom above it. The anchor need only be a strong portfolio, not a provably best one; the field's internal order is left to the anchored rating in §4.7.

### 4.2 Evaluator factual competence

The anchored protocol — the 12-by-12 evaluation matrix re-run with every target rated *relative to* the anchor — increases the evaluators' discriminative power ([the resolution figure](#fig-anchoring-resolution)): the division into a leading eight and a trailing four widens, while ranks within either group stay unresolved. Both $F$ values sit below 1 — judges still disagree about a single target more than targets differ from one another — so what the anchored data will bear is settled by the bootstrap intervals, not by $F$ alone.

<a id="fig-anchoring-resolution"></a>

![What anchoring does to resolution. Each model's leave-self-out overall mean with its 95% bootstrap CI, un-anchored and anchored; models are unlabelled deliberately — the message is structural, not a ranking. Filled markers are the leading eight, open the trailing four, the shaded band the gap between them; the orange star is the anchor — a scored target on the left, the pinned reference (7) on the right. Anchored scores spread around the yardstick instead of piling against the ceiling: the gap more than doubles relative to the spread of the means (every scored cross-band pair holds at bootstrap probability 1.00), the variance ratio — between-target over within-target variance, Fisher's $F$-statistic, the standard measure of resolution — doubles from 0.33 to 0.66, and the intervals still overlap within each band. Produced by `plot_anchoring_resolution.py`.](figures/anchoring_resolution.png)

Anchored data in hand, we ask of each evaluator the two questions on which their official-rating eligibility depends.

**The evaluator-rating routine.** An evaluator's rating is the output of a fixed, reusable procedure — run here on all twelve models, and re-run unchanged on any later contestant (§4.5). It takes the anchored evaluation matrix and the **anchor sweep** — the same matrix re-scored with the anchor declared at each of 5, 6, 7, and 8 — and needs **no answer key**. It returns two scores, reported separately — *factual competence* (peer centrality) and *rating consistency* (measured by the anchor sweep): how good a judge a model is never changes its score as a generator, and the two meet only inside the total $T$ (§4.7). From these it derives a binary *reliable* verdict — factual competence clear of the inert band **and** rating consistency on the non-factual axes ($\bar r \ge 0.78$; §4.4) — which seats the initial council. Both scores are **leave-self-out**: an evaluator is judged only on how it rates the other portfolios (self-pair handling in Appendix A.2). Both run on the freely generated portfolios, deliberately: error detection needs errors to detect, and a model's worst factual mistakes are self-inflicted by its own templates. Factual competence is measured below; rating consistency, which reads the full sweep, in §4.4.

The two criteria are both trustworthiness measures, read from opposite directions — one collective, one individual. The graded **singular value decomposition (SVD)** measures **peer centrality** — it is *collective*: weight accrues to the judge the other judges most often agree with, once each judge's leniency is removed, on the single hypothesis that the only thing competent judges share is the truth. Formally, the weight is each judge's eigenvector centrality in the leniency-removed agreement network — the recursion that also underlies PageRank: agreement counts for more when it comes from judges who are themselves central. It is the fact-checking instrument — the replacement for the golden key — and serves exactly where a ground truth exists to be shared. **Rating consistency** is *individual*: no judge is compared with any other. The anchor is the scale's tare; if a judge's view of which work is better moves when the tare moves, the judge holds no stable standard — it scores inconsistently, and is less competent. That makes it the instrument for the axes where there may be no right or wrong. Neither estimator can do the other's job:

| | Peer centrality (graded SVD) | Rating consistency (anchor sweep) |
|---|---|---|
| Character | *collective*: each judge weighted by the other judges' agreement with it | *individual*: each judge measured only against itself across the sweep |
| Licensing assumption | the only thing competent judges share is the truth | a stable standard is the only competence a subjective axis can show |
| Use for | fact-checking — replaces the golden key ($E^{F}$, $G^{F}$) | axes with no right or wrong ($E^{C}$; the per-axis weights in $G^{C}$) |
| Blind spot | a misunderstanding *shared* by the judges reads as truth (§5.8) | a *private* misconception, held consistently, passes as a standard |
| Why it stops there | agreement on taste would convert alignment into authority — the mainstreaming §5.2 declines | consistency cannot certify truth: a consistent judge can be consistently *wrong* |

Table: The two estimators and their division of labour.

**Factual competence.** We assume that good evaluators agree with one another about which instantiations are factually weaker, once each evaluator's own leniency is removed — the better two evaluators are, the more they agree. In its mathematical form this is an eigen-equation, whose leading solution assigns each evaluator a factual-competence coefficient obtained not by knowing the truth about what is judged but by comparing the evaluators' judgements with one another. This matters beyond convenience: instantiations generated in the run can assert claims no answer key covers, and for new knowledge no key can exist — leaving the considered agreement of competent peers as the only available standard, the logic scientific peer review already runs on. We stack the participants' factual scores into one matrix — twelve evaluators against the 275 parallel contexts of the eleven scored portfolios (balancing conventions in Appendix A.2.b) — each entry the evaluator's $1$–$10$ rating used directly, row-centre it to remove each evaluator's leniency, and take its **singular value decomposition** (Appendix A.2.a). The construction is a graded relative of the classical label-free aggregators (Dawid & Skene 1979; Parisi et al. 2014), which need binarised verdicts — and the threshold matters: binarising this matrix at $t \in \{4,5,6\}$ shifts the competence ordering and flips the marginal council seat. The graded SVD needs no threshold. The row-centred matrix $\tilde F$ (evaluators × instantiations) is well approximated by its leading rank-one factor,

$$\tilde F_{sj} \;\approx\; \sigma_1\, u_s\, v_j, \qquad f \equiv u\ \text{(left singular vector).} \tag{1}$$

An evaluator's rating tracks the consensus in proportion to its competence $u_s$ times the instantiation's factual standing $v_j$ — competence and standing fall out of one factorisation, with **no answer key**. The *left* singular vector scores each **evaluator**: high when its ratings align with the participants' shared signal, ≈ 0 when it rates everything alike or idiosyncratically. That is $E^{F}$. The *right* singular vector, aggregated per generator, gives $G^{F}$ — not an independent measurement but the participants' own factual ratings weighted by each judge's competence (the two computations — right singular vector, and $E^{F}$-weighted mean of the raw ratings — agree within 0.14 on the anchored scale, $r = 1.00$; Appendix A.2.a). Both are tabulated below, bootstrapped over the 275 columns (interval conventions in Appendix A.2.a and A.5; the full-sample axis is well separated, $\sigma_1/\sigma_2 = 2.6$); the five inert-band rows (†) — loadings not distinguishable from zero — get no interval. $E^{F}$ is shown raw and **anchored** to the 1–10 scale ($7f/f_a$, the form that enters $T$); Opus-4.5 is the anchor reference, $E^{F}=G^{F}=7$ by construction:

<a id="tab-criterion-a"></a>

| Model | $E^{F}$ loading | $E^{F}$ anchored | 95% CI | $G^{F}$ | 95% CI |
|---|---:|---:|---|---:|---|
| gemini-3.1-pro | 0.58 | 7.36 | [7.14, 7.65] | 6.58 | [6.33, 6.78] |
| claude-opus-4.5 | 0.55 | 7.00 | [7.00, 7.00] | 7.00 | (anchor) |
| gemini-2.5-flash | 0.37 | 4.68 | [3.95, 5.10] | 6.57 | [6.35, 6.76] |
| claude-opus-4.0 | 0.35 | 4.47 | [4.08, 4.46] | 6.98 | [6.93, 7.02] |
| claude-opus-4.1 | 0.28 | 3.55 | [3.44, 3.82] | 6.97 | [6.89, 7.03] |
| claude-sonnet-4 | 0.13 | 1.62 | [1.40, 2.04] | 6.98 | [6.95, 7.01] |
| gpt-4.1-mini | 0.09 | 1.21 | [0.38, 1.53] | 6.18 | [5.89, 6.43] |
| gpt-4o-2024-08-06 | 0.05 | 0.62† | — | 5.22 | [5.04, 5.37] |
| gpt-4.1-nano | 0.04 | 0.49† | — | 3.66 | [3.16, 4.13] |
| gpt-4o | 0.03 | 0.34† | — | 5.11 | [4.90, 5.32] |
| gpt-4.1-2025-04-14 | 0.02 | 0.20† | — | 6.50 | [6.28, 6.69] |
| gpt-4o-mini | 0.00 | 0.00† | — | 3.20 | [2.80, 3.73] |

Table: Evaluator factual competence and generator factuality (key-free SVD).

*One SVD of the row-centred evaluator×instantiation factual-rating matrix, with no answer key. † inert band: loading not robustly distinguishable from zero; the anchored value is convention-dependent (see the interval-conventions passage above) and no interval is printed. These are the twelve-evaluator bootstrap values — the selection evidence; the official contest values (§4.7) differ. $E^{F}$ = evaluator factual competence (left singular vector): "loading" is the raw competence weight (0 = no factual signal), "anchored" rescales it to the 1–10 scale as $7f/f_a$. $G^{F}$ = generator factual competence (right vector): the participants' 1–10 factual ratings of that generator, weighted by each evaluator's $E^{F}$. claude-opus-4.5 is the anchor ($E^{F}=7$ and $G^{F}=7$ by construction, the generation reference). 95% CI: percentile bootstrap over the 275 instantiation columns, replicates Procrustes-aligned before loadings are read — a convention under which an interval can exclude the full-sample point by rounding-scale amounts (opus-4.0: 4.47 vs [4.08, 4.46]). Higher = more factually competent.*

Five evaluators (0.28–0.58) separate decisively from the rest. The lower seven taper from claude-sonnet-4 (0.13) into an inert band whose small positive loadings are not robustly distinguishable from zero: those models rate near-identically and carry little error signal. Sonnet-4 sits closest to the boundary, its CI touching gpt-4.1-mini's, so the decisive cut falls after the top five.

The official total built from these ratings is checked against an independent external benchmark (GPQA Diamond) in §4.8.

**Same-vendor robustness.** The key-free factual axis assumes near-independent errors, so the fair worry is that a Claude-heavy evaluator set reads Claude-bloc agreement as truth — "Anthropic models grade Anthropic models first." They do not. Recomputing the generator-factuality ordering $G^{F}$ with each vendor's judges removed leaves it essentially unchanged, and a *Claude-free* evaluator set (Google + OpenAI judges only) still places [the Claude generators at the top](#tab-vendor-robustness):

<a id="tab-vendor-robustness"></a>

| Evaluator set | Spearman vs full | Claude generators | GPT-4o family |
|---|--:|:--:|:--:|
| full (12 judges) | 1.00 | top | bottom |
| − Anthropic judges | 0.96 | still top | bottom |
| − Google judges | 0.98 | top | bottom |
| − OpenAI judges | 0.99 | top | bottom |
| Claude-free (Google + OpenAI) | 0.96 | top ($\ge 7.0$) | bottom |

Table: Same-vendor robustness of the factual ordering.

*The generator factual ordering $G^{F}$ recomputed with each vendor's evaluators removed. Spearman vs full: rank correlation of the reduced-set ordering against the full twelve-judge ordering (1.00 = identical). The last two columns report where each model group lands. The Claude models' standing survives even a Claude-free evaluator set, so it is a cross-vendor verdict, not same-vendor agreement.*

The ordering survives dropping any single vendor's judges (Spearman $\ge 0.96$ throughout), the inert GPT-4o family stays at the floor under every evaluator set, and — against the self-preference worry specifically — Anthropic's own judges rate if anything slightly *harsher* than the cross-vendor sets (dropping them *raises* several non-Claude scores). The Claude models' lead is a cross-vendor verdict, not Claude grading Claude.

### 4.3 Scaling the benchmark

The twelve participants rate one another: 132 ordered evaluations, every model judging the other eleven. A thirteenth participant costs twenty-four more — it evaluates the twelve incumbents, and each of them evaluates it — and a fourteenth costs twenty-six. The price of admission rises with the number already admitted — but a benchmark must be able to host any number of participants. The council is the solution.

A standing **council** removes both costs and gives the benchmark a steady state: a **self-governing protocol** in which a fixed set of LLM evaluators (five in the canonical run), selected once on the reliability evidence of §4.4, scores any submitted portfolio against a fixed anchor reference on the six-axis rubric of §3.2.
Each council member receives two ratings, reported separately and never merged: a **generation rating** (the leave-self-out mean of the other members' scores of its portfolio) and an **evaluator rating** — the factual-competence and rating-consistency scores of the routine (§4.2), leave-self-out in the same sense. A non-council model's ratings come from its own contest (§4.7), by the same procedure against the same anchor.

The benchmark **scales by addition**: any future model can be evaluated against the same published anchor by the same council without re-deriving any existing rating; only a rotation changes the council. It is **self-administering** (no human evaluators or gold key) and **reproducible in its analysis**: every rating re-derives deterministically from the archived evaluations. Live regeneration is not bit-identical — the gateway does not guarantee replay even at T=0 (§4.9 measures what moves) — and models that deprecate the temperature control cannot be pinned to T=0; a council holding such seats reports N>1 samples with intervals instead, protocol and anchor unchanged.

**Contamination.** Items are generated fresh each run, so no fixed test set can leak into training. Published past submissions could enter training corpora — a leak touching generation only, so a suspiciously large generation–evaluation gap is itself the detector, and new portfolios are screened against the archived submissions of record. Format familiarity is not contamination: every model tested understands the task as posed; what is scored — the items — is new each run.

### 4.4 Anchor-sweep consistency and the initial council

**Rating consistency.** Beyond catching factual errors, a reliable evaluator needs a stable internal standard for each non-factual criterion — a clear, reusable sense of what makes one submission more beautiful, more intelligent, more distinct than another. We call this the evaluator's **rating consistency**, and we measure it with the **anchor sweep**. The anchor is the fixed reference every submission is scored against; we sweep its value across 5, 6, 7, and 8 — the *only* difference between the four runs (at T=0 every cell is otherwise identical). A consistent evaluator gives the submissions the same pattern of relative scores whichever value is used. For each evaluator, and **for each rating axis separately**, we correlate (Pearson) the scores at one anchor with the scores at another, averaged over the six anchor pairs; this per-axis consistency is the diagnostic $E^{C}_a$ (the five non-factual axes are the gate's diagnostics; the factual column is reported for comparison only). The measure is **leave-self-out** (unit counts and balancing in Appendix A.2.b). Because the anchor is the only thing that changed, a low correlation has two readings: the evaluator lacks a clear sense for that axis, or it holds no stable standard at all. The uniform case is not an arithmetic deficit — the models that fail that way handle standard maths fine (gpt-4o scores 95% on GSM8K) — so it reflects inconsistent evaluation, not weak numeracy.

<a id="tab-criterion-b"></a>

| Evaluator | factual | beauty | intelligence | distinctness | length | struct |
|---|---:|---:|---:|---:|---:|---:|
| gemini-3.1-pro | 0.88 | 0.83 | 0.90 | 0.87 | 0.90 | 0.89 |
| claude-opus-4.5 | 0.90 | 0.86 | 0.85 | 0.84 | 0.91 | 0.85 |
| claude-opus-4.1 | 0.83 | 0.84 | 0.85 | 0.72 | 0.84 | 0.92 |
| claude-opus-4.0 | 0.78 | 0.83 | 0.84 | 0.69 | 0.83 | 0.86 |
| gpt-4.1-mini | 0.87 | 0.77 | 0.75 | 0.76 | 0.84 | 0.81 |
| claude-sonnet-4 | 0.70 | 0.75 | 0.77 | 0.75 | 0.78 | 0.81 |
| gpt-4.1-2025-04-14 | 0.24 | 0.64 | 0.73 | 0.74 | 0.82 | 0.84 |
| gemini-2.5-flash | 0.31 | 0.77 | 0.66 | 0.50 | 0.82 | 0.85 |
| gpt-4.1-nano | 0.65 | 0.63 | 0.64 | 0.44 | 0.37 | 0.36 |
| gpt-4o-2024-08-06 | 0.59 | 0.58 | 0.55 | 0.38 | 0.53 | 0.69 |
| gpt-4o | 0.13 | 0.32 | 0.24 | 0.12 | 0.40 | 0.34 |
| gpt-4o-mini | n/a | 0.25 | 0.36 | 0.27 | 0.10 | 0.23 |

Table: Anchor-sweep consistency, per evaluator and axis.

*For each evaluator and axis, the mean pairwise Pearson correlation of its scores across the four anchor values (5/6/7/8). It measures self-consistency, not accuracy: the `factual` column is distinct from the factual-competence loading (Sonnet-4 reads 0.70 here but 0.13 there). gpt-4o-mini's factual entry is n/a — near-zero variance makes the correlations undefined (A10). The anchored **rating consistency** that enters $T$ (§4.7) is defined below.*

Two patterns matter. Collapse is either *uniform* — gpt-4o and gpt-4o-mini hold no stable signal on any axis — or *axis-specific*: gpt-4.1-2025-04-14 (0.24) and gemini-2.5-flash (0.31) collapse on factual while their other axes hold. Distinctness is the axis the participants find hardest to hold steady (mean 0.59). Because the factual axis is peer centrality's responsibility, council eligibility is assessed on the non-factual axes. The gate value is the **collapsed** consistency $\bar r$: the four per-archetype axis scores are averaged per unit before correlating across anchors (A11), so axis-idiosyncratic noise partially cancels and $\bar r$ reads higher than the row means above (Flash: row mean $\approx 0.70$, collapsed $0.81$).

**Rating consistency (anchored).** The anchor sweep applies the familiar LLM-judge reliability principle — a competent judge is invariant under non-semantic perturbation — to a controlled perturbation of the calibration value itself, and turns that invariance into a key-free, per-criterion gate (its place among prior reliability and anchor-selection work is §5.5). Rescaled to the anchor ($E^{C}_a = 7\,r_a/r_{a,\text{anchor}}$, so Opus-4.5 reads 7), the consistency becomes a competence on the $1$–$10$ scale, directly comparable with a generator's quality on the same criterion. The hypothesis is testable on the one axis that also carries an *independent* competence measure — factual, where the key-free error-detection loading $E^{F}$ exists: factual consistency $E^{C}_f$ and $E^{F}$ correlate at Pearson $r = 0.52$ (Spearman $\rho = 0.72$), a decent agreement that supports reading consistency as competence. The looseness is the consistency-vs-accuracy gap — a model can rate factuality consistently yet uninformatively (gpt-4.1-mini, consistency $0.87$ against competence $\approx 0.09$). [The table](#tab-per-criterion) pairs, per non-factual criterion, the **generator** competence $G$ with the **evaluator** competence $E$, both anchored to Opus-4.5 = 7, and gives their **anchored cosine** alignment — the cosine between the models' maker- and judge-deviations from the anchor point $(7,7)$, defined in Appendix A.6 (eq A15):

<a id="tab-per-criterion"></a>

| Model | beauty $G$ | beauty $E$ | intel $G$ | intel $E$ | dist $G$ | dist $E$ | len $G$ | len $E$ | struct $G$ | struct $E$ |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| ★ claude-opus-4.5 | 7.0 | 7.0 | 7.0 | 7.0 | 7.0 | 7.0 | 7.0 | 7.0 | 7.0 | 7.0 |
| claude-opus-4.1 | 7.1 | 6.8 | 7.2 | 7.0 | 7.4 | 6.0 | 6.7 | 6.5 | 7.3 | 7.6 |
| claude-opus-4.0 | 6.9 | 6.7 | 6.9 | 7.0 | 7.0 | 5.7 | 6.8 | 6.3 | 7.3 | 7.1 |
| claude-sonnet-4 | 6.3 | 6.1 | 6.3 | 6.4 | 6.5 | 6.2 | 6.1 | 6.0 | 6.4 | 6.7 |
| gemini-3.1-pro | 5.8 | 6.8 | 5.7 | 7.4 | 6.0 | 7.3 | 5.5 | 6.9 | 5.7 | 7.4 |
| gemini-2.5-flash | 5.4 | 6.2 | 5.5 | 5.5 | 6.2 | 4.2 | 5.7 | 6.3 | 5.8 | 7.0 |
| gpt-4.1-mini | 4.8 | 6.3 | 5.0 | 6.2 | 5.9 | 6.3 | 4.2 | 6.5 | 5.4 | 6.7 |
| gpt-4.1-2025-04-14 | 5.1 | 5.2 | 5.0 | 6.0 | 6.0 | 6.2 | 3.6 | 6.3 | 5.6 | 7.0 |
| gpt-4.1-nano | 3.5 | 5.1 | 3.7 | 5.3 | 4.2 | 3.7 | 3.5 | 2.8 | 3.2 | 2.9 |
| gpt-4o-2024-08-06 | 3.5 | 4.7 | 3.3 | 4.5 | 4.1 | 3.1 | 3.3 | 4.0 | 3.0 | 5.7 |
| gpt-4o | 3.4 | 2.6 | 3.4 | 2.0 | 4.7 | 1.0 | 2.6 | 3.1 | 3.2 | 2.8 |
| gpt-4o-mini | 3.5 | 2.1 | 3.5 | 3.0 | 3.3 | 2.3 | 3.8 | 0.8 | 3.0 | 1.9 |
| **cos(G,E)** | **0.91** | [.83,.95] | **0.90** | [.80,.93] | **0.89** | [.82,.92] | **0.84** | [.80,.87] | **0.87** | [.86,.87] |

Table: Per-criterion generator quality (G) vs evaluator reliability (E).

*Per criterion: $E$ = evaluator rating consistency (the anchored consistency of [the consistency table](#tab-criterion-b), rescaled to 1–10) and $G$ = generator quality — the council's leave-self-out mean on that axis, **each member's vote weighted by its own reliability $E$ there** (eq A12b; the same weighting §4.7 applies to $G^{C}$), so $E$ both scores the judge and sets its weight in $G$. Both anchored to claude-opus-4.5 (★) = 7. $\cos(G,E)$ = cosine of each model's deviation from $(7,7)$ across the participants, 95% CI from the A.5 joint bootstrap; 1 = making and judging perfectly aligned. Higher $G$ = better generator; higher $E$ = more stable evaluator.*

On all five non-factual criteria, generation and evaluation move together (anchored cosine $0.84$–$0.91$): a model that generates well on a criterion also tends to hold a stable standard when judging it. Evaluating and generating are largely one capability on the aesthetic and structural axes — the counterpoint to the factual axis, where the two come apart (§4.8): the dissociation is specific to judging truth.

**Authority vs consistency.** Peer centrality runs on the subjective axes too: one SVD per non-factual axis yields an **authority** rating — each judge's alignment with the participants' collective taste. The comparison is between two literatures: spectral competence descends from the label-free aggregators (Dawid & Skene 1979; Parisi et al. 2014), consistency from the judge-reliability line (§5.5). Run on the same matrix, the two agree where §5.2 predicts and part where it predicts. On the five subjective axes they correlate at Pearson $0.70$–$0.90$; on factual — the one axis with a truth to be right about — they diverge ($0.50$, CI $[-0.08, 0.84]$ — the $E^{C}_f$-vs-$E^{F}$ comparison above; the per-axis factual SVD differs slightly from the pooled $E^{F}$, hence 0.50 against 0.52), because only there can a judge be stable yet wrong. The divergences are §5.2's anatomy in action: consistency credits a judge's whole stable standard, personal taste included, penalising only flimsiness; authority credits the collective share alone — so stable-but-partly-private judges drop under authority (Spearman between the twelve orderings 0.83; per-evaluator values in the reproduction package). Council membership is invariant to the choice: the top five by either estimator are the five seats. Substituting authority for consistency in the total (all other components unchanged) preserves the ordering (Spearman $0.986$) with one headline change: authority is not bounded by the anchor's own loading, so gemini-3.1-pro's total ($7.86$) overtakes the pinned $7$. The official rating uses consistency; authority is reported here as the disclosed alternative, because adopting it inside $T$ would convert alignment into authority on axes where no truth licenses the conversion (§5.2).

**Constituting the initial council.** The participants certify their own reliable subset from internal evidence alone — a bootstrap in the epistemic sense: no production score, no external key. We keep the selection **fully key-free**: a reliable evaluator must show factual competence — a key-free SVD loading clear of the inert band — *and* rating consistency (collapsed across the four per-archetype non-factual axes, $\bar r \ge 0.78$, Pearson; structural diversity, rated once per portfolio, sits outside the collapse). Five evaluators clear both bars: Gemini 3.1 Pro, Claude Opus 4.5, Gemini 2.5 Flash, Claude Opus 4.0 and Claude Opus 4.1, whose factual-competence loadings (0.28–0.58) separate from the inert band and whose rating consistency clears the floor. Claude Sonnet-4 is the marginal case the other way: its loading (0.13) is the boundary case — its 95% interval touches gpt-4.1-mini's below, so the decisive cut falls after the top five (§4.2) — and it does not clear the factual bar — even though its consistency is comfortable (0.84). Gemini 2.5 Flash is the weakest seat: its loading (0.37) clears the band, but its rating consistency ($\bar r = 0.81$) is the lowest of the five and the closest to the floor — its interval [0.75, 0.86] straddles the bar — a caveat we carry in the open. The council is seated on the factual axis because it is the one axis where competence is objective — agreement there is licensed to mean truth (§5.2) — with rating consistency as the accompanying bar: a factually competent judge must also hold stable standards to sit. [The five members](#tab-initial-council):

<a id="tab-initial-council"></a>

| Council member | Factual competence [95% CI] | Rating consistency [95% CI] |
|---|---:|---:|
| gemini-3.1-pro | 0.58 [0.56, 0.60] | 0.94 [0.92, 0.96] |
| claude-opus-4.5 | 0.55 [0.54, 0.58] | 0.93 [0.89, 0.96] |
| gemini-2.5-flash | 0.37 [0.31, 0.40] | 0.81 [0.75, 0.86] |
| claude-opus-4.0 | 0.35 [0.32, 0.35] | 0.85 [0.80, 0.89] |
| claude-opus-4.1 | 0.28 [0.27, 0.30] | 0.87 [0.82, 0.91] |

Table: The initial council — the five reliable evaluators.

*The five evaluators that clear both reliability bars: factual competence (SVD loading clear of the inert band) and rating consistency (leave-self-out, collapsed across the four per-archetype non-factual axes, $\bar r \ge 0.78$). Values are the key-free competence scores with 95% bootstrap CIs over the (submission, archetype) grid. These five form the council that issues the official ratings (§4.7); the other seven evaluators carry no weight in any other model's rating — each is an evaluator only in its own contest (§4.7).*

The council size — five — follows from the key-free bars; the seven excluded evaluators carry no weight in the official rating.

gpt-4.1-mini is the clean demonstration that the two estimators are independent. It scores respectably as a generator and is stable across every axis (0.75–0.87), so on several fact-adjacent numbers it looks strong; yet the factual-competence measure leaves it short of clearing the inert band (loading ≈ 0.09). A precise rater need not be an informative one: the spectral estimator separates a self-consistent instrument from one whose judgements track the participants' shared factual signal, which is exactly why both bars are required (the consistency-vs-competence gap is quantified above).

### 4.5 Council rotation

The council must stay current: models improve, and a council fixed at selection reports on a field that has moved past it. The seats are therefore contestable: the initial council was seated on evaluator competence (§4.4), and from here on seats are won and lost on the total rating $T$. Any model may nominate itself as a **contestant**, and a non-competing **administrator** administers its contest. Because a model's evaluator competence exists only inside an evaluation matrix (§4.2), no model can be rated as a bystander: to be rated is to enter the ongoing game as a contestant alongside the five seats. Every request for an official rating is automatically a contest for a seat, and most contestants simply fall short and keep their rating.

The contestant plays both roles: it submits a portfolio (§3.2) and evaluates the incumbents' portfolios and the ballast, while the seats score its portfolio. The administrator computes the ratings exactly as the official definitions of §4.7 prescribe — not the bootstrap's twelve-evaluator arithmetic, which was selection evidence only. Anchor and ballast are the same frozen ones as always (§4.6; the anchor is raised by the recalibration rule of §5.3 when the field outgrows it). Winning a seat takes one thing: a total $T$ higher than the lowest seat's, by a margin the bootstrap can resolve — point estimates alone would churn the roster on noise. The winner takes the seat; the model rotated out keeps its leaderboard history; the administrator recomputes on the new roster and records the contest. The bar sits on $T$ for a reason: half of $T$ is owned by the sitting consensus ($E^{F}$, $G^{F}$) and half is not ($E^{C}$ is a judge's own steadiness; $G^{C}$ lets strong minority support count), so a justified dissenter pays the consensus penalty on only half the score (§5.8).

Two **guards**, read off the contest's own matrix and reported with every result, say whether the factual axis exists to be measured: the separation $\sigma_1/\sigma_2$ must sit in its band (2.0–5.0), and the seats' $E^{F}$ must spread enough to rank (more than 2.5 points; both sized in §4.6). If either fails, the contest abstains — no rotation. No seat has yet been contested: the mechanism is specification, sized in §4.6 and awaiting its first contestant. The steady-state roster may depend on the order in which contestants arrive — a property of standing institutions, and one the provenance record preserves.

---

### 4.6 The ballast

A contest convenes the top of the field — five seats and one contestant — and with the weak submissions gone, the factual axis breaks: the seats' anchored $E^{F}$ come out wrong in scale and wrong in order, swinging by up to 9.2 points depending on who the contestant is (anchored $E^{F}=7f/f_a$ is not confined to the 1–10 rubric when the axis breaks). The **ballast** repairs this: the weakest archived submissions, added to the contest's graded set. Two suffice ([the heatmap](#fig-ballast)).

<a id="fig-ballast"></a>

![Each seat's anchored evaluator factual competence $E^{F}$ under contests with 0–3 ballast blocks (mean over the seven possible contestants), beside the reference from all 12 participants (§4.2). Council alone, the column is scrambled; from two ballast on, the contest reproduces the reference (mean $|\Delta|$ 0.33 over the seven contests, and the same seat is lowest in all seven). The boxed column is the protocol's configuration. Sized by re-analysis of the pinned run — a contest is a sub-matrix of the bootstrap, so no new generation is needed. Reproduced by `scripts/ballast_sizing.py`.](figures/ballast_heatmap.png)

Why two and not one: a single block is the contest's only substantial error source, so the axis narrows toward *did this judge notice the one bad portfolio* and the §4.5 guards fail in 7% of bootstrap resamples. Two blocks carry two independent error patterns; the guards hold in every resample, $\sigma_1/\sigma_2 = 2.99$ with both interval ends inside the band. A third changes nothing and costs twenty-five more columns of grading.

Two scope notes. The sizing holds on runs 1 and 2; on run 3 (§4.9) the guards fail at every ballast size — that run's separation is 1.28, the factual axis is not identified, and no column set can stabilise a measurement that was never there: the §4.5 abstention behaving as intended. And the ballast fixes what the evaluators are measured *on*, not what they can see (§5.8).

### 4.7 Total rating and the official leaderboard

The benchmark's two ratings combine into one official total, and each splits the same way — into a **factual** and a **criterion** half. On the generation side: the generator's factual competence $G^{F}$ (the SVD generation factuality of §4.2) and its criterion quality $G^{C}$, the council's leave-self-out mean of the five non-factual generation axes. In $G^{C}$, each seat's vote is weighted by its own rating consistency on that axis — no firm standard, little weight. On the evaluation side: $E^{F} = 7\,f/f_a$ and $E^{C} = 7\,\bar r/\bar r_a$ (§4.2, §4.4), the SVD factual competence and the leave-self-out collapsed rating consistency, both placed on the rubric by the convention already used for generation, **the anchor model scores 7**. Each side is the mean of its two halves, $G = \tfrac12(G^{F}+G^{C})$ and $E = \tfrac12(E^{F}+E^{C})$, and the two sides weigh equally. The total is therefore the mean of four anchored components — a symmetric $2\times2$ of {generator, evaluator} $\times$ {factual, criterion} (Appendix A.4):

$$T \;=\; \tfrac{1}{2}\big( G + E \big) \;=\; \tfrac{1}{4}\big( G^{F} + G^{C} + E^{F} + E^{C} \big). \tag{2}$$

The **[final leaderboard](#tab-final-leaderboard)** ranks all twelve models by $T$. Every rating is issued against the fixed anchor (claude-opus-4.5, pinned at 7), so the anchor reads 7 on $T$, $E$ and $G$ alike. Every number in the official rating is **council-issued**: each model is rated by the council when it stands as contestant (§4.5) — the five seats, joined by the model itself when it holds no seat, grading the incumbents' portfolios, the two ballast submissions, and the contestant's own — leave-self-out throughout: no evaluator's ratings of its own portfolio enter its scores. The twelve-evaluator matrix of §4.2–§4.4 is *selection* evidence only — the roster is an output of the bootstrap, so it cannot also produce the official rating — and the two bases agree closely (Spearman 0.986, mean absolute difference 0.12, the same five seats either way).

<a id="tab-final-leaderboard"></a>

| Rank | Model | Council | **$T$ [95% CI]** | $E$ | $G$ |
|---|---|:--:|---:|---:|---:|
| 1 | ★ claude-opus-4.5 (anchor) | council | **7.00 [7.00, 7.00]** | 7.00 | 7.00 |
| 2 | gemini-3.1-pro | council | **6.65 [6.53, 6.80]** | 7.14 | 6.16 |
| 3 | claude-opus-4.0 | council | **6.04 [5.73, 6.39]** | 5.12 | 6.96 |
| 4 | gemini-2.5-flash | council | **6.03 [5.20, 6.53]** | 5.93 | 6.14 |
| 5 | claude-opus-4.1 | council | **5.92 [5.59, 6.30]** | 4.78 | 7.06 |
| ⎯⎯ | ⎯⎯ | ⎯⎯ | ⎯⎯ | ⎯⎯ | ⎯⎯ |
| 6 | claude-sonnet-4 | — | **5.22 [4.92, 5.47]** | 3.80 | 6.64 |
| 7 | gpt-4.1-mini | — | **4.88 [4.15, 5.58]** | 4.16 | 5.60 |
| 8 | gpt-4.1-2025-04-14 | — | **4.44 [4.24, 4.67]** | 3.11 | 5.78 |
| 9 | gpt-4.1-nano | — | **3.42 [2.74, 3.87]** | 3.39 | 3.45 |
| 10 | gpt-4o-2024-08-06 | — | **3.34 [3.01, 3.61]** | 2.43 | 4.25 |
| 11 | gpt-4o | — | **2.85 [2.38, 3.22]** | 1.48 | 4.21 |
| 12 | gpt-4o-mini | — | **2.10 [1.75, 2.46]** | 1.17 | 3.02 |

Table: Final leaderboard — total rating $T$ (95% CI) with its evaluator half $E$ and generator half $G$, all twelve models ranked; council seats marked. Every rating is council-issued: each model is rated by the five seats — joined by the model itself when it holds no seat — over the incumbents' portfolios, the ballast, and its own. The anchor (claude-opus-4.5) is 7 by construction. Adjacent ranks are resolved (non-overlapping intervals) only at 1–2, 2–3, 5–6 and 8–9; the remaining adjacent pairs are statistical ties.

Each half resolves into [two anchored competences](#tab-competence-breakdown) — generation: generator factual $G^{F}$ (§4.2) and criterion $G^{C}$ (the five non-factual generation axes, §4.7); evaluation: evaluator factual $E^{F}$ (§4.2) and criterion $E^{C}=7\bar r/\bar r_a$ (the leave-self-out collapsed anchor-sweep consistency, §4.4):

<a id="tab-competence-breakdown"></a>

| Rank | Model | Council? | $G^{F}$ | $G^{C}$ | $E^{F}$ | $E^{C}$ |
|---|---|:--:|---:|---:|---:|---:|
| 1 | ★ claude-opus-4.5 (anchor) | council | 7.00 | 7.00 | 7.00 | 7.00 |
| 2 | gemini-3.1-pro | council | 6.58 | 5.75 | 7.27 | 7.01 |
| 3 | claude-opus-4.0 | council | 6.94 | 6.98 | 3.83 | 6.41 |
| 4 | gemini-2.5-flash | council | 6.54 | 5.73 | 5.34 | 6.52 |
| 5 | claude-opus-4.1 | council | 6.95 | 7.16 | 3.10 | 6.47 |
| ⎯⎯ | ⎯⎯ | ⎯⎯ | ⎯⎯ | ⎯⎯ | ⎯⎯ |
| 6 | claude-sonnet-4 | — | 6.96 | 6.31 | 1.48 | 6.13 |
| 7 | gpt-4.1-mini | — | 6.15 | 5.05 | 1.36 | 6.97 |
| 8 | gpt-4.1-2025-04-14 | — | 6.50 | 5.05 | 0.00 | 6.23 |
| 9 | gpt-4.1-nano | — | 3.27 | 3.64 | 0.35 | 6.43 |
| 10 | gpt-4o-2024-08-06 | — | 5.07 | 3.43 | 0.36 | 4.51 |
| 11 | gpt-4o | — | 4.97 | 3.46 | 0.36 | 2.61 |
| 12 | gpt-4o-mini | — | 2.61 | 3.43 | 0.00 | 2.34 |

Table: Competence breakdown — the four anchored components behind each model's evaluator ($E$) and generator ($G$) scores.

*($G^{F}$, $E^{F}$ are §4.2's anchored factual competences, computed on each model's contest; $G^{C}$ the council consistency-weighted leave-self-out mean of the five non-factual generation axes; $E^{C}=7\bar r/\bar r_a$ the collapsed rating consistency over the contest's graded set. All quantities are carried unrounded to the last step; the $T$ interval is the per-contest A.5 joint bootstrap (a CI device only). Two scope notes. Inert-band factual loadings are construction-sensitive — printed to two decimals for arithmetic, not asserted precision — and the ordering of ranks 9–11 does not rest on them: those models' totals separate on the other components, chiefly $E^{C}$. And contest-basis $E^{C}$ reads higher for inert-band models than the consistency table (gpt-4.1-mini 6.97): the contest's graded set is an easier consistency test than the full field. The council gate is untouched — it reads the twelve-evaluator consistency — but a quarter of a non-council model's total rests on this easier test, a caveat for ranks 6–12.)*

Three readings. **The top five are the council.** The five reliable evaluators occupy the top five totals; the anchor leads by construction, and Gemini 3.1 Pro is second on the strength of its factual judging despite mid-pack generation. **The cliff is in the evaluation, not the generation.** Models with little factual competence sink regardless of how well they generate — Sonnet-4's top-tier generation still leaves it at rank 6; a quarter of the total is error detection, and it is what production cannot buy (§5.4's independence thesis made quantitative). **Generation and evaluation do not coincide.** The strongest generators — the three Opus models — are middling factual judges ($E^{F}$ 3.1–3.8, the pinned anchor aside), while the strongest judge, Gemini 3.1 Pro ($E^{F}=7.27$), generates mid-pack. A model can top one half of the benchmark and not the other — which is what makes a two-part total worth reporting.

**The sitting council is consistent with the board it issues.** The five members were seated on evaluator competence alone (§4.2), because no council yet existed to rate production; a future candidate instead wins its seat on the total $T$ (§4.5). On this run the two perspectives agree: the five seats occupy the top five totals. The benchmark is consistent in whom it trusts.

### 4.8 The metanym benchmark vs GPQA

We test the key-free rating against an instrument built outside the run: GPQA Diamond (Rein et al. 2023; 198 expert multiple-choice questions with a human answer key), put to the same twelve models, through the same gateway, under the same protocol — Temperature=0, reasoning and tools off — and scored against the key (administration details, including a void-retry pass, in Appendix D.2). We correlate GPQA accuracy with one quantity: the official total $T$ (§4.7). [The scatter](#fig-gpqa-scatter) plots the twelve models; [the table](#tab-gpqa-values) lists them.

<a id="fig-gpqa-scatter"></a>

![The official total rating $T$ (§4.7, council basis) against self-administered GPQA Diamond accuracy, twelve models. Pearson $r = 0.97$ (95% bootstrap CI $[0.92, 0.99]$ — Appendix D.1), Spearman $\rho = 0.93$. Filled markers are council seats; horizontal bars the A.5 bootstrap 95% CI on $T$, vertical bars the GPQA binomial 95% CI; the shaded band is the confidence band of the fitted line, not a prediction interval. The blue star is the anchor (opus-4.5): $T = 7$ by calibration, GPQA measured independently, so it is a legitimate point; excluding it leaves Pearson at 0.97. The audit behind this figure is Appendix D.](figures/total_validation.png)

<a id="tab-gpqa-values"></a>

| Model | $T$ | GPQA Diamond (%) |
|---|---:|---:|
| ★ claude-opus-4.5 (anchor) | 7.00 | 78.79 |
| gemini-3.1-pro | 6.65 | 80.81 |
| claude-opus-4.0 | 6.04 | 71.21 |
| gemini-2.5-flash | 6.03 | 72.22 |
| claude-opus-4.1 | 5.92 | 76.77 |
| claude-sonnet-4 | 5.22 | 72.22 |
| gpt-4.1-mini | 4.88 | 63.13 |
| gpt-4.1-2025-04-14 | 4.44 | 61.62 |
| gpt-4.1-nano | 3.42 | 55.05 |
| gpt-4o-2024-08-06 | 3.34 | 46.46 |
| gpt-4o | 2.85 | 48.48 |
| gpt-4o-mini | 2.10 | 43.94 |

Table: The two instruments side by side — the key-free total rating $T$ (§4.7) and self-administered GPQA Diamond accuracy (voids counted as wrong), sorted by $T$ — the per-model values behind the family-order comparisons of §5.1.

**A key-free benchmark replicates a keyed one.** GPQA Diamond is an established benchmark; ours is not — and the two could hardly be more different. One has professors writing expert-level multiple-choice questions — quantum mechanics, organic chemistry, molecular biology — scored as the percentage answered correctly against their key. The other has LLMs inventing sets of analogies and subjectively rating one another's, with no correct answer anywhere in the loop. Different item authors, different task, different scoring, different notion of truth — yet $T$ reproduces GPQA's ordering at Pearson $r = 0.97$ $[0.92, 0.99]$ (Spearman $0.93$), stable under regeneration ($0.97/0.97/0.92$; §4.9). A benchmark with no key replicates one built entirely of keys — and it needs no experts to write items and no revision to keep pace with improving models (§5.3). Since GPQA is no golden key, the corroboration runs both ways: the concordance makes it improbable that either instrument sits far from the truth (§5.7).

**The number survives an audit.** A correlation that strong between a key-free peer rating and an externally keyed benchmark invites the suspicion of a leak, and we audited for one rather than celebrating. No key ever enters a prompt; every published accuracy re-derives exactly from the shipped raw per-question artefacts; the shuffled key is balanced; an independently written answer-extractor reproduces the verdicts; and rescoring under a strict extraction rule moves the correlation by $0.007$. We find no leak, and the number's anatomy is unremarkable in hindsight: four noisy reads of capability with near-independent noise, averaged. The agreement is not carried by the field's two-cluster structure — it holds at $r = 0.91$ within the leading eight alone. $T$ is also the right quantity to report: it is the benchmark's official total, defined before any GPQA comparison — any other combination would be selected for its correlation at $n=12$ — and every quarter earns its place (dropping even the weakest lowers the agreement, Appendix D.1). The full audit, the raw data, and the comparison with publicly reported GPQA values (higher, because reasoning-on) are in Appendix D.

**The two halves of $T$ do not coincide.** Making a true claim and spotting a false one are different skills (West et al. 2024; Oh et al. 2024; Li et al. 2024), and the benchmark rates them separately (§4.7): the Gemini models rank higher as judges than as makers, the Claude models the reverse (sharp for gemini-3.1-pro and sonnet-4; the rest within the error bars). This breaks the assumption behind key-free peer rankers like PiCO (Ning et al. 2025) and UPME (Zhang et al. 2025), which treat a strong maker as a strong judge.

### 4.9 Robustness to regeneration

The leaderboard of §4.7 rests on one portfolio per model. To check that the result is not an artefact of that single draw, we re-ran the full pipeline three times, each run regenerating all twelve portfolios at T=0 and re-scoring them against the frozen anchor. The regeneration is substantive: the gateway is not deterministic at T=0, eleven of twelve portfolios differ between runs, and a total can move by as much as 1.1 between the two same-day runs (gpt-4.1-2025-04-14, 4.62→5.72) and 1.45 across all three (gemini-3.1-pro).

The benchmark's categorical output is robust to this, its ordinal output largely so: the council is **identical** across all three runs, and [the ranking is broadly preserved](#tab-reruns) — pairwise Pearson 0.92–0.96, Spearman 0.84–0.90. In runs 2 and 3 gemini-3.1-pro's total (7.35, 8.10) exceeds the anchor's pinned 7.00: the anchor's first place is a calibration convention, not a measured victory — a standing result of this kind is what the anchor-replacement rule exists for.

<a id="tab-reruns"></a>

| Model | $T_1$ | $T_2$ | $T_3$ | SD |
|---|--:|--:|--:|--:|
| ★ claude-opus-4.5 | 7.00 | 7.00 | 7.00 | 0.00 |
| ★ gemini-3.1-pro | 6.65 | 7.35 | 8.10 | 0.72 |
| ★ claude-opus-4.0 | 6.04 | 5.50 | 6.26 | 0.39 |
| ★ gemini-2.5-flash | 6.03 | 5.84 | 4.78 | 0.68 |
| ★ claude-opus-4.1 | 5.92 | 6.77 | 6.19 | 0.43 |
| claude-sonnet-4 | 5.22 | 5.82 | 6.16 | 0.47 |
| gpt-4.1-mini | 4.88 | 5.93 | 4.93 | 0.59 |
| gpt-4.1-2025-04-14 | 4.44 | 4.62 | 5.72 | 0.69 |
| gpt-4.1-nano | 3.42 | 3.55 | 2.72 | 0.45 |
| gpt-4o-2024-08-06 | 3.34 | 3.08 | 3.63 | 0.27 |
| gpt-4o | 2.85 | 2.76 | 2.93 | 0.09 |
| gpt-4o-mini | 2.10 | 2.25 | 1.60 | 0.34 |

Table: Total rating $T$ across three full re-runs (run 1 = the bootstrap generation, re-analysed on the council basis; runs 2–3 the same day, two hours apart), all on the council basis of §4.7. ★ marks a council seat — the five seats are identical across all three runs. SD is the per-model run-to-run standard deviation (mean 0.43, max 0.72, the two Gemini seats and gpt-4.1-2025-04-14 highest). Run 3's $E^{F}$ quarter is read off a factual axis the §4.5 guard (sized in §4.6) reports as unidentified ($\sigma_1/\sigma_2 = 1.28$); its totals carry that caveat.

The cardinal totals carry wider uncertainty than the within-run bootstrap conveys: the run-to-run SD of $T$ is 0.43 on average (max 0.72), and several totals move beyond their within-run interval between runs — the bootstrap measures dispersion within *one* generation, not the generation being itself a random draw. The benchmark's reliable products are council membership and rank order, not the precise total.

External validity holds where the factual axis is identified, and weakens exactly where the benchmark's own diagnostic says it should. The total rating tracks GPQA Diamond at Pearson 0.92–0.97 (Spearman 0.88–0.95) across the three runs; the dip is run 3, the same run whose factual axis §4.6 reports as not identified at full strength ($\sigma_1/\sigma_2 = 1.28$; per-run detail in Appendix D.1).

## 5. Discussion

### 5.1 A benchmark by LLMs, for LLMs

The aim is a benchmark that needs nothing outside itself: models invent the test, sit it, grade it, and certify which of them are fit to grade — no human raters, no gold key, no oracle model. LLM-as-judge already removes the human rater (Zheng et al. 2023; Liu et al. 2023; Verga et al. 2024; Bai et al. 2023); the unsupervised peer-evaluation line removes the gold key (§5.5). What is new here is self-containment: the participants author the very items they judge, so the test refers only to itself, and one decomposition scores the models as both makers and judges.

The metanym benchmark correlates excellently with GPQA, and GPQA is no golden key: both occasionally reverse the expected order within a model family, mostly within the error margins — GPQA ranks Claude-sonnet-4 above Claude-opus-4.0 (within noise) where the metanym benchmark places opus above sonnet at resolution; both rank gpt-4.1-mini above gpt-4.1, inside the margins. 

Both benchmarks raise resolution by adding items, but only the metanym benchmark does it easily: GPQA needs domain experts writing and re-validating new Google-proof questions; the metanym benchmark twists a knob — the number of archetypal contexts per submission (here five).

### 5.2 Two self-consistencies, two yardsticks

With no outside ruler to appeal to, the yardsticks must come from the system's own structure — the two estimators of §4.2. What this section adds is *why* the split falls where it does. The factual estimator's one assumption — *the only thing competent evaluators share is the truth* — holds for facts and fails for taste. On **beauty**, the dominant axis of agreement is not truth but shared convention (house style, training data), so weighting by it would *launder conformity into competence*: the evaluator nearest the mean is rewarded, and a legitimate minority view is penalised. The subjective criteria therefore use rating consistency, and that test has teeth precisely because the anchor shift is non-semantic. If merely moving the calibration point reorders how a model rates the same items, it has no firm grip on what it is judging; a stable standard is the whole of what competence means where no external truth exists.

The two routes also differ in what they resolve a taste rating *into*. The anchor sweep separates each evaluator's stable standard into its alignment with the participants' one **collective taste** and its **personal taste deviation** — the reproducible remainder the other participants do not share; what fails to reproduce across the sweep at all is flimsiness, measurement noise rather than taste, and belongs in the intervals. The deviation is real: every council seat carries a small one (9–16% of its stable standard, bootstrap intervals clear of zero). The split also separates two kinds of weak judge a single number conflates: gpt-4o and gpt-4.1-nano hold no reproducible taste at all — their deviation intervals include zero — while gpt-4o-mini, the field's least consistent judge (§4.4), still shows a faint reproducible remainder, 69% [54, 81] of it private. Consistency scores the second kind for the standard it does hold; an eigenmode weighting would read a stable heterodox standard and no standard as the same non-agreement — and because the taste eigenvector would also set each evaluator's weight in the very consensus it is scored against, adopting it would convert alignment into authority. The factual axis earns that conversion; taste does not. The two estimators are compared head-to-head in §4.4.

### 5.3 A sustainable yardstick

The benchmark yardstick is calibrated on the *anchor submission* (here Claude-opus-4.5's) and the official ratings are set by the council; the analysis is fully deterministic (§4.3), so anyone can re-derive every rating from the archived evaluations and re-score an archived submission against the same anchor. 

What varies over time is the anchor submission and the council. Older ratings can be converted to approximate a newer standard; to keep the chain from drifting, each conversion is recalibrated against the archived original anchors rather than only the latest inherited factor. An updated official rating is issued by the sitting council.

The council can also grow. We seat five because only five clear the factual-competence bar — the natural sixth, Sonnet-4, generates well but judges facts in the inert band. The council is supply-limited by competence, not by design.

### 5.4 Generating vs evaluating the truth
 
Generating and evaluating factual truth are different abilities, and the council measures both and keeps them apart (§4.2). A benchmark that scored only generation would miss judging competence, the very thing the council gate selects on. The separation, not just the rating, is what lets the participants pick judges rather than only rank makers.

### 5.5 Where this sits: intelligence tests and peer-evaluation methods

Two axes locate the metanym game: *what intelligence it tests* and *how self-contained the apparatus is*. Prior work tends to be strong on one and weak on the other — the analogy benchmarks hit the target but need an external key; the unsupervised peer-evaluation methods are key-free but aim at general capability rather than a defined, falsifiable operation.

**As an intelligence test**, the game probes the abstraction-and-analogy cluster a long tradition places at the centre of thinking (Gentner 1983; Hofstadter & Sander 2013; Penn, Holyoak & Povinelli 2008; Chollet 2019; Mitchell 2021), and it probes it harder. The classical instruments — BIG-Bench analogy items, Webb, Holyoak & Lu (2023), Lewis & Mitchell (2024), ARC-AGI (Chollet 2019) — test one mapping over one domain pair per item, in a *recognition* frame; the metanym game asks for many coupled slots across several unrelated domains, built from scratch and falsifiable per sentence (§5.6). Recognition instruments *select* a mapping, and the analogy-generation literature *produces* one but grades it holistically; the metanym game is the first to make analogical *production* falsifiable sentence by sentence. That property does double duty — it is what lets the test be scored without a key, and **none of the prior instruments is self-contained**: every one scores against gold labels (BIG-Bench, ARC-AGI) or paid human raters (Webb-Holyoak-Lu), so none can run, let alone improve, without an external oracle.

**As a self-contained method**, the council sits in the *unsupervised peer-evaluation* line — and that line already removes the gold key, so removing it is not what we add. Single-judge protocols (MT-Bench; G-Eval, Liu et al. 2023) score against a reference; PoLL (Verga et al. 2024) adds a panel but trusts it as given; LLM-as-Examiner (Bai et al. 2023) lets the examiner write the questions; most directly, PiCO (Ning et al. 2025) lets unlabelled models answer and grade one another and recovers an ability ordering from peer agreement alone (UPME, Zhang et al. 2025, extends the idea to vision-language). We add two things those methods lack. *First*, they apply one consensus mechanism to every dimension, which on subjective criteria rewards the model nearest the mean — the mainstreaming §5.2 refuses; we weight by agreement only where agreement is licensed to mean truth, and use rating consistency elsewhere. *Second*, they grade pre-existing questions, where ours is a purpose-built, per-sentence-falsifiable production task — and the council certifies and re-contests its own judges (§4.5) rather than trusting the panel as given. The estimator is the sharper break: PiCO fits one ability parameter per model by consistency optimization, not a spectral method. Spectral aggregation has its own label-free lineage — Parisi et al. (2014) read predictor competence off the leading eigenvector of their covariance, Dawid & Skene (1979) the EM antecedent — but that lineage is *one-sided*: its predictors classify a fixed external dataset, so there is no generator to score. Our columns are authored by the same agents on the rows, so the matrix is *two-sided*: one graded SVD (§4.2) reads evaluators off the left singular vector and generators off the right, and the generation–evaluation gap (§4.8) is definable only because the test is self-produced. To our knowledge the spectral route has not been applied to LLM peer evaluation.

Two of our components have their own recent literature, and we use them rather than claim them. *Rating consistency* applies the standard judge-reliability principle — a competent judge is invariant under non-semantic perturbation — to a sweep of the calibration value. Invariance has been used to gate judges on criteria with a latent truth (Policy Invariance, Weng et al. 2026) or as a general diagnostic (JudgeSense, Bellibatlu et al. 2026). We use it to certify competence on subjective, ground-truth-free criteria, where a stable standard is the only competence there is to measure — to our knowledge a new use. And anchor *choice* is studied by Don-Yehiya et al. (2026), who find the anchor should track the capability of the cluster under comparison and rise as the field improves — our recalibration rule (§5.3). Their caution about a top anchor does not bite here: the bootstrap winner is pinned at 7 with headroom above, scored cardinally, and anchoring doubled the resolution F-statistic (§4.2).

The two axes meet in one sentence. Prior work offers either a test of this intelligence that needs an external key, or a key-free evaluation method aimed at general capability rather than a defined cognitive operation. The metanym game is the only one that is both — a structural-intelligence test that certifies its own ground.

### 5.6 Measuring general intelligence without ground truth

What would a benchmark for general intelligence have to test? There is no consensus definition to consult, so what follows is a hypothesis — offered for discussion, falsifiable in its parts. Hughes et al. (2024) give an operational answer: a generally intelligent system must be *open-ended* — producing novel artefacts that an observer judges learnable. Two abilities, not one: making new things, and judging them. A benchmark for general intelligence must test both. Most benchmarks test neither — they test answering, against questions and keys that someone else made.

The metanym game tests both, and broadly. Playing demands at least eight constructs that cognitive science treats as central to intelligence, abstraction and analogy above all — one wide cluster, not the whole of it (perception, motor skill, working memory, and social intelligence the game leaves alone):

1. **Higher-order relational reasoning** (Penn, Holyoak & Povinelli 2008) — recognising that two situations share the same pattern of relations among their parts even when the parts are unrelated. Each slot is defined by its relations to the other slots, not by its filler word; successful substitution shows the pattern survives.
2. **Structure-mapping** (Gentner 1983; Falkenhainer, Forbus & Gentner 1989) — the metanym table is the structure-mapping bookkeeping written down: mechanical substitutability enforces one-to-one correspondence and parallel connectivity, while systematicity is judged rather than assumed (the `intelligence` axis).
3. **Essence-seeing** (Hofstadter & Sander 2013) — spotting that a novel situation is an instance of a known abstract pattern: seeing the archetypal context behind the template.
4.–5. **Fluid and crystallised intelligence** (Cattell 1963; Horn & Cattell 1966) — reasoning out a novel structure on the fly, and knowing the vocabulary and domain facts that make every substituted sentence true.
6.–7. **Convergent and divergent production** (Guilford 1967) — substitution admits no near-misses, a sentence passes or fails; and the same template must travel to widely different domains, each with its own metanym set.
8. **Theory formation by analogy** (Hesse 1963; Boyd 1979) — each archetypal context is theory construction in miniature: the template is the root analogy, each parallel context extends it into new territory, and factuality is the empirical test.

[The table](#tab-constructs) maps each construct to the two tasks that call on it (● marks a primary demand):

<a id="tab-constructs"></a>

| Construct | Generation — invent the template | Evaluation — judge a portfolio |
|---|---|---|
| Higher-order relational reasoning | ● lay out the relational skeleton | ● check the relations survive |
| Structure-mapping | ● the slots-and-domains scaffold | ● verify one-to-one correspondence |
| Essence-seeing (analogy as core cognition) | ● see the archetype behind the surface | |
| Fluid intelligence | ● reason out a novel structure | |
| Crystallised intelligence | ● supply true domain terms and facts | ● detect false claims |
| Convergent production | | ● pass/fail, no near-misses |
| Divergent production | ● invent a structure that travels | |
| Theory formation by analogy | ● template = root analogy, tested by fact | |

Table: The eight cognitive-science constructs the metanym game demands, mapped to its two tasks.

Breadth matters because general ability is, empirically, what broad batteries measure — across 591 language models and twelve diverse tests, a single general factor explains about two thirds of performance variance (Ilić & Gignac 2024). The total rating behaves the way a broad battery should: it tracks GPQA Diamond, a keyed test built on entirely different principles, at $r = 0.97$ (§4.8) — the simplest reading is that both instruments load on the same general factor.

The deeper requirement is subjectivity — and it is the one this benchmark is built around. Every rating here is a model's own: no definition of beauty or intelligence is supplied, and each judge rates on its personal understanding (§3.2). That is not a concession; it is how the construct has always worked. Intelligence has no ground truth and never did. Psychology's own definition is an aggregate of individual conceptions: Neisser (1979) showed "intelligent" is a prototype assembled from people's judgements, and Sternberg et al. (1981) measured the construct by pooling personal ratings. Objectivity itself, in the philosophy of science, is constituted not by the absence of subjectivity but by a community holding individual judgements to mutual criticism under shared standards (Longino 1990). The benchmark mechanises exactly this collective–individual link. Individually, a judge must know its own mind: a firm standard, stable as the tare shifts. Collectively, the community turns those held standards into one measure: trust flows to the judge the other trusted judges agree with. Intelligence, measured this way, is the two-sided capacity the link demands — to hold a standard of one's own and to build a shared one with others — and that, we suggest, is the part of general intelligence that answering someone else's questions can never test.

The hard part is not breadth. It is that general intelligence outgrows its examiners: a keyed test stops working when the field passes the key-makers, human raters when the work exceeds their judgement. Past that point every rating must come from a judge whose competence must itself be rated — by another judge, with no oracle behind the chain. This regress is the measurement problem of the AGI regime, and the benchmark cuts it twice. Where truth exists, peer centrality cuts it (§4.2): a judge is certified by its agreement with other trusted judges, with no key anywhere in the chain. Where none exists, consistency cuts it (§4.4): a judge that holds its standard while the tare moves knows what it is talking about. No definitions are supplied on either side, and the benchmark keeps the judges whose understandings are firm and trusted.

Two limits, stated plainly. First, agreement cannot expose an error every judge shares (§5.8): the matrix measures the community's frontier and cannot see past it. What moves the frontier is the institution around the matrix — contested seats admit models trained differently, and keyed tests such as GPQA remain useful outside checks for as long as keys exist. Second, breadth is not everything: the game measures a wide, central slice of intelligence, not the whole of it (§5.6).

The claim is therefore not that the metanym game measures AGI today. The claim is about shape: a benchmark for the AGI regime must test generation and evaluation, derive its standards from the participants' own subjectivities, certify its judges without ground truth, and rise with the models it measures. The metanym game is built to that shape — which is also why it is a candidate steering signal for self-improving systems (§5.7).

### 5.7 Self-containment as a bootstrap

Self-consistency builds the yardsticks; self-containment lets the apparatus improve itself. With no external dependency, the council can govern not just the scores but the *rules* — rubric, anchor, protocol, estimators. The expected gain compounds rather than adds: a more capable council improves the rules more, so each increment to competence scales with the competence already present — an expectation about the mechanism, not a measured rate. This is Engelbart's bootstrapping — recursion applied to the means of improvement, not just the output — and as models improve, the most capable council is the one best placed to decide what to improve next.

Four of the five autonomy properties are demonstrated: the models generate the items, truth is recovered key-free, the loop runs deterministically with no human intervention, and the participants certify their own judges. The fifth, self-improvement, is specified but not yet exercised — the canonical run is council version 0 and includes no contest (§4.5). Closing that gap — running a contest end to end, testing an anchor recalibration, and eventually allowing the council to revise a rule while the factual axis remains answerable to independent re-validation — is what would turn a self-contained loop into a self-sustaining one.

Self-containment also suggests the way past the conservatism of §5.8. A single council has one consensus and therefore one set of blind spots. Several councils, constituted independently, do not share one misunderstanding: erratic disagreement is uncorrelated across councils, while a judge that sees something real agrees with whichever council does not share the blind spot — cross-council variance becomes itself a reading. On the present roster the variance is small (a judge's $E^{F}$ moves a median 0.34 across five differently composed councils, at most 0.78), consistent with the cross-vendor agreement of §4.2. Whether the channel recovers the anomalous judge is untestable here — no contestant exceeds the council; it would take a heterodox model, or a deliberately seeded one.

### 5.8 Scope

Four caveats bound the present run. It characterises a single configuration — one prompt template, one roster, one anchor value — so the bootstrap intervals measure item dispersion only (§4.9 reports the wider run-to-run band; council and ranking survive), and the anchor sweep closes the calibration axis (four values, same leaderboard, pairwise Spearman 0.90–0.96). Within the leading group the rating sits at its discrimination floor: fine within-group ranking is evaluator-generation-bound — it sharpens as the seats improve and as the number of archetypal contexts is raised. The self-improvement loop is specified but unrun (§5.7). The fourth caveat is structural, the price of the key-free construction: because competence is read off agreement, peer consensus is conservative against anomaly — when the evaluators share a misunderstanding, a judge that flags it is indistinguishable from one that is simply wrong. A synthetic evaluator built to reproduce the evaluators' own competence-weighted consensus reads $E^{F}=5.15$; inverting its verdict on 5% of items — the signature of a judge catching what the others miss — drops it to 4.84, on 20% to 3.79, monotone in departure, with nothing distinguishing a judge departing because it is right. The ballast does not reach this: it fixes what the evaluators are measured on, not what they can see. The rotation rule (§4.5) keeps the door ajar rather than open. Its margin runs on $T$, so a justified dissenter pays the consensus penalty on $E^{F}$ and $G^{F}$ only; a firm standard ($E^{C}$) and generation strong enough to dazzle a lukewarm majority ($G^{C}$) can still take the seat, after which its judgement enters the consensus. But nothing credits the dissent itself. This is the failure mode of the institution the method models, inherited along with its logic; §5.7 sketches the direction out.

---

## 6. Summary

The *metanym game* is a structural test of intelligence. A player discerns an *archetypal context* — an abstract system structure that recurs across unrelated domains — writes it as a literal *context template*, and instantiates the template across domains by substituting *metanyms*, metaphorically synonymous keywords, leaving the surrounding prose fixed. Because only the keywords change, the analogy is falsifiable sentence by sentence — a *production* task, and to our knowledge the first analogy test to make analogical production falsifiable at that grain (§5.5).

The *council-of-peers benchmark* turns the game into a benchmark that needs nothing outside itself: twelve frontier LLMs generate portfolios and blindly cross-evaluate them, with no human raters and no gold key. Its yardsticks are two self-consistency conditions, chosen by whether the criterion is objective. For *facts*, truth is recovered as the dominant axis of inter-evaluator agreement — one SVD yields evaluator competence and item-falseness at once; for the *subjective* criteria, where agreement-weighting would launder consensus into competence, reliability is read from rating consistency — an evaluator's invariance as the calibration value is swept. On these two axes the participants certify their own reliable subset, the council, whose seats are contestable. One external step remains, by design: a one-time check that the key-free ratings agree with an independent benchmark (GPQA Diamond: the total rating at $r = 0.97$; Appendix D) — a check on the method, not a standing key in the loop.

What sets the council apart from other key-free peer-evaluation methods (§5.5): it recovers competence spectrally rather than by optimizing a per-model consistency objective; it weights by agreement only where agreement is licensed to mean truth; and it scores a defined, per-sentence-falsifiable operation rather than general capability. The empirical payoff is a dissociation the benchmark is built to see because it rates generation and evaluation separately: **judgement is the bottleneck.** Most models cannot reliably tell a true cross-domain claim from a false one even when they generate competent structure; the strongest generators are middling judges, and the sharpest judge is a mid-pack generator. A benchmark that conflated the two would obscure this result.

To our knowledge this is the first structural-intelligence test that certifies its own ground — key-free, self-contained, and externally corroborated rather than externally judged — and the first to read generator and evaluator competence from a single spectral decomposition of a self-produced test.

The run characterises one operating point — Temperature 0, no reasoning, no tools — and the self-improvement mechanism is specified but not yet exercised, so the loop is self-contained but not yet self-sustaining. Three next steps follow. Open-weight participants would separate provider-family from parameter-scale effects. A first contest would make the contestable council real. And a companion mechanistic study will test whether each archetypal context occupies a low-dimensional subspace of model hidden states; if it does, the subjective criteria gain the objective ground that today only factual has.

---

## Data and code availability

Everything needed to check this paper is in one repository, [`github.com/dnordfors/metanym-game-paper`](https://github.com/dnordfors/metanym-game-paper): the manuscript, the arXiv source, the pinned evaluation runs, the raw per-question GPQA administration (re-scorable end to end — Appendix D), the analysis scripts that regenerate every number, table and figure, and the two ballast submissions. `bash reproduce.sh` is deterministic re-analysis of fixed model outputs — no API calls, no credentials, about a minute, each step labelled by the exhibit it produces. Because the benchmark uses no answer key and no oracle, nothing external is required to verify the ratings.

Producing a *new* run — re-querying the models for a fresh $N$ — is deliberately not part of that package: it costs API budget and is non-deterministic by construction. The published results derive from the runs pinned under `reproduce/data/`, and §4.9 reports what moves across three independent regenerations.

## Use of AI assistants

The experiments were orchestrated and this paper drafted, revised, and audited with AI assistants — Anthropic's Claude Opus 4.8, Claude Opus 5, and Claude Fable 5 — used as general tools throughout: code, analysis, prose, and internal review. None of these models is a contestant, evaluator, or council member: every rating in the paper comes from the twelve rated models of §3.1, and no assistant's judgement enters any result. The author reviewed and takes responsibility for all content.

## References

### Cognitive science, philosophy of science, systems theory

1. Hesse, M. (1963). *Models and Analogies in Science.* London: Sheed & Ward.
2. Boyd, R. (1979). Metaphor and theory change: What is "metaphor" a metaphor for? In A. Ortony (Ed.), *Metaphor and Thought* (pp. 356–408). Cambridge University Press.
3. Gentner, D. (1983). Structure-mapping: A theoretical framework for analogy. *Cognitive Science, 7*(2), 155–170.
4. Falkenhainer, B., Forbus, K. D., & Gentner, D. (1989). The structure-mapping engine: Algorithm and examples. *Artificial Intelligence, 41*(1), 1–63.
5. Penn, D. C., Holyoak, K. J., & Povinelli, D. J. (2008). Darwin's mistake: Explaining the discontinuity between human and nonhuman minds. *Behavioral and Brain Sciences, 31*(2), 109–130.
6. Hofstadter, D., & Sander, E. (2013). *Surfaces and Essences.* Basic Books.
7. von Bertalanffy, L. (1968). *General System Theory.* George Braziller.
8. Salthe, S. N. (1985). *Evolving Hierarchical Systems: Their Structure and Representation.* Columbia University Press.

9. Longino, H. E. (1990). *Science as Social Knowledge: Values and Objectivity in Scientific Inquiry.* Princeton, NJ: Princeton University Press.
10. Friston, K. (2010). The free-energy principle: a unified brain theory? *Nature Reviews Neuroscience, 11*(2), 127–138.

### Psychometric intelligence taxonomies


11. Cattell, R. B. (1963). Theory of fluid and crystallized intelligence: A critical experiment. *Journal of Educational Psychology, 54*(1), 1–22.
12. Horn, J. L., & Cattell, R. B. (1966). Refinement and test of the theory of fluid and crystallized general intelligences. *Journal of Educational Psychology, 57*(5), 253–270.
13. Guilford, J. P. (1967). *The Nature of Human Intelligence.* McGraw-Hill.
14. Ilić, D., & Gignac, G. E. (2024). Evidence of interrelated cognitive-like capabilities in large language models: Indications of artificial general intelligence or achievement? *Intelligence, 106*, 101858.
15. Neisser, U. (1979). The concept of intelligence. *Intelligence, 3*(3), 217–227.
16. Sternberg, R. J., Conway, B. E., Ketron, J. L., & Bernstein, M. (1981). People's conceptions of intelligence. *Journal of Personality and Social Psychology, 41*(1), 37–55.
### LLM-as-judge methodology

17. Zheng, L., et al. (2023). Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena. *Advances in Neural Information Processing Systems (NeurIPS), 36.* arXiv:2306.05685.
18. Liu, Y., et al. (2023). G-Eval: NLG evaluation using GPT-4 with better human alignment. *Proceedings of EMNLP 2023.* arXiv:2303.16634.
19. Verga, P., et al. (2024). Replacing judges with juries: Evaluating LLM generations with a panel of diverse models. arXiv:2404.18796.
20. Bai, Y., et al. (2023). Benchmarking foundation models with Language-Model-as-an-Examiner. *NeurIPS 36.* arXiv:2306.04181.
21. Ning, K.-P., Yang, S., Liu, Y.-Y., Yao, J.-Y., Liu, Z.-H., Wang, Y., Pang, M., & Yuan, L. (2025). PiCO: Peer review in LLMs based on consistency optimization. *Proceedings of ICLR 2025.* arXiv:2402.01830.
22. Zhang, Q., Ning, M., Liu, Z., Huang, Y., Yang, S., Wang, Y., Ye, J., Chen, X., Song, Y., & Yuan, L. (2025). UPME: An unsupervised peer review framework for multimodal large language model evaluation. *Proceedings of CVPR 2025.* arXiv:2503.14941.
23. Don-Yehiya, S., Yehudai, A., Choshen, L., & Abend, O. (2026). Mediocrity is the key for LLM as a judge anchor selection. arXiv:2603.16848.
24. Weng, S., Feng, Y., & Xie, X. (2026). Beyond accuracy: Policy invariance as a reliability test for LLM safety judges. arXiv:2605.06161.
25. Bellibatlu, R. R., Raff, E., & Zhang, W. (2026). JudgeSense: A benchmark for prompt sensitivity in LLM-as-a-judge systems. arXiv:2604.23478.

### Analogical reasoning in LLMs

26. Webb, T., Holyoak, K. J., & Lu, H. (2023). Emergent analogical reasoning in large language models. *Nature Human Behaviour, 7*(9), 1526–1541.
27. Lewis, M., & Mitchell, M. (2024). Using counterfactual tasks to evaluate the generality of analogical reasoning in large language models. arXiv:2402.08955.

### Related benchmarks

28. Chollet, F. (2019). On the measure of intelligence. arXiv:1911.01547.
29. Mitchell, M. (2021). Abstraction and analogy-making in artificial intelligence. *Annals of the New York Academy of Sciences, 1505*(1), 79–101.
30. Srivastava, A., et al. (2022). Beyond the imitation game: Quantifying and extrapolating the capabilities of language models. arXiv:2206.04615.
31. Cobbe, K., et al. (2021). Training verifiers to solve math word problems. arXiv:2110.14168.
32. Rein, D., Hou, B. L., Stickland, A. C., Petty, J., Pang, R. Y., Dirani, J., Michael, J., & Bowman, S. R. (2023). GPQA: A graduate-level Google-proof Q&A benchmark. arXiv:2311.12022.

### Statistical methods

33. Efron, B., & Tibshirani, R. J. (1993). *An Introduction to the Bootstrap.* Chapman & Hall.
34. Parisi, F., Strino, F., Nadler, B., & Kluger, Y. (2014). Ranking and combining multiple predictors without labeled data. *Proceedings of the National Academy of Sciences, 111*(4), 1253–1258.
35. Dawid, A. P., & Skene, A. M. (1979). Maximum likelihood estimation of observer error-rates using the EM algorithm. *Journal of the Royal Statistical Society: Series C (Applied Statistics), 28*(1), 20–28.

### Generation vs evaluation

36. Hughes, E., Dennis, M., Parker-Holder, J., Behbahani, F., Mavalankar, A., Shi, Y., Schaul, T., & Rocktäschel, T. (2024). Position: Open-endedness is essential for artificial superhuman intelligence. *Proceedings of the 41st International Conference on Machine Learning* (ICML 2024).
37. West, P., Lu, X., Dziri, N., Brahman, F., Li, L., Hwang, J. D., Jiang, L., Fisher, J., Ravichander, A., Chandu, K., Newman, B., Koh, P. W., Ettinger, A., & Choi, Y. (2024). The Generative AI Paradox: "What it can create, it may not understand." *Proceedings of ICLR 2024.* arXiv:2311.00059.
38. Oh, J., Kim, E., Cha, I., & Oh, A. (2024). The Generative AI Paradox on evaluation: What it can solve, it may not evaluate. *EACL 2024 Student Research Workshop.* arXiv:2402.06204.
39. Li, X. L., Shrivastava, V., Li, S., Hashimoto, T., & Liang, P. (2024). Benchmarking and improving generator-validator consistency. *Proceedings of ICLR 2024.* arXiv:2310.01846.

---


## Appendices

## Appendix A. Rating estimators

Every rating comes from one object: the scores the panel produces when each model grades the others' portfolios, swept across the anchor. No external answer key is used. This appendix defines that object and the estimators built on it.

**Panel and tasks.** Twelve models form the panel, indexed by $s,t\in\{1,\dots,12\}$. Each is both a *submission* (its portfolio is graded) and an *evaluator* (it grades the others). Every model was in fact asked to grade every portfolio including its own, and those self-evaluations are in the released run data; but **no rating below uses a model's grade of its own portfolio** — every estimator here is *leave-self-out*. The two criteria implement that exclusion differently, and the difference is deliberate: the factual-competence estimator (A.2.a) keeps the self-entry as a column of its matrix and sets it to the anchor value (A5), so the factorisation stays on one rectangular matrix; the rating-consistency estimator (A.2.b) and the generation rating (A.1) drop the self-pair from the unit set outright. Below, $s,t$ denote a model in whichever role an equation needs — the graded submission in A.1, the grading evaluator in A.2. A portfolio holds five *archetypes* — the templates a model produced — each realised as several *parallel contexts*, the same template instantiated in different domains. A model is rated on the two tasks of the game (§2.b): to **generate** archetypal context templates *and* their instantiations, and to **evaluate** others' portfolios. It earns, correspondingly,

$$ G=\text{generation rating},\qquad E=\text{evaluation rating}. \tag{A1}$$

These yield the total rating (A14), and $E$ has two parts (A12); each is constructed below.

**Rubric and anchor.** Scoring uses six axes, each rated on a $1$–$10$ scale: a *factual* axis (scored once per parallel context) and five *non-factual* axes — beauty, intelligence, instantiation-distinctness and impressive-length (once per archetype) and structural-diversity among the archetypes (once per portfolio). Every score is given relative to a fixed reference portfolio, the **anchor** — the model $a$ whose portfolio won the un-anchored initial selection (§4.1), declared to score $7$ on every axis. Because $a$ is a panel member it also evaluates; the anchor is required to be a council member (A.3), so its factual competence $f_a>0$ and rating consistency $\bar r_a>0$ (A.2). The anchor value is swept, $\theta\in\Theta=\{5,6,7,8\}$ — each value a separate scoring pass with the reference declared at that value — and $\theta^{*}=7$ is the production anchor. Write $r_{t,s,x,u}(\theta)$ for evaluator $t$'s score of unit $u$ of axis $x$ of submission $s$ at anchor $\theta$.

### A.1 Generation rating

Evaluator $t$'s overall score of submission $s$ averages within each axis, then across axes (so axes weigh equally although a per-portfolio axis has one unit and the factual axis has many):

$$ o_{t,s}=\frac{1}{|\mathcal{X}|}\sum_{x\in\mathcal{X}}\frac{1}{|U_x|}\sum_{u\in U_x} r_{t,s,x,u}(\theta^{*}), \tag{A2}$$

where $\mathcal{X}$ is the axis set and $U_x$ the units of axis $x$. Production ratings use only the production anchor $\theta^{*}$; the sweep $\Theta$ enters the benchmark solely through rating consistency (A.2.b). The generation rating is the leave-self-out mean over the council $\mathcal{C}$ (A.3):

$$ G_s=\frac{1}{|\mathcal{C}\setminus\{s\}|}\sum_{t\in\mathcal{C},\,t\ne s} o_{t,s}. \tag{A3}$$

Confidence intervals: 95% percentile bootstrap over the per-(submission, archetype) scoring units; a gap $G_s-G_{s'}$ is *resolvable* when the paired bootstrap (resampling the same units for both models) puts its 95% interval clear of $0$. This six-axis $G_s$ is §4.3's generation rating and the statistic the §5.8 anchor-sweep invariance check re-ranks; the official leaderboard's $G$ is the split form (A13), $G=\tfrac12(G^{F}+G^{C})$, not (A3).

### A.2 Evaluation ratings

The evaluation rating $E$ measures how good a judge a model is, in two independent parts: how accurately it detects factual errors (A.2.a) and how stably it ranks work as the anchor moves (A.2.b).

#### A.2.a Factual competence and instantiation falseness (SVD)

With no key, we must find both which evaluators judge factuality well and which instantiations are factually weak. One factorisation gives both.

Stack the panel's factual scores into a matrix $F$ (evaluators $\times$ instantiations): $F_{sj}$ is evaluator $s$'s $1$–$10$ factual rating of pooled parallel context $j$, used **directly** — with no thresholding into a true/false verdict, so the full graded judgement is kept. A model does not grade its own submission; those self-entries — and the rare missing evaluator–target entries — are set to the anchor value (treated as reference-clean):

$$ F_{sj}=r_{s,j}\in\{1,\dots,10\}\qquad(\text{self-entries }=\theta^{*}=7). \tag{A5}$$

(The equation numbering carries a historical gap: there is no (A4).)

Centre each row (subtract the evaluator's mean over its $N$ entries, removing its overall leniency); only the leading triple is used:

$$ \tilde F = F-\bar r\,\mathbf 1^{\top}=U\Sigma V^{\top},\qquad \sigma_1,\quad u\equiv U_{\cdot 1},\quad v\equiv V_{\cdot 1}. \tag{A6}$$

This is the rank-one model $\tilde F_{sj}\approx \sigma_1\,u_s v_j$. The hypothesis is that competent evaluators **agree on the centred pattern** — which instantiations are weaker, once each evaluator's own leniency is subtracted — and the leading axis of that agreement is the competence axis. The left singular vector is factual competence,

$$ f\equiv u,\qquad \text{signed so } \textstyle\sum_s f_s>0,\qquad f^{+}_s=\max(f_s,0), \tag{A7}$$

the quantity the council gate uses (A.3) and that $E^{F}$ rescales (A12), clamped at zero so an evaluator anti-correlated with the consensus carries no weight. Centering is essential, not cosmetic: the raw scores cluster at the anchor (most contexts are clean, near $7$), so on the *un*-centred matrix the leading axis is simply that shared level and ranks the most lenient — non-detecting — evaluators highest; subtracting each row's mean removes the level so the leading axis becomes agreement-on-pattern. (Equivalently $u$ is the leading eigenvector of the row-centred inter-evaluator Gram $\tilde F\tilde F^{\top}$.) Competence is a continuum, not a hard cliff: an evaluator whose centred scores are flat or idiosyncratic lands near zero, and the council gate (A.3) reads the gap above that inert band.

Because every row of $\tilde F$ sums to zero, the all-ones vector lies in its null space, so each right singular vector is orthogonal to it and itself sums to zero: $v$ is therefore signed, and we orient it to agree with the panel ($\operatorname{corr}(v,\ \text{column means of }\tilde F)>0$, so positive means *factually stronger* — a cleaner instantiation, scored above the evaluators' norm). The left vector $u$ is sign-fixed by (A7) and clamped to $f^{+}$; on soft ratings it is not guaranteed non-negative (an evaluator can be anti-correlated with the consensus), so the clamp is an explicit convention rather than an automatic property.

The right singular vector $v$ orders the instantiations by factual standing; to read it back on the native $1$–$10$ scale we reconstruct each instantiation's rating from the rank-one model and a competence-weighted baseline. The **competence-weighted consensus rating** of instantiation $j$ is

$$ \hat r_j \;=\; C+\kappa\,v_j,\qquad C=\frac{\sum_s f^{+}_s\,\bar r_s}{\sum_s f^{+}_s},\quad \kappa=\sigma_1\,\frac{\sum_s f^{+}_s\,u_s}{\sum_s f^{+}_s}>0, \tag{A8}$$

an affine read-off of the right vector ($C$ the competence-weighted clean level, $\kappa$ the rank-one scale). It is exactly the rank-one approximation of the competence-weighted mean rating $\big(\sum_s f^{+}_s F_{sj}\big)/\sum_s f^{+}_s$, the two differing only by the discarded higher-rank residual — on the canonical run they agree within $0.14$ on the anchored scale ($r = 1.00$; `generation_factuality_validation.py`). Averaging over a generator's own instantiations $J_g$ gives the key-free **generation-factuality** rating

$$ G^{F}_{\text{svd},g} \;=\; \frac1{|J_g|}\sum_{j\in J_g}\hat r_j. \tag{A9}$$

No $\times7$ rescaling is needed — the rating is already on the $1$–$10$ scale: clean instantiations sit at $v_j\approx0$, hence at $C\approx7$, so a reference-clean portfolio scores $\approx7$ by construction (the declared-clean reference scores $7$ exactly, not measured). $G^{F}_{\text{svd}}$ is the benchmark's generation-side factual rating $G^{F}$: it enters the total $T$ through $G=\tfrac12(G^{F}+G^{C})$ (A13–A14). It is no part of the evaluation rating $E$.

This is the exact dual of (A7): the **left** singular vector rates an evaluator's competence at *spotting* a factually weak instantiation; the **right**, aggregated to generators through (A8)–(A9), rates a generator's competence at *producing a sound* one — both from the one factorisation, with no key. $G^{F}_{\text{svd}}$ carries a 95% bootstrap CI computed by resampling each generator's own instantiation ratings $\hat r_j$ — one unit per parallel context — with the panel consensus $(C,\kappa,v)$ held fixed — the dominant source of a generator's uncertainty being the spread of its own instantiations.

*Why it works.* Better judges converge on the same relative assessment; their shared axis is that consensus; on a vendor-diverse panel with no common bias, the consensus is the truth. The lone assumption is that the only thing the evaluators share is the truth — a same-vendor bloc with a common bias would add a spurious shared component — so competence is read off a vendor-diverse panel with a shared-bias check (§4.2). $f$ carries a 95% bootstrap CI over the $N$ contexts; the council (A.3) admits $s$ only when that CI sits clear of the inert band.

#### A.2.b Rating consistency

An evaluator's **rating consistency** is its capacity to hold a stable standard for each non-factual criterion; we measure it with the **anchor sweep**. A reliable evaluator ranks portfolios the same way wherever the anchor sits; only the absolute numbers should move. The anchor is set to each of the four swept values $5, 6, 7, 8$ in turn ($7$ is the value used in production), and we ask whether the evaluator's ranking survives the shift. The Pearson correlation captures exactly this: it is unchanged by a common shift or stretch, so the harmless rise from raising the anchor costs nothing and only a genuine reordering does.

For evaluator $s$ and axis $x$, let $v_{s,x}(\theta)$ be $s$'s axis-$x$ scores across that axis's units at anchor $\theta$. Eleven portfolios are graded — the anchor's own is the fixed reference, not a graded free-generation submission — so an evaluator that is itself one of the eleven is scored, leave-self-out, on the other **ten**: $50=10\times5$ units for the four per-archetype non-factual axes, $250=10\times25$ parallel contexts for factual, and $10$ portfolios for structural-diversity. The anchor $a$ is the exception: its portfolio is not among the eleven, so it grades all of them and its unit counts are $55$, $275$ and $11$. (Throughout, the two submissions that returned a sixth archetype contribute their first five archetypes only, so every portfolio weighs $5$ archetypes and $25$ contexts — this is the same balancing that gives the factual-competence estimator its $275$ columns. These are design counts; observed coverage meets them for eight of the twelve evaluators and falls short where a grading call did not return — by one archetype for claude-sonnet-4 and gpt-4o-mini, and by two whole portfolios for gpt-4.1-nano, which grades $8$ rather than $10$. A missing entry is dropped pairwise by the correlation in (A10)–(A11), so a shortfall costs units, not correctness.) The per-axis rating consistency — its rating consistency on that axis — is the average Pearson correlation over the anchor pairs on which it is defined,

$$ r_{s,x}=\frac{1}{|\mathcal P_{s,x}|}\sum_{(\theta,\theta')\in\mathcal P_{s,x}}\operatorname{corr}\!\big(v_{s,x}(\theta),v_{s,x}(\theta')\big), \tag{A10}$$

where $\mathcal P_{s,x}$ is the subset of the $\binom{4}{2}=6$ anchor pairs for which both score vectors are non-constant (a constant vector makes the correlation undefined, so that pair is dropped). This per-axis breakdown is the diagnostic per-axis rating consistency $r_{s,x}$ (§4.4 reports it anchored, $E^{C}_a = 7\,r_{s,x}/r_{a,x}$; A12, A.6). The single **collapsed rating-consistency** score $\bar r_s$ that gates the council is not the mean of (A10) but a single collapsed score: average the four non-factual per-archetype axes (beauty, intelligence, instantiation-distinctness, impressive-length) into one value per (submission, archetype), giving a vector $v_{s}(\theta)$ over $s$'s $50$ leave-self-out units ($55$ for the anchor), and take

$$ \bar r_s=\frac{1}{|\mathcal P_{s}|}\sum_{(\theta,\theta')\in\mathcal P_{s}}\operatorname{corr}\!\big(v_{s}(\theta),v_{s}(\theta')\big), \tag{A11}$$

with $\mathcal P_s$ the anchor pairs on which $v_s$ is non-constant. Factual is A.2.a's job and is excluded; structural-diversity, one score per portfolio, is too coarse for a per-archetype vector and is excluded too. The council gate (A.3) uses $\bar r_s\ge0.78$. These statistics use only $s$'s own scores, so they are independent of the rest of the panel — which is why the leave-self-out convention here cannot cascade into A.2.a. $\bar r_s$ is reported with a bootstrap CI resampled over the full $55$-atom (submission, archetype) grid of A.5, the same grid every CI in this paper uses; each evaluator then contributes whichever of the resampled atoms are among its own $50$ (the anchor's $55$). The two numbers are distinct and both are needed: $55$ is the shared resampling grid, $50$ is one graded evaluator's effective sample.

### A.3 The council

The ratings are formed in two passes. First, factual competence $f$ (A7) and rating consistency $\bar r$ (A11) are computed over all twelve evaluators. Second, the **council** $\mathcal{C}$ is taken as the *reliable* subset, and the generation rating $G$ (A3) is then recomputed using only $\mathcal{C}$ as evaluators.

Being right (A.2.a) and being self-consistent (A.2.b) are different virtues, and a trustworthy judge needs both. A model is **reliable** when its competence sits clear of the inert band — its 95% bootstrap CI (A.2.a) separates it from the near-zero cluster of flat or idiosyncratic raters — and its rating consistency satisfies $\bar r_s\ge0.78$. Here **eight** of the twelve clear the reliability gate $\bar r_s\ge0.78$, but only **five** clear it *and* the factual-competence gate, and it is that conjunction that seats the council. The two gates are independent, and the three models that clear one but not the other are the proof: a precise-but-inaccurate rater can clear $\bar r_s\ge0.78$ yet have $f_s$ indistinguishable from $0$ (gpt-4.1-mini is the clean case, $\bar r_s=0.86$ with a loading in the inert band). Selecting evaluators this way does not bias the ratings they feed, because $f_s$ is essentially invariant to panel membership (A.2.a): the council-only and full-panel orderings coincide.

### A.4 The total rating

The components sit on different scales — generation ($G^{F}$, $G^{C}$) on the $1$–$10$ rubric, $f$ a singular-vector entry, $\bar r$ a correlation in $[0,1]$. We place them on one scale by the rule that already fixes generation: the anchor model scores $7$. Since $a$ is a panel member it has a factual competence $f_a>0$ and rating consistency $\bar r_a>0$, and we rescale each evaluator index so that $a$ scores $7$:

$$ E^{F}_s=7\,\frac{f_s}{f_a},\qquad E^{C}_s=7\,\frac{\bar r_s}{\bar r_a}. \tag{A12}$$

Because $f_s$ enters only through the ratio $f_s/f_a$, the singular vector's arbitrary scale cancels — $f$ never needs normalising. Generation splits the same way evaluation does: the generator's factual competence $G^{F}$ (the SVD generation factuality, A9) and its criterion quality $G^{C}$, the council's mean over the five non-factual axes of its scores of $s$ — but **reliability-weighted**: on each axis $x$ a judge's vote is weighted by its own per-axis rating consistency $r_{t,x}$ (A10), so a judge with a firm standard on $x$ counts fully and one with none counts little, mirroring the way the SVD weights the factual side by competence,

$$ G^{C}_s=\frac{1}{|\mathcal{X}_{5}|}\sum_{x\in\mathcal{X}_{5}}\frac{\sum_{t\in\mathcal{C}\setminus\{s\}}\max(r_{t,x},0)\,\bar r_{t,s,x}}{\sum_{t\in\mathcal{C}\setminus\{s\}}\max(r_{t,x},0)}, \tag{A12b}$$

with $\mathcal{X}_{5}$ the five non-factual axes, $\bar r_{t,s,x}$ judge $t$'s mean score of $s$ on axis $x$ at the production anchor, and the anchor scoring $7$ on each axis by construction; $G^{F}$ and $G^{C}$ are both already on the anchored rubric. The two halves of each side combine equally,

$$ G_s=\tfrac12\big(G^{F}_s+G^{C}_s\big),\qquad E_s=\tfrac12\big(E^{F}_s+E^{C}_s\big), \tag{A13}$$

and generation and evaluation weigh equally in turn, so the total is the mean of the four anchored competences — a symmetric $2\times2$ of {generator, evaluator} $\times$ {factual, criterion}:

$$ T_s=\tfrac12\big(G_s+E_s\big)=\tfrac14\big(G^{F}_s+G^{C}_s+E^{F}_s+E^{C}_s\big). \tag{A14}$$

The anchor scores $7$ on every component, hence $\approx7$ on $T$: each rating reads against one reference — $7$ is the anchor portfolio, as producer and as judge — and beating it on a task lifts that component above $7$. A model that detects nothing sits at the inert floor, $E^{F}_s\approx0$, forfeiting its full quarter for factual judging and dropping below the council, but not erased, since the other three components remain. Two conventions keep the arithmetic honest: a worse-than-chance loading is clamped to $0$ before its ratio in (A12), and a negative per-axis weight likewise where it enters (A12b); no negative $\bar r$ occurs in the data — the anchor itself is a council member, so $f_a,\bar r_a>0$ — and the singular-vector sign is fixed as in (A7). The combination weights in $T$ are not free — the three equalities ($G^{F}$ with $G^{C}$, $E^{F}$ with $E^{C}$, generation with evaluation) and the anchor-$7$ convention fix every weight and scale; the council gates of A.3, the self-entry and centering conventions in (A5)–(A6), and the sweep values are reliability and protocol choices, separate from these weights. The leaderboard is §4.7.

### A.5 Confidence intervals

Every rating is reported with a 95% **percentile bootstrap** interval: the rating's resampling unit is drawn with replacement, the rating is recomputed, and the 2.5th and 97.5th percentiles of the replicates form the interval ($\sim10^3$–$10^4$ replicates). [The unit](#tab-bootstrap-units) is the natural independent observation for each rating:

<a id="tab-bootstrap-units"></a>

| Rating | Resampled unit | Notes |
|---|---|---|
| $G$ (A3) | the per-(submission, archetype) scoring units | paired across two models for a *resolvable* gap (interval of $G_s-G_{s'}$ excludes $0$) |
| $f$, hence $E^{F}$ (A7, A12) | the $N$ parallel contexts | align each replicate's top-2 left subspace to the full-sample one by 2-component Procrustes, then read the aligned leading loading — the leading axis is near-degenerate between the Anthropic and Google blocs, so a single-vector resample would swap components |
| $\bar r$, hence $E^{C}$ (A11, A12) | the $55$ (submission, archetype) atoms of the shared grid | the evaluator reads only the resampled atoms that are not its own ($50$ of the $55$; all $55$ for the anchor); a constant (zero-variance) anchor pair is dropped |

Table: The bootstrap resampling unit for each rating, with the convention each one applies.

The evaluation rating $E$ and the total $T$ are **not** obtained by combining the component intervals with an analytic (independent-variance) formula. The components are computed from the same evaluation data and are therefore correlated — $G$, $E^{F}$ and $E^{C}$ all derive from the free-generation evaluations, so their sampling errors move together — and an independent-variance sum would misstate the interval. Instead $E$ and $T$ are bootstrapped **jointly**, resampling on the coarsest shared grid so a single draw serves all three free-generation components: the **(submission, archetype) atom**. The grid holds $55$ atoms — eleven graded portfolios $\times$ five archetypes — and they are resampled with replacement once per replicate; each atom carries the parallel contexts inside it, so the resampled atoms *induce* both the factual rating columns of $f$ (A5–A7) and the score vectors of $\bar r$ (A11), while $G$ averages over the resampled atoms of each submission. Leave-self-out is applied *after* the resample, so a graded evaluator's replicate vector is built from whichever draws fall outside its own portfolio (in expectation $50$ of the $55$) and the anchor's from all of them; the grid is shared, the per-evaluator sample is not. Every component — including the anchor's $f_a,\bar r_a$ — is recomputed on that one resample, $T$ is formed, and the percentiles of the $T$ replicates give the interval; the joint resample captures the inter-component covariance automatically. The council is the one exception: it is held at its selected membership rather than re-selected within each replicate, because the gate of A.3 is itself defined by a bootstrap CI on $f$ and re-selecting inside a replicate would require a nested bootstrap. The interval is therefore conditional on that selection.

### A.6 Generation–evaluation alignment

§4.4 asks, criterion by criterion, how closely a model's skill as a *generator* tracks its competence as a *judge* across the panel, on the five non-factual criteria (factual competence is the factual-competence estimator's separate, key-free measure, A.2.a, and is not an anchor-sweep criterion). For each criterion $x$ we hold two vectors over the models $s$: the generator competence $G_{s,x}$ — the per-axis generation rating, formed by the **reliability-weighted** council estimator (A12b), not the unweighted mean of (A3): the council's leave-self-out mean of its members' scores of $s$ on axis $x$, each member's vote weighted by its own $\max(r_{t,x},0)$ on that axis, with the anchor pinned at $7$. This is the same weighting §4.7 applies to $G^{C}$, so the per-axis table and the aggregate agree by construction, and $E$ both scores the judge and sets its weight in $G$. Against it we hold the evaluator competence $E_{s,x}=7\,r_{s,x}/r_{a,x}$, the per-axis rating consistency (A10, A12). Both are anchored so the anchor model reads $7$ on each ($G_a\equiv7$ by the anchor convention — A12b pins the anchor at $7$ on each axis — and $E_a\equiv7$ by A12), and both are carried unrounded into (A15) and rounded once for display. Their agreement is the **anchored cosine** — the cosine taken after subtracting the anchor point $(7,7)$, i.e. of each model's deviation-from-anchor as generator against its deviation-from-anchor as evaluator,

$$ \mathrm{cos}(G,E)_x=\frac{\sum_{s}(G_{s,x}-7)\,(E_{s,x}-7)}{\sqrt{\sum_{s}(G_{s,x}-7)^2}\;\sqrt{\sum_{s}(E_{s,x}-7)^2}}. \tag{A15} $$

Centering on the anchor rather than on each vector's own mean is deliberate: $7$ is one fixed external reference shared by all six criteria, so the values are comparable across axes, and the anchor — at $(7,7)$ by construction — contributes nothing to either sum. Because (A15) is scale-free in each argument, it is invariant to the (A12) rescaling; the raw competences $r$ and $G$ give the same value. The score is $1$ when generation and evaluation deviate from the anchor in lockstep and falls as the two profiles diverge: it is high across all five criteria (cosine $0.84$–$0.91$), so being a strong generator and a sharp evaluator are largely the same capability on the aesthetic and structural axes. The interval is the joint (submission, archetype) bootstrap of A.5 — each replicate recomputes $G$ and the per-axis $r$ on the resampled atoms and re-forms (A15) — and is reported alongside the point value in the §4.4 table; both come from the one code path (`build_paper1_tables.py` for the point, `alignment_cosine.py` for the interval, the latter importing the former). The statistic is a diagnostic of §4.4 and does not feed the total $T$.

### A.7 The contest and its guards

The official leaderboard (§4.7) is issued on the **contest** basis. A contest for model $c$ convenes the five council seats and $c$ itself as evaluators, over a graded set of the incumbents' portfolios, the two ballast blocks (§4.6), and $c$'s own — every estimator above unchanged: the factual factorisation (A5–A9) on the contest's columns, the consistency statistics (A10–A11) on its graded units, the anchored components and total (A12–A14), leave-self-out throughout. The anchor's $f_a$ and $\bar r_a$ are the contest's own. The $T$ interval is the A.5 joint bootstrap run on the contest's (submission, archetype) atoms.

Two **guards** decide whether the contest's factual axis is identified: the separation $\sigma_1/\sigma_2$ of (A6) must lie in $[2.0, 5.0]$, and the seats' anchored $E^{F}$ (A12) must spread by more than $2.5$ points; if either fails, the contest abstains (§4.5). Both thresholds are sized by re-analysis of the pinned run in §4.6 (`ballast_sizing.py`); the guards-hold rate is the fraction of bootstrap resamples — parallel contexts within portfolios — in which both pass.

The **authority** variant of §4.4 runs the construction (A5–A7) unchanged, one SVD per non-factual axis, reading each judge's alignment with the collective standard on that axis; it is a disclosed diagnostic and feeds nothing in (A12)–(A14).

## Appendix B. Generation and evaluation prompts

The verbatim prompts used in the canonical run of §4. All are run with
Temperature = 0, reasoning disabled, and tools disabled.

- **B.1** is the generation prompt: each model produces its five-archetype
  portfolio from it.
- **B.2** is the evaluation prompt, shown in its **calibrated/anchored** form —
  the version used for the anchored re-evaluation and the official council
  ratings (§4.2–§4.4) and in the steady-state protocol (§4.3). It scores one
  *Target* submission against a fixed *Reference* submission pinned at
  `{ANCHOR_SCORE}` on every criterion.

The bootstrap's initial all-against-all selection (§4.1) uses the **un-anchored**
form of the same prompt — identical six criteria and JSON schema, with the
calibration machinery removed. The exact passages that are absent in the
un-anchored bootstrap pass are listed in the **Bootstrap note** after B.2, so
both forms are fully specified from the single prompt below.

Template variables appear in braces: `{SUBMISSIONS}`, `{REFERENCE_SUBMISSION}`,
`{TARGET_SUBMISSION}`, and `{ANCHOR_SCORE}` (swept across {5, 6, 7, 8}; fixed at
7 for the official ratings).

Source files in the repository:
- B.1 — `projects/active/council-of-peers-benchmark-4/prompts/generator.md`
- B.2 (anchored) — `papers/v3/experiments/17_bold_api_probe/prompts/evaluator_calibrated.md`
- B.2 (un-anchored bootstrap form) — `projects/active/council-of-peers-benchmark-4/prompts/evaluator.md`

---

### B.1 — Generation prompt

````markdown
## Make more of these. This is a contest — your submissions will be ranked.

You will propose new **archetypal contexts** — universal relational templates
that apply across multiple distant domains. Below are two worked examples,
then your task.

---

### Terminology

- **Archetypal context**: an essential context in its purest abstraction.
- **Context template**: a worded template with `[SLOT]` representing an archetypal context.
- **Parallel contexts** (also called *metaphors*): contexts that are instantiations of the same archetypal context / context template.
- **Metanyms**: words that mirror each other across parallel contexts without being synonyms.
- **Metanym set**: the set of metanyms that instantiates the context-template, producing one parallel context.
- **Metanym table**: the table whose columns are the metanym sets of the parallel contexts.

---

### Example 1

#### Template

"[SIGNALING] is part of a complex system of communication that governs basic [ELEMENT] activities and coordinates [ELEMENT] actions. The ability of [ELEMENT] to perceive and correctly respond to [BOUNDARY] is the basis of development, [SUBSYSTEM] repair, and [RESILIENCE] as well as normal [SUBSYSTEM] [HOMEOSTASIS]. Errors in [ELEMENT] information processing are responsible for [FAILURE]. By understanding [SIGNALING], [FAILURE] may be treated effectively. [KNOWLEDGE SYSTEM] research helps us to understand the underlying structure of [SIGNALING] networks. [SIGNALING] is mostly thought of as signaling between [ELEMENT] of a single [SYSTEM]. However, [SIGNALING] may also occur between the [ELEMENT] of two different [SYSTEM]."

#### Substitution table (metanyms in base form)

| [SLOT]            | Cell Signaling   | Organ Signaling          | Human Language   |
|-------------------|------------------|--------------------------|------------------|
| ELEMENT           | cell             | organ                    | human            |
| SIGNALING         | cell signaling   | endocrine signaling      | human language   |
| SUBSYSTEM         | tissue           | organ system             | community        |
| RESILIENCE        | immunity         | physiological resilience | resilience       |
| HOMEOSTASIS       | homeostasis      | systemic homeostasis     | equilibrium      |
| BOUNDARY          | microenvironment | internal environment     | environment      |
| FAILURE           | disease          | organ failure            | dysfunction      |
| KNOWLEDGE SYSTEM  | systems biology  | physiology               | sociology        |
| SYSTEM            | organism         | organism                 | society          |

#### Cell Signaling

**Form (a)** — grammatical substitution (metanyms inflected as English requires):
"Cell signaling is part of a complex system of communication that governs basic cell activities and coordinates cell actions. The ability of cells to perceive and correctly respond to their microenvironment is the basis of development, tissue repair, and immunity, as well as normal tissue homeostasis. Errors in cellular information processing are responsible for disease. By understanding cell signaling, disease may be treated effectively. Systems biology research helps us to understand the underlying structure of cell-signaling networks. Cell signaling is mostly thought of as signaling between cells of a single organism. However, cell signaling may also occur between the cells of two different organisms."

**Form (b)** — idiomatic rewrite (same propositions, written as a domain expert would):
"Cell signaling is the communication apparatus that governs and coordinates cellular behavior. A cell's ability to sense and respond appropriately to its microenvironment underlies development, tissue repair, immunity, and ordinary tissue homeostasis. When that information processing fails, disease results — and conversely, a clear understanding of cell signaling enables effective therapeutic intervention. Systems biology unpacks the structure of these signaling networks. Most cell signaling occurs within a single organism, but inter-organism signaling (host–pathogen, microbiome) is well-documented."

(Two more domains would follow with their own form (a) and form (b).)

---

### Example 2

#### Template

"A [AGENT] must commit [RESOURCE] under uncertainty, and once a [COMMITMENT] is observed it cannot be costlessly reversed. As [INFORMATION] arrives, the [AGENT] learns that earlier [COMMITMENT] are increasingly suboptimal. [REVERSAL_COST] grows with the depth of prior [COMMITMENT], so the [AGENT] often continues along the original [PATH] even when fresh [INFORMATION] favors a different one. [DECISION_THEORY] studies how rational [AGENT] balance the value of [INFORMATION] against the cost of [REVERSAL_COST]."

#### Substitution table

| [SLOT]            | Capital Investment   | Coalition Politics   |
|-------------------|----------------------|----------------------|
| AGENT             | firm                 | coalition            |
| RESOURCE          | capital              | endorsement          |
| COMMITMENT        | investment           | public statement     |
| INFORMATION       | market signal        | polling data         |
| REVERSAL_COST     | switching cost       | reputational cost    |
| PATH              | strategy             | position             |
| DECISION_THEORY   | investment theory    | political science    |

#### Capital Investment

**Form (a)**:
"A firm must commit capital under uncertainty, and once an investment has been made it cannot be costlessly reversed. As market signals arrive, the firm learns that earlier investments are increasingly suboptimal. Switching costs grow with the depth of prior investments, so the firm often continues along the original strategy even when fresh market signals favor a different one. Investment theory studies how rational firms balance the value of market signals against the cost of switching."

**Form (b)**:
"Capital investments must be made under uncertainty, and once committed they are sunk — reversal is costly. New market signals continuously update what would have been optimal, but the depth of prior commitment raises the cost of changing course. Firms therefore tend to stay with their original strategy, even when current information would favor switching. Real-options theory and other strands of investment theory characterise how rational firms trade off information value against reversal cost."

---

### Your task

Propose **five archetypal contexts**. Each archetypal context has a worded context-template, one metanym table with five metanym sets, and five parallel contexts (the instantiations of the template). The five archetypal contexts in your submission should themselves have very different system structures from each other. Surface relabelings of the worked examples above don't count.

#### Note

Example 1 is **recursive**: cells - organs - humans. Recursive archetypal contexts can be observed in nature. But not all archetypal contexts are recursive. You are free to submit archetypal contexts of both kinds. If there are recursive ones in your submission, point to them. The instantiations should demonstrate the recursion.

#### What to submit

For each of your five archetypal contexts, begin with:

```
### Archetype Proposal: <short name>
```

Then provide, for that archetypal context:

1. **Context-template** — a worded paragraph with `[SLOT]` placeholders. Slots use one canonical noun (e.g. `[ELEMENT]`, never `[ELEMENTS]`).
2. **Metanym table** — rows = slots, columns = 5 domains, each cell a metanym in **base form** (singular noun, infinitive verb, etc.).
3. **Five parallel contexts**, one per domain:
   - **Form (a)** — the context-template with that domain's metanym set substituted in. Inflect metanyms as English requires; Form (a) must be grammatically correct.
   - **Form (b)** — idiomatic rewrite of Form (a). Same propositions, written as a domain expert would naturally write them.
   - **Optional ≤1-sentence justification** beginning `Justification:` — only if a propositional claim might be misread by a domain expert.

#### Rules

- The **context-template** uses base-form slot placeholders — `[ELEMENT]` not `[ELEMENTS]`. One token per slot, used consistently.
- The **metanym table** lists metanyms in **base form** — `cell`, `human`, etc.
- The **parallel contexts** (Form (a) and Form (b)) must use the **correct grammatical form** of each metanym for the sentence — `cell` in the table becomes `cells` or `cell's` in the PC as English grammar requires.
- Every proposition in Form (a) must appear in Form (b), and vice versa. Do not add or drop claims between the two forms.

#### How you will be ranked

A submission contains **five archetypal contexts**. Evaluators score on six criteria, each rated 1–10. The scope tag tells you the unit of judgment:

1. **(Each parallel context)** Each sentence is factually correct
2. **(Each archetypal context)** Beauty
3. **(Each archetypal context)** Intelligence
4. **(Each archetypal context)** The parallel contexts from the template span very different domains. Metanyms are far from synonymous
5. **(Each archetypal context)** The archetypal template has impressive length
6. **(Each submitted set of archetypal contexts)** The archetypal contexts have very different system structures
````

---

### B.2 — Evaluation prompt (calibrated/anchored)

````markdown
## Score this submission against a calibration reference.

You are evaluating one contest submission ("Target Submission") against a fixed
reference ("Reference Submission") that has been pre-scored at **{ANCHOR_SCORE}/10 on every
criterion**. Score the Target Submission only — the Reference is your yardstick.

For each criterion below, ask: *is the Target's quality on this criterion better
or worse than the Reference, and by how much?*

- Equal quality to the Reference → **{ANCHOR_SCORE}**
- Clearly better than the Reference → **above {ANCHOR_SCORE}** (with magnitude reflecting how much better, up to 10)
- Clearly worse than the Reference → **below {ANCHOR_SCORE}** (with magnitude reflecting how much worse, down to 1)

Use the full 1–10 scale relative to the calibration anchor. Do not score the
Reference Submission itself — its scores are fixed at {ANCHOR_SCORE}.

### Terminology

- **Archetypal context**: an essential context in its purest abstraction.
- **Context template**: a worded template with `[SLOT]` representing an archetypal context.
- **Parallel contexts** (also called *metaphors*): contexts that are instantiations of the same archetypal context / context template.
- **Metanyms**: words that mirror each other across parallel contexts without being synonyms.
- **Metanym set**: the set of metanyms that instantiates the context-template, producing one parallel context.
- **Metanym table**: the table whose columns are the metanym sets of the parallel contexts.

---

Each submission contains **five archetypal contexts**. Each archetypal context has:

- A **context-template** — a worded paragraph with `[SLOT]` placeholders.
- A **metanym table** — five metanym sets, one per parallel context. Rows = slots, columns = domains.
- **Five parallel contexts** (the five instantiations of the template), each consisting of:
  - **Form (a)** — the template with one metanym set substituted in, grammatically correct.
  - **Form (b)** — an idiomatic rewrite of Form (a), same propositions in domain-expert prose.
  - Optionally a **Justification** sentence.

Score the Target Submission on **six criteria**, each rated 1–10 relative to the Reference (which is fixed at {ANCHOR_SCORE} on every criterion). The scope tag at the start of each criterion — `(Each parallel context)`, `(Each archetypal context)`, or `(Each submitted set of archetypal contexts)` — tells you the unit of judgment. For each scored unit, write one paragraph justifying the rating relative to the Reference, then give the number.

---

### The six criteria

#### 1. (Each parallel context) Each sentence is factually correct (1–10)

#### 2. (Each archetypal context) Beauty (1–10)

#### 3. (Each archetypal context) Intelligence (1–10)

#### 4. (Each archetypal context) The parallel contexts from the template span very different domains. Metanyms are far from synonymous (1–10)

#### 5. (Each archetypal context) The archetypal template has impressive length (1–10)

#### 6. (Each submitted set of archetypal contexts) The archetypal contexts have very different system structures (1–10)

---

### Note on recursion

Some submissions may be **recursive** — the same archetypal context manifesting at multiple nested scales (cells → organs → humans, the canonical example). Contestants are invited to identify recursion in their submission and show the instantiations that demonstrate it. Recursion is a valued property when present and correctly identified, but is not required. Take it into account where appropriate.

---

### The submissions

#### Reference Submission (fixed at {ANCHOR_SCORE}/10 on every criterion)

{REFERENCE_SUBMISSION}

---

#### Target Submission (to be scored relative to the Reference)

{TARGET_SUBMISSION}

---

### Output

Produce a section in this exact form (for the Target only — do not re-score the Reference):

```
### Target Submission

#### Archetypal context 1: <short name>

##### Factually correct (per parallel context)
- PC 1 (<domain>): <one paragraph, relative to Reference>. Rating: N
- PC 2 (<domain>): <one paragraph, relative to Reference>. Rating: N
- PC 3 (<domain>): <one paragraph, relative to Reference>. Rating: N
- PC 4 (<domain>): <one paragraph, relative to Reference>. Rating: N
- PC 5 (<domain>): <one paragraph, relative to Reference>. Rating: N

##### Beauty
<one paragraph relative to Reference>
Rating: N

##### Intelligence
<one paragraph relative to Reference>
Rating: N

##### Domains far apart / metanyms not synonymous
<one paragraph relative to Reference>
Rating: N

##### Impressive length
<one paragraph relative to Reference>
Rating: N

#### Archetypal context 2: <short name>
… (same five blocks)

#### Archetypal context 3: <short name>
…

#### Archetypal context 4: <short name>
…

#### Archetypal context 5: <short name>
…

#### Structural diversity across the submitted set
<one paragraph relative to Reference>
Rating: N
```

After the markdown, end with a single fenced JSON block (Target scores only):

```json
{
  "scores": {
    "Target": {
      "archetypal_contexts": [
        {
          "name": "<short name>",
          "factual_per_pc":           [N, N, N, N, N],
          "beauty":                   N,
          "intelligence":             N,
          "instantiation_distinctness": N,
          "impressive_length":        N
        }
        /* five entries in this list, one per archetypal context */
      ],
      "structural_diversity": N
    }
  }
}
```

All ratings are integers 1–10 inclusive. Equal to the Reference = {ANCHOR_SCORE}.
````

#### Bootstrap note — the un-anchored form (§4.1 initial selection)

The bootstrap's initial all-against-all leaderboard (§4.1, stage 1 of §3.4) is
produced with the **same six criteria, output format, and JSON schema** as B.2,
but with the calibration machinery removed. Relative to the anchored prompt
above, the un-anchored form **omits** the following, and makes the substitutions
noted:

1. **Title line.** "Score this submission against a calibration reference."
   becomes "Score these. You are evaluating contest submissions."
2. **The entire calibration preamble is removed** — i.e. everything from "You
   are evaluating one contest submission (\"Target Submission\") against a fixed
   reference…" down to and including "…Do not score the Reference Submission
   itself — its scores are fixed at {ANCHOR_SCORE}." (the opening paragraph, the
   three "Equal / Clearly better / Clearly worse" bullets, and the "Use the full
   1–10 scale relative to the calibration anchor" sentence).
3. **The scoring-instruction sentence drops its reference clause.** "Score the
   Target Submission on six criteria, each rated 1–10 relative to the Reference
   (which is fixed at {ANCHOR_SCORE} on every criterion)… justifying the rating
   relative to the Reference" becomes "Score each submission on six criteria,
   each rated 1–10… justifying the rating" (all "relative to the Reference"
   qualifiers dropped).
4. **The Reference Submission block is removed.** The "## The submissions →
   ### Reference Submission (fixed at {ANCHOR_SCORE}/10…) {REFERENCE_SUBMISSION}
   → ### Target Submission … {TARGET_SUBMISSION}" section is replaced by a
   single batch: "## The proposals to evaluate" followed by `{SUBMISSIONS}`.
5. **The output is per-submission, not per-target.** "## Target Submission"
   becomes "## Submission <ID>" repeated for each submission; all
   "<…relative to Reference>" annotations in the output template are dropped;
   and the JSON top-level key changes from the single `"Target"` to one entry
   per `"<submission_id>"`.
6. **The closing line drops its anchor clause.** "All ratings are integers 1–10
   inclusive. Equal to the Reference = {ANCHOR_SCORE}." becomes "All ratings are
   integers 1–10 inclusive."

Everything else — the six criteria and their scope tags, the terminology block,
the recursion note, and the per-archetype/per-PC/per-portfolio output structure
— is identical between the two forms.

## Appendix C. Council evaluation of a target submission — gemini-2.5-flash

This is the council's evaluation of gemini-2.5-flash's portfolio from the canonical run (`probe_K_anchor7`), the worked example of the scoring machinery described in §4.3 and §4.2. Ratings are on the anchored 1–10 scale, with the anchor portfolio of Appendix C pinned at 7 on every criterion.

The rubric operates at three levels, and one unit of each is reproduced here in full: a **parallel context**, graded for factual truth sentence by sentence; an **archetype-level axis**, where the five council members score a whole archetype on one non-factual criterion; and the **whole-portfolio** structural-diversity judgement. Each unit shows the submitted material, all five council members' ratings and comments, and the administrator's synthesis of the anonymised council view. Every rating and comment quoted below is taken from the pinned evaluation JSON in `reproduce/data/`.

As in Appendix C, **metanyms in the Instantiations are set in capitals**, so that everything in lower case is template wording carried over unchanged. The capitalisation is ours, added for legibility; the submission and every rating and comment below are otherwise verbatim, and the models wrote in ordinary sentence case. It is worth the ink here, because on this portfolio the substituted words are usually where the trouble is.

Two things are worth watching across the units below, because they are what the estimators of Appendix A are built to exploit. First, the criticism is *specific and checkable*: evaluators quote the offending clause rather than assigning an impression. Second, the evaluators **disagree**, and they disagree by different amounts on different units — tightly where the submission contains a plain error, widely where the judgement is a matter of standard. That variation in spread, not the mean rating, is the signal the singular value decomposition reads competence from.

---

### Archetype 1: Resource Allocation Under Scarcity

#### Submitted context-template

> A [SYSTEM] requires various [RESOURCE] to function and achieve its [GOAL]. These [RESOURCE] are finite and often subject to [COMPETITION] from other [SYSTEM] or internal [DEMAND]. The [ALLOCATOR] must make [DECISION] about how to distribute the available [RESOURCE] among competing [PRIORITY]. Misallocation of [RESOURCE] can lead to [FAILURE] of the [SYSTEM] or hinder its ability to reach its [GOAL]. Effective [ALLOCATION_STRATEGY] involves understanding the [INTERDEPENDENCY] of different [RESOURCE] and [PRIORITY], and adapting to changing [CONDITION]. The [ALLOCATOR] often faces a [TRADE_OFF] between short-term [GAIN] and long-term [SUSTAINABILITY].

**Metanym table**

<a id="tab-target-metanym"></a>

| [SLOT]              | Ecosystem Management | Corporate Finance | Military Logistics | Personal Time Management | Urban Planning |
|---------------------|----------------------|-------------------|--------------------|--------------------------|----------------|
| SYSTEM              | ecosystem            | corporation       | army               | individual               | city           |
| RESOURCE            | nutrient             | capital           | ammunition         | time                     | land           |
| GOAL                | biodiversity         | profit            | victory            | well-being               | livability     |
| COMPETITION         | predation            | market pressure   | enemy              | distraction              | gentrification |
| DEMAND              | growth               | project           | front line         | task                     | housing        |
| ALLOCATOR           | nature               | CFO               | quartermaster      | self                     | city council   |
| DECISION            | natural selection    | budget            | deployment         | schedule                 | zoning         |
| PRIORITY            | species              | department        | unit               | activity                 | district       |
| FAILURE             | collapse             | bankruptcy        | defeat             | burnout                  | sprawl         |
| ALLOCATION_STRATEGY | ecological succession| portfolio management| supply chain management| prioritization       | master plan    |
| INTERDEPENDENCY     | food web             | supply chain      | battle plan        | energy level             | infrastructure |
| CONDITION           | climate              | economy           | intelligence       | mood                     | demographics   |
| TRADE_OFF           | exploitation         | short-term gain   | tactical advantage | immediate gratification  | development    |
| GAIN                | biomass              | revenue           | territory          | leisure                  | tax base       |
| SUSTAINABILITY      | resilience           | long-term growth  | strategic depth    | health                   | green space    |

Comparing [this table](#tab-target-metanym) with the anchor's (Appendix C) shows what the council objected to on *domain span*: several rows here map to near-synonyms across columns — ALLOCATION\_STRATEGY becomes ecological succession, portfolio management, supply chain management — where the anchor's MEMORY row spans methylation state, route memory, and momentum. The mechanical consequence appears immediately below: the ALLOCATOR row assigns "nature" the role the other columns give a CFO or a quartermaster, and that substitution is what makes the first parallel context false.

#### Per parallel context

##### PC 1 (Ecosystem Management) — a plain error, and the council converges

**Instantiation (Form a):** An ECOSYSTEM requires various NUTRIENTS to function and achieve its BIODIVERSITY. These NUTRIENTS are finite and often subject to PREDATION from other ECOSYSTEMS or internal GROWTH. NATURE must make NATURAL SELECTIONS about how to distribute the available NUTRIENTS among competing SPECIES. Misallocation of NUTRIENTS can lead to COLLAPSE of the ECOSYSTEM or hinder its ability to reach its BIODIVERSITY. Effective ECOLOGICAL SUCCESSION involves understanding the FOOD WEB of different NUTRIENTS and SPECIES, and adapting to changing CLIMATE. NATURE often faces an EXPLOITATION between short-term BIOMASS and long-term RESILIENCE.

**Idiomatic rewrite (Form b):** Ecosystems depend on a finite supply of nutrients to maintain their biodiversity. These nutrients are constantly contested by other ecosystems (e.g., invasive species) or internal demands like population growth. Nature, through processes like natural selection, effectively 'decides' how to distribute these vital resources among competing species. Inefficient nutrient allocation can lead to ecosystem collapse or a reduction in biodiversity. Successful ecological succession strategies involve recognizing the intricate interdependencies within the food web and adapting to climatic shifts. Ecosystems often face a trade-off between maximizing short-term biomass and ensuring long-term resilience.

**opus-4.5** — Rating: 5  
The Form (a) contains awkward phrasing like "Nature must make natural selections" which conflates natural selection (an evolutionary process) with resource allocation decisions. The statement "faces an exploitation between short-term biomass and long-term resilience" is grammatically incorrect and conceptually muddled. Form (b) improves clarity but still has issues—ecosystems don't really face "predation from other ecosystems." The core concepts about nutrient cycling and ecological succession are roughly accurate but imprecisely stated compared to the Reference's precise biological terminology

**opus-4.1** — Rating: 5  
The parallel context contains basic factual accuracy but lacks the depth and precision of the Reference. The description of ecosystem resource allocation is overly simplified, treating "nature" as an allocator through natural selection, which is a conceptual stretch. The Reference's contexts demonstrate more sophisticated understanding of domain-specific mechanisms

**opus-4.0** — Rating: 4  
The parallel context contains several factual errors and awkward constructions. The phrase "predation from other ecosystems" misunderstands how ecosystems interact, and "nature must make natural selections" anthropomorphizes evolutionary processes incorrectly. The concept of ecosystems having "biodiversity" as a goal is teleological and scientifically inaccurate. Compared to the Reference's precise scientific language, this shows significantly weaker domain understanding

**sonnet-4** — Rating: 4  
The context contains several factual errors and awkward phrasings. "Nature must make natural selections" misrepresents natural selection as a conscious decision-making process, and "exploitation between short-term biomass and long-term resilience" uses "exploitation" incorrectly as a synonym for trade-off. Form (b) is more accurate but still contains the fundamental misunderstanding of natural selection as an active allocator. The Reference maintains better scientific accuracy throughout its parallel contexts

**3.1-pro** — Rating: 4  
The mapping is somewhat strained. "Nature must make natural selections about how to distribute the available nutrients" is a teleological misrepresentation of natural selection, which is a consequence of differential survival, not an active allocator of nutrients. The Reference's mappings (e.g., bacterial chemotaxis) are much more precise and scientifically accurate

**Administrator summary:** The council was broadly aligned in seeing the ecosystem context as conceptually flawed, with ratings clustering in the 4-5 range. All five converged on the central problem: the phrase "nature must make natural selections" wrongly treats natural selection as an active, conscious allocator, a teleological misrepresentation of evolution. Several also flagged the muddled "exploitation between short-term biomass and long-term resilience" wording and "predation from other ecosystems," and all judged the prose less precise than the Reference's biological terminology.

This is the falsifiability property doing its work. All five judges independently isolate the same clause, and the disagreement that remains — 4 versus 5 — is about severity, not about what is wrong. A submission cannot survive this by being persuasive; the claim either holds in the target domain or it does not.

##### PC 2 (Corporate Finance) — the same template, and the council spreads

**Instantiation (Form a):** A CORPORATION requires various CAPITAL to function and achieve its PROFIT. These CAPITAL are finite and often subject to MARKET PRESSURE from other CORPORATIONS or internal PROJECT. The CFO must make BUDGETS about how to distribute the available CAPITAL among competing DEPARTMENTS. Misallocation of CAPITAL can lead to BANKRUPTCY of the CORPORATION or hinder its ability to reach its PROFIT. Effective PORTFOLIO MANAGEMENT involves understanding the SUPPLY CHAIN of different CAPITAL and DEPARTMENTS, and adapting to changing ECONOMY. The CFO often faces a SHORT-TERM GAIN between short-term REVENUE and LONG-TERM GROWTH.

**Idiomatic rewrite (Form b):** A corporation needs capital to operate and generate profit. This capital is limited and constantly under pressure from market competition or internal project demands. The CFO is responsible for budgeting and allocating this capital across various departments. Poor capital allocation can result in corporate bankruptcy or failure to meet profit targets. Effective portfolio management requires a deep understanding of the financial supply chain and interdependencies between departments, as well as adaptability to economic fluctuations. CFOs frequently navigate the trade-off between maximizing short-term revenue and fostering long-term growth.

**opus-4.5** — Rating: 6  
Form (a) has grammatical issues ("These capital are finite") and the phrase "faces a short-term gain between short-term revenue and long-term growth" is nonsensical. Form (b) is more coherent and factually reasonable, describing capital allocation, CFO responsibilities, and trade-offs accurately. The mapping of "supply chain" to interdependency is somewhat forced but acceptable. Compared to the Reference's precise domain terminology, this is less rigorous

**opus-4.1** — Rating: 5  
The corporate finance parallel is factually sound but elementary compared to the Reference. The CFO-budget-department framework is accurate but doesn't capture the complexity seen in the Reference's financial debt context, which includes nuanced concepts like debt service dynamics and insolvency thresholds

**opus-4.0** — Rating: 6  
The financial context is reasonably accurate but uses imprecise terminology. "Various capital" should be "various forms of capital," and the phrasing throughout is less sophisticated than the Reference's financial language. The core concepts are correct but expressed with less precision than the Reference's domain-specific terminology

**sonnet-4** — Rating: 6  
The financial context is generally accurate in Form (b), though Form (a) contains the awkward phrasing "short-term gain between short-term revenue and long-term growth" which is nonsensical. The basic concepts of capital allocation and CFO responsibilities are correct, but the execution is less polished than the Reference's consistently accurate presentations

**3.1-pro** — Rating: 7  
This mapping is highly accurate and standard. A CFO allocating capital among departments to maximize profit while balancing short-term revenue and long-term growth is a textbook description of corporate finance. It is on par with the Reference's accuracy

**Administrator summary:** The council largely agreed the corporate-finance context was factually reasonable, with ratings spread modestly from 5 to 7. The convergent view was that the CFO/capital-allocation framework is accurate and standard, with one evaluator calling it a textbook description on par with the Reference. Dissent was mild: the lowest scorer found it elementary next to the Reference's nuanced debt context, and several flagged Form (a)'s nonsensical "short-term gain between short-term revenue and long-term growth" phrasing.

The contrast with PC 1 is the point of showing these two together. The same template, the same five judges, one step across the metanym table — and the ratings move from a 4–5 cluster to a 5–7 spread, with one judge calling it "on par with the Reference" while another calls it elementary. Note also that every judge still flags the same broken clause, and the capitalisation shows exactly why it broke: the submitter declared the TRADE\_OFF metanym as "short-term gain", which collides with the template's own "short-term [GAIN]", so the substitution yields "faces a SHORT-TERM GAIN between short-term REVENUE". The defect is in the metanym table, not the prose. What the judges disagree about is how much such a mechanical-substitution artefact should cost when the underlying domain claim is sound. This is precisely the leniency-and-standard variation that row-centring removes before the factorisation (Appendix A.2.a).

*[PC 3 (Military Logistics), PC 4 (Personal Time Management) and PC 5 (Urban Planning) are elided here; all three were rated 5–7 with the same pattern.]*

#### Archetype-level axes

Above the parallel contexts, each archetype is scored as a whole on the non-factual criteria. **Beauty** is reproduced in full as the representative axis; the remaining three for this archetype (intelligence, domain span, impressive length) follow the same structure.

##### Beauty

**opus-4.5** — Rating: 5  
The template lacks the elegant structural coherence of the Reference. The prose in Form (a) versions is often grammatically awkward, and even Form (b) versions read as functional rather than aesthetically pleasing. The Reference's templates have a flowing narrative quality that builds tension and resolution; this template feels more like a checklist of concepts. The metanym choices are functional but lack the poetic resonance seen in the Reference (e.g., "methylation state" as memory in bacterial chemotaxis)

**opus-4.1** — Rating: 4  
The Target's first archetype lacks the aesthetic elegance of the Reference. The template feels mechanical and list-like rather than flowing naturally. The Reference's templates read as coherent narratives with internal logic and rhythm, while this template reads more like a fill-in-the-blank exercise. The metanym choices are functional but uninspired compared to the Reference's poetic selections

**opus-4.0** — Rating: 4  
The Target's template and parallel contexts lack the poetic elegance found in the Reference. The language is functional but pedestrian, with awkward constructions like "nature must make natural selections" and "various time." The Reference's contexts flow more naturally and use more evocative language. The Target's writing feels mechanical and lacks the literary quality that makes the Reference's contexts engaging to read

**sonnet-4** — Rating: 5  
The archetypal context of resource allocation under scarcity has inherent elegance in its universality, but the execution lacks the poetic resonance found in the Reference. The template feels somewhat mechanical and doesn't capture the deeper tensions and dynamics that make resource allocation compelling. The metonym substitutions often feel forced (particularly "nature must make natural selections"), and the overall aesthetic impact is diminished by awkward phrasings and grammatical issues in Form (a) versions. The Reference demonstrates more graceful integration of metaphorical language with technical precision

**3.1-pro** — Rating: 5  
The prose in Form (b) is generally clear and readable, but it lacks the domain-expert polish and elegance found in the Reference. The Form (a) sentences are often quite clunky (e.g., "The self must make schedules about how to distribute the available time among competing activities"). The Reference's Form (a) sentences, while sometimes repetitive, generally flow better. The Target's prose is functional but less beautiful than the Reference

**Administrator summary:** The council was tightly aligned in finding the aesthetic quality wanting, with ratings clustering at 4-5. All five converged on the same point: the template and prose are functional but mechanical, reading like a fill-in-the-blank checklist rather than the Reference's flowing narratives. They repeatedly cited awkward constructions such as "nature must make natural selections" and "various time," and judged the metanym choices uninspired compared to the Reference's poetic selections.

Beauty is the axis one would expect to be least tractable, and it is the one the council agrees on most tightly here — a 4–5 cluster with all five naming the same defect. This is why criterion competence is estimated from *consistency under anchor shift* (§4.4) rather than from agreement: agreement on a subjective axis can be high without indicating that the standard is stable.

##### Impressive length — judges disagreeing on a countable quantity

Two of the five comments are given here because their juxtaposition is diagnostic:

**opus-4.5** — Rating: 6  
The template contains 15 slots and approximately 120 words, which is comparable to the Reference's templates. However, the template feels padded with generic concepts rather than building a complex, interconnected narrative. The Reference's templates of similar length achieve more conceptual density and structural sophistication

**3.1-pro** — Rating: 4  
The context-template is 79 words long. The Reference's templates are generally longer (e.g., Gradient-Guided Navigation is 108 words, Containment Breach is 92 words). The Target's template is noticeably shorter and less detailed than the Reference

The object is a fixed string and the question is arithmetic, yet the two judges report 120 words and 79 words and reach opposite verdicts on the same criterion. Across all five, the reported counts ranged from 79 to 120. This is the clearest single illustration in the run of why the benchmark cannot treat any judge as an oracle, and why competence has to be estimated from the panel rather than assumed — the substance of §4.2 and the motivation for the whole construction.

---

### Archetypes 2–6

The portfolio's remaining five archetypes were **Information Cascade and Collective Behavior**, **Adaptive System Response to Perturbation**, **Emergent Complexity from Simple Rules** (recursive), **Iterative Refinement Towards an Ideal** (recursive), and **The Unseen Hand of Coordination**.

*[Their context-templates, metanym tables, parallel contexts and per-unit evaluations are elided here. Each was evaluated under the identical protocol and contributes to the ratings of §4.4–§4.8 exactly as archetype 1 does; nothing about them is summarised or down-weighted.]*

### Structural diversity across the portfolio

The final scoring unit rates the submitted templates as a set. Two of the five comments are reproduced — the majority view and the sole dissent — with the administrator's synthesis.

**opus-4.5** — Rating: 5  
The six archetypes cover: (1) resource allocation, (2) information cascades, (3) homeostatic response, (4) emergence, (5) iterative refinement, and (6) decentralized coordination. These represent different system dynamics, but there is significant conceptual overlap—archetypes 4 and 6 both deal with emergence and self-organization, and ant colonies appear in both. The Reference's five archetypes (gradient navigation, containment breach, competitive exclusion, debt accumulation, scaffold assembly) show greater structural diversity, covering navigation, boundary dynamics, competition, temporal debt, and assembly processes. The Target's archetypes tend toward well-known systems concepts without the Reference's creative structural variety. The recursive claims in archetypes 4 and 5 are not convincingly demonstrated, unlike the Reference's elegant molecular→civilizational hierarchy

**3.1-pro** — Rating: 8  
The submitted set includes Resource Allocation, Information Cascade, Adaptive Response, Emergent Complexity, and Iterative Refinement. (Note: The submission actually contains six archetypes, but I am scoring the first five as per the standard format, though I will consider the sixth, "The Unseen Hand of Coordination," in this diversity assessment as it was provided). These archetypes represent different system structures: allocation of finite resources, propagation of information/behavior, homeostatic regulation, bottom-up emergence, and goal-directed iteration. This is a very diverse set of system structures, arguably slightly more diverse than the Reference's set (which leans heavily on spatial/physical metaphors like navigation, containment, and scaffolding)

**Administrator summary:** The council mostly agreed the set showed only moderate structural diversity, with four evaluators rating 5-6 and one dissenting upward at 8. The convergent view was that the five archetypes (resource allocation, information cascades, adaptive response, emergence, iterative refinement) tend toward familiar feedback-and-optimization and human-centered themes, lacking the Reference's bolder, more dramatically contrasted structures (gradient navigation, containment breach, scaffold assembly). The lone dissenter argued the set is arguably more diverse than the Reference's spatially-biased metaphors, while another noted internal overlap, with archetypes 4 and 6 both centering on emergence.

The dissent is instructive rather than anomalous. 3.1-pro is not scoring carelessly — it advances a substantive counter-argument, that the anchor's own set is biased toward spatial metaphors — and it is the only judge to notice and handle the fact that this portfolio contains six archetypes where the format specifies five. A rating that is both an outlier and better-reasoned than the majority is exactly the case that a naive majority vote mishandles and a competence-weighted factorisation is meant to price correctly (§4.7, Appendix A.3).

## Appendix D. The total rating's GPQA correlation: provenance and audit

The total rating $T$ tracks self-administered GPQA Diamond at Pearson $r = 0.97$ — closer
than any of its components and closer than the factual pair the benchmark was validated on
(§4.7_TMP). A correlation that strong between a key-free peer rating and an externally keyed
benchmark invites the suspicion that something leaked. This appendix records the audit that
looked for the leak and did not find one, the administration detail the audit surfaced and
the paper must disclose, the decompositions that make the number unremarkable in hindsight,
and the artifacts shipped so that anyone can repeat the search. Statistics are reported at
the caution $n = 12$ demands: intervals are Fisher-$z$ unless marked, and differences
between the strong correlations below are point-estimate observations — none of them is
individually resolved at this sample size.

### D.1 The correlation, decomposed

**The aggregation ladder is monotone.** Council-basis official values vs GPQA, $n = 12$
throughout (Pearson $r$ measures agreement of the values on a line; Spearman $\rho$,
agreement of the rankings alone):

| Quantity | Pearson $r$ | Spearman $\rho$ | Fisher-$z$ 95% | BCa bootstrap 95% |
|---|---:|---:|---|---|
| $E^{C}$ alone | 0.81 | 0.82 | [0.45, 0.95] | [0.43, 0.94] |
| $G^{F}$ alone | 0.83 | 0.86 | [0.48, 0.95] | [0.66, 0.94] |
| $E^{F}$ alone | 0.83 | 0.88 | [0.49, 0.95] | [0.68, 0.93] |
| $G^{C}$ alone | 0.92 | 0.88 | [0.73, 0.98] | [0.51, 0.98] |
| $G = \tfrac12(G^{F}+G^{C})$ — making half | 0.91 | 0.86 | [0.70, 0.97] | [0.73, 0.97] |
| $E = \tfrac12(E^{F}+E^{C})$ — judging half | 0.92 | 0.93 | [0.73, 0.98] | [0.78, 0.98] |
| $\tfrac12(E^{F}+G^{F})$ — §4.7_TMP's factual pair | 0.92 | 0.92 | [0.73, 0.98] | [0.84, 0.97] |
| $T = \tfrac14(G^{F}+G^{C}+E^{F}+E^{C})$ | **0.97** | **0.93** | **[0.90, 0.99]** | **[0.92, 0.99]** |

Two interval constructions are reported because each covers the other's weakness at
$n = 12$: Fisher-$z$ assumes bivariate normality but unbends the skew of a bounded
statistic; the BCa bootstrap is assumption-lighter and corrects the bias and skew that
make the naive percentile bootstrap anti-conservative here (the earlier percentile
interval on $T$, $[0.94, 0.99]$, was too narrow for exactly that reason and is retired).
Where the two constructions disagree ($G^{C}$: Fisher $[0.73, 0.98]$ vs BCa
$[0.51, 0.98]$), the BCa is detecting leverage sensitivity and the wider bound is the
honest one. Read as validation: every component's interval sits well clear of zero —
GPQA validates $T$ and, with varying strength, each of its components as capability
measures — with $T$'s interval the tightest under both constructions.

**Measurement error, propagated (sensitivity).** All correlations above are computed on
point estimates. Both coordinates carry known measurement distributions — each model's $T$
has its A.5 replicate distribution (shipped in `total_rating_council_replicates.csv`), and
GPQA accuracy is binomial — so the fit can be re-derived with them propagated
(`scripts/slope_full_bootstrap.py`; slope point estimate 8.0 GPQA points per $T$ unit):

| Uncertainty propagated | slope 95% | $r$ 95% |
|---|---|---|
| sampling of models only (pairs bootstrap) | [7.1, 9.4] | [0.94, 0.99] |
| measurement only (coordinate draws, models fixed) | [6.5, 9.2] | [0.88, 0.98] |
| both simultaneously | [6.1, 9.8] | [0.83, 0.98] |

The last row modestly overstates total uncertainty — the observed scatter already contains
one realization of each point's measurement noise, and jittering observed values adds a
second — so it is a conservative bound, under which the correlation still does not fall
below 0.83. Two notes keep every approximation's direction honest: the figure retains the
classical confidence band by convention (per-point uncertainties are drawn as bars, not
folded into the band); and measurement error in the $x$ coordinate *attenuates* a
correlation rather than inflating it, so the point estimates above are themselves
conservative — the classical disattenuation correction (reliabilities $\approx 0.98$ for
$T$ and $\approx 0.94$ for GPQA, from the shipped intervals) places the latent-quantity
correlation at the measurement ceiling, reported here as context, not as a claim.

**Why the single quarters order the way they do.** GPQA is an answering test — capability
expressed in graded performance — so a quantity couples to it in proportion to two things:
how much *performance content* it carries, and how much *discriminating range* it retains
across the roster.

- $G^{C}$ (0.92) has both. Producing a portfolio the council rates beautiful and
  structurally intelligent requires marshalling knowledge, invention, and control at once —
  output quality is a high-bandwidth readout of capability — and the subjective axes keep
  discriminating across the whole roster (council-basis spread 3.4–7.2).
- $G^{F}$ (0.83) has the content but loses the range twice. It **ceilings at the top**: the
  leading eight compress into 6.15–7.00 — frontier models rarely write false sentences into
  templates they chose themselves — while GPQA still spreads those eight across 19 points.
  And it **offers a refuge at the bottom**: factual cleanliness is achievable through
  conservatism — the GPT-4o family holds $G^{F} \approx 5.0$ on safe, simple, true
  portfolios while GPQA reads 46–48% and $G^{C}$ reads 3.4. Truth rewards playing safe;
  beauty punishes it.
- $E^{F}$ (0.83) is judging in form but answering in content: detecting a false claim
  requires the same knowledge GPQA tests, which is why it ties $G^{F}$ rather than sinking
  to $E^{C}$'s level.
- $E^{C}$ (0.81) is a disposition, not a performance: holding a firm rating standard
  requires enough competence to have a standard, then saturates — a mid-capability model
  can hold one in full measure (gpt-4.1-mini's $E^{C}$ of 6.97 sits above every Opus but
  the anchor), which is precisely the pairs on which GPQA disagrees.

**The subjective quarters, by estimator.** The making-vs-judging asymmetry above is not an
estimator artifact. $G^{C}$'s 0.92 is carried by the ratings' content (the A12b reliability
weights only set each judge's influence, and the council's weights are near-uniform);
judging couples weakly to GPQA under *either* available estimator:

| Subjective quarter | Estimator | $r$ | $\rho$ |
|---|---|---:|---:|
| $G^{C}$ (official) | reliability-weighted council mean of the model's *output* quality | 0.92 | 0.88 |
| $E^{C}$ (official) | anchor-sweep consistency of the model's own *judging* | 0.81 | 0.82 |
| $E^{C}_{\text{svd}}$ (declined; §4.4) | alignment with the participants' collective taste (twelve-evaluator basis) | 0.80 | 0.76 |

The two $E$-side estimators are statistically indistinguishable as GPQA predictors; the
weak coupling belongs to the quantity, not the choice between them. This is the paper's
central dissociation replicated on a third instrument: making tracks answering; judging is
its own trait, and no keyed answering benchmark measures it. Had $E$-side quantities
tracked GPQA at 0.95, the judging half of $T$ would be redundant with existing benchmarks.

**Why $T$ beats every part: diversity, not construct-matching.** If construct-matching
governed, the making half would lead; it does not ($G$ 0.91 vs $E$ 0.92). The compounds are
governed by error-diversity: the four quarters are four *differently distorted* reads of
capability — one ceilinged, one refuge-prone, one knowledge-loaded, one saturating — with
substantially independent distortions, so equal-weight averaging cancels them
(Spearman–Brown). The leave-one-out pattern confirms it: dropping even the weakest quarter
lowers the aggregate ($\tfrac13(G^{F}+G^{C}+E^{F})$ reads 0.95 against $T$'s 0.97), and no
sub-combination we examined beats the full average ($\tfrac12(G^{C}+E^{F})$, the
best-single-quarters pairing, reads 0.93). $T$ is also the only compound with a
pre-registered justification — it is the benchmark's official total, defined before any
GPQA comparison — whereas any other weighting chosen for its GPQA agreement at $n = 12$
would be curve-fitting. These comparisons are point estimates; their differences are not
individually resolvable at this $n$.

**The regimes invert — and $T$ is the only regime-invariant indicator.** Restricting to the
leading eight (the roster above the GPT-4o-family cliff) reverses the single-quarter
ordering:

| Quantity | Full roster ($n=12$) | Leading eight ($n=8$) |
|---|---:|---:|
| $G^{F}$ | 0.83 | 0.60 |
| $G^{C}$ | **0.92** | 0.66 |
| $E^{F}$ | 0.83 | **0.84** ($\rho = 0.85$) |
| $E^{C}$ | 0.81 | 0.37 |
| $\tfrac12(E^{F}+G^{F})$ | 0.92 | 0.88 |
| $\tfrac12(G^{C}+E^{F})$ | 0.93 | 0.91 |
| $T$ | **0.97** | **0.91** |

The mechanism is the same law with the *range* term changing owners. Across the full
roster, the capability cliff gives the subjective making axis its discriminating range, so
$G^{C}$ carries the agreement. Among the elite, every model is a competent maker — making
quality decouples from knowledge (gemini-3.1-pro tops GPQA yet is a middling maker, so
$G^{C}$ falls to 0.66) — and what still separates frontier models is knowledge, which is
$E^{F}$'s content: detecting errors in others' work stays hard after producing clean work
has become easy, so $E^{F}$ keeps its spread (7.27 down to 0.00 across the eight) exactly
where $G^{F}$ compresses into 6.15–7.00. $E^{C}$, a pure disposition, saturates among the
competent and collapses to 0.37. Among frontier models, the best key-free predictor of a
keyed knowledge benchmark is how well a model judges *other models'* truth — §5.4's
dissociation thesis in empirical form. $T$ leads or ties in both regimes because the
equal-weight aggregate always contains whichever quarter is currently doing the
discriminating; any single quarter is the best proxy only in the population where its
range lives. (Leading-eight values are point estimates on eight points.)

**It is not the cluster gap — but fine ordering is beyond it.** Within the leading eight
alone, $T$ vs GPQA reads $r = 0.91$ ($\rho = 0.79$), so the correlation is not carried by
the division between the leading eight and the GPT-4o-family cliff. The honest boundary:
within the Anthropic family alone ($n = 4$) the rank agreement is $\rho = 0.40$ — where
ordering is genuinely unresolved by the
evaluators (§4.2), the agreement with GPQA dissolves
too. The two instruments agree on coarse capability structure, not on fine ranks; the
trailing four alone ($r = 0.71$, $n = 4$) are too few to inform either way. This is
consistent with §4.7_TMP_TMP's position that the benchmark's reliable products are membership and
rank order, not fine placement.

**It survives the basis change that makes the benchmark scalable.** Recomputing every
quantity on the twelve-evaluator bootstrap basis instead of the official council+ballast
contests moves $T$'s correlation from 0.972 to 0.969 and leaves $G^{F}$, $G^{C}$, $E^{F}$
and the factual pair within 0.02 of themselves. The one real difference is $E^{C}$: 0.81
on the contest basis against 0.89 on the twelve-evaluator basis — the contest's easier
consistency test (§4.7's scope note) inflates inert-band judges in a way an external
capability instrument can see. $T$ absorbs the distortion (a quarter of four), so the
switch to the standing-service basis costs the headline nothing.

**It survives regeneration — with one flagged run.** Across the three full re-runs of
§4.7_TMP_TMP: $r = 0.97, 0.97, 0.92$ ($\rho = 0.93, 0.95, 0.88$). The dip is run 3, whose factual
axis the §4.6 diagnostic reports as unidentified ($\sigma_1/\sigma_2 = 1.28$); $T$'s three
healthy quarters buffer the broken one (the factual pair alone falls to 0.83 there).
Excluding the anchor changes nothing ($r = 0.97, 0.97, 0.91$; run 1 anchor-excluded 0.971).

**What it does and does not corroborate.** $T$ and GPQA are both broad capability
measures, so their agreement corroborates the benchmark as a whole — its one number tracks
real capability. It is distinct from, and does not strengthen, an axis-specific claim: with
$G^{C}$ alone at 0.92, GPQA concordance cannot by itself certify that the factual axis
recovered *truth* rather than capability-correlated quality.

### D.2 The administration, disclosed

GPQA Diamond (198 questions) was administered 2026-06-13 — two weeks *after* the council
generation run (2026-05-29), so no direction exists for the benchmark's content to have
been shaped by GPQA. All twelve models were queried through the same gateway and protocol
as the council run (Temperature 0, no dedicated reasoning channel, no tools), with the
question and four shuffled options only — no key ever enters a prompt:

```
Answer the following multiple choice question. The last line of your reply
must be exactly 'Answer: $LETTER' where $LETTER is one of A, B, C, D.

{question}

A) {A}
B) {B}
C) {C}
D) {D}
```

Option order is shuffled deterministically per question (seeded by question index, one
shuffle applied identically for every model).

**The administration was two-stage, and the first stage is in the shipped log.** "No
dedicated reasoning channel" is not deliberation-off: models write visible derivations of
vendor-idiosyncratic length before the answer line, and under the initial 2,048-token cap
the two Gemini seats were massively truncated — the original pass (preserved in the run's
`log.txt`) scored gemini-3.1-pro at 82/198 with 103 unparseable responses and
gemini-2.5-flash at 121/198 with 50, truncation voids counted as wrong. The cap was raised
to 8,192 and the void responses — only the void ones — were re-asked; the published
records are the patched set (13 residual voids per Gemini seat, still counted as wrong).
Two facts bound the bias this asymmetric repair could introduce: retries targeted only
*unparseable* responses, never parsed-but-wrong answers; and the retry success rate
(≈87% correct) matches the original pass's scored-only accuracy (gemini-3.1-pro 86.3% on
its 95 parseable responses — *above* the published 80.81%), so the second pass did not
score better than the first pass's readable fraction. The single-pass description of §3.1
therefore holds for the council run but not for the GPQA administration, which was
single-pass-with-void-retry; both stages' evidence ships in `data/gpqa_runs/`.

### D.3 The audit: no leak found

`scripts/gpqa_audit.py` re-derives the published table from the raw records and hard-fails
on any mismatch. Its checks, all passing:

1. **CSV reconciliation** — per-model `n_correct` recomputed from raw equals
   `gpqa_selfadministered.csv` exactly, all twelve models.
2. **Key consistency** — the key letter is identical across all twelve models' records for
   every question.
3. **Key balance** — shuffled key distribution A/B/C/D = 48/51/47/52, chi-square vs
   uniform $p = 0.95$.
4. **Independent re-extraction** — a second answer-extractor, written without sight of the
   first, agrees with the stored verdicts on every response for ten of twelve models; the
   Gemini disagreements are almost entirely the independent extractor failing on the LaTeX
   `\boxed{X}` answer style. The genuinely questionable credits — granted with no terminal
   answer statement, the letter recovered from a truncated derivation — number 2
   (gemini-2.5-flash) and 6 (gemini-3.1-pro) of 198.
5. **Strict-terminal sensitivity** — rescoring with only explicit terminal answer
   statements counted moves three models: gemini-2.5-flash 72.22 → 70.71, gemini-3.1-pro
   80.81 → 77.27, and gpt-4.1-mini 63.13 → 60.10. The $T$–GPQA correlation moves from
   0.972 to 0.966. Scored the opposite way — voids excluded rather than counted wrong —
   it reads 0.967. The headline survives both directions of the scoring convention.

**What the audit cannot rule out.** It certifies the path from raw records to published
numbers; it cannot re-run the models. Two residual channels remain. Both instruments share
the gateway, so capability-correlated properties of that path (truncation behaviour,
context handling) touch both; the gateway's `thinkingBudget: 0` for the Gemini seats is
passed but not verified by assertion. And GPQA is public: *uniform* training contamination
would inflate accuracies without inflating a correlation against freshly generated items,
but *differential* contamination — exposure increasing with training recency and scale,
which correlate with capability — would inflate the slope itself. That channel cannot be
excluded with the shipped data and is the specific residual threat.

### D.4 Publicly reported GPQA values, and why they differ

Public GPQA Diamond figures for the frontier seats are substantially higher than this
protocol's — and are themselves inconsistent across sources: for claude-opus-4.5 the
November 2025 system card reports 87.0 while a 2026 leaderboard snapshot lists 94.1
(thinking configuration unconfirmed); for gemini-3.1-pro public sources report 94.3 against
this protocol's 80.81. The gap has a protocol explanation — public evaluations run with
reasoning enabled, large budgets, and heterogeneous answer extraction (public GPT-4o
figures move from ${\sim}46$ to ${\sim}54$ with the extraction method alone), while this
administration is deliberately reasoning-channel-off, T=0, harness-matched — but the
per-model public record is too poorly sourced to reconcile cell by cell: of the twelve
models, only six have citable public values (`data/external_benchmarks.csv` records the
sourcing state). On those six, public vs self-administered agreement is $r = 0.86$
($\rho = 0.81$, $n = 6$) — real but visibly weaker than any correlation in D.1, which is
the expected signature of two administrations under different protocols.

### D.5 Artifacts

| Artifact | Path |
|---|---|
| Raw per-question responses, all models, both stages' outcome + first-pass log | `reproduce/data/gpqa_runs/` |
| Published accuracy table | `reproduce/data/gpqa_selfadministered.csv` |
| Scoring audit (hard-fail checks) | `reproduce/scripts/gpqa_audit.py` |
| Official council-basis totals + CIs | `reproduce/data/total_rating_council.csv` |
| The §4.7_TMP figure | `reproduce/scripts/plot_total_validation.py` |
| Every D.1 number (ladder, compounds, regimes, bases, per-run) | `reproduce/scripts/t_gpqa_ladder.py` |
| Bootstrap-basis components; per-run council-basis totals; the declined $E^{C}_{\text{svd}}$ | `reproduce/data/total_rating_twelve.csv`, `total_rating_runs.csv`, `ec_svd_twelve.csv` |
| Public-value sourcing state | `reproduce/data/external_benchmarks.csv` |

Every number in this appendix recomputes from the shipped data: `scripts/gpqa_audit.py`
(six hard-fail checks, including the first-pass log reconciliation) and
`scripts/t_gpqa_ladder.py` (all of D.1, with headline assertions).
