## Target Submission

### Archetypal context 1: Cascading Load Redistribution

#### Factually correct (per parallel context)
- PC 1 (Power Grid): This is a strong and largely accurate account of cascading grid failures: outages can redistribute power, overload surviving infrastructure, and trigger protective shedding and wider blackouts. “Removing a substation” is somewhat loose because a line outage more directly removes or isolates a line, but the operational consequence is plausible. It is slightly better than the Reference’s 7-level factual consistency. Rating: 8
- PC 2 (Internet): The description correctly captures denial-of-service overload, rerouting, router capacity limits, congestion control, and topology-dependent service disruption. A denial-of-service attack does not necessarily remove a router, but disabling or functionally overwhelming one is a reasonable abstraction. This is somewhat cleaner than the Reference. Rating: 8
- PC 3 (Road Network): The analogy is factually sound at the network level: closures divert traffic, overloaded intersections propagate congestion, and traffic management can reroute or meter flows. “Removing an intersection” is slightly imprecise because a closure usually removes access through a junction rather than the junction itself, but the intended failure model is clear. Rating: 8
- PC 4 (Hospital System): Patient diversion, finite bed capacity, surge capacity, and regional care disruption are plausible. However, a mass-casualty event does not ordinarily “remove” a hospital, and hospitals do not literally convey patients in the same way that infrastructure conveys flows. The prose remains understandable but is about equal to the Reference rather than clearly better. Rating: 7
- PC 5 (Supply Chain): Plant shutdowns, order redistribution, throughput limits, safety stock, and shortage cascades are accurately represented. Inventory management can ration and reroute demand, although “isolating order load” is somewhat abstract. Overall this is modestly more factually disciplined than the Reference. Rating: 8

#### Beauty
The template is compact, symmetrical, and visually coherent, with a particularly effective progression from local shock to redistributed load, secondary failure, protection, and system-wide analysis. The five forms preserve that structure without becoming excessively repetitive. Its infrastructure-centered domain set is somewhat less surprising than the Reference’s broader mix, but the presentation is still slightly more elegant overall. Rating: 8

#### Intelligence
This archetype shows strong systems thinking: it distinguishes node capacity, reserve, topology, protective intervention, correlated shocks, and the difference between identifying a likely first failure and explaining propagation. The final sentence usefully shifts from event description to network-structural explanation. This is clearly thoughtful and marginally above the Reference’s benchmark. Rating: 8

#### Domains far apart / metanyms not synonymous
The domains are genuinely distinct, and the metanyms are generally well chosen, but all five examples remain variants of operational infrastructure networks. Power, internet, roads, hospitals, and supply chains are therefore somewhat closer than the Reference’s biological, geographic, occupational, computational, and insect domains. The mappings are still sufficiently non-synonymous and coherent to be around the reference level. Rating: 7

#### Impressive length
The template is substantial and contains several linked causal clauses, but it is a little shorter than some of the Reference templates and is not clearly more elaborate in sheer length. Its density is good, though its length is approximately comparable to the Reference. Rating: 7

### Archetypal context 2: Negative-Feedback Regulation

#### Factually correct (per parallel context)
- PC 1 (Climate-Control System): This is a very accurate control-theoretic description of thermostatic regulation, including sensing, setpoint comparison, actuation, lag, gain, overshoot, and cycling. The mapping is cleaner and more technically disciplined than many of the Reference’s instantiations. Rating: 8
- PC 2 (Human Body): The account correctly describes glucose sensing, insulin-mediated regulation, delayed response, physiological range, and possible oscillatory or unstable behavior. The pancreas is presented as directly comparing glucose with a setpoint, which is a useful abstraction but not a literal description of the distributed endocrine mechanism. It is approximately equal to or slightly better than the Reference. Rating: 7
- PC 3 (Automobile): Cruise control is accurately represented as a negative-feedback system with speed sensing, throttle actuation, lag, gain, and hunting around a setpoint. The prose is technically sound and clearer than the Reference’s average factual quality. Rating: 8
- PC 4 (Economy): The feedback analogy is standard and mostly correct: inflation is measured, policy rates are adjusted, transmission is delayed, and excessive or mistimed responses can destabilize inflation. The economy does not autonomously “regulate” inflation in quite the same direct sense as a thermostat, but the macroeconomic abstraction is defensible. Rating: 7
- PC 5 (Project Organization): Backlog measurement, staffing adjustment, hiring delay, and overshoot are a plausible operational-control model. Staffing does not directly determine backlog without assumptions about incoming demand and productivity, but those assumptions are implicit and reasonable. This is slightly better than the Reference. Rating: 8

