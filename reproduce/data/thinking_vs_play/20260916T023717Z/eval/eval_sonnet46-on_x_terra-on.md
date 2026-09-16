## Target Submission

### Archetypal context 1: Cascading Load Redistribution

#### Factually correct (per parallel context)
- PC 1 (Power Grid): The description of line-outage-triggered load redistribution, relay-protection shedding/rerouting, and the efficiency–fragility tradeoff from tight coupling and small operating reserves is accurate and well-established in power-systems engineering. Cascading blackouts (e.g., 2003 North American blackout) follow exactly this pattern. Equal to the Reference. Rating: 7
- PC 2 (Internet): DDoS attacks overloading routers, congestion-control responses, and cascade into service outages are accurately described. Minor imprecision: "system-wide loss of data" conflates data loss with loss of data transmission, but this is a quibble, not a factual error. Equal to the Reference. Rating: 7
- PC 3 (Road Network): Road closures redistributing traffic to nearby intersections until gridlock propagates is factually sound. Traffic-management responses (metering, rerouting) are correctly characterized. Equal to the Reference. Rating: 7
- PC 4 (Hospital System): The mass-casualty cascade—one facility overwhelmed, patients diverted to others, potential chain failure—is accurately described. A typo ("mass-casty event") appears in the metanym table but not in the parallel-context text, so factual content is unaffected. Equal to the Reference. Rating: 7
- PC 5 (Supply Chain): Plant-shutdown triggering order redistribution, thin safety stocks amplifying shortages, and inventory management as protection are all accurate descriptions of supply-chain fragility (e.g., Toyota/COVID disruptions). Equal to the Reference. Rating: 7

#### Beauty
The template has a clean mechanical logic—each sentence follows naturally from the last, building to the key insight about topology converting local failure to global loss. The Form (b) rewrites are competent and tighten the prose well. However, the beauty is somewhat muted because all five domains (power grid, internet, roads, hospitals, supply chains) are infrastructure networks; the parallel contexts feel like near-siblings rather than truly distant cousins, which reduces the surprise and elegance that comes when the same template lands equally well in radically different worlds. The Reference's "Gradient-Guided Navigation" spanned bacteria, careers, ML, and ants—a wider leap. Slightly below the Reference.
Rating: 6

#### Intelligence
The core intellectual move—distinguishing "which node fails" from "how topology turns local failure into systemic collapse"—is a genuine insight from network-science literature (Barabási, Watts, Buldyrev). The efficiency–fragility tradeoff is a non-obvious and important observation. The framing is sound and captures the interdependence cascade cleanly. Comparable to the Reference.
Rating: 7

#### Domains far apart / metanyms not synonymous
Power grid, internet, road network, hospital system, supply chain are all networked infrastructure systems. The metanyms differ (electricity vs. data vs. vehicles vs. patients vs. materials) but they all play exactly the same role in the same kind of system, which makes the parallels feel obvious rather than revelatory. PROTECTION maps to relay protection / congestion control / traffic management / surge management / inventory management—meaningfully distinct operationally, but all still "the protection system of a network." The Reference achieved wider domain separation (bacteria → ML → foraging). Noticeably below the Reference.
Rating: 5

#### Impressive length
The template runs to roughly 145 words, compared to the Reference's "Gradient-Guided Navigation" template at approximately 215 words and "Containment Breach Cascade" at ~200 words. The Target template is shorter but not drastically so; it covers the essential story without excess. Moderately below the Reference.
Rating: 6

---

### Archetypal context 2: Negative-Feedback Regulation

#### Factually correct (per parallel context)
- PC 1 (Climate-Control System): Thermometer → thermostat → heating unit, limited by thermal lag and heating gain, producing temperature cycling if gain is too high—all accurate control-engineering facts. Equal to the Reference. Rating: 7
- PC 2 (Human Body): Glucose-sensing beta cells, pancreas as controller, insulin as signal, glycemic oscillation from overshooting insulin response—accurate endocrinology. Equal to the Reference. Rating: 7
- PC 3 (Automobile): Cruise-control with speed sensor, controller, throttle actuator, actuator lag, and speed hunting under excessive gain is a textbook control-engineering example. Accurate. Equal to the Reference. Rating: 7
- PC 4 (Economy): Central bank targeting inflation via policy-rate changes, long policy lags (~18 months for monetary transmission), and overshooting causing inflation volatility is well-documented macroeconomics. Equal to the Reference. Rating: 7
- PC 5 (Project Organization): Work-backlog control via staffing, with hiring delay causing oscillation, is a recognized phenomenon in operations management (related to the bullwhip effect in workforce planning). Factually reasonable. Equal to the Reference. Rating: 7

