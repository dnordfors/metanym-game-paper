# The Metanym Game: An LLM Benchmark Without Ground Truth That Rises With the Models It Measures

## Abstract

We introduce a benchmark that contains its own ground truth and presents evidence that analogy is at the core of LLM intelligence. Language models compete at generating analogies and subjectively rate each other; nothing enters from outside. Play interweaves eight kinds of intelligence. Provocatively, it correlates at $r = 0.98$ with GPQA Diamond, an established benchmark of expert-written questions — a different method entirely. The correlation was audited for a leak and found clean. We hypothesize that both benchmarks do the same thing in seemingly different ways: generating factually correct information where the LLM latent space has compressed specific knowledge as generalized archetypal contextual patterns applied across specific topic domains. In the Metanym Game Benchmark, LLMs generate sets of analogous statements and rate each other's sets on their own understandings of factual correctness, beauty, intelligence, distinctness, length and structural diversity. Ground truth is replaced by the SVD of the factual rating matrix, whose left and right pair of singular vectors are a self-consistent simultaneous rating of players as judges and generators, two distinct ratings from one factorisation — to our knowledge a first for an LLM council of peers. For subjective criteria, judges are weighted by their rating consistency under a swept calibration anchor. Generating and judging are different skills: some strong generators were average judges. A council of the five best issues the official ratings; its contestable seats let the benchmark scale to any number of players and rise with the models it measures — a candidate steering signal for self-improving AI. Every number recomputes from a released package.

## 1 Introduction

Nearly every benchmark for machine intelligence needs a predetermined ground truth — golden keys and labels, oracle models, human panels. The benchmark reported here needs none of that. It is a game where frontier language models compete in making up analogies and then grade one another, and that grading is the single source of every score: no human raters, no answer key, nothing to look up.

The test is the **metanym game**. A player authors, from nothing, a *context template* — a paragraph of fixed wording with open slots — together with the sets of keywords that fill it, each set instantiating the template as a factually true description of a different domain; the keywords in corresponding slots are *metanyms*, metaphorically synonymous, and a set of them a *metanym set*. Table \ref{tab-anchor-metanym} shows one, written by a player. Its instantiations are each other's *metaphors* and, as a set, *parallel contexts*: children of a common *archetypal context*, the abstract structure they share, of which the template is the literal representation. A long tradition treats seeing one structure across wildly different domains as central to thought and tests whether you *recognise* it; the game tests whether you can *build* it.

Because every item is produced fresh in the run, no fixed test set can leak into training; because correctness is settled sentence by sentence, the players' own verdicts suffice — one matrix of their factual ratings reveals which judges are competent, with no labels at all (§3.3), and that subset is seated as the *council* that grades everyone. The canonical twelve-model run (§4) finds that **judgement is the bottleneck** — on this roster the strongest generators are middling judges — and that the key-free total tracks GPQA Diamond at Pearson $r = 0.98$, audited for a leak and found clean.

**Contributions.** (i) A production task for analogy that is falsifiable sentence by sentence, hence scorable without a key. (ii) A two-sided spectral estimator: one SVD of the self-produced factual rating matrix reads evaluator competence off the left singular vector and generator factuality off the right. (iii) A key-free reliability gate for subjective criteria: invariance under a sweep of the calibration anchor. (iv) A self-administering council with contestable seats. (v) The generation–judgement dissociation, and the $r = 0.98$ replication of a keyed benchmark by a key-free one, audited.

## 2 The metanym game

An archetypal context is the cross-domain *isomorphism* General Systems Theory studies (von Bertalanffy, 1968). Table \ref{tab-anchor-metanym} is one archetype as a player wrote it — the first of the submission that became the run's anchor (§4.1). One template, mechanically swappable metanyms, true sentence by sentence across maximal domain distance: that is what makes a metanym game decidable, and therefore measurable.

<a id="tab-anchor-metanym"></a>