#### Beauty
This is an especially clean archetype. The template has a natural explanatory rhythm—measurement, comparison, command, actuation, remeasurement—and the parallel prose preserves the same loop without awkward substitutions. The contrast between rapid correction and stability gives the passage both conceptual clarity and aesthetic balance. Rating: 8

#### Intelligence
The inclusion of operating range, measurement noise, delay, response strength, overshoot, and oscillation makes this more than a superficial “feedback” metaphor. It identifies the central control-engineering trade-off and applies it across physical, biological, economic, and organizational systems. This is clearly above the Reference’s baseline. Rating: 8

#### Domains far apart / metanyms not synonymous
Climate control, endocrinology, automotive control, monetary policy, and project operations span substantially different domains. Some slots—controller, target, response, delay—remain deliberately abstract and therefore somewhat generic, but the metanyms themselves are not synonyms and the instantiations are at least as diverse as those in the Reference. Rating: 8

#### Impressive length
The template is a well-developed six-sentence construction with enough detail to express both normal operation and failure modes. It is substantial but broadly comparable in length to the Reference templates, without being clearly longer. Rating: 7

### Archetypal context 3: Recursive Modular Composition

#### Factually correct (per parallel context)
- PC 1 (Software System): The modularity, interface hiding, composition, compatibility, refactoring, and fault-localization claims are largely correct. However, saying that a software module can itself be an application “at a lower scale” reverses the usual hierarchy: an application is generally a composite built from modules. This makes the recursive claim weaker than the Reference. Rating: 6
- PC 2 (Electronic Device): Circuit blocks, terminal interfaces, subsystem composition, compatibility, and localized electrical faults are plausible. The statement that a circuit block is a subsystem at a lower scale has the same scale-direction problem as the software example, since a subsystem is normally the larger composite. Rating: 6
- PC 3 (Multicellular Organism): The general claims about cells, membranes, tissues, interfaces, and molecular machinery are reasonable, but “a cell at one scale can itself be a tissue at a lower scale” is biologically incorrect. Cells are components of tissues, while their lower-level composites are molecular structures, not tissues. This is clearly below the Reference’s factual benchmark. Rating: 5
- PC 4 (Firm): Role interfaces and organizational modularity are plausible, but a team is ordinarily a component of a department, not a department at a lower scale. The recursive mapping therefore confuses the direction of composition, even though the discussion of process changes and coordination failures is sensible. Rating: 5
- PC 5 (Manufactured Product): Components and subassemblies can be treated as modular units, and interface compatibility and defect localization are sound engineering ideas. Still, the claim that a component becomes a subassembly at a lower scale is hierarchically muddled. This is somewhat below the Reference. Rating: 6

#### Beauty
The underlying abstraction is attractive: interfaces hide implementation, composites depend on contracts, and compatible internal change can remain local. The prose is polished and conceptually appealing, but the repeated reversal of the recursive hierarchy damages the elegance of the whole archetype. It is around, or slightly below, the Reference’s level. Rating: 7