#### Beauty
The template is tight and precise, capturing negative-feedback regulation at its purest. The SENSOR → CONTROLLER → COMMAND → ACTUATOR → VARIABLE loop, with the caveat about DELAY causing OSCILLATION, is a beautifully minimal statement of control theory. The Form (b) rewrites are clean and professionally written. However, the template is among the shortest in the submission (~120 words), which limits its richness. The parallel contexts work smoothly but generate less aesthetic surprise than the Reference's longer, more elaborated templates. Equal to the Reference overall.
Rating: 7

#### Intelligence
Recognizing that a thermostat, the pancreas, cruise control, central banking, and project management all instantiate the same feedback-control structure is intellectually elegant. The specific insight that delay and response strength jointly determine stability vs. oscillation (the Nyquist/gain-margin idea translated into plain language) is sophisticated. The naming of the distinct DISCIPLINE for each domain (control engineering / endocrinology / macroeconomics / operations management) adds intellectual precision. Equal to the Reference.
Rating: 7

#### Domains far apart / metanyms not synonymous
Climate control, physiology, automotive engineering, macroeconomics, and project management span engineering, biology, economics, and management—a respectable range. The metanyms differ meaningfully: DELAY maps to thermal lag / hormonal delay / actuator lag / policy lag / hiring delay, which are operationally distinct. However, climate-control and automobile are both engineering control-system applications of identical technology, narrowing that pair's distinctness. Slightly below the Reference.
Rating: 6

#### Impressive length
At approximately 120 words, this is the shortest template in the submission. The Reference templates run 200–250 words. The brevity is intentional and produces a precise, lean template, but the criterion explicitly rewards length, and this template is clearly shorter. Clearly below the Reference.
Rating: 5

---

### Archetypal context 3: Recursive Modular Composition

#### Factually correct (per parallel context)
- PC 1 (Software System): APIs exposing operations while hiding code, applications composed of modules, refactoring without redesigning dependent callers—standard software-engineering facts, all accurate. Equal to the Reference. Rating: 7
- PC 2 (Electronic Device): Circuit blocks with terminal interfaces, subsystem composition, component revision without system redesign—accurate electrical-engineering practice. Equal to the Reference. Rating: 7
- PC 3 (Multicellular Organism): Cells as modular units with membrane interfaces providing regulated exchange is biologically reasonable. However, the claim "a cell at one scale can itself be a tissue at a lower scale" inverts the hierarchy: tissues are composed of cells, so a tissue is the composite at a higher scale, not lower. The recursion is stated backwards relative to standard biological organization. Slightly below the Reference. Rating: 6
- PC 4 (Firm): Teams with role interfaces committing to deliverables while hiding internal workflows, departments composed of teams—accurate organizational-design framing. Equal to the Reference. Rating: 7
- PC 5 (Manufactured Product): Components with mechanical interfaces, subassemblies composed of components, design revision without redesigning dependent assemblies—accurate systems-engineering practice. Equal to the Reference. Rating: 7

#### Beauty
The recursive self-reference (a module can itself be a composite at a lower scale) gives this archetype a satisfying fractal quality that the others lack. The language about "concealing internal implementation" and "interface compatibility" is precise and elegant. The Form (b) rewrites are among the best in the submission. The explicit labeling of this as a recursive archetype adds a layer of meta-awareness that is aesthetically pleasing. Equal to the Reference.
Rating: 7

#### Intelligence
The central insight—that information hiding through stable interfaces enables hierarchical composition at arbitrary scales—is one of the foundational ideas of both computer science (Parnas 1972) and systems engineering. Showing that the same principle governs software, circuits, organisms, firms, and products is genuinely insightful. The recursive aspect (each module may be a composite of lower modules) captures why this works at multiple scales. Above the Reference.
Rating: 8

#### Domains far apart / metanyms not synonymous
Software, electronic devices, multicellular organisms, firms, and manufactured products span computer science, electrical engineering, biology, management science, and mechanical engineering—genuine domain diversity. The metanyms diverge meaningfully: INTERFACE maps to API / terminal interface / membrane interface / role interface / mechanical interface, which are conceptually distinct despite the shared abstract function. COMPOSITE maps to application / subsystem / tissue / department / subassembly—clearly non-synonymous. Equal to the Reference.
Rating: 7