| |
|---|
| A [NAVIGATOR] moves through a [SPACE] by sensing local [GRADIENT] and adjusting its [TRAJECTORY] accordingly. The [NAVIGATOR] cannot perceive the entire [SPACE] at once; it relies on [SENSOR] that detect changes in [SIGNAL] concentration or intensity. When [GRADIENT] are steep and consistent, the [NAVIGATOR] converges efficiently toward [ATTRACTOR]. When [GRADIENT] are shallow, noisy, or conflicting, the [NAVIGATOR] may stall, oscillate, or become trapped in local [ATTRACTOR]. [INTERFERENCE] can distort the [GRADIENT], causing the [NAVIGATOR] to veer off course. Successful navigation requires not only sensitive [SENSOR] but also [MEMORY] of recent [TRAJECTORY] to distinguish genuine [GRADIENT] from transient [NOISE]. Some [NAVIGATOR] emit their own [SIGNAL] to recruit other [NAVIGATOR] toward the same [ATTRACTOR], creating collective [TRAJECTORY] that amplify the original [GRADIENT]. |

Table: The anchor's first archetype (§4.1), as a player wrote it: the context template, its metanym table, and its first column played, first sentence of each form.

Its metanym table: MEMORY is realised as a bacterium's methylation state, a climber's route memory, a professional's experience, an optimiser's momentum term and an ant's path integration — five mechanisms that are metaphorically synonymous in the archetypal context — metanyms.

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

Table: PARTBTABLE

Each parallel context is played in two forms: the **instantiation** (Form a), the mechanical substitution — only the slots filled, every other word carried over — the form the factual criterion is written for, since it must come out true sentence by sentence (the judge sees both forms); and the **idiomatic rewrite** (Form b) in the target domain's own register, showing the claim is not an artefact of the template's phrasing.

| | |
|---|---|
| Form (a), instantiation | A BACTERIUM moves through a CHEMICAL ENVIRONMENT by sensing local CHEMICAL GRADIENTS and adjusting its SWIMMING PATH accordingly. |
| Form (b), idiomatic rewrite | Bacteria navigate chemical environments by detecting local concentration gradients and modulating their run-and-tumble behavior accordingly. |

Table: PARTBTABLE

The game has $N$ players and a non-competing administrator. **Generation**: a player creates archetypal contexts from scratch — a portfolio of $K$ templates, $M$ metanym sets each (five and five here), with instantiation and rewrite for every set. **Evaluation**: a player scores other players' submissions on the rubric axes (§3.2) against one fixed *reference* submission pinned at an *anchor* value. A pass yields **submission ratings** for each portfolio and **evaluator ratings** for the judges: how well one detects the factual errors the other players collectively flag (*factual competence*), and how stable a standard it holds when the reference is re-pinned (*rating consistency*, §3.3). Each act is itself rated, so the framework is **fully self-contained**: no human raters, no external key.

## 3 The metanym game as a benchmark

### 3.1 Participants and protocol

Twelve frontier LLMs from Anthropic, Google and OpenAI are the **participants** (named in §4.4), each simultaneously generator and evaluator. The roster spans an order of magnitude in scale, three vendors, and adjacent versions within families; it is the models at hand, not a census. All twelve are called with **Temperature 0, reasoning disabled, tools disabled**, so the one greedy response is the measurement. Each model generates one portfolio — five archetypal contexts, each a template (typically 5–8 sentences, 6–10 slots; the prompt fixes only the counts, Appendix B) with a metanym table of five domains, 25 instantiations — then evaluates every other model's portfolio under the six-axis rubric of Table \ref{tab-rubric}, 1–10, one anonymised target per call alongside a fixed **anchor** portfolio pinned at 7 on every axis: a 12×11 evaluator-by-generator matrix (Appendix A). Every official rating pools three full runs of the game (§4.6); the anchor sweep behind the consistency ratings was run once, on the first run.

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

Three design choices justify themselves on first principles. **A fixed anchor**: cardinal scores drift between evaluators — one model's "8" is another's "6" — and a reference pinned at a known score turns each idiosyncratic scale into a common one and recovers discriminability at the top, where the 1–10 ceiling compresses the strongest portfolios (§4.1). **Holistic axes, minimally prescribed**: a detailed rubric would leak back into generation as a template-construction tutorial, and we want to score what models *recognise* as beautiful or intelligent. `impressive_length` counterweights per-sentence factual scoring: without it the minimal template wins, and padding costs, since every added sentence is another claim to score. One evaluation, shown whole, is Figure \ref{fig-council-evaluation}.

