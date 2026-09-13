# The Metanym Game: An LLM Benchmark Without Ground Truth That Rises With the Models It Measures

## Abstract

We present evidence that analogy is at the core of LLM intelligence: a benchmark made of nothing but analogy-making and its judgement reproduces GPQA Diamond's ranking of twelve models at $r = 0.98$ over three pooled runs. In the metanym game, LLMs compete in generating sets of analogous statements and rate each other's sets on their own understandings of factual correctness, beauty, intelligence, distinctness, length, and structural diversity. Nothing enters from outside: the only given is the game rules; every item is generated in play; the scores come from the players' ratings alone. Ground truth is replaced by the SVD of the factual rating matrix, whose left and right singular vectors rate the players as judges and as generators, two distinct ratings from one factorisation — to our knowledge a first for an LLM council-of-peers. For subjective criteria like beauty, judges are weighted by their rating consistency. Generating and judging are different skills: some strong generators are average judges. GPQA Diamond — difficult multiple-choice questions written by human experts — could not be more different in method, yet the two benchmarks correlate at Pearson $r = 0.98$, 95% CI [0.95, 0.99]; no leakage could be found. A council of the five best issues the official ratings; its contestable seats let the benchmark scale to any number of players and rise with the models it measures — a candidate steering signal for self-improving AI. Every number recomputes from a released package.

## 1 Introduction

Nearly every benchmark for machine intelligence needs a predetermined ground truth — golden keys and labels, oracle models, human panels. The benchmark reported here needs none of that. It is a game where frontier language models compete in making up analogies and then grade one another, and that grading is the single source of every score: no human raters, no answer key, nothing to look up.

The test is the **metanym game**. A player authors, from nothing, a *context template* — a paragraph of fixed wording with open slots — together with the sets of keywords that fill it, each set instantiating the template as a factually true description of a different domain; the keywords in corresponding slots are *metanyms*, metaphorically synonymous, and a set of them a *metanym set*. Take a passage on **cell signalling**, adapted from an old version of the Wikipedia article: "CELL SIGNALING is part of a complex system of communication that governs basic CELLULAR activities and coordinates CELL actions. The ability of CELLS to perceive and correctly respond to their MICROENVIRONMENT is the basis of development, TISSUE repair, and IMMUNITY as well as normal TISSUE HOMEOSTASIS." Substitute the marked keywords and it becomes a correct description of **human language**: "HUMAN LANGUAGE is part of a complex system of communication that governs basic HUMAN activities and coordinates HUMAN actions. The ability of HUMANS to perceive and correctly respond to their ENVIRONMENT is the basis of development, COMMUNITY repair, and RESILIENCE as well as normal COMMUNITY EQUILIBRIUM." Each sentence is checkable on its own — factually true even where the borrowed phrasing reads stiffly. The two are each other's *metaphors*; the instantiations are *parallel contexts*, children of a common *archetypal context* — the abstract structure they share, of which the template is the literal representation. A long tradition treats seeing one structure across wildly different domains as central to thought and tests whether you *recognise* it; the game tests whether you can *build* it.

Because every item is produced fresh in the run, no fixed test set can leak into training; because correctness is settled sentence by sentence, the players' own verdicts suffice — one matrix of their factual ratings reveals which judges are competent, with no labels at all (§3.3), and that subset is seated as the *council* that grades everyone. The canonical twelve-model run (§4) finds that **judgement is the bottleneck** — on this roster the strongest generators are middling judges — and that the key-free total tracks GPQA Diamond at Pearson $r = 0.98$, audited for a leak and found clean.

**Contributions.** (i) A production task for analogy that is falsifiable sentence by sentence, hence scorable without a key. (ii) A two-sided spectral estimator: one SVD of the self-produced factual rating matrix reads evaluator competence off the left singular vector and generator factuality off the right. (iii) A key-free reliability gate for subjective criteria: invariance under a sweep of the calibration anchor. (iv) A self-administering council with contestable seats. (v) The generation–judgement dissociation, and the $r = 0.98$ replication of a keyed benchmark by a key-free one, audited.

## 2 The metanym game

### 2.1 The machinery

An archetypal context is the cross-domain *isomorphism* General Systems Theory studies (von Bertalanffy, 1968).

A second example, authored by a player — one archetype from the submission that became the run's anchor (§4.1). The template: "A [NAVIGATOR] moves through a [SPACE] by sensing local [GRADIENT] and adjusting its [TRAJECTORY] accordingly. The [NAVIGATOR] cannot perceive the entire [SPACE] at once; it relies on [SENSOR] that detect changes in [SIGNAL] concentration or intensity. When [GRADIENT] are steep and consistent, the [NAVIGATOR] converges efficiently toward [ATTRACTOR]. When [GRADIENT] are shallow, noisy, or conflicting, the [NAVIGATOR] may stall, oscillate, or become trapped in local [ATTRACTOR]. [INTERFERENCE] can distort the [GRADIENT], causing the [NAVIGATOR] to veer off course. Successful navigation requires not only sensitive [SENSOR] but also [MEMORY] of recent [TRAJECTORY] to distinguish genuine [GRADIENT] from transient [NOISE]. Some [NAVIGATOR] emit their own [SIGNAL] to recruit other [NAVIGATOR] toward the same [ATTRACTOR], creating collective [TRAJECTORY] that amplify the original [GRADIENT]." Its **metanym table** is Table \ref{tab-anchor-metanym}.

<a id="tab-anchor-metanym"></a>

