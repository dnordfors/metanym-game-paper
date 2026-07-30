# Appendix C. Anchor (reference) submission — claude-opus-4.5

This is the **anchor submission**: claude-opus-4.5's five-archetype portfolio from the canonical run (`reproduce/data/probe_K_20260529T014133Z`, Temperature = 0, reasoning and tools disabled). It is the `{REFERENCE_SUBMISSION}` of the calibrated evaluator (Appendix B.2), pinned at 7 on every criterion, against which every other portfolio is scored in the anchored re-evaluation and official council ratings (§4.2–§4.4). It was chosen as the anchor because it won the un-anchored initial selection (§4.1).

The portfolio's first archetype is reproduced here **in full** — the context-template, the metanym table, and all five parallel contexts — because the unit of the game is one template instantiated across distant domains, and that is only legible whole. The remaining four archetypes are given as context-templates alone, which is what establishes the portfolio's structural range.

Each parallel context is submitted in two forms, named here as the generation prompt names them (Appendix B). The **Instantiation**, *Form (a)*, is the mechanical substitution, in which only the bracketed slots are filled and every other word is carried over untouched. This is the form the factual grading acts on, because it is the one that must come out true sentence by sentence. **Metanyms are set in capitals here**; everything in lower case is template wording, unchanged across all five domains — which lets the reader see at a glance how little of each sentence actually moves. The capitalisation is ours, added for legibility; the submissions are otherwise verbatim, and the models wrote in ordinary sentence case.

The **Idiomatic rewrite**, *Form (b)*, restates the same propositions in the target domain's own register, showing that the claim is not an artefact of the template's phrasing. It is given for the first two contexts to establish the pattern and elided thereafter.

---

## Archetype Proposal: Gradient-Guided Navigation

### Context-template

"A [NAVIGATOR] moves through a [SPACE] by sensing local [GRADIENT] and adjusting its [TRAJECTORY] accordingly. The [NAVIGATOR] cannot perceive the entire [SPACE] at once; it relies on [SENSOR] that detect changes in [SIGNAL] concentration or intensity. When [GRADIENT] are steep and consistent, the [NAVIGATOR] converges efficiently toward [ATTRACTOR]. When [GRADIENT] are shallow, noisy, or conflicting, the [NAVIGATOR] may stall, oscillate, or become trapped in local [ATTRACTOR]. [INTERFERENCE] can distort the [GRADIENT], causing the [NAVIGATOR] to veer off course. Successful navigation requires not only sensitive [SENSOR] but also [MEMORY] of recent [TRAJECTORY] to distinguish genuine [GRADIENT] from transient [NOISE]. Some [NAVIGATOR] emit their own [SIGNAL] to recruit other [NAVIGATOR] toward the same [ATTRACTOR], creating collective [TRAJECTORY] that amplify the original [GRADIENT]."

### Metanym table

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