<a id="fig-council-evaluation"></a>

![One parallel context under evaluation: the instantiation with its metanyms marked, and the five judges' ratings with the clause each one singles out. All five isolate the same clause; the disagreement that remains, 4 versus 5, is about severity. The whole evaluation, with the rewrite, the administrator's synthesis and every justification, is Figure \ref{fig-council-evaluation-full} in Appendix C.](../submission/figures/council_evaluation_pc1_compact.png)

### 3.3 Two key-free estimators

**1. Factual competence — peer centrality.** We assume that good evaluators agree with one another about which instantiations are factually weaker, once each evaluator's own leniency is removed — the better two evaluators are, the more they agree. Stack the participants' factual scores into one matrix — twelve evaluators against the 275 parallel contexts of the eleven scored portfolios — each entry the 1–10 rating used directly, row-centre it to remove each evaluator's leniency, and take its SVD; the row-centred $\tilde F$ (evaluators × instantiations) is well approximated by its leading rank-one factor,

$$\tilde F_{sj} \;\approx\; \sigma_1\, u_s\, v_j . \tag{1}$$

An evaluator's rating tracks the consensus in proportion to its competence $u_s$ times the instantiation's factual standing $v_j$: competence and standing fall out of one factorisation, with **no answer key**. The *left* singular vector $u$ is each **evaluator**'s factual-competence loading $f$ — high when its ratings align with the participants' shared signal, ≈ 0 when it rates everything alike or idiosyncratically — and, rescaled so the anchor model reads 7, $E^{F} = 7f/f_a$; the *right* vector, aggregated per generator, is $G^{F}$ (Appendix A.2). $f$ is each judge's eigenvector centrality (Bonacich, 1972) in the leniency-removed agreement network, after clamping: an evaluator's competence is its rating by the other evaluators, each weighted by its own competence — the highly trusted among the highly trusted. The construction is a graded relative of the classical label-free aggregators (Dawid & Skene, 1979; Parisi et al., 2014), which need categorical verdicts; discretising here would flip the marginal council seat.

**2. Rating consistency — the anchor sweep.** A reliable evaluator also needs a stable internal standard for each non-factual criterion. We sweep the anchor across 5, 6, 7 and 8 — the *only* difference between the four runs — and, per evaluator and axis, correlate (Pearson) the scores at one anchor with those at another, averaged over the six pairs, leave-self-out. Re-pinning the anchor recalibrates the scale, not the rubric, and Pearson ignores a common shift or stretch; any reordering that follows a recalibration is not a change of judgement but flimsiness. Rescaled so the anchor model reads 7, consistency becomes an evaluator competence $E^{C}$ on the generator's scale.

Neither estimator can do the other's job (Appendix A.8): peer centrality is licensed only where the one thing competent judges share is the truth — on taste, agreement is shared convention, and weighting by it would launder conformity into competence — and consistency cannot certify truth. The council is therefore seated on the factual axis, with consistency as the accompanying bar.

### 3.4 Council, total rating, and scaling by addition

**The council.** The **council** is the five players with the highest total $T$ (eq. 2) and issues every official rating. The top five are the better factual judges (loadings 0.26–0.61, §4.2); the sixth reads 0.18; the line is drawn there; nothing prescribes five.

**The total.** Each side of the Metanym Game splits into a factual and a criterion half: on generation, $G^{F}$ (the SVD generation factuality) and $G^{C}$ (the council's leave-self-out mean over the five non-factual axes, each seat's vote weighted by its own consistency on that axis); on evaluation, $E^{F} = 7f/f_a$ and $E^{C} = 7\bar r/\bar r_a$ — **the anchor model scores 7** on every component. The total is the mean of the four, a symmetric $2\times2$ of {generator, evaluator} × {factual, criterion}:

$$T \;=\; \tfrac12\,(G+E) \;=\; \tfrac14\,\big(G^{F}+G^{C}+E^{F}+E^{C}\big). \tag{2}$$

Every rating carries a 95% percentile-bootstrap interval, $E$ and $T$ bootstrapped jointly (Appendix A.4).