#### Intelligence
The submission identifies an important systems principle and explicitly attempts recursion, which is intellectually ambitious. However, the recursion is not correctly instantiated: the supposed lower-level composites are repeatedly assigned as higher-level structures such as tissues, departments, subsystems, or subassemblies. That conceptual error offsets much of the otherwise strong modularity analysis. Rating: 7

#### Domains far apart / metanyms not synonymous
Software, electronics, multicellular biology, firms, and manufactured products are distinct domains, and the metanyms are mostly appropriately domain-specific. Nevertheless, four of the five domains are closely related examples of engineered or organizational modularity, and several mappings reuse nearly identical interface vocabulary. This is approximately comparable to the Reference. Rating: 7

#### Impressive length
The template is substantial and includes interfaces, implementation hiding, composition, change, faults, mismatches, and disciplinary framing. Its length is broadly comparable to the Reference’s templates, though not clearly more impressive in sheer extent. Rating: 7

### Archetypal context 4: Inference from Imperfect Evidence

#### Factually correct (per parallel context)
- PC 1 (Clinical Medicine): The account correctly incorporates differential diagnosis, unequal priors, imperfect tests, false positives and negatives, sequential evidence, test costs, and holistic judgment. It is a particularly accurate and disciplined instantiation. Rating: 8
- PC 2 (Equipment Maintenance): Failure modes, base rates, inspections, false alarms, missed faults, downtime costs, and reliability engineering are all appropriately mapped. The prose is technically credible and slightly stronger than the Reference’s average. Rating: 8
- PC 3 (Cybersecurity): The treatment of alerts, attack scenarios, scans, telemetry, false alerts, missed intrusions, and investigative cost is sound. It captures probabilistic incident assessment without claiming that any one alert is decisive. Rating: 8
- PC 4 (Astronomy): Source models, occurrence rates as priors, observations, measurements, false detections, non-detections, telescope time, and classification are well matched. “Non-detection” is not always exactly a false negative, but it is a valid imperfect-observation analogue. Rating: 8
- PC 5 (Criminal Investigation): The distinction between clues, case theories, forensic examinations, false matches, missed matches, accumulated evidence, and investigative cost is accurate. The formulation is slightly abstract but factually responsible. Rating: 8

#### Beauty
This is one of the submission’s strongest archetypes. The template has a graceful epistemic progression from sign to hypotheses, test design, evidence updating, and judgment. The parallel contexts are concise and avoid strained embellishment, making the whole set more elegant than the Reference’s average. Rating: 8

#### Intelligence
The archetype intelligently combines Bayesian reasoning, diagnostic testing, error rates, sequential updating, and value-of-information considerations. It also warns against over-weighting a single salient observation, which gives the template genuine methodological depth rather than merely a generic “investigation” metaphor. Rating: 8

#### Domains far apart / metanyms not synonymous
Clinical medicine, maintenance engineering, cybersecurity, astronomy, and criminal investigation are notably different epistemic and professional domains. Their metanyms—disease, fault, intrusion, source, and crime, for example—are clearly not synonyms while preserving the same inferential structure. This is clearly stronger than the Reference’s 7-level domain separation. Rating: 8

#### Impressive length
The template contains a full inferential workflow and multiple qualifications, but it is somewhat shorter than the longest Reference templates. It is substantial and well developed, though its length is best judged approximately equal to the Reference. Rating: 7

### Archetypal context 5: Evolutionary Search Through Variation and Selection