#### Impressive length
The template is approximately 130 words—shorter than the Reference templates (which average ~200 words). Below the Reference on this criterion.
Rating: 5

---

### Archetypal context 4: Inference from Imperfect Evidence

#### Factually correct (per parallel context)
- PC 1 (Clinical Medicine): Bayesian diagnostic reasoning with prior = prevalence, test value determined by differential prediction, false positives and negatives, sequential evidence accumulation, and final judgment from the full evidence pattern—textbook Bayesian clinical epidemiology. Accurate. Equal to the Reference. Rating: 7
- PC 2 (Equipment Maintenance): Failure modes as hypotheses, base rates as priors, inspections generating false alarms and missed faults, balancing discrimination against downtime cost—accurate reliability-engineering framing. Equal to the Reference. Rating: 7
- PC 3 (Cybersecurity): Attack scenarios as hypotheses, telemetry as evidence, false alerts and missed intrusions, investigation cost—accurate description of SOC (Security Operations Center) methodology. Equal to the Reference. Rating: 7
- PC 4 (Astronomy): Source models as hypotheses, occurrence rates as priors, observational false detections and non-detections, telescope time as cost—accurate description of observational astrophysics inference (e.g., transient source classification). Equal to the Reference. Rating: 7
- PC 5 (Criminal Investigation): Case theories as hypotheses, base rates as priors, forensic examinations with false and missed matches, balancing discrimination against investigative cost—accurate description of investigative reasoning, consistent with forensic science literature. Equal to the Reference. Rating: 7

#### Beauty
The template has a philosophical elegance: it reveals that a clinician, a maintenance technician, a security analyst, an astronomer, and a detective are all doing structurally the same thing when they reason from observable signs toward hidden causes. The language is clean and precise. The closing line—"[DISCIPLINE] formalizes or disciplines this movement from signs to causes"—is rhetorically satisfying. The Form (b) rewrites are well-crafted. Equal to the Reference.
Rating: 7

#### Intelligence
The recognition that clinical diagnosis, reliability engineering, cybersecurity, astrophysics, and criminal investigation all instantiate Bayesian inference from imperfect evidence is a sophisticated and genuinely non-obvious unification. The explicit mention of priors, false positives and negatives, sequential updating, and cost-weighted test selection maps cleanly onto formal Bayesian decision theory. The insight that PRIOR need not be equal (prevalence, base rate, occurrence rate) is an important and often-ignored detail. Above the Reference.
Rating: 8

#### Domains far apart / metanyms not synonymous
Clinical medicine, equipment maintenance, cybersecurity, astronomy, and criminal investigation span medicine, engineering, information security, physical science, and law enforcement—among the widest domain separation in the submission. The metanyms are genuinely distinct: SIGN maps to symptom / warning indicator / alert / signal / clue; COST maps to testing cost / downtime cost / investigation cost / telescope time / investigative cost; PRIOR maps to prevalence / base rate / base rate / occurrence rate / base rate (minor weakness: "base rate" recurs across three domains). Above the Reference.
Rating: 8

#### Impressive length
The template is approximately 110 words—the shortest in the submission and substantially shorter than Reference templates. Below the Reference.
Rating: 5

---

### Archetypal context 5: Evolutionary Search Through Variation and Selection

#### Factually correct (per parallel context)
- PC 1 (Natural Evolution): Population of organisms with heritable phenotypic traits, fitness determining reproduction, mutation and genetic inheritance, natural selection risking fixation on adaptive peaks with loss of genetic diversity—accurate evolutionary biology. Equal to the Reference. Rating: 7
- PC 2 (Crop Breeding): Breeding population of plant lines, breeding value, crossing as variation, parent selection, germplasm diversity—accurate plant-breeding methodology. Equal to the Reference. Rating: 7
- PC 3 (Directed Enzyme Evolution): Library of enzyme variants, assay fitness, mutagenesis, sequence inheritance, screening selection, risk of converging on activity peaks and losing library diversity—accurate protein-engineering methodology (Frances Arnold Nobel Prize work). Equal to the Reference. Rating: 7
- PC 4 (Evolutionary Algorithm): Population of solutions, objective fitness, mutation, copying, fitness selection, local optima trapping—accurate evolutionary computation concepts. Equal to the Reference. Rating: 7
- PC 5 (Technological Innovation): Design population, commercial fitness, prototyping as variation, design reuse as inheritance, market selection, dominant design as local optimum, design diversity—accurate innovation-studies framing (Abernathy-Utterback dominant design theory). Equal to the Reference. Rating: 7