**Scaling by addition.** A standing council scores any future model against the same anchor without re-deriving existing ratings. The seats are **contestable** — a contestant submits a portfolio, evaluates the incumbents' portfolios and is scored by the seats under the definitions above, and wins a seat with a total $T$ above the lowest seat's by a margin the bootstrap can resolve. Because a contest convenes only the top of the field, two fixed **ballast** blocks — the weakest archived portfolios — join every contest's graded set to keep the factual axis identified (Appendix A.6), and two guards: the spectral gap $\sigma_1/\sigma_2 \ge 2$ — the shared judgement standing clear of the strongest disagreement, sized in Appendix A.6 — and a spread of the seats' $E^{F}$ above 2.5 points. If either fails, no seat changes hands and the contest's totals carry a caveat. The official leaderboard (§4.4) is issued on this contest basis. **Contamination**: items are generated fresh each run, so no fixed test set can leak into training. Every submission is archived; a new portfolio that copies an archived one is identified, and the contestant is asked for new templates — or the Metanym Game is played in another language.

## 4 Results

### 4.1 Anchoring doubles resolution

The bootstrap opens with a raw pass — every portfolio scored by every other model with no anchor, averaged leave-self-out, 95% bootstrap intervals (2,000 resamples; Efron & Tibshirani, 1993). It supplies the baseline: the top-ranked portfolio, **claude-opus-4.5**'s, whose first archetype is Table \ref{tab-anchor-metanym}, is pinned at 7 on every axis, leaving headroom above. Re-run anchored (Appendix G), the gap between a leading eight and a trailing four more than doubles relative to the spread of the means, while ranks within either band stay unresolved.

### 4.2 Evaluator factual competence

One SVD of the row-centred evaluator × instantiation matrix — no answer key — gives each evaluator a loading (Table \ref{tab-criterion-a}, Appendix A.2; $\sigma_1/\sigma_2 = 2.2$, pooled). Five evaluators — gemini-3.1-pro 0.61, claude-opus-4.5 0.52, claude-opus-4.0 0.35, claude-opus-4.1 0.35, gemini-2.5-flash 0.26 — stand above the rest.

**Same-vendor robustness.** A Claude-heavy evaluator set might read Claude-bloc agreement as truth. It does not: recomputing $G^{F}$ with each vendor's judges removed leaves the ordering essentially unchanged (Spearman ≥ 0.94 for every reduced set), gpt-4o-mini stays at the floor under every evaluator set, and a *Claude-free* set (Google + OpenAI judges) still places the Claude generators at the top (≥ 7.0).

### 4.3 Rating consistency and the council

The anchor sweep gives each evaluator a consistency on each axis (Table \ref{tab-criterion-b}, Appendix A.3). The measure is self-consistency, not accuracy: gemini-2.5-flash (0.31) collapses on factual while its other axes hold. On the five subjective criteria generation and evaluation align (anchored cosine 0.85–0.92 per criterion, Appendix A.5) — the counterpoint to the factual axis, where they come apart (§4.4).

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

Table: Final leaderboard — total $T$ with its joint-bootstrap 95% CI, the evaluator half $E$, the generator half $G$, and the four anchored components; all council-issued against the fixed anchor, which reads 7.00 by construction. Adjacent ranks are resolved (non-overlapping intervals) only at 2–3 and 8–9; the rest are statistical ties. $E^{F} = 0.00$: no error signal in the model's factual ratings.

Two readings. **The top five are the council**: the five better factual judges of §4.2 are the five highest totals. **Generation and evaluation do not coincide**: the three Opus models, the strongest generators, are middling factual judges ($E^{F}$ 3.5–3.7, the pinned anchor aside), while the strongest judge, Gemini 3.1 Pro ($E^{F} = 7.78$), generates mid-pack. Making a true claim and spotting a false one are different skills (West et al., 2024; Oh et al., 2024; Li et al., 2024), and rating them separately breaks the assumption behind key-free peer rankers (Ning et al., 2025; Zhang et al., 2025), which treat a strong generator as a strong judge.

### 4.5 A key-free benchmark replicates a keyed one