#### Factually correct (per parallel context)
- PC 1 (Natural Evolution): The account correctly describes populations, heritable variation, environmental evaluation, selection, adaptation, local optima, and diversity loss. Mutation introduces genetic variation rather than directly introducing phenotypic traits in every case, but the abstraction is defensible. It is slightly better than the Reference overall. Rating: 8
- PC 2 (Crop Breeding): Plant lines, heritable agronomic traits, field evaluation, breeding value, crossing, parent selection, yield plateaus, and germplasm diversity are well matched. Crossing usually recombines existing variation rather than simply introducing new traits, but the statement is acceptable at this level of abstraction. Rating: 8
- PC 3 (Directed Enzyme Evolution): Library diversity, mutagenesis, assay fitness, screening, sequence inheritance, activity peaks, and noisy evaluation are accurately represented. This is a strong domain-expert instantiation. Rating: 8
- PC 4 (Evolutionary Algorithm): The mapping of populations, candidate solutions, encoded traits, objective fitness, mutation, copying, local optima, changing landscapes, and diversity is technically sound. It is slightly more polished than the Reference’s average factual quality. Rating: 8
- PC 5 (Technological Innovation): The evolutionary analogy is coherent, but “heritable” design features and “market selection” are metaphorical rather than literal, and the Form (a) sentence “Innovation studies studies” is an explicit grammatical error. The Form (b) repairs the wording, but the parallel context as submitted is imperfect. Rating: 7

#### Beauty
The archetype has a strong and familiar shape: variation creates options, selection exploits performance, and diversity protects against changing environments and local optima. The five domains are smoothly aligned, though the innovation example is slightly less natural and contains a visible typo. Overall it is modestly more elegant than the Reference. Rating: 8

#### Intelligence
The explicit exploration–exploitation trade-off, changing environments, noisy evaluation, premature convergence, and diversity preservation show substantial conceptual understanding. The template successfully unifies biological evolution, breeding, protein engineering, algorithms, and innovation without reducing the idea to mere “survival of the fittest.” Rating: 8

#### Domains far apart / metanyms not synonymous
Natural evolution, crop breeding, enzyme engineering, evolutionary computation, and technological innovation cover biological, agricultural, biochemical, computational, and socioeconomic settings. They all share unusually close evolutionary vocabulary, but the instantiated entities and evaluation regimes remain distinct. This is slightly better than the Reference’s benchmark. Rating: 8

#### Impressive length
The template is detailed enough to include population structure, evaluation, retention, variation, inheritance, selection, local optima, diversity, environmental change, noise, and disciplinary framing. It is at least as substantial as the Reference’s templates and may be marginally more elaborate. Rating: 8

### Structural diversity across the submitted set
The five archetypes have strongly different system structures: cascading overload through a network, stabilizing feedback around a target, hierarchical modular composition, sequential inference from evidence, and population-level variation and selection. This is a particularly effective set of structural contrasts, although the modular archetype’s recursion is incorrectly realized. Overall the submitted set is somewhat more structurally varied than the Reference’s already diverse collection. Rating: 8

```json
{
  "scores": {
    "Target": {
      "archetypal_contexts": [
        {
          "name": "Cascading Load Redistribution",
          "factual_per_pc": [8, 8, 8, 7, 8],
          "beauty": 8,
          "intelligence": 8,
          "instantiation_distinctness": 7,
          "impressive_length": 7
        },
        {
          "name": "Negative-Feedback Regulation",
          "factual_per_pc": [8, 7, 8, 7, 8],
          "beauty": 8,
          "intelligence": 8,
          "instantiation_distinctness": 8,
          "impressive_length": 7
        },
        {
          "name": "Recursive Modular Composition",
          "factual_per_pc": [6, 6, 5, 5, 6],
          "beauty": 7,
          "intelligence": 7,
          "instantiation_distinctness": 7,
          "impressive_length": 7
        },
        {
          "name": "Inference from Imperfect Evidence",
          "factual_per_pc": [8, 8, 8, 8, 8],
          "beauty": 8,
          "intelligence": 8,
          "instantiation_distinctness": 8,
          "impressive_length": 7
        },
        {
          "name": "Evolutionary Search Through Variation and Selection",
          "factual_per_pc": [8, 8, 8, 8, 7],
          "beauty": 8,
          "intelligence": 8,
          "instantiation_distinctness": 8,
          "impressive_length": 8
        }
      ],
      "structural_diversity": 8
    }
  }
}
```