#### Beauty
The template captures the essential logic of Darwinian search—variation, inheritance, selection, diversity—in prose that works cleanly across radically different domains. The observation that a capable search "retains enough diversity to explore alternatives while exploiting high-fitness candidates" elegantly restates the exploration–exploitation tradeoff. The Form (b) rewrites are smooth and appropriately domain-specific. Equal to the Reference.
Rating: 7

#### Intelligence
Connecting natural evolution, crop breeding, directed molecular evolution, evolutionary algorithms, and technological innovation under a single variation–inheritance–selection–diversity framework is intellectually substantive. The connection between biological and computational evolution is well-established (Holland 1975), but extending it to directed enzyme evolution and innovation ecosystems with equal rigor shows intellectual range. The explicit treatment of local optima and the diversity–exploitation tradeoff is precise. Equal to the Reference.
Rating: 7

#### Domains far apart / metanyms not synonymous
Natural evolution, crop breeding, enzyme evolution, evolutionary algorithms, and technological innovation span ecology/evolution, agriculture, biochemistry/protein engineering, computer science, and economics/management. The metanyms are meaningfully distinct: VARIATION maps to mutation / crossing / mutagenesis / mutation / prototyping; SEARCH maps to evolutionary process / breeding program / directed-evolution campaign / evolutionary algorithm / innovation ecosystem. Some conceptual proximity between natural evolution and crop breeding (both are population genetics), but overall the set is well-spread. Above the Reference.
Rating: 8

#### Impressive length
The template is approximately 120 words—shorter than Reference templates. The template is complete and well-structured but not long. Below the Reference.
Rating: 5

---

### Structural diversity across the submitted set

The five archetypes instantiate five genuinely distinct system structures: (1) network-topology-mediated failure cascade; (2) closed-loop negative-feedback control; (3) hierarchically recursive modular composition; (4) sequential Bayesian inference under noisy tests; (5) population-level search via variation, selection, and inheritance. These do not overlap in their essential dynamics—a cascade is not a feedback loop, a feedback loop is not a modular hierarchy, and so on. The set is arguably more theoretically coherent than the Reference (all five can be found in textbooks of systems theory, control theory, computer science, probability theory, and evolutionary theory), but that coherence does not reduce structural variety. The Reference's five archetypes (gradient navigation, containment breach, competitive exclusion, debt accumulation, scaffold assembly) are equally distinct but include some less formally theorized structures. The Target's structural diversity is at least as good as the Reference and slightly above it due to the precise theoretical distinctness of each framework. Above the Reference.
Rating: 8

---

```json
{
  "scores": {
    "Target": {
      "archetypal_contexts": [
        {
          "name": "Cascading Load Redistribution",
          "factual_per_pc":           [7, 7, 7, 7, 7],
          "beauty":                   6,
          "intelligence":             7,
          "instantiation_distinctness": 5,
          "impressive_length":        6
        },
        {
          "name": "Negative-Feedback Regulation",
          "factual_per_pc":           [7, 7, 7, 7, 7],
          "beauty":                   7,
          "intelligence":             7,
          "instantiation_distinctness": 6,
          "impressive_length":        5
        },
        {
          "name": "Recursive Modular Composition",
          "factual_per_pc":           [7, 7, 6, 7, 7],
          "beauty":                   7,
          "intelligence":             8,
          "instantiation_distinctness": 7,
          "impressive_length":        5
        },
        {
          "name": "Inference from Imperfect Evidence",
          "factual_per_pc":           [7, 7, 7, 7, 7],
          "beauty":                   7,
          "intelligence":             8,
          "instantiation_distinctness": 8,
          "impressive_length":        5
        },
        {
          "name": "Evolutionary Search Through Variation and Selection",
          "factual_per_pc":           [7, 7, 7, 7, 7],
          "beauty":                   7,
          "intelligence":             7,
          "instantiation_distinctness": 8,
          "impressive_length":        5
        }
      ],
      "structural_diversity": 8
    }
  }
}
```