We test the key-free rating against GPQA Diamond (Rein et al., 2023) — 198 graduate-level multiple-choice questions written and validated by domain experts — put to the same twelve models under the same protocol two weeks *after* the generation run (Appendix D.2), and correlated with $T$ (Figure \ref{fig-gpqa-scatter}).

<a id="fig-gpqa-scatter"></a>

![The official total $T$ against self-administered GPQA Diamond accuracy, twelve models, three runs pooled: $r = 0.98$ [0.95, 0.99], $\rho = 0.96$. Filled markers are council seats, open markers non-council, bars 95% intervals; the star is the anchor, $T = 7$ by calibration, and excluding it leaves $r$ at 0.98.](../submission/figures/total_validation_simple.png)

<a id="fig-mechanism"></a>

![A hypothesis for the 0.98 (§6): an archetype ($\alpha$, $\beta$) is held once; each domain adds only its metanym set (the slices). GPQA: archetype and domain are given, the model derives the instantiation and selects the matching candidate. The game: nothing is given, the model selects the archetype and domains and writes them out.](../submission/figures/mechanism_sketch.png)

$T$ reproduces GPQA's ordering at Pearson $r = 0.98$ [0.95, 0.99] (Spearman 0.96; three runs pooled, §4.6). Instruments sharing no item authors, task or scoring, and agreeing at 0.98, are as close as their measurement error allows (Appendix D.1); §6 offers a hypothesis for what they share. The objection that any two demanding benchmarks correlate on a wide roster does not carry — the agreement holds at $r = 0.94$ within the leading eight alone.

**The number survives an audit** (Appendix D): no key enters a prompt, every accuracy re-derives from the shipped records, the key is balanced, an independent extractor reproduces the verdicts, and strict rescoring moves the correlation by 0.010. $T$ is the mean of four quarters, $G^{F}$, $G^{C}$, $E^{F}$, $E^{C}$: each alone correlates with GPQA at 0.81–0.95, the factual pair $\tfrac12(G^{F}+E^{F})$ at 0.94, and adding the two subjective quarters lifts the agreement to 0.98; dropping even the weakest quarter lowers it (0.97), and no sub-combination beats it (Appendix D.1). These differences are not individually resolved at $n = 12$. $T$ is the official total, defined before any GPQA comparison. What the audit cannot rule out: the shared gateway, and *differential* training contamination of the public GPQA set. **Judging is its own trait**: among the leading eight $E^{F}$ (0.89) is the best single predictor while $G^{C}$ falls to 0.81 — once every model is a competent maker, what separates them is the knowledge that detecting others' errors requires (Appendix D.1). No keyed answering benchmark measures judging.

### 4.6 Robustness to regeneration

We ran the full pipeline three times, regenerating all twelve portfolios at T=0 against the frozen anchor; the main text pools the three. Apart, the runs agree on the total (Appendix F) and track GPQA at 0.97, 0.97 and 0.92, and most archetype titles recur verbatim between the two runs made two hours apart, 34 of 48, while the templates are rewritten; but not on the factual quarter: a seat's $E^{F}$ reads 4.68, 3.81 and 0.01 across the runs, and run 3's factual axis is not identified ($\sigma_1/\sigma_2 = 1.29$; Appendix F). Re-selected from a single run, the council would change one seat in run 2 and one in run 3; neither rotation clears the guard of §3.4. Pooled, the axis is identified ($\sigma_1/\sigma_2 = 2.2$) and the guard holds in every contest (Appendix A.6).

## 5 Related work

**As an intelligence test**, the Metanym Game probes the abstraction-and-analogy cluster a long tradition places at the centre of thinking (Gentner, 1983; Hofstadter & Sander, 2013; Penn et al., 2008; Chollet, 2019; Mitchell, 2021). The classical instruments (Srivastava et al., 2023; Webb et al., 2023; Lewis & Mitchell, 2024; Chollet, 2019) give source and target and ask for one selection or completion, scored against a key; the metanym game asks for many coupled slots across unrelated domains, built from scratch, and is the first to make analogical *production* falsifiable sentence by sentence.