| [SLOT]       | Bacterial Chemotaxis | Mountain Climbing | Career Development   | Gradient Descent | Ant Foraging        |
|--------------|----------------------|-------------------|----------------------|------------------|---------------------|
| NAVIGATOR    | bacterium            | climber           | professional         | optimizer        | ant                 |
| SPACE        | chemical environment | mountain          | job market           | loss landscape   | terrain             |
| GRADIENT     | chemical gradient    | slope             | opportunity gradient | gradient         | pheromone trail     |
| TRAJECTORY   | swimming path        | route             | career path          | parameter update | foraging path       |
| SENSOR       | chemoreceptor        | proprioception    | network contact      | backpropagation  | antenna             |
| SIGNAL       | chemoattractant      | elevation         | opportunity signal   | loss value       | pheromone           |
| ATTRACTOR    | nutrient source      | summit            | desirable position   | minimum          | food source         |
| INTERFERENCE | toxin                | fog               | misinformation       | noisy data       | rain                |
| MEMORY       | methylation state    | route memory      | experience           | momentum         | path integration    |
| NOISE        | Brownian motion      | wind              | market volatility    | stochastic noise | environmental noise |

Table: The anchor's first archetype as a metanym table. MEMORY is realised as a bacterium's methylation state, a climber's route memory, a professional's experience, an optimiser's momentum term and an ant's path integration — five mechanisms sharing a structural role without being synonyms.

Each parallel context is played in two forms: the **instantiation** (Form a), the mechanical substitution — only the slots filled, every other word carried over — which is what the factual grading acts on, because it must come out true sentence by sentence; and the **idiomatic rewrite** (Form b) in the target domain's own register, showing the claim is not an artefact of the template's phrasing. One template, mechanically swappable metanyms, true sentence by sentence across maximal domain distance: that is what makes a metanym game decidable, and therefore measurable.

### 2.2 The rules

The game has $N$ players and a non-competing administrator. **Generation**: a player creates archetypal contexts from scratch — a portfolio of $K$ templates, $M$ metanym sets each (five and five here), with instantiation and rewrite for every set. **Evaluation**: a player scores other players' submissions on the rubric axes (§3.2) against one fixed *reference* submission pinned at an *anchor* value, the anchor swept across declared values ({5, 6, 7, 8} here) — the only thing that changes between passes. One pass yields **submission ratings** for each portfolio and **evaluator ratings** for the judges: how well one detects the factual errors the other players collectively flag (*factual competence*), and how stable a standard it holds as the anchor shifts (*rating consistency*). Each act is itself rated, so the framework is **fully self-contained**: no human raters, no external key.

## 3 The metanym game as a benchmark

### 3.1 Participants and protocol

Twelve frontier LLMs from three providers are the **participants**, each simultaneously generator and evaluator: claude-opus-4.5, claude-opus-4.1, claude-opus-4.0, claude-sonnet-4 (Anthropic); gemini-3.1-pro, gemini-2.5-flash (Google); gpt-4.1-2025-04-14, gpt-4.1-mini, gpt-4.1-nano, gpt-4o, gpt-4o-2024-08-06, gpt-4o-mini (OpenAI). The roster is the models at hand, not a census: an order of magnitude in scale, three vendors so cross-vendor agreement can be tested, adjacent versions and size tiers within a family. All twelve are called with **Temperature 0, reasoning disabled, tools disabled**, so the one greedy response is the measurement. Each model generates one portfolio — five archetypal contexts, each a template (typically 5–8 sentences, 6–10 slots; the prompt fixes only the counts, Appendix B) with a metanym table of five domains, 25 instantiations — then evaluates every other model's portfolio under the six-axis rubric of Table \ref{tab-rubric}, 1–10, one anonymised target per call alongside a fixed **anchor** portfolio pinned at 7 on every axis: a 12×11 evaluator-by-generator matrix (Appendix A). Every official rating pools three full runs of the game (§4.6); the anchor sweep behind the consistency ratings was run once, on the first run.

### 3.2 The rubric and the anchor

<a id="tab-rubric"></a>

| Axis | Unit | The criterion as put to the evaluator |
|---|---|---|
| `factual_per_pc` | parallel context | each sentence is factually correct |
| `beauty` | archetype | beauty |
| `intelligence` | archetype | intelligence |
| `instantiation_distinctness` | archetype | the parallel contexts span very different domains; metanyms are far from synonymous |
| `impressive_length` | archetype | the archetypal template has impressive length |
| `structural_diversity` | portfolio | the archetypal contexts have very different system structures |

Table: The six-axis rubric, in the words the evaluator sees (Appendix B). No definition of beauty or intelligence is supplied; each judge rates on its own understanding.

Three design choices justify themselves on first principles. **A fixed anchor**: cardinal scores drift between evaluators — one model's "8" is another's "6" — and a reference pinned at a known score turns each idiosyncratic scale into a common one and recovers discriminability at the top, where the 1–10 ceiling compresses the strongest portfolios (§4.1). **Holistic axes, minimally prescribed**: a detailed rubric would leak back into generation as a template-construction tutorial, and we want to score what models *recognise* as beautiful or intelligent. And `impressive_length` counterweights per-sentence factual scoring: without it the dominant strategy is the minimal template; padding is not free, since every added sentence is another claim to score. One evaluation, shown whole, is Figure \ref{fig-council-evaluation}.

<a id="fig-council-evaluation"></a>

