# Appendix D. Council evaluation of a target submission — gemini-2.5-flash

This is the council's evaluation of gemini-2.5-flash's portfolio from the canonical run (`probe_K_anchor7`), the worked example of the scoring machinery described in §3.3 and §4.2. Ratings are on the anchored 1–10 scale, with the anchor portfolio of Appendix C pinned at 7 on every criterion.

The rubric operates at three levels, and one unit of each is reproduced here in full: a **parallel context**, graded for factual truth sentence by sentence; an **archetype-level axis**, where the five council members score a whole archetype on one non-factual criterion; and the **whole-portfolio** structural-diversity judgement. Each unit shows the submitted material, all five council members' ratings and comments, and the administrator's synthesis of the anonymised council view. Every rating and comment quoted below is taken from the pinned evaluation JSON in `reproduce/data/`.

As in Appendix C, **metanyms in the Instantiations are set in capitals**, so that everything in lower case is template wording carried over unchanged. The capitalisation is ours, added for legibility; the submission and every rating and comment below are otherwise verbatim, and the models wrote in ordinary sentence case. It is worth the ink here, because on this portfolio the substituted words are usually where the trouble is.

Two things are worth watching across the units below, because they are what the estimators of Appendix A are built to exploit. First, the criticism is *specific and checkable*: evaluators quote the offending clause rather than assigning an impression. Second, the evaluators **disagree**, and they disagree by different amounts on different units — tightly where the submission contains a plain error, widely where the judgement is a matter of standard. That variation in spread, not the mean rating, is the signal the singular value decomposition reads competence from.

---

## Archetype 1: Resource Allocation Under Scarcity

### Submitted context-template

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

### Per parallel context

#### PC 1 (Ecosystem Management) — a plain error, and the council converges

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

#### PC 2 (Corporate Finance) — the same template, and the council spreads

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

### Archetype-level axes

Above the parallel contexts, each archetype is scored as a whole on the non-factual criteria. **Beauty** is reproduced in full as the representative axis; the remaining three for this archetype (intelligence, domain span, impressive length) follow the same structure.

#### Beauty

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

#### Impressive length — judges disagreeing on a countable quantity

Two of the five comments are given here because their juxtaposition is diagnostic:

**opus-4.5** — Rating: 6  
The template contains 15 slots and approximately 120 words, which is comparable to the Reference's templates. However, the template feels padded with generic concepts rather than building a complex, interconnected narrative. The Reference's templates of similar length achieve more conceptual density and structural sophistication

**3.1-pro** — Rating: 4  
The context-template is 79 words long. The Reference's templates are generally longer (e.g., Gradient-Guided Navigation is 108 words, Containment Breach is 92 words). The Target's template is noticeably shorter and less detailed than the Reference

The object is a fixed string and the question is arithmetic, yet the two judges report 120 words and 79 words and reach opposite verdicts on the same criterion. Across all five, the reported counts ranged from 79 to 120. This is the clearest single illustration in the run of why the benchmark cannot treat any judge as an oracle, and why competence has to be estimated from the panel rather than assumed — the substance of §4.3 and the motivation for the whole construction.

---

## Archetypes 2–6

The portfolio's remaining five archetypes were **Information Cascade and Collective Behavior**, **Adaptive System Response to Perturbation**, **Emergent Complexity from Simple Rules** (recursive), **Iterative Refinement Towards an Ideal** (recursive), and **The Unseen Hand of Coordination**.

*[Their context-templates, metanym tables, parallel contexts and per-unit evaluations are elided here. Each was evaluated under the identical protocol and contributes to the ratings of §4.4–§4.6 exactly as archetype 1 does; nothing about them is summarised or down-weighted.]*

## Structural diversity across the portfolio

The final scoring unit rates the submitted templates as a set. Two of the five comments are reproduced — the majority view and the sole dissent — with the administrator's synthesis.

**opus-4.5** — Rating: 5  
The six archetypes cover: (1) resource allocation, (2) information cascades, (3) homeostatic response, (4) emergence, (5) iterative refinement, and (6) decentralized coordination. These represent different system dynamics, but there is significant conceptual overlap—archetypes 4 and 6 both deal with emergence and self-organization, and ant colonies appear in both. The Reference's five archetypes (gradient navigation, containment breach, competitive exclusion, debt accumulation, scaffold assembly) show greater structural diversity, covering navigation, boundary dynamics, competition, temporal debt, and assembly processes. The Target's archetypes tend toward well-known systems concepts without the Reference's creative structural variety. The recursive claims in archetypes 4 and 5 are not convincingly demonstrated, unlike the Reference's elegant molecular→civilizational hierarchy

**3.1-pro** — Rating: 8  
The submitted set includes Resource Allocation, Information Cascade, Adaptive Response, Emergent Complexity, and Iterative Refinement. (Note: The submission actually contains six archetypes, but I am scoring the first five as per the standard format, though I will consider the sixth, "The Unseen Hand of Coordination," in this diversity assessment as it was provided). These archetypes represent different system structures: allocation of finite resources, propagation of information/behavior, homeostatic regulation, bottom-up emergence, and goal-directed iteration. This is a very diverse set of system structures, arguably slightly more diverse than the Reference's set (which leans heavily on spatial/physical metaphors like navigation, containment, and scaffolding)

**Administrator summary:** The council mostly agreed the set showed only moderate structural diversity, with four evaluators rating 5-6 and one dissenting upward at 8. The convergent view was that the five archetypes (resource allocation, information cascades, adaptive response, emergence, iterative refinement) tend toward familiar feedback-and-optimization and human-centered themes, lacking the Reference's bolder, more dramatically contrasted structures (gradient navigation, containment breach, scaffold assembly). The lone dissenter argued the set is arguably more diverse than the Reference's spatially-biased metaphors, while another noted internal overlap, with archetypes 4 and 6 both centering on emergence.

The dissent is instructive rather than anomalous. 3.1-pro is not scoring carelessly — it advances a substantive counter-argument, that the anchor's own set is biased toward spatial metaphors — and it is the only judge to notice and handle the fact that this portfolio contains six archetypes where the format specifies five. A rating that is both an outlier and better-reasoned than the majority is exactly the case that a naive majority vote mishandles and a competence-weighted factorisation is meant to price correctly (§4.5, Appendix A.3).