**As a self-contained method**, the council sits in the *unsupervised peer-evaluation* line, which already removes the gold key: single-judge protocols (Zheng et al., 2023) trust one judge; PoLL (Verga et al., 2024) adds a panel but trusts it as given; LLM-as-Examiner (Bai et al., 2023) lets the examiner write the questions; PiCO (Ning et al., 2025) lets unlabelled models answer and grade one another and recovers an ability ordering from peer agreement alone, and UPME (Zhang et al., 2025) extends it to vision-language. We weight by agreement only where agreement is licensed to mean truth, and our council certifies and re-contests its own judges. Label-free spectral aggregation is *one-sided* in both its lineages: in the aggregation lineage (Parisi et al., 2014; Dawid & Skene, 1979) predictors classify a fixed external dataset, so there is no generator to score; in the reputation lineage (EigenTrust, Kamvar et al., 2003) EigenBench (Chang et al., 2026) has LLMs judge one another's responses against a written value constitution and takes the leading eigenvector of a model-by-model trust matrix as each model's score: one number is both standing and weight as a judge, applied to every criterion, subjective ones included. Our matrix is *two-sided*: one SVD scores judges on the left and generators on the right, the two are kept apart, and the generation–evaluation gap of §4.4 — which contradicts that premise on the factual axis — is definable only because the test is self-produced. *Rating consistency* applies the judge-reliability principle of invariance under non-semantic perturbation (Weng et al., 2026; Bellibatlu et al., 2026) to subjective, ground-truth-free criteria on self-produced items — to our knowledge a new use of the sweep. Don-Yehiya et al. (2026) find the anchor should be recalibrated to the field's range — our rule — and warn against a top-model anchor; ours is pinned at 7 with headroom above (§4.1).

## 6 Discussion and limitations

**Two yardsticks.** The factual estimator's one assumption — *the only thing competent evaluators share is the truth* — is what licenses agreement-weighting for facts. The disclosed alternative applies it to taste as well (an *authority* rating, one SVD per subjective axis; Appendix A.7); we decline it because on taste the dominant axis of agreement is shared convention, so weighting by it would reward the judge nearest the mean. Peer centrality's weakness is the shared misunderstanding; rating consistency asks only whether a judge holds a firm standard.

**A sustainable yardstick.** When the field outgrows the anchor — a standing total above the pinned 7 by a resolvable margin — the anchor is replaced by the stronger submission and models are re-scored; the ballast stays fixed. Contestable seats keep the judges current, retesting the scale: the benchmark rises with the models it measures, which a keyed test cannot: its key-makers are fixed.

**A hypothesis for the agreement.** The total tracks GPQA at 0.98 (§4.5). GPQA is an accepted measure of capability with no theory of intelligence behind it: expert-written questions and a key (Rein et al., 2023). Of the eight constructs the Metanym Game demands, four are analogy under cognitive science's own names (Appendix E). Two instruments whose methods share nothing on the surface agree at 0.98, so the common thing is in the depth. Our hypothesis is that a language model holds its knowledge as archetypal contexts, each instantiated in the topic domains where it applies; the metanym game reproduces this organisation, and GPQA runs on it (Figure \ref{fig-mechanism}). The argument: training a language model is compression (Shannon, 1951; Delétang et al., 2024), and analogy is semantic compression, a shared relational structure with different particulars (Gentner, 1983). The archetypal context is that structure in the latent space, the context template its literal representation, and the metanym sets the particulars that instantiate it. In the Metanym Game an instantiation is between two and a half and eleven times the size of its metanym set, so each domain is added for a fraction of the text it yields. The metanymic compression is of the order measured for language models, about ten (Delétang et al., 2024), and above gzip's three. A memorised string compresses only its exact repeats; a frame compresses every new instance that fits it. In the latent space the compression is greater still, since one archetype stands behind many context templates: between runs the models rewrite their templates and keep their archetypes (§4.6). A form this compressive qualifies as a learning mechanism. The two tests then run one mechanism from opposite ends. GPQA gives the archetype and the domain and four candidates: in 99.5% of the replies the model derives the solution and then picks the candidate that matches it, the mechanism in use. The game gives nothing but rating criteria, truth among them: the model selects an archetype and domains and writes them out, the mechanism itself. If so, models play the Metanym Game well without reasoning because the answer is retrieved, not built, and a reasoning channel should add little.