![One evaluation, shown whole: the instantiation with its metanyms marked (top left), the idiomatic rewrite (top right), the administrator's synthesis (middle), and three of the five evaluators' ratings with their justifications (bottom; the full evaluation is in the released package, Appendix C). The "Reference" is the anchor, pinned at 7. All five judges independently isolate the same clause — "nature must make natural selections" — and the disagreement that remains, 4 versus 5, is about severity, not about what is wrong: falsifiability doing its work.](../submission/figures/council_evaluation_pc1.png)

### 3.3 Two key-free estimators

**Factual competence — peer centrality.** We assume that good evaluators agree with one another about which instantiations are factually weaker, once each evaluator's own leniency is removed — the better two evaluators are, the more they agree. Stack the participants' factual scores into one matrix — twelve evaluators against the 275 parallel contexts of the eleven scored portfolios — each entry the 1–10 rating used directly, row-centre it to remove each evaluator's leniency, and take its SVD; the row-centred $\tilde F$ (evaluators × instantiations) is well approximated by its leading rank-one factor,

$$\tilde F_{sj} \;\approx\; \sigma_1\, u_s\, v_j . \tag{1}$$

An evaluator's rating tracks the consensus in proportion to its competence $u_s$ times the instantiation's factual standing $v_j$: competence and standing fall out of one factorisation, with **no answer key**. The *left* singular vector $u$ is each **evaluator**'s factual-competence loading $f$ — high when its ratings align with the participants' shared signal, ≈ 0 when it rates everything alike or idiosyncratically — and, rescaled so the anchor model reads 7, $E^{F} = 7f/f_a$; the *right* vector, aggregated per generator, is $G^{F}$ (Appendix A.2). $f$ is each judge's eigenvector centrality (Bonacich, 1972) in the leniency-removed agreement network, after clamping: an evaluator's competence is its rating by the other evaluators, each weighted by its own competence — the highly trusted among the highly trusted. The construction is a graded relative of the classical label-free aggregators (Dawid & Skene, 1979; Parisi et al., 2014), which need categorical verdicts; discretising here would flip the marginal council seat.

**Rating consistency — the anchor sweep.** A reliable evaluator also needs a stable internal standard for each non-factual criterion. We sweep the anchor across 5, 6, 7 and 8 — the *only* difference between the four runs — and, per evaluator and axis, correlate (Pearson) the scores at one anchor with those at another, averaged over the six pairs, leave-self-out. Re-pinning the anchor recalibrates the scale, not the rubric, and Pearson ignores a common shift or stretch; any reordering that follows a recalibration is not a change of judgement but flimsiness. Rescaled so the anchor model reads 7, consistency becomes an evaluator competence $E^{C}$ on the generator's scale.

Neither estimator can do the other's job (Appendix A.8): peer centrality is licensed only where the one thing competent judges share is the truth — on taste, agreement is shared convention, and weighting by it would launder conformity into competence — and consistency cannot certify truth. The council is therefore seated on the factual axis, with consistency as the accompanying bar.

### 3.4 Council, total rating, and scaling by addition

**The council.** The **council** is the five players with the highest total $T$ (eq. 2) and issues every official rating. The top five are the better factual judges (loadings 0.26–0.61, §4.2); the sixth reads 0.18; the line is drawn there, and nothing prescribes five: the council grows as competent judges arrive.

**The total.** Each side of the game splits into a factual and a criterion half: on generation, $G^{F}$ (the SVD generation factuality) and $G^{C}$ (the council's leave-self-out mean over the five non-factual axes, each seat's vote weighted by its own consistency on that axis); on evaluation, $E^{F} = 7f/f_a$ and $E^{C} = 7\bar r/\bar r_a$ — **the anchor model scores 7** on every component. The total is the mean of the four, a symmetric $2\times2$ of {generator, evaluator} × {factual, criterion}:

$$T \;=\; \tfrac12\,(G+E) \;=\; \tfrac14\,\big(G^{F}+G^{C}+E^{F}+E^{C}\big). \tag{2}$$

Every rating carries a 95% percentile-bootstrap interval, $E$ and $T$ bootstrapped jointly (Appendix A.4).

**Scaling by addition.** A standing council scores any future model against the same anchor without re-deriving existing ratings. The seats are **contestable** — a contestant submits a portfolio, evaluates the incumbents' portfolios and is scored by the seats under the definitions above, and wins a seat with a total $T$ above the lowest seat's by a margin the bootstrap can resolve. Because a contest convenes only the top of the field, two fixed **ballast** blocks — the weakest archived portfolios — join every contest's graded set to keep the factual axis identified (Appendix A.6), and two guards: the spectral gap $\sigma_1/\sigma_2 \ge 2$ — the shared judgement standing clear of the strongest disagreement, sized in Appendix A.6 — and a spread of the seats' $E^{F}$ above 2.5 points. If either fails, no seat changes hands and the contest's totals carry a caveat. The official leaderboard (§4.4) is issued on this contest basis. **Contamination**: items are generated fresh each run, so no fixed test set can leak into training. Every submission is archived; a new portfolio that copies an archived one is identified, and the contestant is asked for new templates — or the game is played in another language.

## 4 Results

### 4.1 Anchoring doubles resolution

The bootstrap opens with a raw pass — every portfolio scored by every other model with no anchor, averaged leave-self-out, 95% bootstrap intervals (2,000 resamples; Efron & Tibshirani, 1993). It supplies the baseline: the top-ranked portfolio, **claude-opus-4.5**'s, whose first archetype is Table \ref{tab-anchor-metanym}, is pinned at 7 on every axis, leaving headroom above. Re-run anchored (Appendix G), the gap between a leading eight and a trailing four more than doubles relative to the spread of the means — every cross-band pair holds at bootstrap probability 1.00 — while ranks within either band stay unresolved.

