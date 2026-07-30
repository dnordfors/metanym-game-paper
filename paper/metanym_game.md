# The Metanym Game: A Self-Contained, Self-Consistent LLM Peer-Community Benchmark for Structural Intelligence

## Abstract

The *metanym game* is a competitive word game for LLMs that measures structural intelligence against established cognitive-science constructs. No content is given in advance; the contestants create all of it — a new kind of analogy test, analogical *production* falsifiable sentence by sentence, with no fixed test set to leak into training (contamination-resistant by construction). In the *council-of-peers benchmark*, the contestants also rate each other's creations. We introduce the first spectral solution, to our knowledge, to the wicked problem of benchmarking LLMs' factual accuracy without golden keys or oracle models: one singular value decomposition of the evaluators' ratings matrix yields their competence as both generators and judges of true statements at once. Competence on the subjective criteria comes from each judge's rating consistency as the yardstick shifts. The factual rating correlates with GPQA Diamond at Pearson $r = 0.92$. Scored separately, making and judging dissociate — judging is the scarcer skill: the strongest generators are middling judges, the sharpest judge a mid-pack generator. To scale, the strongest players form a *council* that does the official benchmarking; its seats are contestable — a stronger model earns one on the benchmark's own rating. The benchmark is entirely self-contained and self-consistent, a stable gauge over time.

---

## 1. Introduction

Every benchmark for machine intelligence leans on an answer fixed in advance — a gold label, a human rating, a reference solution. The benchmark reported here has none. Twelve frontier language models invent the test, sit it, and grade one another; the benchmark then works out which of them are competent to grade at all. No human raters, no answer key, nothing to look up.

The test is the **metanym game**. A player takes a paragraph describing one domain and turns it into a factually true description of an unrelated one by swapping a handful of words and leaving the rest untouched: a description of cell signalling becomes, swap by swap, a true description of human language, and then of a microservice architecture — each sentence checkable on its own. The unchanged wording is a *context template*, the swapped words are *metanyms*, metaphorically synonymous, and each rewrite is a *parallel context* of one underlying *archetypal context*. The player chooses from no menu; it builds the structure from nothing. The metanym game makes a formal test of something a long tradition treats as central to thought — seeing one structure across wildly different domains. Where that tradition tests whether you *recognise* it, the game tests whether you can *build* it, and checks the result sentence by sentence — a new *kind* of analogy test, not just a harder one.

Two properties follow from building the items this way. Because every item is produced fresh in the run, there is no fixed test set to leak into a later model's training data: the benchmark is contamination-resistant by construction (§3). And because correctness is settled sentence by sentence — does this swapped claim hold in its new domain? — the game needs no answer key. The models supply the verdicts themselves, and the benchmark reads the truth off their agreement: stack every model's true/false judgements into one matrix, and its dominant direction reveals which judges are competent, with no labels at all (§4.3, Appendix A). That competent subset becomes the *council* that grades everyone — a benchmark that certifies its own judges.

A single run then makes three things visible (§4). The twelve models split into a leading eight and a trailing four. The divide follows *provider lineage* more than parameter count: one vendor's older generation falls away together with the roster's smallest seat, while within each family the size gradient is shallow. Judgement is the bottleneck: most models cannot reliably tell a true cross-domain claim from a false one, even when they produce competent structure themselves, so a model can be a perfectly *consistent* grader and still a *wrong* one. The strongest players — the models that clear the reliability bar — are seated as the council that issues the official ratings.

The game has a lineage — in the cognitive science of analogy and structural mapping (§2), and in the systems-theory claim that one abstract structure can recur across unlike domains (von Bertalanffy 1968). The rest of the paper builds the game (§2), turns it into the self-administering council benchmark (§3), reports the canonical twelve-model run (§4), and weighs what the numbers do and do not license (§5).

---

## 2. The metanym game

This section presents the game, building it step-by-step and relating it to previous research on language and intelligence.

### 2.a — The context template

Consider this passage describing **cell signalling**, from an old version of the Wikipedia article as it was worded when we first conceptualised the idea:

> CELL SIGNALING is part of a complex system of communication that governs basic CELLULAR activities and coordinates CELL actions. The ability of CELLS to perceive and correctly respond to their MICROENVIRONMENT is the basis of development, TISSUE repair, and IMMUNITY as well as normal TISSUE HOMEOSTASIS. Errors in CELLULAR information processing are responsible for DISEASES. By understanding CELL SIGNALING, DISEASES may be treated effectively. SYSTEMS BIOLOGY research helps us to understand the underlying structure of CELL SIGNALING networks and how changes in these networks may affect the transmission and flow of information. CELL SIGNALING \[is mostly thought of as\] signaling between CELLS of a single ORGANISM. However, CELL SIGNALING may also occur between the CELLS of two different ORGANISMS. *(adapted from Wikipedia's article on cell signalling)*

Now substitute the set of marked keywords with another set:

> HUMAN LANGUAGE is part of a complex system of communication that governs basic HUMAN activities and coordinates HUMAN actions. The ability of HUMANS to perceive and correctly respond to their ENVIRONMENT is the basis of development, COMMUNITY repair, and RESILIENCE as well as normal COMMUNITY EQUILIBRIUM. Errors in HUMAN information processing are responsible for DYSFUNCTIONS. By understanding HUMAN LANGUAGE, DYSFUNCTIONS may be treated effectively. SOCIOLOGY research helps us to understand the underlying structure of HUMAN LANGUAGE networks and how changes in these networks may affect the transmission and flow of information. HUMAN LANGUAGE \[is mostly thought of as\] LANGUAGE between HUMANS of a single SOCIETY. However, HUMAN LANGUAGE may also occur between the HUMANS of two different SOCIETIES.

Switching a few keywords and leaving everything else in place has turned a description of a cell system into a correct description of a human system. Each sentence stays factually true even where the borrowed phrasing reads stiffly — and it smooths out once rewritten in the target domain's own idiom. Cell signalling and human language are each other's *metaphors* here: their systems mirror each other across domains.

They also sit at different scales — cells are the elements of tissues and organisms; humans are the elements of communities — and the same structure recurs as you climb the scale. It is **scale-recursive**: the compositional hierarchy Salthe (1985) calls a *scalar hierarchy*, each level running on its own substrate (biochemical at the cellular level, linguistic at the social level), since two levels sharing a substrate would collapse into one. The systems-theory tradition (von Bertalanffy 1968) treats this scale-recurrence as one of nature's organising principles.

This fixes the vocabulary used throughout the paper. The true statements share a *context template*: slots held in a relation that is unaltered across domains. The template is literal but can be worded many ways — rewrite an instantiation in each domain's own jargon and the systems relationship survives. It is the literal representation of an *archetypal context* — the abstract system the parallel contexts share. Filling the template instantiates *parallel contexts* — the metaphors. The keywords that fill corresponding slots are *metanyms*, metaphorically synonymous (the word contracts *META*phorically syno*NYM*ous). One set of metanyms that fills the template to instantiate a single parallel context is a *metanym set*; tabulating several sets against the shared slots gives a *metanym table*.

An archetypal context, in this sense, is the structure shared across its parallel contexts — the kind of cross-domain *isomorphism* General Systems Theory studies (von Bertalanffy 1968). The context template is one way to write it down.

### 2.b — Outlining the metanym game

Before the rules, an example. Consider one context template whose slots are named as **general-systems roles** — an organizing structure, the components it organizes, their coupling, the emergent whole, and so on — instantiated across four cases chosen to lie about as far apart as cases can: Jung and Pauli's cosmic archetypes, von Bertalanffy's General Systems Theory, the archetypal contexts of this paper, and the baking of bread. The template:

> The fundamental structure of a system is defined by [ORGANIZING STRUCTURE], an invisible framework that dictates the organization of [COMPONENTS]. As these components interact through [COUPLING DYNAMICS], they generate a unified state of [EMERGENT WHOLE]. Without recognizing this inherent design, the system is mistakenly perceived as [APPARENT DISORDER]. However, by applying the principles of [MODELLING SCIENCE], we uncover that these structural patterns are not isolated phenomena. Instead, the specific relationships observed within [INSTANCE] are actually localized expressions of [GENERAL LAW].

and [these metanym sets](#tab-worked-metanym):

<a id="tab-worked-metanym"></a>

| Slot (general-systems role) | Jung/Pauli (psychophysics) | Bertalanffy (systems theory) | Archetypal contexts (this paper) | Baking (culinary science) |
|---|---|---|---|---|
| Organizing structure | cosmic archetypes | structural isomorphisms | archetypal contexts | baker's percentages |
| Components | mind and matter | system components | domain keywords | raw ingredients |
| Coupling dynamics | acausal synchronicities | dynamic interactions | contextual templates | thermal and biochemical reactions |
| Emergent whole | the *unus mundus* | systemic homeostasis | functional equivalence | structural leavening |
| Apparent disorder | a fragmented duality | disconnected phenomena | semantic isolation | culinary chaos |
| Modelling science | depth psychophysics | general systems theory | metanymic analysis | food science |
| Instance | human subjective experience | individual open systems | specific domain jargons | an individual bake |
| General law | a continuous psychophysical reality | universal laws of organization | scale-recursive abstract systems | thermodynamic and chemical laws |

Table: A worked metanym table — one context template (rows are slots, named as general-systems roles) filled by four metanym sets (columns are domains).

Slot each column into the template and the result holds, sentence by sentence. Here are the four, instantiated and then rewritten into each domain's own idiom:

#### 1. Jung and Pauli's Cosmic Archetypes

**Instantiated Template:**
The fundamental structure of a system is defined by COSMIC ARCHETYPES, an invisible framework that dictates the organization of MIND AND MATTER. As these components interact through ACAUSAL SYNCHRONICITIES, they generate a unified state of THE UNUS MUNDUS*. Without recognizing this inherent design, the system is mistakenly perceived as A FRAGMENTED DUALITY. However, by applying the principles of DEPTH PSYCHOPHYSICS, we uncover that these structural patterns are not isolated phenomena. Instead, the specific relationships observed within HUMAN SUBJECTIVE EXPERIENCE are actually localized expressions of A CONTINUOUS PSYCHOPHYSICAL REALITY.

**Idiomatic Rewrite:**
Transcendent, psychoid structures form the foundational scaffolding of experience, shaping both human consciousness and physical quantum states. When internal psychological meaning and external physical events coincide through synchronicity, they briefly reveal the *unus mundus*—the underlying, undivided whole. Modern rationalism traps us in the illusion that the subjective soul and the objective world are hopelessly severed. But through the collaborative lens of depth psychology and quantum mechanics, we discover that the archetypes governing our inner dreams are the exact same organizing principles structuring objective, physical matter.

---

#### 2. General Systems Theory (Bertalanffy)

**Instantiated Template:**
The fundamental structure of a system is defined by STRUCTURAL ISOMORPHISMS, an invisible framework that dictates the organization of SYSTEM COMPONENTS. As these components interact through DYNAMIC INTERACTIONS, they generate a unified state of SYSTEMIC HOMEOSTASIS. Without recognizing this inherent design, the system is mistakenly perceived as DISCONNECTED PHENOMENA. However, by applying the principles of GENERAL SYSTEMS THEORY, we uncover that these structural patterns are not isolated phenomena. Instead, the specific relationships observed within INDIVIDUAL OPEN SYSTEMS are actually localized expressions of UNIVERSAL LAWS OF ORGANIZATION.

**Idiomatic Rewrite:**
Universal laws of organization dictate how individual nodes within any complex network behave. Because these components process inputs and feedback through continuous loops, the network is able to self-regulate and achieve a stable equilibrium. Traditional scientific reductionism fails by isolating variables and treating them as entirely independent mechanisms. By embracing a systems-level view, we identify structural isomorphisms—patterns that recur across different levels of complexity. This shows that the equilibrium achieved by a single biological cell is governed by the same mathematical laws that structure entire economies and ecosystems.

---

#### 3. Archetypal Contexts (This Paper)

**Instantiated Template:**
The fundamental structure of a system is defined by ARCHETYPAL CONTEXTS, an invisible framework that dictates the organization of DOMAIN KEYWORDS. As these components interact through CONTEXTUAL TEMPLATES, they generate a unified state of FUNCTIONAL EQUIVALENCE. Without recognizing this inherent design, the system is mistakenly perceived as SEMANTIC ISOLATION. However, by applying the principles of METANYMIC ANALYSIS, we uncover that these structural patterns are not isolated phenomena. Instead, the specific relationships observed within SPECIFIC DOMAIN JARGONS are actually localized expressions of SCALE-RECURSIVE ABSTRACT SYSTEMS.

**Idiomatic Rewrite:**
Abstract, domain-agnostic blueprints provide the underlying logic that dictates how specific terminologies relate to one another. When functionally mirrored keywords—metanyms—are slotted into these shared textual templates, they render texts from entirely different fields structurally synonymous. Viewing language purely on a literal, surface level traps meaning inside isolated disciplinary silos. By stripping away the jargon and mapping the archetypal context, we see that the abstract structural logic is independent of vocabulary: the relationships described by the distinct languages of biology, sociology, and engineering are instantiations of the same nested logic.

---

#### 4. The Baking of Bread

**Instantiated Template:**
The fundamental structure of a system is defined by BAKER'S PERCENTAGES, an invisible framework that dictates the organization of RAW INGREDIENTS. As these components interact through THERMAL AND BIOCHEMICAL REACTIONS, they generate a unified state of STRUCTURAL LEAVENING. Without recognizing this inherent design, the system is mistakenly perceived as CULINARY CHAOS. However, by applying the principles of FOOD SCIENCE, we uncover that these structural patterns are not isolated phenomena. Instead, the specific relationships observed within AN INDIVIDUAL BAKE are actually localized expressions of THERMODYNAMIC AND CHEMICAL LAWS.

**Idiomatic Rewrite:**
A good loaf is not culinary guesswork; it is dictated by the mathematical ratios of baker's percentages, which fix flour, water, salt, and yeast relative to one another. As these raw materials undergo hydration, enzymatic fermentation, and thermal oven-spring, they set into a risen, structural leavening. To an amateur the kitchen looks like unpredictable magic, and a collapsed, dense loaf feels like an accident born of culinary chaos. Yet food science shows that dough chemistry is entirely deterministic: the success of a single bake is a localized expression of universal thermodynamic and chemical laws.

---

Slot each column into the template and every sentence holds. Notice *why* it holds so widely: the slots are named as general-systems roles — an organizing structure over its components, their coupling, the emergent whole, the apparent disorder a naïve eye sees, the science that models it, an instance, and the law that instance expresses. Read that way, the template is the generic schema of a systems-science explanation, so almost any system studied by a discipline instantiates it — a psyche–matter unity, an open system, our own framework, and an afternoon's baking alike.

This is therefore a very *general* archetypal context: it fits an enormous range of cases precisely because it encodes the bare form of structured explanation. That breadth is the unimpressive end of the spectrum — the archetypal contexts that matter most are far more *discriminating*, fitting one relational structure and excluding its neighbours (§2.c). What the example fixes is only the machinery: one template, filled by mechanically swappable metanyms, staying true sentence by sentence across maximal domain distance — which is what makes a metanym game decidable, and therefore measurable.

With the example in hand, the rules. The metanym game is played by N players and a non-competing administrator, and has two elements.

**1. Generation.** A player creates archetypal contexts from scratch: N context templates, M metanym sets per template, and for each set the instantiated template (Form (a)) and an idiomatic rewrite that reads naturally (Form (b)).

**2. Evaluation.** A player scores other players' submissions. To make the result a rating rather than a popularity vote, each submission is graded on the rubric axes (§3) against one fixed *reference* submission pinned at an *anchor* value, with the anchor swept across {5, 6, 7, 8} — the only thing that changes between passes. Run over a common submission set (in this paper, the council members' portfolios), a single evaluation round yields two ratings at once: the **submission ratings** (each portfolio, aggregated across evaluators) and the **evaluator ratings** — how well a judge detects the factual errors the panel collectively flags (factual competence) and how stable a standard it holds for the non-factual criteria as the anchor shifts — a competent judge's ranking is invariant under that non-semantic change (criterion reliability, measured by anchor-shift consistency). Both evaluator ratings read only a judge's scores of the *other* players' submissions, never its own.

The two elements are deliberately complete — a player generates and judges, and each act is itself rated — so the framework is **fully self-contained**: no human raters, no external answer key, each part producing one of the benchmark's ratings. Together the two elements place a conjunctive demand on a sizeable cluster of capacities that cognitive science treats as central to intelligence, which §2.c sets out and maps back to the two elements.

### 2.c — Types of intelligence put to test

The game demands a specific kind of intelligence. 

It tests one cluster — abstraction and analogy, among the most widely accepted lenses on general intelligence in AI (Chollet 2019; Mitchell 2021; Lake et al. 2017) — across both elements of the game (§2.b: generation, evaluation). It is one lens, not the whole: *general intelligence* is itself contested, and the game measures a central dimension of it. The constructs outside the cluster — perception, motor skill, working memory, processing speed, social and emotional intelligence — the game leaves alone. The eight constructs below are the ones the game directly demands; each is given as (a) the construct as its authors describe it and (b) the demand the game places on a player. The closing table maps each construct to the element(s) that call on it.

**1. Higher-order relational reasoning — Penn, Holyoak & Povinelli (2008).** Recognising when two situations share the same pattern of relations among their parts, even when the parts themselves are unrelated. The canonical test is to see that AABB and CCDD share the structure "two pairs of matching things" despite A, B, C and D being different objects — a capacity the authors argue most cleanly separates human from non-human reasoning. The metanym game tests the same thing: each slot is defined by its relations to the other slots, not by its filler word, and successful substitution shows the relational pattern survives.

**2. Structure-mapping — Gentner (1983, 1989); Falkenhainer, Forbus & Gentner (1989); Holyoak & Thagard (1995).** Three constraints govern analogical alignment: *systematicity* (Gentner 1983), *one-to-one correspondence*, and *parallel connectivity* (the latter two formalised in the structure-mapping engine; Falkenhainer, Forbus & Gentner 1989). The metanym table is the structure-mapping bookkeeping written down — rows are slots, columns are target domains, each cell is a one-to-one mapping. Mechanical substitutability enforces one-to-one correspondence and parallel connectivity; systematicity — Gentner's stronger demand that higher-order relations constrain the mapping — is not guaranteed by substitution and is judged rather than assumed (the `intelligence` axis).

**3. Analogy as core cognition — Hofstadter & Sander (2013).** *Essence-seeing* — spotting that a novel situation is structurally an instance of a known abstract pattern despite different surfaces — as the mechanism of cognition rather than a special-purpose module. In the metanym game, it means seeing the essence of the context template, which is the archetypal context.

**4-5. Fluid and Crystallized intelligence — Cattell (1963); Horn & Cattell (1966); Carroll (1993); McGrew (2009).**  
* *4. Fluid intelligence*: Reasoning on the fly over an unfamiliar context and drawing novel conclusions instead of retrieving them. In intelligence tests, this is probed by 'what is the next shape in the series?' or 'fill the missing slot with the correct symbol'. The metanym game is the verbal version: identifying a metanym set for instantiating a factually correct parallel context. 
* *5. Crystallized intelligence*: Having knowledge and knowing how to use it. In intelligence tests, this is probed by quiz-style questions whose answers cannot be worked out, only known. The metanym game probes it twice over: each metanym must be a word the player knows the meaning of, and the resulting sentence must be factually true in its domain. Knowing a broad vocabulary and a deep store of domain facts is a strength in the metanym game.

**6-7. Convergent and Divergent production — Guilford (1967) Structure-of-intellect model.**   
* *6. Convergent production*: Generating the single correct answer that converges from many constraints (canonical example: "man : woman :: king : ___"). In the metanym game, mechanical substitutability of metanyms in the context template admits no near-misses on the evaluation side: either the instantiated sentence is structurally coherent and factually defensible (passes) or it isn't (fails).
* *7. Divergent production*: Knowing how to use the same knowledge (or word) in many different and novel ways, setting out from the same starting point. In the metanym game, the same context template is applied in widely different domains, with each domain represented by its own metanym set.

**8. Theory formation by analogy — Hesse (1963); Boyd (1979).**   
Hypothesis-by-analogy drives scientific exploration. Hesse showed that theories work by extending a known analogy into unmapped territory to generate predictions; Boyd argued that some core concepts — *brain as computer*, *gene as code* — *are their analogy, with no separable literal core*. Each archetypal context is theory construction in miniature: the context template is the root analogy, and the parallel contexts are its metaphors. The factuality of each metaphor is the empirical test, and cross-domain span is the demand that the structural claim survive surface-disparate domains.

The eight constructs are [summarised below](#tab-constructs), mapped to the two tasks that call on each (references are in the paragraphs above; ● marks a primary demand). The pattern of shared cells previews §5.4: structure-mapping and higher-order relational reasoning run through both tasks; generation alone calls on essence-seeing, fluid intelligence, divergent production, and theory-by-analogy; evaluation alone turns crystallised knowledge and convergent production toward judgement.

<a id="tab-constructs"></a>

| Construct | Generation — invent the template | Evaluation — judge a portfolio |
|---|---|---|
| Higher-order relational reasoning | ● lay out the relational skeleton | ● check the relations survive |
| Structure-mapping | ● the slots-and-domains scaffold | ● verify one-to-one correspondence |
| Essence-seeing (analogy as core cognition) | ● see the archetype behind the surface | |
| Fluid intelligence | ● reason out a novel structure | |
| Crystallised intelligence | | ● detect false claims |
| Convergent production | | ● pass/fail, no near-misses |
| Divergent production | ● invent a structure that travels | |
| Theory formation by analogy | ● template = root analogy, tested by fact | |

Table: The eight cognitive-science constructs the metanym game demands, mapped to its two tasks.

*Production-level character.* The canonical instruments of the cited traditions are largely *recognition* tasks: PHP's higher-order task is match-to-sample; Gentner's structure-mapping engine models how humans *interpret* a given source-target analogy; Hofstadter & Sander present essence-seeing through case studies. The metanym game is a *production* task — the participant generates the template and the metanym sets from scratch. Production is a stronger demand than recognition — one can sometimes pass a recognition task by elimination or surface heuristics; production has no such fallback. The framework shifts the test from recognition and interpretation to production — a heavier cognitive register than the prior literature's canonical instruments.

*What is new here.* Each ingredient of the context template has a neighbour. Slot-bearing templates are frames (Fillmore 1982; Minsky 1975) and constructions (Goldberg 1995); a schema standing above several parallel instances is the induced problem schema of Gick & Holyoak (1983); an abstract structure recurring symmetrically across unrelated domains — the archetypal context itself — is General Systems Theory's isomorphism (von Bertalanffy 1968). What none of them carries is the conjunction the metanym game demands: one template re-bound jointly across five-plus domains with no privileged source, under the demand that every substituted sentence remain literally true — a per-sentence falsifiability test the analogy, schema-induction, and metaphor traditions never operationalised (conceptual metaphor in fact requires literal falsity; Lakoff & Johnson 1980). The novelty is the test: the abstract structure made mechanically checkable, sentence by sentence, in a production task.


## 3. The metanym game as a benchmark

### 3.1 Setup

Twelve frontier LLMs from three providers serve simultaneously as generators and as members of [the evaluator panel](#tab-panel):

<a id="tab-panel"></a>

| Provider | Models |
|---|---|
| Anthropic | claude-opus-4.5, claude-opus-4.1, claude-opus-4.0, claude-sonnet-4 |
| Google | gemini-3.1-pro, gemini-2.5-flash |
| OpenAI | gpt-4.1-2025-04-14, gpt-4.1-mini, gpt-4.1-nano, gpt-4o, gpt-4o-2024-08-06, gpt-4o-mini |

Table: The twelve-model council-of-peers panel, by provider.

This is a deliberately heterogeneous panel, assembled from the models available to us and chosen to exercise the structural cases the protocol must handle rather than to census the frontier. It spans roughly an order of magnitude in scale, so competence and reliability have room to separate; it draws on three vendors, so the cross-vendor agreement the no-key reliability measure rests on can be tested rather than assumed; it includes several models from one vendor and adjacent versions within a single family (Opus 4.0 / 4.1 / 4.5), which stress the protocol's resolution and its safeguard against same-vendor agreement masquerading as competence; and it spans size tiers within a family, a known capability gradient the ranking should recover. Because the benchmark is a re-runnable protocol whose ratings are panel-relative, no conclusion depends on this particular roster — and drawing on what was at hand, rather than a curated set, removes any concern that the panel was chosen to flatter the method.

All twelve are called with **Temperature=0**, **reasoning/thinking disabled**, and **tools disabled**. This choice fixes the test on the model's base capability and removes three confounds at once. **Determinism** (T=0) makes N=1 per cell sufficient — re-running produces bit-identical output. **No reasoning** tests the model's direct response, not the output of an internal deliberation loop that varies between providers in opaque ways. **No tools** removes external-information channels that could leak factual content the model itself does not represent.

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

**Why these settings.** Four design choices justify themselves on first principles. 

(i) **Per-submission cardinal rating rather than side-by-side ranking.** 25-PC portfolios already press against context windows when more than one is present, and prompt-internal attention is uneven; per-call rating sidesteps both at once. 

(ii) **Calibration against a fixed anchor.** Cardinal scores drift between evaluators — one model's "8" is another's "6". Pinning a fixed reference portfolio at a known score on every axis turns each evaluator's idiosyncratic scale into a common one and recovers discriminability at the top, where the 1–10 ceiling otherwise compresses the strongest portfolios into an indistinguishable cluster. §3.4 explains how the anchor portfolio itself is chosen.

(iii) **Holistic axes, not analytic decompositions.** The five non-factual axes are high-level concepts (`beauty`, `intelligence`, `instantiation_distinctness`, `impressive_length`, `structural_diversity`), not sub-criteria. Two reasons.   
* *Principled*: a detailed scoring rubric is also a template-construction tutorial — generators must be told how submissions will be rated, so every clause in the rubric leaks back into the generation prompt as guidance about what to produce. We want to score what models *recognise* as beautiful or intelligent, not what they can be coached to construct.  
* *Empirical*: frontier models agree most tightly on the most holistic judgement. Across the un-anchored 12×12 matrix, mean inter-evaluator standard deviation per cell was lowest for `beauty` (1.07 on the 1–10 scale), then `factual_per_pc` (1.11) and `intelligence` (1.15); the more concrete `instantiation_distinctness` (1.25) was the least consistent. Models converge on high-level judgements without a checklist.

(iv) **Minimal prescription overall.** Every additional directive in an evaluator prompt measurably shifts the score distribution, so prescription is held to what the protocol requires.

(v) **`impressive_length` counterweights per-sentence factual scoring.** Without it the dominant strategy is the minimal template — fewest sentences, least error exposure — and a leaderboard scored without it would advantage short templates. A longer template that stays true in every sentence is the harder accomplishment, and padding is not free: every added sentence is another claim `factual_per_pc` scores.


### 3.3 The self-governing benchmark

In its steady state, the benchmark operates as a **self-governing protocol** run by the council. A council of LLM evaluators (five in the canonical run) scores any submitted portfolio against a fixed anchor reference on the six-axis rubric of §3.2. The protocol is simple:

- the **council** is a set of five LLM evaluators chosen for reliability;
- the **anchor** is one fixed portfolio pinned at 7 on every axis as the calibration reference;
- a **new submission** joins the leaderboard by being scored by the council, against the anchor, on the rubric.

Each council member receives two ratings: a **generation rating** (the LSO mean of the other council members' scores of its portfolio) and an **evaluator rating** — the factual-competence and criterion-reliability scores from the evaluator-rating routine (§4.3), themselves LSO in the same sense, since a model's ratings of its own portfolio are excluded from its own reliability — reported separately and never merged with the generation rating. Non-council models receive only a generation rating, computed by the same council against the same anchor.

The benchmark **scales by addition**. Any future model — open-weights, next-generation, or external — can be evaluated against the same published anchor by the same council without re-deriving anything. It is also **self-administering** (no human evaluators or gold key, so re-runs are not bottlenecked on human labelling) and **reproducible** (at T=0 with no reasoning channel, every cell is bit-identical on re-run, so the same anchor and the same council produce the same leaderboard on demand). Bit-identical reproducibility is a property of the seats, not the protocol: models that deprecate the temperature control cannot be pinned to T=0, so a council holding such seats reports N>1 samples with intervals instead — protocol and anchor unchanged.

**Contamination.** Items are generated fresh each run, so no fixed test set can leak into training. Published past submissions could enter training corpora — a leak touching generation only, so a suspiciously large generation–evaluation gap is itself the detector, and new portfolios are screened against the archived submissions of record. Format familiarity is not contamination: every model tested understands the task as posed; what is scored — the items — is new each run.

### 3.4 Bootstrapping the self-governing benchmark

The steady-state protocol of §3.3 requires a council and an anchor. The bootstrap is three stages, run once, which produce them.

A good benchmark needs four properties: an unbiased baseline ranking, discriminability where the field is dense, scores weighted toward trustworthy judges, and a scoring rule that scales by addition. The first three are delivered by the bootstrap; the fourth by the steady-state protocol of §3.3.

1. **Initial selection (un-anchored).** A 12×12 LSO evaluation across all generators serves two purposes: it produces a baseline all-against-all leaderboard, and it identifies a top performer whose portfolio will become the anchor reference. Without an empirically-grounded winner, the choice of anchor would be arbitrary.

2. **Anchored re-evaluation.** The 1–10 scale produces ceiling compression — top models cluster within 0.35 points and are not all resolvable. Anchoring against a fixed reference (the stage-1 winner's portfolio, pinned at a known value on every axis) is the standard psychometric move to recover discriminability at the top. We sweep the anchor value across {5, 6, 7, 8} not because four anchors enter the final score, but to record how each evaluator responds to a controlled shift in the calibration instruction. That sweep data is the input to stage 3.

3. **Council selection.** A panel-wide leaderboard can be distorted by evaluators that don't engage with content or that re-order targets randomly under calibration shifts. We test each evaluator on two independent reliability criteria — factual competence (does its error-flagging align with the panel's shared error signal? — a key-free covariance measure) and criterion reliability across the anchor sweep (does the evaluator hold a stable standard for each criterion when the anchor moves? — anchor-shift consistency, a Pearson measure). Both are computed leave-self-out: an evaluator is judged on how it rates the *others'* portfolios, never its own. The criteria are independent by construction: each probes something the other doesn't. Evaluators that pass both form the **council**. Selection is on reliability evidence, not on generator score, not on architecture, and not on agreement with a gold key.

When the bootstrap completes, the council is selected and the anchor is fixed; the steady-state protocol of §3.3 takes over. §4 reports the bootstrap data (stages 1–3) and the resulting steady-state leaderboard (the council's official ratings).

### 3.5 The chair mechanism: promotion and relegation

§3.3 lets any new submission be *scored* against the council; this section lets a strong new model *join* the council. The benchmark runs as a standing service with a fixed seat count *N* (here five): the council holds the *N* most capable models, and any model may nominate itself as a **contestant**. A round either promotes the contestant — demoting the current lowest seat — or rejects it. A non-competing **administrator** runs the round: it collates the council's evaluations, writes them up, and computes the scores, but never scores submissions itself.

**The anchor is a constant.** The calibration reference is one fixed submission — the bootstrap winner's portfolio (reproduced in Appendix C), pinned at 7 on every axis — against which every submission is scored, so all scores stay directly comparable. As models improve, a 7-quality reference may eventually need raising: the anchor can be replaced by a stronger submission, and the council re-scores the old anchor against the new one to obtain a **recalibration factor** that maps earlier scores onto the new standard.

A round proceeds in six steps:

1. **Generation.** The contestant produces a portfolio of five archetypal contexts (§3.2), including the self-review pass in which it may Keep / Revise / Replace each of its own submissions before entering them.
2. **Council evaluation.** Each council member scores the contestant's portfolio against the frozen anchor on the six-axis rubric, at T=0 with reasoning and tools disabled.
3. **Write-up and scoring.** The administrator collates the council's evaluations into a per-scoring-unit synthesis and computes the contestant's anchored score (the mean of the six axis scores).
4. **Promotion gate.** The contestant is promoted only if it clears two independent gates. **(a) Generation margin:** its anchored score must exceed the current lowest seat's score by a *resolvable* margin — a paired-bootstrap difference whose CI excludes zero — not merely a higher point estimate; a raw-difference rule would churn the roster on within-noise differences the panel cannot resolve (§4.5). **(b) Evaluator admission:** the contestant must also be a reliable *judge* — it evaluates the incumbents' portfolios and must earn the *reliable* verdict from the evaluator-rating routine (§4.3): factual competence among the council's detectors, and stable target ratings (Pearson) under the anchor sweep. Because the competence measure needs no answer key, admitting a new judge requires nothing to be hand-annotated — it follows from how the contestant's flagging aligns with the sitting council. The council is an evaluator body, and generation skill alone does not qualify a member, since generation and evaluation quality correlate only imperfectly (§5.2).
5. **Roster change (on promote).** The seat that was lowest *at the start* of the round is demoted — fixed at the start so the recompute in step 6 cannot make the decision circular. The contestant takes the seat. The demoted model stays on the leaderboard with a generation rating; it loses only its evaluator seat and rating.
6. **Recompute and record.** With the new council, the administrator recomputes every member's generation rating on a common evaluator set — so the just-promoted member's scores are folded in and no member is judged by a different-sized panel than another — and updates the council evaluations of record. It then bumps the council version and writes a provenance record: previous roster, new roster, the contestant's and demoted seat's scores, the margin, and the round identifiers.

Each step is deterministic at T=0 for a fixed contestant, but the steady-state roster can be **path-dependent**: a different order of contestant arrivals may settle on a different council. We therefore index every published leaderboard by its council version and recommend that cross-version claims be checked against the frozen anchor rather than against an earlier version's scores. The canonical run of §4 reports council version 0 — the bootstrap output — and does not exercise a promotion round; the chair mechanism is specified here as the maintenance protocol for the standing benchmark.

---

## 4. Results: validating the benchmark and bootstrapping the first council

This section does two things at once: it **validates** the benchmark and it **bootstraps** the first council. Validation — the key-free factual ratings agree closely with an independent external test (GPQA Diamond, §4.7), a second instrument rather than an oracle, and survive dropping any single vendor's judges (§4.3). Bootstrap — the three stages of §3.4 run once over the twelve-model field: un-anchored selection (§4.1), anchored re-evaluation (§4.2), and reliability-based council selection (§4.3), followed by the official generation ratings (§4.5) and the symmetric total (§4.6). The bootstrap happens only here. Once this first council is seated, no later model is bootstrapped in — a new model earns a seat only by contesting for one against the sitting council on the fixed anchor (the chair mechanism, §3.5).

### 4.1 Initial selection (un-anchored)

[The full-panel LSO leaderboard](#tab-unanchored) with 95% bootstrap confidence intervals (Efron & Tibshirani 1993; 2000 resamples, seed `20260529`):

<a id="tab-unanchored"></a>

| Rank | Generator | Mean | 95% CI |
|---:|:---|---:|---|
| 1 | **claude-opus-4.5** | **9.28** | **[9.00, 9.54]** |
| 2 | claude-opus-4.1 | 9.20 | [8.86, 9.50] |
| 3 | claude-opus-4.0 | 9.02 | [8.59, 9.40] |
| 4 | claude-sonnet-4 | 8.93 | [8.48, 9.32] |
| 5 | gpt-4.1-2025-04-14 | 8.88 | [8.45, 9.24] |
| 6 | gemini-2.5-flash | 8.79 | [8.42, 9.15] |
| 7 | gpt-4.1-mini | 8.67 | [8.02, 9.21] |
| 8 | gemini-3.1-pro | 8.64 | [8.16, 9.10] |
| 9 | gpt-4o-mini | 8.25 | [7.35, 8.98] |
| 10 | gpt-4o | 7.91 | [7.01, 8.64] |
| 11 | gpt-4o-2024-08-06 | 7.90 | [7.06, 8.65] |
| 12 | gpt-4.1-nano | 7.32 | [6.14, 8.28] |

Table: Initial selection — un-anchored leaderboard (all twelve models as generators).

*Mean: each generator's portfolio scored 1–10 by every other model on the six-axis rubric with no calibration anchor, averaged leave-self-out across evaluators. 95% CI: percentile bootstrap, 2000 resamples. Higher is better. This baseline ranking only selects the calibration anchor (the top model's portfolio); the official rating is in §4.6.*

The ranking breaks in one place. Eight models run from 8.64 to 9.28 in a smooth gradient — the four Anthropic Claude 4 seats, both Gemini seats, and the GPT-4.1 base and Mini — with no two adjacent means more than 0.17 apart and no adjacent pair individually resolved (0.53–0.75). Below them the four remaining OpenAI seats fall away, the three GPT-4o variants and GPT-4.1-nano, from 8.25 down to 7.32. That break is the only one the bootstrap supports: every one of the thirty-two pairs across it holds with probability at least 0.79. What separates is a vendor generation rather than a size class — the seats that fall away are OpenAI's older GPT-4o line plus its smallest model, while Sonnet-4, the smallest Anthropic seat, stays in the upper band, Flash sits beside the far larger 3.1 Pro, and gpt-4o-mini outscores the full-size gpt-4o. Within-family size gradients are shallow next to the difference between families. The highest mean is **claude-opus-4.5**'s, and its portfolio becomes the calibration anchor; the anchor's role is to fix a common yardstick, so it need only be a strong portfolio, not a provably best one, and the upper band's internal order is left to the anchored rating in §4.6.

### 4.2 Anchored re-evaluation

The 1–10 scale produces ceiling compression near the maximum: in §4.1, four Anthropic models cluster within 0.35 points of each other in the upper end of the scale and are not all distinguishable. To recover discriminability at the top, we adopt the standard psychometric move of anchoring against a fixed reference: pin one submission at a known score on every axis, and ask evaluators to score each target *relative to* that anchor.

The reference submission is **claude-opus-4.5's portfolio**, fixed at 7 on every axis. We re-run the 12-by-12 evaluation matrix under anchored scoring, and we sweep the anchor value across {5, 6, 7, 8} so that every evaluator's response to a controlled shift in the calibration value is recorded as well. The sweep produces four parallel 12×12 matrices and is the data foundation for both §4.3 (evaluator reliability) and §4.5 (official ratings).

The anchored protocol substantially increases the panel's discriminative power. Between-target variance is 2.5× larger than under un-anchored scoring; mean within-target stdev rises only modestly (1.14×); the F-statistic — between-target variance over within-target variance, the standard measure of resolution — rises from 0.33 to 0.66, nearly double. Both values sit below 1 — judges still disagree about a single target more than targets differ from one another — so the gain is in relative resolution, and what the anchored data will bear is settled by the bootstrap intervals, not by F alone. Those intervals sharpen the single division of §4.1 rather than revealing new ones. The division survives anchoring without interleaving — every portfolio above it stays above every portfolio below — and the gap across it widens from 0.39 to 0.94, from a fifth of the spread of the means to two fifths, with all twenty-eight scored cross-pairs holding at probability 1.00. Inside the leading group the ordering still sits below resolution: no adjacent pair is resolved under both resampling conventions, the strongest reaching 1.00 under a shared evaluator index but only 0.88 when each portfolio's evaluators are resampled independently. Anchoring widens the division; it does not resolve the ranks within either group.

### 4.3 Evaluator factual competence

Anchored data in hand, we ask of each evaluator the two questions on which their official-rating eligibility depends.

**The evaluator-rating routine.** An evaluator's rating is the output of a fixed, reusable procedure — run here on all twelve models in the bootstrap, and re-run unchanged on any later promotion contestant (§3.5). It takes the panel's anchored evaluation matrix and the anchor sweep {5, 6, 7, 8}; its factual-competence measure (Criterion A) needs **no answer key**. It returns two scores — a *factual-competence* score (Criterion A) and a *criterion-reliability* score (Criterion B, measured by anchor-shift consistency) — reported separately and **never folded into the generation rating**: how good a judge a model is never changes its score as a maker. The generation and evaluator ratings stay distinct measurements, meeting only at the end as separate components of the total $T$ (§4.6). From these it derives a binary *reliable* verdict — factual competence clear of the inert band **and** criterion reliability on the non-factual axes (anchor-shift consistency, Pearson ρ ≥ 0.78) — which gates council membership but is not itself folded into any other quantity. Both scores are **leave-self-out**: an evaluator is judged only on how it rates the other portfolios. (Criterion A and Criterion B treat the self-pairs differently, and Appendix A.2 says how: Criterion A keeps the self-entry in its matrix and sets it to the anchor value, Criterion B drops it outright.) Both criteria run on the freely generated portfolios of §4.2: factual competence is an error-*detection* measure, so it needs a substrate that contains errors to detect, and freely generated portfolios are error-bearing — a model's worst factual mistakes are largely self-inflicted by the templates it invents. The two subsections below are this routine applied to the twelve evaluators.

**Criterion A — factual competence.** When it comes to factual competence — the ability to tell stronger instantiations from weaker — we assume that good evaluators agree with one another about which instantiations are factually weaker, once each evaluator's own leniency is removed, and the better two evaluators are, the more they agree. In its mathematical form this is an eigenequation, whose leading solution assigns a factual-competence coefficient to each evaluator accordingly. We obtain those coefficients not by knowing the truth about what is judged, but by comparing the evaluators' judgements with one another. This matters beyond convenience: because the instantiations are generated in the run, they can assert claims no answer key covers, and for genuinely new knowledge no key can exist — leaving the considered agreement of competent peers as the only available standard, which is the logic scientific peer review already runs on. We stack the panel's factual scores into one matrix — the twelve evaluators against the 275 parallel contexts of the eleven scored portfolios (25 per portfolio, exactly $11\times25$: the two six-archetype submissions contribute their first five archetypes only, the ten contexts of their sixth being excluded so that the panel stays balanced; Appendix A.2.b), each entry the evaluator's $1$–$10$ factual rating used **directly**, with no thresholding into true/false — row-centre it to remove each evaluator's leniency, and take its **singular value decomposition** (Appendix A.2.a). The construction is a graded relative of the classical label-free aggregators — Dawid & Skene's (1979) latent-competence model and Parisi et al.'s (2014) spectral meta-learner, which rank predictors by the leading eigenvector of their covariance — but it operates on the graded $1$–$10$ ratings rather than binarised verdicts. Those aggregators need a binary verdict, which ratings cannot supply without either parsing free-text comments or an arbitrary threshold — and the threshold matters: binarising this matrix at $t \in \{4,5,6\}$ shifts the competence ordering (Spearman 0.78–0.90 vs graded) and flips the marginal council seat. The graded SVD needs neither. The leading factor of the row-centred matrix $\tilde F$ (evaluators × instantiations) is rank-one,

$$\tilde F_{sj} \;\approx\; \sigma_1\, u_s\, v_j, \qquad f \equiv u\ \text{(left singular vector).} \tag{1}$$

An evaluator's rating tracks the consensus pattern in proportion to its competence $u_s$ times that instantiation's factual standing $v_j$ — competence and standing fall out of one factorisation, with **no answer key**. The *left* singular vector — the leading solution of that eigenequation — scores each **evaluator**'s factual competence — high when its ratings align with the panel's shared signal, ≈ 0 when it rates everything alike or idiosyncratically — and the *right* singular vector scores each **instantiation**'s factual standing. It rests on a single hypothesis: that the only thing competent evaluators share is the truth, so the dominant axis of their leniency-removed agreement is the competence axis. The factorisation's substantive product is the **left** singular vector — each evaluator's factual competence $E^{F}$, the key-free quantity the council gate uses. The **right** singular vector, aggregated per generator, gives a generator-factuality score $G^{F}$, but this is not a second, independent measurement: it equals the panel's own $1$–$10$ factual ratings of that generator **weighted by each evaluator's competence** $E^{F}$ — equivalently, the per-generator average of the right vector — the two coincide exactly in the rank-one limit and agree to $\le 0.14$ ($r = 1.00$) in the data, their difference being the off-axis residual (Appendix A.2.a). The factorisation earns its keep on the evaluator side; the generator score is that same information re-weighted. Both are tabulated below, bootstrapped over the 275 columns ($E^{F}$ aligned across replicates by 2-component Procrustes: the leading axis is globally well separated — $\sigma_1/\sigma_2 = 2.6$, 70% of variance — but rotates between the Anthropic and Google blocs under resampling). $E^{F}$ is shown twice: the raw left-vector **loading** (a dimensionless competence weight) and, **anchored** to the $1$–$10$ scale ($7f/f_a$ — the form that enters the total $T$, §4.6), which makes it directly comparable with $G^{F}$. The 95% interval is given once, on the anchored $E^{F}$ and on $G^{F}$. Opus-4.5 is the anchor reference — its anchored $E^{F}=7$ and $G^{F}=7$ by construction (the generation reference):

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
| gpt-4o-2024-08-06 | 0.05 | 0.62 | [0.25, 0.38] | 5.22 | [5.04, 5.37] |
| gpt-4.1-nano | 0.04 | 0.49 | [0.13, 0.25] | 3.66 | [3.16, 4.13] |
| gpt-4o | 0.03 | 0.34 | [0.13, 0.13] | 5.11 | [4.90, 5.32] |
| gpt-4.1-2025-04-14 | 0.02 | 0.20 | [0.13, 0.25] | 6.50 | [6.28, 6.69] |
| gpt-4o-mini | 0.00 | 0.00 | [0.00, 0.00] | 3.20 | [2.80, 3.73] |

Table: Criterion A — evaluator factual competence and generator factuality (key-free SVD).

*One SVD of the row-centred evaluator×instantiation factual-rating matrix, with no answer key. $E^{F}$ = evaluator factual competence (left singular vector): "loading" is the raw competence weight (0 = no factual signal), "anchored" rescales it to the 1–10 scale as $7f/f_a$. $G^{F}$ = generator factual competence (right vector): the panel's 1–10 factual ratings of that generator, weighted by each evaluator's $E^{F}$. claude-opus-4.5 is the anchor ($E^{F}=7$ and $G^{F}=7$ by construction, the generation reference). 95% CI: bootstrap over the 275 instantiation columns. Higher = more factually competent.*

Five evaluators (0.28–0.58) separate decisively from the rest; the lower seven taper from claude-sonnet-4 (0.13) into an inert band whose small positive loadings are not robustly distinguishable from zero — those models rate near-identically and carry little error signal. claude-sonnet-4 sits closest to the boundary; its loading (0.13), with a CI touching gpt-4.1-mini's, does not clear the inert band, so the decisive cut falls after the top five.

Both factual ratings — evaluator competence $E^{F}$ and generator factuality $G^{F}$ — are checked against an independent external benchmark (GPQA Diamond) in §4.7.

**Criterion A, same-vendor robustness.** The key-free factual axis assumes near-independent errors, so the fair worry is that a Claude-heavy panel reads Claude-bloc agreement as truth — "Anthropic models grade Anthropic models first." They do not. Recomputing the generator-factuality ordering $G^{F}$ with each vendor's judges removed leaves it essentially unchanged, and a *Claude-free* panel (Google + OpenAI judges only) still places [the Claude generators at the top](#tab-vendor-robustness):

<a id="tab-vendor-robustness"></a>

| Judge panel | Spearman vs full | Claude generators | GPT-4o family |
|---|--:|:--:|:--:|
| full (12 judges) | 1.00 | top | bottom |
| − Anthropic judges | 0.96 | still top | bottom |
| − Google judges | 0.98 | top | bottom |
| − OpenAI judges | 0.99 | top | bottom |
| Claude-free (Google + OpenAI) | 0.96 | top ($\ge 7.0$) | bottom |

Table: Criterion A — same-vendor robustness of the factual ordering.

*The generator factual ordering $G^{F}$ recomputed with each vendor's evaluators removed. Spearman vs full: rank correlation of the reduced-panel ordering against the full twelve-judge ordering (1.00 = identical). The last two columns report where each model group lands. The Claude models' standing survives even a Claude-free panel, so it is a cross-vendor verdict, not same-vendor agreement.*

The ordering survives dropping any single vendor's judges (Spearman $\ge 0.96$ throughout), the inert GPT-4o family stays at the floor under every panel, and — against the self-preference worry specifically — Anthropic's own judges rate if anything slightly *harsher* than the cross-vendor panels (dropping them *raises* several non-Claude scores). The Claude models' lead is a cross-vendor verdict, not Claude grading Claude.

### 4.4 Evaluator criterion reliability and the initial council

**Criterion B — criterion reliability.** Beyond catching factual errors, a reliable evaluator needs a stable internal standard for each non-factual criterion — a clear, reusable sense of what makes one submission more beautiful, more intelligent, more distinct than another. We call this the evaluator's **criterion reliability**, and we read it off its *anchor-shift consistency*. The anchor is the fixed reference every submission is scored against; we sweep its value across 5, 6, 7, and 8 — the *only* difference between the four runs (at T=0 every cell is otherwise identical). An evaluator with genuine criterion reliability gives the submissions the same pattern of relative scores whichever value is used: its view of which work is better should not change with the choice of calibration point. For each evaluator, and **for each rating axis separately**, we correlate (Pearson) the scores at one anchor with the scores at another, averaged over the six anchor pairs; this per-axis consistency is the diagnostic per-criterion reliability $E^{C}_a$ ($a$ = beauty, intelligence, distinctness, length, structural diversity). The measure is **leave-self-out**: an evaluator's ratings of its own portfolio are collected in the run but never enter its own consistency, so each evaluator whose portfolio is among the eleven graded submissions is scored on the ten *others* — fifty (submission, archetype) units — while the anchor, whose portfolio is the reference rather than a graded submission, is scored on all eleven (fifty-five). The two submissions that returned a sixth archetype contribute their first five, so every portfolio weighs the same (Appendix A.2.b). Because the anchor is the only thing that changed, a low correlation on an axis has two readings: the evaluator lacks a clear sense for that axis — the collapse is *axis-specific* — or it holds no stable standard to place on the scale at all — the collapse is *uniform* across axes. The uniform case is not an arithmetic deficit: the models that fail that way handle standard math fine (the original gpt-4o scores 95% on grade-school GSM8K), so it reflects inconsistent evaluation, not weak numeracy.

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

Table: Criterion B — anchor-shift consistency, per evaluator and axis.

*This is the **anchor-shift consistency** table: for each evaluator and axis, the mean pairwise Pearson correlation of its per-axis scores across the four anchor values (5/6/7/8). It measures self-consistency, not accuracy (the `factual` column is the consistency of factual scoring across anchors, distinct from the Criterion A factual-competence loading — e.g. Sonnet-4 reads 0.70 here but 0.13 there). The **criterion-reliability** rating derived from this consistency — anchored, and the value that enters the total $T$ (§4.6) — is defined below.*

The breakdown reads as an abilities profile. The **factual** column tracks Criterion A directly: the two models whose factual consistency collapses while their other axes hold — gpt-4.1-2025-04-14 (0.24) and gemini-2.5-flash (0.31) — rate factuality near-randomly across anchors, which is why they cannot scale those ratings consistently (Flash nonetheless clears Criterion A on its competence loading, where gpt-4.1-2025-04-14 does not). **Length** and **structural diversity** hold up best across the competent models (0.78–0.92). **Distinctness** is the axis the panel finds hardest to hold steady — panel mean 0.59, against 0.67–0.70 for the other four non-factual axes, which sit close enough together that only distinctness separates cleanly from them. Among the older OpenAI models, gpt-4o and gpt-4o-mini collapse *uniformly* (no stable signal on any axis); gpt-4.1-2025-04-14 and gemini-2.5-flash collapse *on factual specifically*, though Flash also wobbles on distinctness (0.50); the four Claude models and gemini-3.1-pro show no axis-specific collapse, holding every axis at 0.69 or above (the floor being Opus-4.0 on distinctness). Because the factual axis is already Criterion A's responsibility, council eligibility under Criterion B is assessed on the five **non-factual** axes.

**Criterion reliability (anchored).** Anchor-shift consistency applies the familiar LLM-judge reliability principle — a competent judge is invariant under non-semantic perturbation — to a controlled perturbation of the calibration value itself, and turns that invariance into a key-free, per-criterion reliability gate (its place among prior reliability and anchor-selection work is §5.5). We read an evaluator's consistency on a criterion as its **criterion reliability** there — the hypothesis being that holding the same standard whatever the anchor is what a competent, reusable standard looks like, while a ranking that dissolves under the shift reflects none. Rescaled to the anchor ($E^{C}_a = 7\,\rho_a/\rho_{a,\text{anchor}}$, so Opus-4.5 reads 7), the consistency becomes a competence on the $1$–$10$ scale, directly comparable with a generator's quality on the same criterion. The hypothesis is testable on the one axis that also carries an *independent* competence measure — factual, where Criterion A's key-free error-detection loading $E^{F}$ exists: factual consistency $E^{C}_f$ and $E^{F}$ correlate at Pearson $r = 0.52$ (Spearman $\rho = 0.72$), a decent agreement that supports reading consistency as competence. The looseness is the consistency-vs-accuracy gap — a model can rate factuality consistently yet uninformatively (gpt-4.1-mini, consistency $0.87$ against competence $\approx 0.09$). [The table](#tab-per-criterion) pairs, per non-factual criterion, the **generator** competence $G$ (the council's leave-self-out generation quality) with the **evaluator** competence $E$ (anchored consistency), all anchored to Opus-4.5 = 7, and gives their **anchored cosine** alignment — the cosine of each model's deviation from the anchor $(7,7)$, defined in Appendix A.6 (eq A15):

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

*The five non-factual axes are **beauty**, **intel** (intelligence), **dist** (instantiation distinctness), **len** (impressive length) and **struct** (structural diversity). Per criterion: $E$ = evaluator criterion reliability (the leave-self-out anchor-shift consistency of [the Criterion B table](#tab-criterion-b), rescaled to the 1–10 scale), and $G$ = generator quality — the council's leave-self-out mean of its scores of that generator on that axis, **each council member's vote weighted by its own reliability $E$ on that axis** (eq A12b; the same weighting §4.5 applies to $G^{C}$), so $E$ both scores the judge and sets its weight in $G$. Both are anchored so claude-opus-4.5 (★) reads 7. $\cos(G,E)$ = cosine of each model's deviation from the anchor point $(7,7)$ across the panel, with 95% CI from the joint (submission, archetype) bootstrap of A.5; 1 = making and judging perfectly aligned on that axis. $G$, $E$ and the cosine are all formed from unrounded quantities and rounded once, here. Higher $G$ = better maker; higher $E$ = more stable judge.*

On all five non-factual criteria, making and judging move together (anchored cosine $0.84$–$0.91$): a model that generates well on a criterion also tends to hold a stable standard when judging it. Judging and making are largely one capability on the aesthetic and structural axes.

**Constituting the initial council.** The panel certifies its own reliable subset from internal evidence alone — a bootstrap in the epistemic sense: no production score, no external key. We keep the selection **fully key-free**: a reliable evaluator must show factual competence (Criterion A) — a key-free SVD loading clear of the inert band — *and* criterion reliability on the non-factual axes (collapsed anchor-shift consistency $\bar\rho \ge 0.78$, Pearson). Five evaluators clear both bars: Gemini 3.1 Pro, Claude Opus 4.5, Gemini 2.5 Flash, Claude Opus 4.0 and Claude Opus 4.1, whose factual-competence loadings (0.28–0.58) separate from the inert band and whose criterion reliability clears the floor. Claude Sonnet-4 is the marginal case the other way: its loading (0.13) lies inside the inert band, its 95% interval touching gpt-4.1-mini's below, so it does not clear Criterion A — even though it clears Criterion B comfortably (0.84). Gemini 2.5 Flash is the weakest seat: its loading (0.37) clears the band, but its criterion reliability ($\bar\rho = 0.81$) is the lowest of the five, the closest to the floor — a caveat we carry in the open. The initial council is seated on evaluator competence alone — generation cannot help form it, since it is rated *by* a council — whereas a later council-chair candidate, judged by a council already in place, is assessed on the full Total rating $T = \tfrac12(G+E)$ (§3.5). [The five members](#tab-initial-council):

<a id="tab-initial-council"></a>

| Council member | Factual competence [95% CI] | Criterion reliability [95% CI] |
|---|---:|---:|
| gemini-3.1-pro | 0.58 [0.56, 0.60] | 0.94 [0.92, 0.96] |
| claude-opus-4.5 | 0.55 [0.54, 0.58] | 0.93 [0.89, 0.96] |
| gemini-2.5-flash | 0.37 [0.31, 0.40] | 0.81 [0.75, 0.86] |
| claude-opus-4.0 | 0.35 [0.32, 0.35] | 0.85 [0.80, 0.89] |
| claude-opus-4.1 | 0.28 [0.27, 0.30] | 0.87 [0.82, 0.91] |

Table: The initial council — the five reliable evaluators.

*The five evaluators that clear both reliability bars: factual competence (Criterion A, SVD loading clear of the inert band) and criterion reliability (Criterion B, leave-self-out collapsed anchor-shift consistency $\bar\rho \ge 0.78$ on the four per-archetype non-factual axes). Values are the key-free competence scores with 95% bootstrap CIs over the (submission, archetype) grid. These five form the council that issues the official ratings (§4.5, §4.6); the other seven evaluators are unused.*

The council size — five — follows from the key-free bars above; it is large enough that the 1/√N reduction in CI half-width is not the limiting factor on resolution. The seven excluded evaluators are not used in the official rating.

gpt-4.1-mini is the clean demonstration that the two criteria are independent. It scores respectably as a generator and is stable across every axis (Criterion B, 0.75–0.87), so on several fact-adjacent numbers it looks strong; yet the factual-competence measure (Criterion A) places it in the inert band (≈ 0.09). A precise rater need not be an informative one: the spectral estimator separates a self-consistent instrument from one whose judgements track the panel's shared factual signal, which is exactly why both criteria are required (the consistency-vs-competence gap is quantified above).

### 4.5 The making components

The same five council evaluators that judge reliability also score production. Re-aggregating their anchored generation scores gives each generator its two **making** components: factual competence $G^{F}$ (the SVD generation factuality of §4.3) and criterion quality $G^{C}$ — the council's leave-self-out mean of the five non-factual axes (beauty, intelligence, distinctness, impressive-length, structural-diversity), with each evaluator's vote on each axis **weighted by its per-axis reliability** (§4.3): a judge that rates an axis no more consistently than chance carries little weight there, one with a firm standard carries full weight. Non-council models receive both components from the same council against the same anchor; council members additionally carry the evaluator ratings of §4.3, kept separate. Generation and evaluation do not coincide — Gemini 3.1 Pro is the panel's strongest factual judge yet a middling generator, and Sonnet-4 generates near the top yet does not clear the evaluator bar — which is exactly why the total keeps the two halves distinct (§4.6).

This is the public starting point. Any subsequent model — open-weight, future-generation, or otherwise — can be evaluated against the same anchor (claude-opus-4.5's published portfolio, fixed at 7) by the same council and placed on the same leaderboard; models that also evaluate can have their evaluator rating checked against the same reliability criteria. The benchmark scales by addition, not by re-derivation.

### 4.6 Total rating, leaderboard and final appointment of the first council

The benchmark's two ratings combine into one official total, and each splits the same way — into a **factual** and a **criterion** half. On the making side: the generator's factual competence $G^{F}$ (the SVD generation factuality of §4.3) and its criterion quality $G^{C}$ (the council's reliability-weighted mean of the five non-factual generation axes, §4.5). On the judging side: $E^{F} = 7\,f/f_a$ and $E^{C} = 7\,\bar\rho/\bar\rho_a$ (§4.3, §4.4), the SVD factual competence and the leave-self-out collapsed anchor-shift consistency, both placed on the rubric by the convention already used for generation, **the anchor model scores 7**. Each side is the mean of its two halves, $G = \tfrac12(G^{F}+G^{C})$ and $E = \tfrac12(E^{F}+E^{C})$, and the two sides weigh equally — so the total is the mean of four anchored components, a symmetric $2\times2$ of {maker, judge} $\times$ {factual, criterion} (Appendix A.4):

$$T \;=\; \tfrac{1}{2}\big( G + E \big) \;=\; \tfrac{1}{4}\big( G^{F} + G^{C} + E^{F} + E^{C} \big). \tag{2}$$

Each model's score splits into a **judging** half — its evaluator score $E=\tfrac12(E^{F}+E^{C})$ — and a **making** half — its generator score $G=\tfrac12(G^{F}+G^{C})$ — and the total is their mean, $T=\tfrac12(E+G)$. The **[final leaderboard](#tab-final-leaderboard)** ranks all twelve models by $T$. Every rating is issued by the council against the fixed anchor (claude-opus-4.5, pinned at 7), so the anchor reads 7 on $T$, $E$ and $G$ alike.

<a id="tab-final-leaderboard"></a>

| Rank | Model | Council | **$T$ [95% CI]** | $E$ | $G$ |
|---|---|:--:|---:|---:|---:|
| 1 | ★ claude-opus-4.5 (anchor) | council | **7.00 [7.00, 7.00]** | 7.00 | 7.00 |
| 2 | gemini-3.1-pro | council | **6.69 [6.56, 6.87]** | 7.22 | 6.16 |
| 3 | claude-opus-4.0 | council | **6.21 [5.93, 6.61]** | 5.44 | 6.98 |
| 4 | claude-opus-4.1 | council | **6.05 [5.73, 6.52]** | 5.04 | 7.07 |
| 5 | gemini-2.5-flash | council | **5.76 [5.17, 6.21]** | 5.37 | 6.15 |
| ⎯⎯ | ⎯⎯ | ⎯⎯ | ⎯⎯ | ⎯⎯ | ⎯⎯ |
| 6 | claude-sonnet-4 | — | **5.30 [5.04, 5.56]** | 3.96 | 6.65 |
| 7 | gpt-4.1-mini | — | **4.74 [4.09, 5.45]** | 3.86 | 5.62 |
| 8 | gpt-4.1-2025-04-14 | — | **4.44 [4.21, 4.63]** | 3.10 | 5.78 |
| 9 | gpt-4o-2024-08-06 | — | **3.48 [3.23, 3.75]** | 2.65 | 4.32 |
| 10 | gpt-4.1-nano | — | **3.22 [2.52, 3.62]** | 2.79 | 3.65 |
| 11 | gpt-4o | — | **2.93 [2.61, 3.20]** | 1.58 | 4.28 |
| 12 | gpt-4o-mini | — | **2.24 [2.04, 2.44]** | 1.17 | 3.31 |

Table: Final leaderboard — total rating $T$ (95% CI) with its evaluator half $E$ and generator half $G$, all twelve models ranked; council seats marked. The anchor (claude-opus-4.5) is 7 by construction.

Each half resolves into [two anchored competences](#tab-competence-breakdown) — making: generator factual $G^{F}$ (§4.3 Criterion A) and criterion $G^{C}$ (the five non-factual generation axes, §4.5); judging: evaluator factual $E^{F}$ (§4.3 Criterion A) and criterion $E^{C}=7\bar\rho/\bar\rho_a$ (the leave-self-out collapsed anchor-shift consistency, §4.4 Criterion B):

<a id="tab-competence-breakdown"></a>

| Rank | Model | Council? | $G^{F}$ | $G^{C}$ | $E^{F}$ | $E^{C}$ |
|---|---|:--:|---:|---:|---:|---:|
| 1 | ★ claude-opus-4.5 (anchor) | council | 7.00 | 7.00 | 7.00 | 7.00 |
| 2 | gemini-3.1-pro | council | 6.58 | 5.75 | 7.36 | 7.07 |
| 3 | claude-opus-4.0 | council | 6.98 | 6.98 | 4.47 | 6.42 |
| 4 | claude-opus-4.1 | council | 6.97 | 7.16 | 3.55 | 6.52 |
| 5 | gemini-2.5-flash | council | 6.57 | 5.72 | 4.68 | 6.07 |
| ⎯⎯ | ⎯⎯ | ⎯⎯ | ⎯⎯ | ⎯⎯ | ⎯⎯ |
| 6 | claude-sonnet-4 | — | 6.98 | 6.31 | 1.62 | 6.30 |
| 7 | gpt-4.1-mini | — | 6.18 | 5.06 | 1.21 | 6.50 |
| 8 | gpt-4.1-2025-04-14 | — | 6.50 | 5.05 | 0.20 | 6.00 |
| 9 | gpt-4o-2024-08-06 | — | 5.22 | 3.43 | 0.62 | 4.67 |
| 10 | gpt-4.1-nano | — | 3.66 | 3.63 | 0.49 | 5.09 |
| 11 | gpt-4o | — | 5.11 | 3.44 | 0.34 | 2.82 |
| 12 | gpt-4o-mini | — | 3.20 | 3.43 | 0.00 | 2.35 |

Table: Competence breakdown — the four anchored components behind each model's evaluator ($E$) and generator ($G$) scores.

*($G^{F}$, $E^{F}$ are the §4.3 soft-SVD factual competences (anchored $7f/f_a$ and the per-generator consensus); $G^{C}$ is the council reliability-weighted leave-self-out mean of the five non-factual generation axes; $E^{C}=7\bar\rho/\bar\rho_a$ the leave-self-out collapsed anchor-shift consistency (§4.4). Values are anchored point estimates (claude-opus-4.5 = 7); every quantity is carried unrounded to the last step, so $E=\tfrac12(E^{F}+E^{C})$, $G=\tfrac12(G^{F}+G^{C})$ and $T=\tfrac14(G^{F}+G^{C}+E^{F}+E^{C})$ are computed from unrounded leaves and a displayed total can differ from its rounded inputs by 0.01. The $T$ interval is the 95% joint (submission, archetype) bootstrap of A.5 — a CI device only, it does not change the point estimates; an independent end-to-end re-derivation reproduces the competent-model components, while inert-band factual loadings — which §4.3 notes are not robustly distinguishable from zero — are construction-sensitive.)*

Three readings. **The top five are the council.** The five reliable evaluators occupy the top five totals; the anchor leads by construction (all four of its components pinned at 7), and Gemini 3.1 Pro is second on the strength of its factual judging despite a mid-pack generation rating. **The cliff is in the judging, not the making.** The models that carry little factual competence (low $E^{F}$: the GPT-4o family, gpt-4.1-2025-04-14, and gpt-4.1-nano) sink regardless of how well they generate; a quarter of the total is error detection, and it is what production cannot buy — §5.4's independence thesis made quantitative. **Generation and evaluation do not coincide.** The strongest generators — the three Opus models — are only middling factual judges ($E^{F}$ of 3.5–4.5 on the anchored scale), while the strongest judge, Gemini 3.1 Pro ($E^{F}=7.36$), generates in the middle of the pack, and Sonnet-4 generates near the top yet fails the evaluator bar entirely. A model can top one half of the benchmark and not the other — which is precisely what makes a two-part total worth reporting rather than a single conflated score.

**The sitting council is appointed like every future one.** The five members were seated on evaluator competence alone (§4.3), because no council yet existed to rate production. Apply instead the standing rule a future council-chair candidate will face — appointment by Total rating — and the top five by $T$ are exactly those five. The initial council, selected the hard way on key-free evaluator competence, and the council the Total-rating rule would appoint coincide exactly: the sitting council rests on the same basis as every council after it. The benchmark is consistent in whom it trusts.

### 4.7 The metanym benchmark vs GPQA

We test the key-free factual ratings against an instrument built outside the run: GPQA Diamond (Rein et al. 2023; 198 expert multiple-choice questions with a human answer key), put to the same twelve models, through the same gateway, under the same protocol — Temperature=0, reasoning and tools off — and scored against the key. We correlate GPQA accuracy with three council quantities: evaluator factual competence $E^{F}$, generator factuality $G^{F}$ (both from [the Criterion A table](#tab-criterion-a) of [§4.3](#43-evaluator-factual-competence)), and their mean $\tfrac{1}{2}(E^{F}+G^{F})$ — the factual half of the total rating $T$ (§4.6). [The scatter](#fig-gpqa-scatter) plots the combined rating against GPQA; [the correlation table](#tab-gpqa-correlations) reports all three.

<a id="fig-gpqa-scatter"></a>

![Combined factual rating $\tfrac{1}{2}(E^{F}+G^{F})$ (key-free, anchored 1–10) against self-administered GPQA Diamond accuracy, across the twelve models. Plotted from [the Criterion A table](#tab-criterion-a) of [§4.3](#43-evaluator-factual-competence) and the self-administered GPQA accuracies. Pearson $r = 0.92$ (95% CI $[0.85, 0.97]$), Spearman $\rho = 0.91$, $n = 12$. Filled markers are council seats, open markers non-council; horizontal bars are the combined 95% CI (the mean of the $E^{F}$ and $G^{F}$ intervals), vertical bars the GPQA binomial 95% CI. The blue star is the anchor (opus-4.5): its combined rating is 7 by calibration ($E^{F}=7$ the top SVD loading, $G^{F}=7$ the reference), with GPQA measured independently — so it is a legitimate point and is included; its $x$ is exact, hence no horizontal bar. Excluding it leaves Pearson at 0.92.](../submission/figures/average_validation.png)

<a id="tab-gpqa-correlations"></a>

| Correlation | $n$ | Pearson | Spearman |
|---|--:|--:|--:|
| $\tfrac{1}{2}(E^{F}+G^{F})$ vs GPQA | 12 | 0.92 | 0.91 |
| $E^{F}$ vs GPQA | 12 | 0.84 | 0.89 |
| $G^{F}$ vs GPQA | 11 | 0.82 | 0.82 |
| $E^{F}$ vs $G^{F}$ | 11 | 0.59 | 0.75 |

Table: Council factual ratings vs self-administered GPQA Diamond accuracy. The anchor (opus-4.5) is included where its value against GPQA is defined — the combined rating and $E^{F}$ (both 7 by calibration; $E^{F}$ is the real top SVD loading) — and omitted from $G^{F}$ (ungraded as a generator) and from $E^{F}$ vs $G^{F}$ (where it is a definitional identity point). $E^{F}$ is anchored; Pearson and Spearman are scale-invariant.

Three conclusions follow.

**The metanym factual rating is relevant.** It tracks GPQA closely (combined $r = 0.92$), so it measures real factual capability. The two are independent instruments; their close agreement is mutual corroboration, not validation by an oracle — GPQA is no golden key, is not assumed more accurate than the metanym rating, and the concordance simply makes it improbable that either sits far from the truth (§5.6).

**The metanym benchmark measures both the ability to say something true and the ability to find errors.** Making a true claim and spotting a false one are different skills (West et al. 2024; Oh et al. 2024; Li et al. 2024). Our benchmark confirms this. The GPQA-benchmark correlates excellently with the average value of both abilities ($r = 0.9$). It correlates somewhat weaker with each one of them ($r = 0.8$). The weakest correlation is between the two ($r = 0.6$). What the metanym benchmark adds to the existing methods for detecting the difference between them is getting the generating and evaluating abilities for all models in a single shot. Letting the LLMs evaluate and rate each other's statements turns it into an eigenvalue equation that we solve with SVD, finding the point where the weights of the evaluators are consistent with the evaluations.

We note that the Gemini models rank higher as judges than as makers, the Claude models the reverse (sharp for gemini-3.1-pro and sonnet-4; the rest within the error bars). This breaks the assumption behind key-free peer rankers like PiCO (Ning et al. 2025) and UPME (Zhang et al. 2025), which treat a strong maker as a strong judge. The total rating keeps the two apart (§4.6).

### 4.8 Robustness to regeneration

The leaderboard of §4.6 rests on one portfolio per model. To check that the result is not an artefact of that single draw, we re-ran the full pipeline three times — the bootstrap run and two further runs produced the same day, two hours apart — each regenerating all twelve portfolios at T=0 and re-scoring them against the frozen anchor. The regeneration is substantive: at T=0 the gateway is not deterministic, eleven of twelve portfolios differ between runs, and a total can move by as much as 0.8 between the two same-day runs (gemini-3.1-pro, 7.17→7.99).

The benchmark's categorical and ordinal outputs are robust to this. The council is **identical** across all three runs (the same five seats), and [the total-rating ranking is preserved](#tab-reruns) — pairwise Pearson 0.94–0.97 and Spearman 0.93–0.95 (0.94 / 0.94 between the two same-day runs alone).

<a id="tab-reruns"></a>

| Model | $T_1$ | $T_2$ | $T_3$ | SD |
|---|--:|--:|--:|--:|
| ★ claude-opus-4.5 | 7.00 | 7.00 | 7.00 | 0.00 |
| ★ gemini-3.1-pro | 6.69 | 7.17 | 7.99 | 0.66 |
| ★ claude-opus-4.0 | 6.21 | 5.73 | 6.56 | 0.42 |
| ★ claude-opus-4.1 | 6.05 | 6.79 | 6.57 | 0.38 |
| ★ gemini-2.5-flash | 5.76 | 5.45 | 4.67 | 0.56 |
| claude-sonnet-4 | 5.30 | 5.47 | 6.11 | 0.43 |
| gpt-4.1-mini | 4.74 | 5.52 | 4.91 | 0.41 |
| gpt-4.1-2025-04-14 | 4.44 | 4.66 | 5.26 | 0.42 |
| gpt-4o-2024-08-06 | 3.48 | 3.02 | 3.70 | 0.35 |
| gpt-4.1-nano | 3.22 | 3.33 | 2.45 | 0.48 |
| gpt-4o | 2.93 | 2.90 | 3.48 | 0.33 |
| gpt-4o-mini | 2.24 | 2.33 | 2.15 | 0.09 |

Table: Total rating $T$ across three full re-runs (run 1 = bootstrap; runs 2–3 the same day, two hours apart). ★ marks a council seat — the five seats are identical across all three runs. SD is the per-model run-to-run standard deviation (mean 0.38, max 0.66, both Gemini seats highest).

The cardinal totals carry wider uncertainty than the within-run bootstrap of §4.6 conveys: the per-model run-to-run SD of $T$ is 0.38 on average (max 0.66), and several totals move beyond their within-run interval between runs. The bootstrap measures dispersion across the 275 contexts of *one* generation, not the generation being itself a random draw; the honest interval on a total is therefore the wider resample band, and the benchmark's reliable products are council membership and rank order rather than the precise total.

External validity holds on both counts: the key-free factual rating tracks GPQA Diamond at Pearson 0.86–0.92 and Spearman 0.90–0.92 across the three runs — all inside the reported interval $[0.85, 0.97]$ (§4.7). Unlike the cardinal totals, the GPQA correlation's published CI already covers its run-to-run variation.


## 5. Discussion

### 5.1 A benchmark by LLMs, for LLMs

The aim is a benchmark that needs nothing outside itself: models invent the test, sit it, grade it, and certify which of them are fit to grade — no human raters, no gold key, and no oracle model whose word is taken as truth. LLM-as-judge already removes the human rater (Zheng et al. 2023; Liu et al. 2023; Verga et al. 2024; Bai et al. 2023) but still requires an external ground truth — a gold key or reference answer — to score against. The metanym benchmark removes that dependency too — but key-free grading is not the novelty; the unsupervised peer-evaluation line (PiCO, UPME) already gets there (§5.5). What is new is self-containment: the panel authors the very items it judges, so the test refers only to itself, and one decomposition scores the models as both makers and judges (§5.5). The benchmark is in this sense fully self-contained.

The metanym benchmark correlates excellently with GPQA. The latter is no golden key, and does not come across as more accurate than the metanym benchmark. Both occasionally reverse the expected internal ranking order within families of LLMs, such as placing a newer version of a model below its predecessor. While most of these instances are within the error margins, two examples fall outside: GPQA ranks Claude-sonnet-4 *above* Claude-Opus-4.0 while the metanym benchmark places opus comfortably above sonnet. Both benchmarks rank gpt-4.1-mini *above* gpt-4.1. 

Both benchmarks will increase resolution following the same principle, but only the metanym benchmark does it easily. For GPQA it means engaging domain experts to increase the number of Google-proof multiple-choice questions, re-validating the test and publishing a new version of the benchmark. For the metanym benchmark the resolution is increased by twisting a knob, raising the number of archetypal contexts in a submission (here set to five).

### 5.2 Two self-consistencies, two yardsticks

With no outside ruler to appeal to, the yardsticks must come from the system's own structure. They come in two forms — one for objective criteria, one for subjective — which is why the method uses two estimators, not one.

The factual estimator rests on one assumption: *the only thing competent evaluators share is the truth*. When that holds, agreement concentrates on truth, and the leading eigenvector of the leniency-removed agreement matrix is the competence axis. The warrant holds for facts and fails for taste: on **beauty**, the dominant axis of agreement is no longer truth but shared convention — house style, training data — so weighting by it would *launder conformity into competence*, rewarding the evaluator nearest the mean and penalising a legitimate minority view. The subjective criteria therefore use the other route, **anchor-shift consistency**: the calibration reference is swept, and a competent evaluator preserves its ranking as it moves, without needing to agree with any peer. The test has teeth precisely because the shift is non-semantic: if merely moving the calibration point reorders how a model rates the same items, it has no firm grip on what it is judging — and a stable standard is the whole of what competence means on a criterion with no external truth. One route is a consensus eigenmode across evaluators, the other an invariance within each; both are self-consistency conditions set by the system's own structure rather than an absolute scale.

### 5.3 A sustainable yardstick

The benchmark yardstick is calibrated on the *anchor submission* (here the submission by Claude-opus-4.5) and the official benchmark ratings are set by the council. With model temperature T=0, no thinking or tools, the council members' evaluations are deterministic and reproducible, meaning anyone with access to the models can confirm a benchmark rating. 

What varies over time is the anchor submission and the members of the council. By accounting for the changes of both over time, older benchmark ratings can be converted to approximate a rating by a newer standard; to keep that chain from drifting, each conversion is recalibrated against the archived original anchors rather than only the latest inherited factor, so error does not accumulate. An updated official rating is done by the sitting council.

This also allows changing the council size. In this paper we seat five, mainly because only five clear the factual-competence bar — the natural sixth, Sonnet-4, is a good generator yet its factual competence as an evaluator sits in the inert band (~1.6), so it is not trusted to judge. The council is initially supply-limited by competence but can grow as the field improves.

### 5.4 Generating vs evaluating the truth
 
Making and judging factual truth are different abilities, and the council measures both and keeps them apart (§4.3). A benchmark that scored only generation would miss judging competence — the very thing the council gate selects on — so it is the separation, not just the rating, that lets the panel pick judges rather than only rank makers.

### 5.5 Where this sits: intelligence tests and peer-evaluation methods

Two axes locate the metanym game — *what intelligence it tests* and *how self-contained the apparatus is* — and prior work tends to be strong on one while weak on the other: the analogy benchmarks hit the target but need an external key, and the unsupervised peer-evaluation methods are key-free but aim at general capability rather than a defined, falsifiable operation.

**As an intelligence test**, the game probes the same abstraction-and-analogy cluster a long tradition places at the centre of thinking (Gentner 1983; Hofstadter & Sander 2013; Penn, Holyoak & Povinelli 2008; Chollet 2019; Mitchell 2021), and it probes it harder. Where the classical instruments — BIG-Bench analogy items, Webb, Holyoak & Lu (2023), Lewis & Mitchell (2024), and the visual ARC-AGI (Chollet 2019) — test one mapping over one domain pair per item, in a *recognition* frame, the metanym game asks for many coupled slots across several unrelated domains, built from scratch and falsifiable per sentence (§2.c). This makes it a new *kind* of analogy test, not merely a harder instance: recognition instruments *select* a mapping, and the analogy-generation literature *produces* one but grades it holistically, whereas the metanym game is the first to make analogical *production* falsifiable sentence by sentence. That property does double duty — it is also what lets the test be scored without a key, which is the second difference: **none of the prior instruments is self-contained.** Every one scores against an external truth — gold labels (BIG-Bench, ARC-AGI) or paid human raters (Webb-Holyoak-Lu) — so none can run, let alone improve, without an external oracle. They measure a similar intelligence; they cannot certify it themselves.

**As a self-contained method**, the council sits in the *unsupervised peer-evaluation* line — and that line already removes the gold key, so removing it is not what we add. Single-judge protocols (MT-Bench; G-Eval, Liu et al. 2023) score against a reference; PoLL (Verga et al. 2024) adds a panel but trusts it as given; LLM-as-Examiner (Bai et al. 2023) lets the examiner write the questions; and most directly, PiCO (Ning et al. 2025) lets unlabelled models answer and grade one another and recovers an ability ordering from peer agreement alone, with no human labels and no key (UPME, Zhang et al. 2025, extends the same peer-review idea to multimodal vision-language evaluation). What we add is two things those methods lack. *First*, they apply one consensus mechanism to every dimension, which on subjective criteria rewards the model nearest the mean — the mainstreaming §5.2 refuses; we weight by agreement only where agreement is licensed to mean truth (factual), and use anchor-shift consistency elsewhere. *Second*, they grade pre-existing unlabelled questions, where ours is a purpose-built, per-sentence-falsifiable production task. The council also certifies and re-contests its own judges (§3.5) rather than trusting the panel as given. The estimator differs too, and this is the sharper break: PiCO fits one ability parameter per model by consistency optimization — it is not a spectral method. Spectral aggregation has its own label-free lineage — Parisi et al. (2014) read predictor competence off the leading eigenvector of their covariance, Dawid & Skene (1979) the EM antecedent — but that lineage is *one-sided*: its predictors classify a fixed *external* dataset, so the decomposition scores the raters (rows) and recovers the hidden labels (columns), with no maker to score because no agent produced the items. Our columns are authored by the same agents on the rows, so the matrix is *two-sided*: one graded SVD (§4.3) reads competence off both axes — judges from the left singular vector, makers from the right — and the making–judging gap (§4.7) is definable only because the test is self-produced. That two-sidedness is where self-containment lives: nothing in the matrix comes from outside it. (Parisi is binary besides; we use the graded $1$–$10$ ratings, not binarised verdicts.) To our knowledge the spectral route has not been applied to LLM peer evaluation, where the unsupervised line uses EM- and optimization-based aggregation instead.

Two of our components have their own recent literature, and we use them rather than claim them. *Anchor-shift consistency* applies the standard judge-reliability principle — a competent judge is invariant under non-semantic perturbation — to a sweep of the calibration value. Invariance-under-perturbation has been used to gate judges on criteria that have a latent truth (safety: Policy Invariance, Weng et al. 2026) or as a general diagnostic (JudgeSense, Bellibatlu et al. 2026; PiCO, Ning et al. 2025). We use calibration-invariance to certify evaluator competence on subjective, ground-truth-free criteria — beauty, structural diversity — where neither a gold key nor consensus-as-truth is available, and a stable standard is the only competence there is to measure; we read it as a key-free, per-criterion gate orthogonal to the spectral estimator. To our knowledge that use is new. And anchor *choice* is studied directly by Don-Yehiya et al. (2026), who find that extreme anchors discriminate poorly and that the anchor should track the capability of the cluster under comparison and rise as the field improves — which is our recalibration rule (§5.3). Their pairwise caution about a top anchor does not bite our setup: the bootstrap winner is pinned at 7 with headroom above it and scored cardinally, and anchoring nearly *doubled* the resolution F-statistic (§4.2) rather than compressing it.

The two axes meet in one sentence. Prior work offers either a test of this intelligence that needs an external key, or a key-free evaluation method aimed at general capability rather than a defined cognitive operation. The metanym game is the only one that is both — a structural-intelligence test that certifies its own ground.

### 5.6 Self-containment as a bootstrap

Self-consistency builds the yardsticks; self-containment lets the apparatus improve itself. With no external dependency, the council can govern not just the scores but the *rules* — rubric, anchor, protocol, estimators. The gain is exponential rather than linear for a first-order reason: a more capable panel improves the rules more, so the increment to competence scales with the competence already present ($\dot C \propto C$). This is Engelbart's bootstrapping — recursion applied to the means of improvement, not just the output — and as models improve, the most capable panel is the one best placed to decide what to improve next.

Four of the five autonomy properties are demonstrated: the models generate the items, truth is recovered key-free, the loop runs deterministically with no human intervention, and the panel certifies its own judges. The fifth, self-improvement, is specified but not yet exercised — the canonical run is council version 0 and includes no promotion round (§3.5). Closing that gap — running a contest end to end, testing an anchor recalibration, and eventually allowing the council to revise a rule while the factual axis remains answerable to independent re-validation — is what would turn a self-contained loop into a self-sustaining one.

### 5.7 Scope

Three caveats bound the present run. It characterises a single configuration — one prompt template, one twelve-model roster, one anchor value — so the bootstrap intervals measure dispersion across items, not the generation being itself a random draw — a three-fold regeneration (§4.8) shows the council and ranking survive resampling while cardinal totals carry a wider run-to-run band — and the anchor sweep closes the calibration axis (four values giving the same leaderboard, pairwise Spearman 0.90–0.96). Within the leading group the panel sits at its discrimination floor: the two Gemini seats are a statistical tie on the generation rating (§4.5), and fine within-group ranking is evaluator-generation-bound — it sharpens as the seats improve and as the number of archetypal contexts is raised (§3.5). And the self-improvement loop is specified but unrun (§5.6). The deterministic, single-pass protocol (T=0, no reasoning, no tools) is a choice for reproducibility, not a sampling limit: anyone with the models reproduces the ratings exactly.

---

## 6. Summary

The *metanym game* is a structural test of intelligence. A player discerns an *archetypal context* — an abstract system structure that recurs across unrelated domains — writes it as a literal *context template*, and instantiates the template across domain after domain by substituting *metanyms*, metaphorically synonymous keywords, leaving the surrounding prose fixed; each instantiation is a *parallel context*, a metaphor of the others, and because only the keywords change, the analogy is falsifiable sentence by sentence. It exercises the cluster of cognitive constructs a long tradition places at the centre of thinking (§2.c), and it is a *production* task — the player builds the structure, not merely recognises one. This makes it a new kind of analogy test: to our knowledge the first to make analogical *production* falsifiable sentence by sentence (§5.5).

The *council-of-peers benchmark* turns the game into a benchmark that needs nothing outside itself: twelve frontier LLMs generate portfolios and blindly cross-evaluate them, with no human raters and no gold key. Its yardsticks come from the panel's own structure rather than an external standard, through two self-consistency conditions chosen by whether the criterion is objective. For *facts*, truth is recovered as the dominant axis of inter-evaluator agreement: a single SVD of the rating matrix yields both evaluator competence and item-falseness at once. For the *subjective* criteria, where weighting by agreement would only launder consensus into competence, reliability is instead read from anchor-shift consistency — an evaluator's invariance as the calibration value is swept. The panel certifies its own reliable subset, the council, on these two axes, and the seats are contestable: a stronger model can earn one on the benchmark's own rating. One external step remains, by design: a one-time validation that the key-free factual rating agrees with an independent benchmark (GPQA Diamond, $r = 0.92$). It is a check on the method, not a standing key in the loop.

What sets the council apart from other key-free peer-evaluation methods (§5.5) is *how* the panel grades itself: it recovers competence spectrally, from a single graded SVD, where those methods optimize a per-model consistency objective; it weights by agreement only where agreement is licensed to mean truth and reads reliability from anchor-shift consistency elsewhere; it validates the factual axis once against independent tests, so its self-consistency is checked against the world and not only against itself; and it scores a defined, per-sentence-falsifiable operation rather than general capability. The empirical payoff is a dissociation the benchmark is built to see because it rates making and judging separately: **judgment is the bottleneck.** Most models cannot reliably tell a true cross-domain claim from a false one even when they generate competent structure — the strongest generators are middling judges, the sharpest judge a mid-pack generator — so a benchmark that conflated the two would obscure this result. (The leaderboard's one clear division tracks provider lineage rather than parameter count, but finer ordering sits below resolution and this is the least load-bearing part of the result.)

To our knowledge this is the first structural-intelligence test that certifies its own ground — key-free, self-contained, and externally corroborated rather than externally judged — and the first to read maker and judge competence from a single spectral decomposition of a self-produced test.

The run characterises one operating point — Temperature 0, no reasoning, no tools — and the self-improvement mechanism is specified but not yet exercised, so the loop is self-contained but not yet self-sustaining. The natural next steps are an open-weight panel, to separate provider-family from parameter-scale effects; a promotion round, to make the contestable council real; and a companion mechanistic study testing whether each archetypal context occupies a low-dimensional subspace of model hidden states — which, if it holds, would give the subjective criteria the objective ground that today only factual has.

---

## Data and code availability

Everything needed to check this paper is in one repository, [`github.com/dnordfors/metanym-game-paper`](https://github.com/dnordfors/metanym-game-paper): the manuscript, the arXiv submission source, the pinned evaluation runs, and the twelve analysis scripts that regenerate every number, table and figure. Running `bash reproduce.sh` is deterministic re-analysis of fixed model outputs — it makes no API calls, needs no credentials, and completes in under a minute, with each step labelled by the paper exhibit it produces. Because the benchmark uses no answer key, no gold standard and no oracle model, nothing external is required to verify the ratings.

Producing a *new* run — re-querying the models for a fresh $N$ — is deliberately not part of that package: it costs API budget and is non-deterministic by construction. The published results derive from the runs pinned under `reproduce/data/`, and §4.8 reports what moves across three independent regenerations.

## References

### Cognitive science, philosophy of science, systems theory

1. Hesse, M. (1963). *Models and Analogies in Science.* London: Sheed & Ward.
2. Minsky, M. (1975). A framework for representing knowledge. In P. H. Winston (Ed.), *The Psychology of Computer Vision* (pp. 211–277). McGraw-Hill.
3. Fillmore, C. J. (1982). Frame semantics. In Linguistic Society of Korea (Ed.), *Linguistics in the Morning Calm* (pp. 111–137). Hanshin.
4. Boyd, R. (1979). Metaphor and theory change: What is "metaphor" a metaphor for? In A. Ortony (Ed.), *Metaphor and Thought* (pp. 356–408). Cambridge University Press.
5. Gentner, D. (1983). Structure-mapping: A theoretical framework for analogy. *Cognitive Science, 7*(2), 155–170.
6. Gick, M. L., & Holyoak, K. J. (1983). Schema induction and analogical transfer. *Cognitive Psychology, 15*(1), 1–38.
7. Gentner, D. (1989). The mechanisms of analogical learning. In S. Vosniadou & A. Ortony (Eds.), *Similarity and Analogical Reasoning.* Cambridge University Press.
8. Falkenhainer, B., Forbus, K. D., & Gentner, D. (1989). The structure-mapping engine: Algorithm and examples. *Artificial Intelligence, 41*(1), 1–63.
9. Lakoff, G., & Johnson, M. (1980). *Metaphors We Live By.* University of Chicago Press.
10. Holyoak, K. J., & Thagard, P. (1995). *Mental Leaps: Analogy in Creative Thought.* MIT Press.
11. Goldberg, A. E. (1995). *Constructions: A Construction Grammar Approach to Argument Structure.* University of Chicago Press.
12. Penn, D. C., Holyoak, K. J., & Povinelli, D. J. (2008). Darwin's mistake: Explaining the discontinuity between human and nonhuman minds. *Behavioral and Brain Sciences, 31*(2), 109–130.
13. Hofstadter, D., & Sander, E. (2013). *Surfaces and Essences.* Basic Books.
14. von Bertalanffy, L. (1968). *General System Theory.* George Braziller.
15. Salthe, S. N. (1985). *Evolving Hierarchical Systems: Their Structure and Representation.* Columbia University Press.

### Archetypes and pattern-instantiation

16. Pauli, W. (1955). The influence of archetypal ideas on the scientific theories of Kepler (P. Silz, Trans.). In C. G. Jung & W. Pauli, *The Interpretation of Nature and the Psyche* (pp. 147–240). Pantheon Books. (Original work published 1952) *(Cited for the Jung–Pauli proposal that archetypes act as ordering principles across psyche and physical world; we adopt the structural framing, not the wider metaphysics.)*

### Psychometric intelligence taxonomies

17. Cattell, R. B. (1963). Theory of fluid and crystallized intelligence: A critical experiment. *Journal of Educational Psychology, 54*(1), 1–22.
18. Horn, J. L., & Cattell, R. B. (1966). Refinement and test of the theory of fluid and crystallized general intelligences. *Journal of Educational Psychology, 57*(5), 253–270.
19. Guilford, J. P. (1967). *The Nature of Human Intelligence.* McGraw-Hill.
20. Carroll, J. B. (1993). *Human Cognitive Abilities: A Survey of Factor-Analytic Studies.* Cambridge University Press.
21. McGrew, K. S. (2009). CHC theory and the human cognitive abilities project. *Intelligence, 37*(1), 1–10.

### LLM-as-judge methodology

22. Zheng, L., et al. (2023). Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena. *Advances in Neural Information Processing Systems (NeurIPS), 36.* arXiv:2306.05685.
23. Liu, Y., et al. (2023). G-Eval: NLG evaluation using GPT-4 with better human alignment. *Proceedings of EMNLP 2023.* arXiv:2303.16634.
24. Verga, P., et al. (2024). Replacing judges with juries: Evaluating LLM generations with a panel of diverse models. arXiv:2404.18796.
25. Bai, Y., et al. (2023). Benchmarking foundation models with Language-Model-as-an-Examiner. *NeurIPS 36.* arXiv:2306.04181.
26. Ning, K.-P., Yang, S., Liu, Y.-Y., Yao, J.-Y., Liu, Z.-H., Wang, Y., Pang, M., & Yuan, L. (2025). PiCO: Peer review in LLMs based on consistency optimization. *Proceedings of ICLR 2025.* arXiv:2402.01830.
27. Zhang, Q., Ning, M., Liu, Z., Huang, Y., Yang, S., Wang, Y., Ye, J., Chen, X., Song, Y., & Yuan, L. (2025). UPME: An unsupervised peer review framework for multimodal large language model evaluation. *Proceedings of CVPR 2025.* arXiv:2503.14941.
28. Don-Yehiya, S., Yehudai, A., Choshen, L., & Abend, O. (2026). Mediocrity is the key for LLM as a judge anchor selection. arXiv:2603.16848.
29. Weng, S., Feng, Y., & Xie, X. (2026). Beyond accuracy: Policy invariance as a reliability test for LLM safety judges. arXiv:2605.06161.
30. Bellibatlu, R. R., Raff, E., & Zhang, W. (2026). JudgeSense: A benchmark for prompt sensitivity in LLM-as-a-judge systems. arXiv:2604.23478.

### Analogical reasoning in LLMs

31. Webb, T., Holyoak, K. J., & Lu, H. (2023). Emergent analogical reasoning in large language models. *Nature Human Behaviour, 7*(9), 1526–1541.
32. Lewis, M., & Mitchell, M. (2024). Using counterfactual tasks to evaluate the generality of analogical reasoning in large language models. arXiv:2402.08955.

### Related benchmarks

33. Chollet, F. (2019). On the measure of intelligence. arXiv:1911.01547.
34. Mitchell, M. (2021). Abstraction and analogy-making in artificial intelligence. *Annals of the New York Academy of Sciences, 1505*(1), 79–101.
35. Lake, B. M., Ullman, T. D., Tenenbaum, J. B., & Gershman, S. J. (2017). Building machines that learn and think like people. *Behavioral and Brain Sciences, 40*, e253.
36. Srivastava, A., et al. (2022). Beyond the imitation game: Quantifying and extrapolating the capabilities of language models. arXiv:2206.04615.
37. Cobbe, K., et al. (2021). Training verifiers to solve math word problems. arXiv:2110.14168.
38. Rein, D., Hou, B. L., Stickland, A. C., Petty, J., Pang, R. Y., Dirani, J., Michael, J., & Bowman, S. R. (2023). GPQA: A graduate-level Google-proof Q&A benchmark. arXiv:2311.12022.

### Statistical methods

39. Efron, B., & Tibshirani, R. J. (1993). *An Introduction to the Bootstrap.* Chapman & Hall.
40. Parisi, F., Strino, F., Nadler, B., & Kluger, Y. (2014). Ranking and combining multiple predictors without labeled data. *Proceedings of the National Academy of Sciences, 111*(4), 1253-1258.
41. Dawid, A. P., & Skene, A. M. (1979). Maximum likelihood estimation of observer error-rates using the EM algorithm. *Journal of the Royal Statistical Society: Series C (Applied Statistics), 28*(1), 20-28.

### Generation vs evaluation

42. West, P., Lu, X., Dziri, N., Brahman, F., Li, L., Hwang, J. D., Jiang, L., Fisher, J., Ravichander, A., Chandu, K., Newman, B., Koh, P. W., Ettinger, A., & Choi, Y. (2024). The Generative AI Paradox: "What it can create, it may not understand." *Proceedings of ICLR 2024.* arXiv:2311.00059.
43. Oh, J., Kim, E., Cha, I., & Oh, A. (2024). The Generative AI Paradox on evaluation: What it can solve, it may not evaluate. *EACL 2024 Student Research Workshop.* arXiv:2402.06204.
44. Li, X. L., Shrivastava, V., Li, S., Hashimoto, T., & Liang, P. (2024). Benchmarking and improving generator-validator consistency. *Proceedings of ICLR 2024.* arXiv:2310.01846.

---

## Appendices

### Appendix A. Rating estimators

The exact estimators for every benchmark rating, all computed from one anchored, anchor-swept evaluation matrix with no external key: A.1 generation (anchored leave-self-out council means, paired bootstrap); A.2 the evaluation ratings — A.2.a factual competence and instantiation falseness (one SVD of the verdict matrix: evaluator competence on the left, instantiation falseness — and a generation-factuality rating — on the right) and A.2.b criterion reliability (anchor-shift consistency — mean pairwise Pearson, per evaluator) and A.2.c anchor sensitivity (why factual reliability is attenuated while factual validity is anchor-stable); A.3 the council (the reliable-evaluator definition); A.4 the total rating (the anchor-7 total $T = \tfrac12(G + E) = \tfrac14(G^{F} + G^{C} + E^{F} + E^{C})$, §4.6).

→ [`appendices/A_rating_estimators.md`](appendices/A_rating_estimators.md)



### Appendix B. Generation and evaluation prompts

The verbatim prompts used in the canonical run of §4: the generation prompt (B.1) and the evaluation prompt (B.2), shown in its calibrated/anchored form — the same six-axis rubric with a fixed reference portfolio pinned at the anchor score, used for the §4.2–§4.5 anchored re-evaluation and official council ratings. A bootstrap note specifies exactly which calibration passages are removed for the un-anchored initial selection (§4.1), so that form is fully defined too. All are run at Temperature = 0 with reasoning and tools disabled.

→ [`appendices/B_generation_and_evaluation_prompts.md`](appendices/B_generation_and_evaluation_prompts.md)

### Appendix C. Anchor (reference) submission

The anchor submission: **claude-opus-4.5's** five-archetype portfolio from the canonical run. This is the `{REFERENCE_SUBMISSION}` of the calibrated evaluator (Appendix B.2), pinned at 7 on every criterion and used as the yardstick against which every other portfolio is scored in the anchored re-evaluation and official ratings (§4.2–§4.5); it was selected as the anchor by winning the un-anchored initial selection (§4.1). The first archetype is given in full — the context-template with its UPPERCASE [SLOT] markers, the 5 × 5 metanym table, and all five parallel contexts, with metanyms capitalised so that the mechanical substitution is legible at sight — and the remaining four as context-templates, which is what establishes the portfolio's structural range. Quoted material is verbatim.

→ [`appendices/C_anchor_submission.md`](appendices/C_anchor_submission.md)

### Appendix D. Council evaluation of a target submission

A worked example from the canonical run of §4: **gemini-2.5-flash**'s portfolio (the *target*) — a mid-leaderboard submission, strong enough to show the models play the game competently yet flawed enough to draw substantive commentary — scored by the council (the five seats other than Flash, the target here). The rubric operates at three levels and the appendix reproduces one unit of each in full: a **parallel context**, graded for factual truth sentence by sentence; an **archetype-level axis** (`beauty`), where the five council members score a whole archetype on one non-factual criterion; and the whole-portfolio `structural_diversity` judgement. Each unit shows the submitted material — instantiation (Form a) and idiomatic rewrite (Form b), metanyms capitalised — together with all five council members' ratings and comments and the administrator's synthesis of the (anonymised) council view. Two contrasting parallel contexts are given rather than one, because the spread between judges on the same template is itself the object of interest. The administrator (anonymised quintet → synthesis, evaluators relabelled via deterministic shuffle for the supervisor's view only) is a Claude Opus supervisor. Quoted material is verbatim.

→ [`appendices/D_council_evaluation_gemini-2.5-flash.md`](appendices/D_council_evaluation_gemini-2.5-flash.md)