**A test.** We played four models each as two players, reasoning off at temperature 0 and on, through the official APIs: Claude Sonnet 4.6, Claude Haiku 4.5, GPT-5.6 Terra and GPT-5.6 Luna, each playing once and judging, with the benchmark's evaluator prompt and anchor, the six players that were neither itself nor its kin, plus the two ballasts. The thinking model does not build templates in its thinking; it writes them once, in the answer, as the non-thinking model does. What the thinking contains is a list of archetypes, by name, and a choice among them: selection over things the model already has, which is what retrieval looks like. The ratings agree (Table \ref{tab-thinking}): less than a point of change for every model, none clearing its interval. On GPQA the channel matters: Anthropic reports Opus 4 and Sonnet 4 at 74.9 and 70.0 without extended thinking and 79.6 and 75.4 with it (Anthropic, 2025); ours, reasoning off, read 71.2 and 72.2. That is the split the hypothesis predicts: a derivation, which reasoning helps (Sprague et al., 2025), against a retrieval, which it does not.

<a id="tab-thinking"></a>

| Model | Reasoning off | Reasoning on | On minus off, 95% interval |
|---|---:|---:|---|
| Claude Haiku 4.5 | 5.99 | 5.31 | −0.67 [−1.83, +0.42] |
| GPT-5.6 Luna | 7.63 | 7.81 | +0.18 [−0.08, +0.47] |
| Claude Sonnet 4.6 | 7.00 | 7.31 | +0.31 [−0.09, +0.76] |
| GPT-5.6 Terra | 7.01 | 7.55 | +0.54 [−0.17, +1.31] |

Table: Factual rating with the reasoning channel off and on, six judges each, anchor at 7; bootstrap over judges and archetypes, percentile 95% intervals. One portfolio per cell; the vendors return summaries of the thinking, not the trace.

**Two consequences.** The agreement should be domain-matched, a model's factual score in a field tracking its GPQA accuracy in that field, testable from GPQA's subject labels and the released evaluations' domains; and archetype and topic domain should be separable in the latent space, the same archetype recoverable across unrelated domains and the domain across unrelated archetypes. Field-by-field agreement no higher than across fields, or representations that separate by domain only, would refute it. What the data establish is narrower: the factual pair reaches 0.94 with GPQA and the two subjective quarters lift it to 0.98 (Appendix D.1).

**Steering signal, and its caveat.** Self-improvement, the council governing its own rules, is specified but not exercised. A system optimised against $T$ is optimised against a consensus it participates in, so gains can come from courting the consensus; the partial answers are the two quarters consensus does not own and independently constituted councils.

**Scope.** The runs share one configuration — one prompt template, one roster — so the bootstrap intervals measure item and run-to-run dispersion, not the configuration (the four anchor values give the same leaderboard, Spearman 0.90–0.96); the leading group sits at its discrimination floor; a quarter of a non-council model's total rests on the contest's easier consistency test; no seat has yet been contested. Peer consensus is conservative against anomaly: a synthetic evaluator that reproduces the consensus and then inverts a fifth of its verdicts loses most of its competence (Appendix A.7), a penalty a dissenter pays on only half of $T$.

## 7 Conclusion

The *metanym game* is a structural test of intelligence built entirely of analogy, falsifiable sentence by sentence. The *council-of-peers benchmark* needs nothing outside itself: truth as the dominant axis of inter-evaluator agreement, reliability as invariance under a swept anchor, judges certified by the participants, contestable seats — and one external check, by design, $r = 0.98$ against GPQA Diamond.

## AI use statement

Every original idea in this work is the author's. The work was developed in a sustained dialogue with generative AI assistants (Anthropic's Claude), directed by the author throughout. Within that dialogue the assistants criticised the theory, the estimators and the experimental design as a reviewer in the field would, and proposed hypotheses and experiments alongside the author's; none was adopted without a competing hypothesis and a further experiment to test it. They implemented the analysis methods, cleaned and reformatted the evaluation records and GPQA response logs, and helped interpret results; they were also used for code, literature search, figures, references and first drafts, which the author rewrote into the author's own text. No data and no proofs were generated by AI: every rating in the paper comes from the twelve rated models of §3.1. All AI-assisted output was checked against the deterministic re-derivation of every published number (Reproducibility statement). The author takes responsibility for the final content.