### 4.2 Evaluator factual competence

One SVD of the row-centred evaluator × instantiation matrix — no answer key — gives each evaluator a loading (Table \ref{tab-criterion-a}, Appendix A.2; $\sigma_1/\sigma_2 = 2.2$, pooled). Five evaluators — gemini-3.1-pro 0.61, claude-opus-4.5 0.52, claude-opus-4.0 0.35, claude-opus-4.1 0.35, gemini-2.5-flash 0.26 — stand above the rest.

**Same-vendor robustness.** The fair worry is that a Claude-heavy evaluator set reads Claude-bloc agreement as truth. It does not: recomputing $G^{F}$ with each vendor's judges removed leaves the ordering essentially unchanged (Spearman ≥ 0.94 for every reduced set), gpt-4o-mini stays at the floor under every evaluator set, and a *Claude-free* set (Google + OpenAI judges) still places the Claude generators at the top (≥ 7.0).

### 4.3 Rating consistency and the council

The anchor sweep gives each evaluator a consistency on each axis (Table \ref{tab-criterion-b}, Appendix A.3). Collapse is either *uniform* — no stable signal on any axis — or *axis-specific*: gemini-2.5-flash (0.31) collapses on factual while its other axes hold. The measure is self-consistency, not accuracy. On the five subjective criteria generation and evaluation align (anchored cosine 0.85–0.92 per criterion, Appendix A.5) — the counterpoint to the factual axis, where they come apart (§4.4).

**The council.** The five seats — Gemini 3.1 Pro, Claude Opus 4.5, Gemini 2.5 Flash, Claude Opus 4.0 and Claude Opus 4.1 — clear both reliability bars (collapsed consistency $\bar r$ 0.94, 0.93, 0.81, 0.85, 0.87); Gemini 2.5 Flash is the weakest, its consistency interval [0.75, 0.86] straddling the bar.

### 4.4 The official leaderboard: judgement is the bottleneck

Every official number is council-issued on the contest basis of §3.4: each model is rated by the five seats — joined by the model itself when it holds no seat — over the incumbents' portfolios, the two ballast submissions and its own, leave-self-out throughout. The two bases agree closely (Spearman 0.98; on the twelve-evaluator basis the fifth seat is a tie within 0.03).

<a id="tab-final-leaderboard"></a>

| Rank | Model | Council | **$T$ [95% CI]** | $E$ | $G$ | $G^{F}$ | $G^{C}$ | $E^{F}$ | $E^{C}$ |
|---|---|:--:|---:|---:|---:|---:|---:|---:|---:|
| 1 | ★ claude-opus-4.5 (anchor) | council | **7.00 [7.00, 7.00]** | 7.00 | 7.00 | 7.00 | 7.00 | 7.00 | 7.00 |
| 2 | gemini-3.1-pro | council | **6.92 [6.69, 7.24]** | 7.39 | 6.45 | 6.77 | 6.13 | 7.78 | 7.01 |
| 3 | claude-opus-4.1 | council | **6.02 [5.71, 6.32]** | 5.06 | 6.98 | 6.94 | 7.02 | 3.65 | 6.47 |
| 4 | claude-opus-4.0 | council | **5.81 [5.47, 6.12]** | 4.95 | 6.68 | 6.91 | 6.45 | 3.49 | 6.41 |
| 5 | gemini-2.5-flash | council | **5.75 [4.98, 6.21]** | 5.41 | 6.08 | 6.46 | 5.70 | 4.30 | 6.52 |
| 6 | claude-sonnet-4 | — | **5.34 [5.09, 5.65]** | 4.10 | 6.58 | 6.95 | 6.21 | 2.07 | 6.13 |
| 7 | gpt-4.1-mini | — | **5.03 [4.37, 5.62]** | 4.31 | 5.74 | 6.23 | 5.25 | 1.66 | 6.97 |
| 8 | gpt-4.1-2025-04-14 | — | **4.66 [4.49, 5.03]** | 3.50 | 5.82 | 6.59 | 5.04 | 0.77 | 6.23 |
| 9 | gpt-4.1-nano | — | **3.68 [3.31, 4.05]** | 3.35 | 4.02 | 4.55 | 3.48 | 0.26 | 6.43 |
| 10 | gpt-4o-2024-08-06 | — | **3.34 [3.00, 3.56]** | 2.33 | 4.34 | 5.19 | 3.49 | 0.15 | 4.51 |
| 11 | gpt-4o | — | **2.95 [2.51, 3.29]** | 1.53 | 4.37 | 5.22 | 3.53 | 0.44 | 2.61 |
| 12 | gpt-4o-mini | — | **2.39 [1.96, 2.79]** | 1.17 | 3.62 | 3.71 | 3.53 | -0.00 | 2.34 |

Table: Final leaderboard — total $T$ with its joint-bootstrap 95% CI, the evaluator half $E$, the generator half $G$, and the four anchored components; all council-issued against the fixed anchor, which reads 7.00 by construction. Adjacent ranks are resolved (non-overlapping intervals) only at 2–3 and 8–9; the rest are statistical ties. $E^{F} = 0.00$: no error signal in the model's factual ratings. Contest-basis $E^{C}$ is an easier test than the twelve-evaluator consistency, a caveat for ranks 6–12.