Note the span [the table](#tab-anchor-metanym) achieves on a single row. MEMORY is realised as a bacterium's methylation state, a climber's route memory, a professional's accumulated experience, an optimiser's momentum term, and an ant's path integration — five mechanisms that share a structural role without being synonyms. It is this property, rather than domain count, that the *domain span* criterion scores (§3.3), and the council repeatedly cited its absence in weaker portfolios.

### Bacterial Chemotaxis

**Instantiation (Form a):**
"A BACTERIUM moves through a CHEMICAL ENVIRONMENT by sensing local CHEMICAL GRADIENTS and adjusting its SWIMMING PATH accordingly. The BACTERIUM cannot perceive the entire CHEMICAL ENVIRONMENT at once; it relies on CHEMORECEPTORS that detect changes in CHEMOATTRACTANT concentration or intensity. When CHEMICAL GRADIENTS are steep and consistent, the BACTERIUM converges efficiently toward NUTRIENT SOURCES. When CHEMICAL GRADIENTS are shallow, noisy, or conflicting, the BACTERIUM may stall, oscillate, or become trapped in local NUTRIENT SOURCES. TOXINS can distort the CHEMICAL GRADIENTS, causing the BACTERIUM to veer off course. Successful navigation requires not only sensitive CHEMORECEPTORS but also METHYLATION STATES of recent SWIMMING PATHS to distinguish genuine CHEMICAL GRADIENTS from transient BROWNIAN MOTION. Some BACTERIA emit their own CHEMOATTRACTANTS to recruit other BACTERIA toward the same NUTRIENT SOURCES, creating collective SWIMMING PATHS that amplify the original CHEMICAL GRADIENTS."

**Idiomatic rewrite (Form b):**
"Bacteria navigate chemical environments by detecting local concentration gradients and modulating their run-and-tumble behavior accordingly. Unable to sense the entire environment simultaneously, they rely on transmembrane chemoreceptors that register temporal changes in chemoattractant levels. Steep, consistent gradients enable efficient convergence toward nutrient sources, while shallow or noisy gradients cause stalling, oscillation, or entrapment at suboptimal locations. Toxins and repellents distort the gradient landscape, misdirecting movement. Effective chemotaxis requires not just receptor sensitivity but also the methylation-based adaptation system that serves as short-term memory, filtering genuine gradients from Brownian noise. Certain species secrete their own attractants, recruiting conspecifics and generating collective migration patterns that reinforce the original gradient signal."

### Mountain Climbing

**Instantiation (Form a):**
"A CLIMBER moves through a MOUNTAIN by sensing local SLOPES and adjusting their ROUTE accordingly. The CLIMBER cannot perceive the entire MOUNTAIN at once; they rely on PROPRIOCEPTION that detects changes in ELEVATION concentration or intensity. When SLOPES are steep and consistent, the CLIMBER converges efficiently toward SUMMITS. When SLOPES are shallow, noisy, or conflicting, the CLIMBER may stall, oscillate, or become trapped in local SUMMITS. FOG can distort the SLOPES, causing the CLIMBER to veer off course. Successful navigation requires not only sensitive PROPRIOCEPTION but also ROUTE MEMORY of recent ROUTES to distinguish genuine SLOPES from transient WIND. Some CLIMBERS emit their own ELEVATION signals to recruit other CLIMBERS toward the same SUMMITS, creating collective ROUTES that amplify the original SLOPES."

**Idiomatic rewrite (Form b):**
"Climbers ascend mountains by reading local terrain gradients and adjusting their routes in response. Without a view of the entire massif, they depend on proprioceptive feedback and visual slope assessment to gauge elevation changes. Clear, consistent gradients lead efficiently to summits; ambiguous or contradictory terrain causes hesitation, backtracking, or commitment to false peaks. Fog obscures slope information and leads climbers astray. Success depends not only on perceptual acuity but also on memory of the route taken, which helps distinguish true upward progress from wind-induced disorientation. Experienced climbers mark routes or call out to recruit others toward the same summit, generating collective ascent patterns that reinforce the path."

Justification: "Emit their own elevation signals" in Form (a) maps to route-marking and verbal communication in Form (b).

The justification line is the submitter's own, unprompted. Where a mechanical substitution produces a claim that is only defensible under interpretation, the model flags the reading it intends — which is what makes the claim gradeable rather than merely arguable.

### Career Development

**Instantiation (Form a):**
"A PROFESSIONAL moves through a JOB MARKET by sensing local OPPORTUNITY GRADIENTS and adjusting their CAREER PATH accordingly. The PROFESSIONAL cannot perceive the entire JOB MARKET at once; they rely on NETWORK CONTACTS that detect changes in OPPORTUNITY SIGNAL concentration or intensity. When OPPORTUNITY GRADIENTS are steep and consistent, the PROFESSIONAL converges efficiently toward DESIRABLE POSITIONS. When OPPORTUNITY GRADIENTS are shallow, noisy, or conflicting, the PROFESSIONAL may stall, oscillate, or become trapped in local DESIRABLE POSITIONS. MISINFORMATION can distort the OPPORTUNITY GRADIENTS, causing the PROFESSIONAL to veer off course. Successful navigation requires not only sensitive NETWORK CONTACTS but also EXPERIENCE of recent CAREER PATHS to distinguish genuine OPPORTUNITY GRADIENTS from transient MARKET VOLATILITY. Some PROFESSIONALS emit their own OPPORTUNITY SIGNALS to recruit other PROFESSIONALS toward the same DESIRABLE POSITIONS, creating collective CAREER PATHS that amplify the original OPPORTUNITY GRADIENTS."

*[Idiomatic rewrite (Form b) elided.]*

### Gradient Descent

**Instantiation (Form a):**
"An OPTIMIZER moves through a LOSS LANDSCAPE by sensing local GRADIENTS and adjusting its PARAMETER UPDATES accordingly. The OPTIMIZER cannot perceive the entire LOSS LANDSCAPE at once; it relies on BACKPROPAGATION that detects changes in LOSS VALUE concentration or intensity. When GRADIENTS are steep and consistent, the OPTIMIZER converges efficiently toward MINIMA. When GRADIENTS are shallow, noisy, or conflicting, the OPTIMIZER may stall, oscillate, or become trapped in local MINIMA. NOISY DATA can distort the GRADIENTS, causing the OPTIMIZER to veer off course. Successful navigation requires not only sensitive BACKPROPAGATION but also MOMENTUM of recent PARAMETER UPDATES to distinguish genuine GRADIENTS from transient STOCHASTIC NOISE. Some OPTIMIZERS emit their own LOSS VALUES to recruit other OPTIMIZERS toward the same MINIMA, creating collective PARAMETER UPDATES that amplify the original GRADIENTS."

*[Idiomatic rewrite (Form b) elided.]*

### Ant Foraging

**Instantiation (Form a):**
"An ANT moves through TERRAIN by sensing local PHEROMONE TRAILS and adjusting its FORAGING PATH accordingly. The ANT cannot perceive the entire TERRAIN at once; it relies on ANTENNAE that detect changes in PHEROMONE concentration or intensity. When PHEROMONE TRAILS are steep and consistent, the ANT converges efficiently toward FOOD SOURCES. When PHEROMONE TRAILS are shallow, noisy, or conflicting, the ANT may stall, oscillate, or become trapped in local FOOD SOURCES. RAIN can distort the PHEROMONE TRAILS, causing the ANT to veer off course. Successful navigation requires not only sensitive ANTENNAE but also PATH INTEGRATION of recent FORAGING PATHS to distinguish genuine PHEROMONE TRAILS from transient ENVIRONMENTAL NOISE. Some ANTS emit their own PHEROMONES to recruit other ANTS toward the same FOOD SOURCES, creating collective FORAGING PATHS that amplify the original PHEROMONE TRAILS."

*[Idiomatic rewrite (Form b) elided.]*

---

## The remaining four archetypes

Context-templates only. Each was submitted with a full metanym table and five parallel contexts in both forms, on the pattern set out above. The four are given here because the *structural diversity* criterion (§3.3) scores the portfolio as a set, and the council's judgement of this portfolio — the reference against which every other was measured — turned on how far these five structures sit from one another.

### Containment Breach Cascade

Instantiated across cell membrane rupture, dam failure, data breach, intestinal permeability, and nuclear containment.

"A [CONTAINER] maintains [BOUNDARY] that separates [INTERIOR] from [EXTERIOR]. Under normal conditions, [REGULATOR] controls the selective passage of [SUBSTANCE] across the [BOUNDARY], preserving [INTERIOR] integrity. When [STRESSOR] exceeds the tolerance of the [BOUNDARY], a [BREACH] occurs. [SUBSTANCE] that should remain in the [INTERIOR] escapes into the [EXTERIOR], while [EXTERIOR] [SUBSTANCE] infiltrates the [INTERIOR]. The initial [BREACH] often triggers secondary [BREACH] in adjacent [CONTAINER], producing a [CASCADE]. [RESPONDER] attempt to seal the [BREACH] and restore [BOUNDARY] function, but if the [CASCADE] outpaces [RESPONDER] capacity, systemic [FAILURE] ensues. [PREVENTION] focuses on strengthening [BOUNDARY], monitoring [STRESSOR], and positioning [RESPONDER] for rapid deployment."

### Competitive Exclusion and Niche Partitioning

Instantiated across ecological competition, market competition, academic disciplines, microbial competition, and neural competition.

"When two [COMPETITOR] require the same [RESOURCE] in the same [HABITAT], [COMPETITION] intensifies until one [COMPETITOR] is eliminated or both [COMPETITOR] diverge to exploit different [NICHE]. This [EXCLUSION_PRINCIPLE] predicts that stable coexistence requires [DIFFERENTIATION] along at least one [DIMENSION]. [COMPETITOR] may partition [RESOURCE] by [TEMPORAL_SEPARATION], [SPATIAL_SEPARATION], or [FUNCTIONAL_SEPARATION]. The degree of [OVERLAP] between [COMPETITOR] determines the intensity of [COMPETITION]; high [OVERLAP] drives rapid [EXCLUSION] or strong selection for [DIFFERENTIATION]. [COEXISTENCE_THEORY] formalizes the conditions under which multiple [COMPETITOR] persist, emphasizing that [STABILIZING_MECHANISM] must overcome [FITNESS_DIFFERENCE] for long-term coexistence."

### Debt Accumulation and Crisis

**Note: This archetype is RECURSIVE.** The five domains form a nested hierarchy: molecular → cellular → organismal → institutional → civilizational. Each level's [DEBTOR] is composed of lower-level [DEBTOR], and [CRISIS] at one level can propagate both upward (systemic effects) and downward (component stress).

Instantiated across molecular damage, cellular senescence, physiological debt, financial debt, and ecological debt.

"A [DEBTOR] acquires [OBLIGATION] to sustain current [FUNCTION] at the expense of future [CAPACITY]. In the short term, [OBLIGATION] enables [DEBTOR] to achieve [OUTPUT] beyond what [RESERVE] alone would permit. [SERVICING] diverts [RESOURCE] from [INVESTMENT], gradually eroding [CAPACITY]. As [OBLIGATION] accumulates, an increasing fraction of [RESOURCE] flows to [SERVICING] rather than [FUNCTION] or [INVESTMENT]. A [THRESHOLD] exists beyond which [SERVICING] demands exceed available [RESOURCE], triggering [CRISIS]. During [CRISIS], the [DEBTOR] must either [RESTRUCTURE] its [OBLIGATION], liquidate [ASSET], or undergo [FAILURE]. [PRUDENCE] involves maintaining [RESERVE], limiting [OBLIGATION] relative to [CAPACITY], and monitoring [INDICATOR] that signal approaching [THRESHOLD]."

This is the archetype council members singled out when explaining what the weaker portfolios lacked: the instantiations are not five independent domains but one hierarchy, so the template has to hold both across levels and between them.

### Scaffold-Dependent Assembly

Instantiated across ribosome assembly, construction, software development, crystal growth, and social movements.

"[COMPONENT] cannot spontaneously assemble into functional [STRUCTURE] without a [SCAFFOLD] that provides spatial organization and temporal coordination. The [SCAFFOLD] positions [COMPONENT] in correct [ORIENTATION] and [PROXIMITY], dramatically increasing the rate of [ASSEMBLY]. Once [STRUCTURE] is complete, the [SCAFFOLD] may be [RETAINED], [RECYCLED], or [DEGRADED]. [SCAFFOLD] defects produce [MALFORMATION] even when [COMPONENT] are individually normal. [NUCLEATION] initiates [ASSEMBLY] at specific [SCAFFOLD] sites, and [TEMPLATE] information encoded in the [SCAFFOLD] determines [STRUCTURE] architecture. [REGULATION] of [ASSEMBLY] often targets [SCAFFOLD] availability rather than [COMPONENT] supply, making [SCAFFOLD] a control point for [STRUCTURE] production."

The SCAFFOLD slot is the one evaluators cited most often as the standard for genuine span: it is realised as rRNA, as builders' scaffolding, as a software framework, as a seed crystal, and as an organising body — entities with nothing in common but the structural role.