## Ethics statement

The study evaluates commercial language models via their public APIs on self-generated material; no human subjects, personal data or annotators are involved. The benchmark is proposed as a candidate steering signal for self-improving systems. Steering by it would mean letting a consensus of models, with no human key, decide what counts as better, and a misunderstanding the models share would then be reinforced rather than corrected. The paper keeps the factual axis answerable to independent checks (§4.5) and leaves the self-improvement loop specified but unrun (§6); we regard that as the condition under which such a signal may be used. We consider the release of a key-free, contamination-resistant evaluation to be net positive for the field's ability to measure models past the point where human-written keys remain reliable, and we release all data and code under permissive licences.

## Reproducibility statement

Every number, table and figure in this paper recomputes deterministically from a released package (anonymised repository, supplementary material): the pinned evaluation runs (the un-anchored pass, the anchored pass at each of the four anchor values, and the three runs of the full pipeline — the canonical run and two regenerations), the raw per-question GPQA administration including both stages' records and the first-pass log, the anchor and ballast portfolios, the verbatim generation and evaluation prompts (Appendix B), the analysis scripts, and a one-command `reproduce.sh` whose steps are each labelled by the exhibit they produce. The re-analysis makes no API calls and needs no credentials; it takes about a minute. The estimators are specified to the equation in Appendix A, including every convention (self-entry filling, row-centering, sign and clamp, Procrustes alignment of bootstrap replicates, the joint (run, submission, archetype) resampling grid). Producing a *new* run — re-querying the models — is deliberately not part of the package: it costs API budget and is non-deterministic by construction; §4.6 reports what moves across three independent regenerations.

## References

Anthropic (2025). Introducing Claude 4. Announcement, 22 May 2025. https://www.anthropic.com/news/claude-4

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

Mitchell, M. (2021). Abstraction and analogy-making in artificial intelligence. *Annals of the New York Academy of Sciences, 1505*(1), 79–101.

Neisser, U. (1979). The concept of intelligence. *Intelligence, 3*(3), 217–227.

Ning, K.-P., Yang, S., Liu, Y.-Y., Yao, J.-Y., Liu, Z.-H., Tian, Y.-H., Song, Y., & Yuan, L. (2025). PiCO: Peer review in LLMs based on consistency optimization. *ICLR 2025.* arXiv:2402.01830.

Oh, J., Kim, E., Cha, I., & Oh, A. (2024). The Generative AI Paradox in evaluation: What it can solve, it may not evaluate. *EACL 2024 Student Research Workshop*, 248–257. arXiv:2402.06204.

Parisi, F., Strino, F., Nadler, B., & Kluger, Y. (2014). Ranking and combining multiple predictors without labeled data. *PNAS, 111*(4), 1253–1258.

Penn, D. C., Holyoak, K. J., & Povinelli, D. J. (2008). Darwin's mistake: Explaining the discontinuity between human and nonhuman minds. *Behavioral and Brain Sciences, 31*(2), 109–130.

Rein, D., Hou, B. L., Stickland, A. C., Petty, J., Pang, R. Y., Dirani, J., Michael, J., & Bowman, S. R. (2023). GPQA: A graduate-level Google-proof Q&A benchmark. arXiv:2311.12022.

Shannon, C. E. (1951). Prediction and entropy of printed English. *Bell System Technical Journal, 30*(1), 50–64.

Sprague, Z., Yin, F., Rodriguez, J. D., Jiang, D., Wadhwa, M., Singhal, P., Zhao, X., Ye, X., Mahowald, K., & Durrett, G. (2025). To CoT or not to CoT? Chain-of-thought helps mainly on math and symbolic reasoning. In *International Conference on Learning Representations (ICLR 2025)*. arXiv:2409.12183.

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

→ [`appendices/E_constructs.md`](appendices/E_constructs.md) — E. The eight constructs of intelligence the Metanym Game demands

→ [`appendices/F_regeneration.md`](appendices/F_regeneration.md) — F. Totals across three regenerations

→ [`appendices/G_anchoring.md`](appendices/G_anchoring.md) — G. What anchoring does to resolution