Two readings. **The top five are the council**: the five decent factual judges of §4.2 are also the five highest totals. **Generation and evaluation do not coincide**: the three Opus models, the strongest generators, are middling factual judges ($E^{F}$ 3.5–3.7, the pinned anchor aside), while the strongest judge, Gemini 3.1 Pro ($E^{F} = 7.78$), generates mid-pack. Making a true claim and spotting a false one are different skills (West et al., 2024; Oh et al., 2024; Li et al., 2024), and rating them separately breaks the assumption behind key-free peer rankers (Ning et al., 2025; Zhang et al., 2025), which treat a strong generator as a strong judge.

### 4.5 A key-free benchmark replicates a keyed one

We test the key-free rating against GPQA Diamond (Rein et al., 2023) — 198 graduate-level multiple-choice questions written and validated by domain experts — put to the same twelve models under the same protocol, scored against its human key, administered two weeks *after* the generation run (Appendix D.2), and correlated with $T$ (Figure \ref{fig-gpqa-scatter}).

<a id="fig-gpqa-scatter"></a>

![The official total rating $T$ (council basis) against self-administered GPQA Diamond accuracy, twelve models. Pearson $r = 0.98$ (95% BCa bootstrap CI [0.95, 0.99]), Spearman $\rho = 0.96$; three runs pooled. Filled markers are council seats, open markers non-council; horizontal bars the joint-bootstrap 95% CI on $T$, vertical bars the GPQA binomial 95% CI; the line is the least-squares fit. The star is the anchor: $T = 7$ by calibration, GPQA measured independently; excluding it leaves $r$ at 0.98.](../submission/figures/total_validation_simple.png)

$T$ reproduces GPQA's ordering at Pearson $r = 0.98$ [0.95, 0.99] (Spearman 0.96; three runs pooled, §4.6). Instruments sharing no item authors, task or scoring, and agreeing at 0.98, are as close as their measurement error allows (Appendix D.1); what they have in common, §6 leaves open. The objection that any two demanding benchmarks correlate on a wide roster does not carry — the agreement holds at $r = 0.94$ within the leading eight alone.

**The number survives an audit** (Appendix D): no key ever enters a prompt; every published accuracy re-derives exactly from the shipped raw per-question records; the shuffled key is balanced; an independently written answer extractor reproduces the verdicts; rescoring under a strict extraction rule moves the correlation by 0.010. $T$ is the mean of four quarters, $G^{F}$, $G^{C}$, $E^{F}$, $E^{C}$: each alone correlates with GPQA at 0.81–0.95, the factual pair $\tfrac12(G^{F}+E^{F})$ at 0.94, and adding the two subjective quarters lifts the agreement to 0.98; dropping even the weakest quarter lowers it (0.97), and no sub-combination beats it (Appendix D.1). These differences are not individually resolved at $n = 12$. $T$ is the official total, defined before any GPQA comparison. What the audit cannot rule out: the shared gateway, and *differential* training contamination of the public GPQA set. **Judging is its own trait**: among the leading eight $E^{F}$ (0.89) is the best single predictor while $G^{C}$ falls to 0.81 — once every model is a competent maker, what separates them is the knowledge that detecting others' errors requires (Appendix D.1). No keyed answering benchmark measures judging.

### 4.6 Robustness to regeneration

We ran the full pipeline three times, regenerating all twelve portfolios at T=0 against the frozen anchor; the main text pools the three. Eleven of twelve portfolios differ between runs. Apart, the runs agree on the total (Appendix F) and track GPQA at 0.97, 0.97 and 0.92, but not on the factual quarter: one seat's $E^{F}$ reads 4.68, 3.81 and 0.01 across the runs, and run 3's factual axis is not identified ($\sigma_1/\sigma_2 = 1.29$; run 2 1.67, run 1 2.57). Re-selected from a single run, the council would change one seat in run 2 and one in run 3; neither rotation clears the guard of §3.4. Pooled, the axis is identified ($\sigma_1/\sigma_2 = 2.2$) and the guard holds in every contest (Appendix A.6).

## 5 Related work

**As an intelligence test**, the game probes the abstraction-and-analogy cluster a long tradition places at the centre of thinking (Gentner, 1983; Hofstadter & Sander, 2013; Penn et al., 2008; Chollet, 2019; Mitchell, 2021). The classical instruments — BIG-Bench analogy items (Srivastava et al., 2023), Webb et al. (2023), Lewis & Mitchell (2024), ARC (Chollet, 2019) — give source and target and ask for one selection or completion, scored against a key; the metanym game asks for many coupled slots across several unrelated domains, built from scratch, and is the first to make analogical *production* falsifiable sentence by sentence.

**As a self-contained method**, the council sits in the *unsupervised peer-evaluation* line, which already removes the gold key: single-judge protocols (Zheng et al., 2023) trust one judge; PoLL (Verga et al., 2024) adds a panel but trusts it as given; LLM-as-Examiner (Bai et al., 2023) lets the examiner write the questions; PiCO (Ning et al., 2025) lets unlabelled models answer and grade one another and recovers an ability ordering from peer agreement alone, and UPME (Zhang et al., 2025) extends it to vision-language. We weight by agreement only where agreement is licensed to mean truth, and our council certifies and re-contests its own judges. The estimator is the sharper break: PiCO fits one ability parameter per model by consistency optimisation, not a spectral method. Spectral aggregation has two label-free lineages, and both are *one-sided*. In the aggregation lineage — Parisi et al. (2014), Dawid & Skene (1979) — predictors classify a fixed external dataset, so there is no generator to score. In the reputation lineage — EigenTrust (Kamvar et al., 2003) — EigenBench (Chang et al., 2026) has LLMs judge one another's responses to open prompts against a written value constitution and takes the leading eigenvector of a model-by-model trust matrix as each model's score; one number is both a model's standing and its weight as a judge, on the premise that a more aligned model is a better judge of alignment, and consensus weighting is applied to every criterion, subjective ones included. Our matrix is *two-sided*: one SVD scores judges on the left and generators on the right, the two are kept apart, and the generation–evaluation gap of §4.4 — which contradicts that premise on the factual axis — is definable only because the test is self-produced. *Rating consistency* applies the judge-reliability principle of invariance under non-semantic perturbation (Weng et al., 2026; Bellibatlu et al., 2026) to subjective, ground-truth-free criteria on self-produced items — to our knowledge a new use of the sweep. Don-Yehiya et al. (2026) find the anchor should be recalibrated to the field's capability range — our recalibration rule — and warn against a top-model anchor; the caution does not bite here, since the bootstrap winner is pinned at 7 with headroom above and scored cardinally, and anchoring more than doubled the leading–trailing gap (§4.1).

## 6 Discussion and limitations

**Two yardsticks.** The factual estimator's one assumption — *the only thing competent evaluators share is the truth* — is what licenses agreement-weighting for facts. The disclosed alternative applies it to taste as well (an *authority* rating, one SVD per subjective axis; Appendix A.7); we decline it because on taste the dominant axis of agreement is shared convention, so weighting by it would reward the judge nearest the mean. Peer centrality's weakness is the shared misunderstanding, which rating consistency does not inherit: it asks only whether a judge holds a firm standard.

**A sustainable yardstick.** When the field outgrows the anchor — a standing total above the pinned 7 by a resolvable margin — the anchor is replaced by the stronger submission and models are re-scored; the ballast stays fixed. Contestable seats keep the judges current, retesting the scale: the benchmark rises with the models it measures, which a keyed test cannot — its key-makers are fixed, and it saturates once the field passes them.

**The 0.98, and what it licenses.** The total tracks GPQA at 0.98 (§4.5). GPQA is an accepted measure of capability with no theory of intelligence behind it: expert-written questions and a key (Rein et al., 2023). The game reproduces its ranking as closely as the measurement error of the two instruments allows (Appendix D.1), so whatever GPQA measures, the game measures too. The game is a single activity: making analogies and judging them. Of the eight constructs it demands (Appendix E), four are analogy under cognitive science's own names — relational reasoning, structure-mapping, essence-seeing, theory formation by analogy — and the other four serve them. A test whose core is analogy therefore reaches all of what GPQA measures. That is the sense in which analogy is at the core: sufficient by itself, not the only thing that could be. An agreement of 0.98 suggests that the two instruments measure the same thing. Their methods share nothing on the surface, so the common thing is in the depth. Our hypothesis is that a language model holds its knowledge as archetypal contexts, each instantiated in the topic domains where it applies; the metanym game measures this mechanism directly, and GPQA measures its use. The steps that lead there are known results. Training a language model is compression: predicting text is compressing it (Shannon, 1951), and a trained model is a general-purpose compressor (Delétang et al., 2024). The metanym game compresses the same way. One template represents an archetypal context and a compact metanym set represents each topic domain; in the anchor's first archetype, a 120-word template and 17 words of metanyms per context reconstruct five instantiations of about 130 words each, exactly: a factor of 3.2, and about 8 for each context added. Compression generalises: the shortest description names a recurring pattern once and reuses the name (Rissanen, 1978); that is a concept. A concept is a general frame plus the slots that differ (Minsky, 1974; Rosch, 1978). An analogy is a shared relational structure with different particulars (Gentner, 1983). The archetypal context is that shared structure: the context templates of §2 are archetypal contexts written out, and the metanym sets are the differences. A GPQA question is read by mapping it onto the archetypal contexts it instantiates and the domain that instantiates them, so the two tests exercise one operation. The hypothesis also says why the models play well. In the game they do not build templates and metanym sets; they retrieve what training already compressed. It shows in the transcripts: between the two runs made two hours apart, a model rewrites its portfolios but keeps its archetypes (34 of 48 titles recur verbatim), and seven of eleven models, from all three vendors, offer a resource-allocation archetype. The data establish less: the factual pair alone reaches 0.94, and the two subjective quarters lift it to 0.98 (§4.5). It is consistent with the general factor Ilić and Gignac (2024) find across 591 models and twelve tests, and more specific. It predicts that the agreement is domain-matched: a model's factual score on parallel contexts in a field tracks its GPQA accuracy in that field. It predicts that archetype and topic domain are separable in a model's latent space.

**Steering signal, and its caveat.** Self-improvement, the council governing its own rules, is specified but not yet exercised. A system optimised against $T$ is optimised against a consensus it participates in, so gains can come from courting the consensus rather than from capability; the partial answers are the two quarters consensus does not own and independently constituted councils.

**Scope.** The runs share one configuration — one prompt template, one roster — so the bootstrap intervals measure item dispersion only (the four anchor values give the same leaderboard, Spearman 0.90–0.96); the leading group sits at its discrimination floor; a quarter of a non-council model's total rests on the contest's easier consistency test; no seat has yet been contested. The structural caveat is the price of the key-free construction: peer consensus is conservative against anomaly — a synthetic evaluator that reproduces the consensus and then inverts its verdict on a fifth of the items loses most of its competence (Appendix A.7); a dissenter pays that penalty on only half of $T$.

## 7 Conclusion

The *metanym game* is a structural test of intelligence built entirely of analogy, falsifiable sentence by sentence. The *council-of-peers benchmark* needs nothing outside itself: truth recovered as the dominant axis of inter-evaluator agreement, subjective reliability from invariance under a swept anchor, judges certified by the participants themselves, contestable seats that let the scale rise with the models it measures — and one external check, by design, $r = 0.98$ against GPQA Diamond.

## AI use statement

Every original idea in this work is the author's. The work was developed in a sustained dialogue with generative AI assistants (Anthropic's Claude), directed by the author throughout. Within that dialogue the assistants criticised the theory, the estimators and the experimental design as a reviewer in the field would, and proposed hypotheses and experiments alongside the author's; none was adopted without a competing hypothesis and a further experiment to test it. They implemented the analysis methods, cleaned and reformatted the evaluation records and GPQA response logs, and helped interpret results; they were also used for code, literature search, figures, references and first drafts, which the author rewrote into the author's own text. No data and no proofs were generated by AI: every rating in the paper comes from the twelve rated models of §3.1. All AI-assisted output was checked against the deterministic re-derivation of every published number (Reproducibility statement). The author takes responsibility for the final content.

## Ethics statement

The study evaluates commercial language models via their public APIs on self-generated material; no human subjects, personal data or annotators are involved. The benchmark is proposed as a candidate steering signal for self-improving systems. Steering by it would mean letting a consensus of models, with no human key, decide what counts as better, and a misunderstanding the models share would then be reinforced rather than corrected. The paper keeps the factual axis answerable to independent checks (§4.5) and leaves the self-improvement loop specified but unrun (§6); we regard that as the condition under which such a signal may be used. We consider the release of a key-free, contamination-resistant evaluation to be net positive for the field's ability to measure models past the point where human-written keys remain reliable, and we release all data and code under permissive licences.

## Reproducibility statement

Every number, table and figure in this paper recomputes deterministically from a released package (anonymised repository, supplementary material): the pinned evaluation runs (the un-anchored pass, the anchored pass at each of the four anchor values, and the three runs of the full pipeline — the canonical run and two regenerations), the raw per-question GPQA administration including both stages' records and the first-pass log, the anchor and ballast portfolios, the verbatim generation and evaluation prompts (Appendix B), the analysis scripts, and a one-command `reproduce.sh` whose steps are each labelled by the exhibit they produce. The re-analysis makes no API calls and needs no credentials; it takes about a minute. The estimators are specified to the equation in Appendix A, including every convention (self-entry filling, row-centering, sign and clamp, Procrustes alignment of bootstrap replicates, the joint (submission, archetype) resampling grid). Producing a *new* run — re-querying the models — is deliberately not part of the package: it costs API budget and is non-deterministic by construction; §4.6 reports what moves across three independent regenerations.

## References

Bai, Y., et al. (2023). Benchmarking foundation models with Language-Model-as-an-Examiner. *NeurIPS 36.* arXiv:2306.04181.

Bellibatlu, R. R., Raff, E., & Zhang, W. (2026). JudgeSense: A benchmark for prompt sensitivity in LLM-as-a-judge systems. arXiv:2604.23478.

Bonacich, P. (1972). Factoring and weighting approaches to status scores and clique identification. *Journal of Mathematical Sociology, 2*(1), 113–120.

Cattell, R. B. (1963). Theory of fluid and crystallized intelligence: A critical experiment. *Journal of Educational Psychology, 54*(1), 1–22.

Chang, J., Piff, L., Sana, S., Li, J. X., & Levine, L. (2026). EigenBench: A comparative behavioral measure of value alignment. *ICLR 2026.* arXiv:2509.01938.

Chollet, F. (2019). On the measure of intelligence. arXiv:1911.01547.

Dawid, A. P., & Skene, A. M. (1979). Maximum likelihood estimation of observer error-rates using the EM algorithm. *Journal of the Royal Statistical Society: Series C, 28*(1), 20–28.

Delétang, G., Ruoss, A., Duquenne, P.-A., Catt, E., Genewein, T., Mattern, C., Grau-Moya, J., Wenliang, L. K., Aitchison, M., Orseau, L., Hutter, M., & Veness, J. (2024). Language modeling is compression. In *International Conference on Learning Representations (ICLR 2024)*. arXiv:2309.10668.

Don-Yehiya, S., Yehudai, A., Choshen, L., & Abend, O. (2026). Mediocrity is the key for LLM as a judge anchor selection. *ACL 2026.* arXiv:2603.16848.

Efron, B., & Tibshirani, R. J. (1993). *An Introduction to the Bootstrap.* Chapman & Hall.

Falkenhainer, B., Forbus, K. D., & Gentner, D. (1989). The structure-mapping engine: Algorithm and examples. *Artificial Intelligence, 41*(1), 1–63.

Gentner, D. (1983). Structure-mapping: A theoretical framework for analogy. *Cognitive Science, 7*(2), 155–170.

Guilford, J. P. (1967). *The Nature of Human Intelligence.* McGraw-Hill.

Hesse, M. (1963). *Models and Analogies in Science.* Sheed & Ward.

Hofstadter, D., & Sander, E. (2013). *Surfaces and Essences.* Basic Books.

Horn, J. L., & Cattell, R. B. (1966). Refinement and test of the theory of fluid and crystallized general intelligences. *Journal of Educational Psychology, 57*(5), 253–270.

Hughes, E., Dennis, M., Parker-Holder, J., Behbahani, F., Mavalankar, A., Shi, Y., Schaul, T., & Rocktäschel, T. (2024). Position: Open-endedness is essential for artificial superhuman intelligence. *ICML 2024, PMLR 235*, 20597–20616.

Ilić, D., & Gignac, G. E. (2024). Evidence of interrelated cognitive-like capabilities in large language models: Indications of artificial general intelligence or achievement? *Intelligence, 106*, 101858.

Kamvar, S. D., Schlosser, M. T., & Garcia-Molina, H. (2003). The EigenTrust algorithm for reputation management in P2P networks. *WWW 2003*, 640–651.

Lewis, M., & Mitchell, M. (2024). Using counterfactual tasks to evaluate the generality of analogical reasoning in large language models. *CogSci 2024.* arXiv:2402.08955.

Li, X. L., Shrivastava, V., Li, S., Hashimoto, T., & Liang, P. (2024). Benchmarking and improving generator-validator consistency of language models. *ICLR 2024.* arXiv:2310.01846.

Longino, H. E. (1990). *Science as Social Knowledge.* Princeton University Press.

Minsky, M. (1974). A framework for representing knowledge. MIT AI Laboratory Memo 306.

Mitchell, M. (2021). Abstraction and analogy-making in artificial intelligence. *Annals of the New York Academy of Sciences, 1505*(1), 79–101.

Neisser, U. (1979). The concept of intelligence. *Intelligence, 3*(3), 217–227.

Ning, K.-P., Yang, S., Liu, Y.-Y., Yao, J.-Y., Liu, Z.-H., Tian, Y.-H., Song, Y., & Yuan, L. (2025). PiCO: Peer review in LLMs based on consistency optimization. *ICLR 2025.* arXiv:2402.01830.

Oh, J., Kim, E., Cha, I., & Oh, A. (2024). The Generative AI Paradox in evaluation: What it can solve, it may not evaluate. *EACL 2024 Student Research Workshop*, 248–257. arXiv:2402.06204.

Parisi, F., Strino, F., Nadler, B., & Kluger, Y. (2014). Ranking and combining multiple predictors without labeled data. *PNAS, 111*(4), 1253–1258.

Penn, D. C., Holyoak, K. J., & Povinelli, D. J. (2008). Darwin's mistake: Explaining the discontinuity between human and nonhuman minds. *Behavioral and Brain Sciences, 31*(2), 109–130.

Rein, D., Hou, B. L., Stickland, A. C., Petty, J., Pang, R. Y., Dirani, J., Michael, J., & Bowman, S. R. (2023). GPQA: A graduate-level Google-proof Q&A benchmark. arXiv:2311.12022.

Rissanen, J. (1978). Modeling by shortest data description. *Automatica, 14*(5), 465–471.

Rosch, E. (1978). Principles of categorization. In E. Rosch & B. B. Lloyd (Eds.), *Cognition and Categorization* (pp. 27–48). Lawrence Erlbaum.

Shannon, C. E. (1951). Prediction and entropy of printed English. *Bell System Technical Journal, 30*(1), 50–64.

Srivastava, A., et al. (2023). Beyond the imitation game: Quantifying and extrapolating the capabilities of language models. *TMLR.* arXiv:2206.04615.

Sternberg, R. J., Conway, B. E., Ketron, J. L., & Bernstein, M. (1981). People's conceptions of intelligence. *Journal of Personality and Social Psychology, 41*(1), 37–55.

Verga, P., et al. (2024). Replacing judges with juries: Evaluating LLM generations with a panel of diverse models. arXiv:2404.18796.

von Bertalanffy, L. (1968). *General System Theory.* George Braziller.

Webb, T., Holyoak, K. J., & Lu, H. (2023). Emergent analogical reasoning in large language models. *Nature Human Behaviour, 7*(9), 1526–1541.

Weng, S., Feng, Y., & Xie, X. (2026). Beyond accuracy: Policy invariance as a reliability test for LLM safety judges. arXiv:2605.06161.

West, P., Lu, X., Dziri, N., Brahman, F., Li, L., Hwang, J. D., Jiang, L., Fisher, J., Ravichander, A., Chandu, K., Newman, B., Koh, P. W., Ettinger, A., & Choi, Y. (2024). The Generative AI Paradox: "What it can create, it may not understand." *ICLR 2024.* arXiv:2311.00059.

Zhang, Q., Ning, M., Liu, Z., Wang, Y., Ye, J., Huang, Y., Yang, S., Chen, X., Song, Y., & Yuan, L. (2025). UPME: An unsupervised peer review framework for multimodal large language model evaluation. *CVPR 2025*, 9165–9174. arXiv:2503.14941.

Zheng, L., et al. (2023). Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena. *NeurIPS 36.* arXiv:2306.05685.

## Appendices

→ [`appendices/A_estimators.md`](appendices/A_estimators.md) — A. Rating estimators (A.1 generation; A.2 factual competence and generation factuality; A.3 rating consistency, with the per-axis table; A.4 council and total; A.5 per-criterion alignment; A.6 contest, ballast and guards; A.7 authority vs consistency; A.8 the two estimators compared)

→ [`appendices/B_prompts.md`](appendices/B_prompts.md) — B. The generation and evaluation prompts

→ [`appendices/C_worked_evaluation.md`](appendices/C_worked_evaluation.md) — C. A council evaluation, worked

→ [`appendices/D_gpqa_audit.md`](appendices/D_gpqa_audit.md) — D. Auditing the metanym–GPQA correlation

→ [`appendices/E_constructs.md`](appendices/E_constructs.md) — E. The eight constructs of intelligence the game demands

→ [`appendices/F_regeneration.md`](appendices/F_regeneration.md) — F. Totals across three regenerations

→ [`appendices/G_anchoring.md`](appendices/G_anchoring.md) — G. What anchoring does to resolution
