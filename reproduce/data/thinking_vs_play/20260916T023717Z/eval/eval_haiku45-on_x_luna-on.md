# Evaluation: Target Submission vs. Reference (7/10 baseline)

## Target Submission

### Archetypal context 1: Negative-Feedback Regulation

#### Factually correct (per parallel context)
- PC 1 (Building heating): The thermostat-based heating system with temperature feedback is technically sound. Thermal lag effects and heating gain dynamics are accurate. Rating: 7
- PC 2 (Glucose regulation): The description of beta cells, pancreatic islets, and hormonal feedback is fundamentally correct, but Form (a) awkwardly states that a beta cell "sends a glucose concentration to a pancreatic islet"—beta cells *are* part of islets—which creates factual imprecision. Form (b) recovers well. Rating: 7
- PC 3 (Aircraft altitude control): The altimeter-flight-computer-elevator feedback loop is accurate; control gain and sensor-actuator lag are correctly characterized. Rating: 8
- PC 4 (Spacecraft attitude control): Star-tracker and reaction-wheel dynamics are accurate; light-time delay and torque gain effects are correctly presented. Rating: 8
- PC 5 (Industrial fermentation): Dissolved-oxygen probe feedback, aeration valve control, and measurement delay are factually accurate. Rating: 7

#### Beauty
The template elegantly captures the universal control-loop structure: measurement, comparison, error-driven correction. The instantiations are clean and recognizable. However, the prose lacks some of the rhythmic polish seen in Reference templates (e.g., "Gradient-Guided Navigation," "Containment Breach Cascade"); the language is more functional than lyrical.
Rating: 7

#### Intelligence
The archetype rests on a fundamental insight from control theory: that gain, delay, and measurement accuracy interact to determine stability. The trade-off between strong correction (avoiding persistent deviation) and overshoot (causing oscillation) is mathematically grounded and non-obvious. This compares well to the Reference's sophistication.
Rating: 8

#### Domains far apart / metanyms not synonymous
The five domains span physics (building climate), biology (endocrinology), aeronautics, astronautics, and bioprocess engineering—genuinely distinct fields. Metonyms are sharply differentiated: thermostat vs. beta cell vs. altimeter vs. star tracker vs. oxygen probe. No domain pair is synonymous.
Rating: 8

#### Impressive length
The template is moderate in length (approximately 115 words, 8 slots). Compared to the Reference's "Gradient-Guided Navigation" (9 slots, ~140 words) and "Containment Breach Cascade" (12 slots, ~155 words), this is on the shorter end of the spectrum.
Rating: 7

---

### Archetypal context 2: Service-Queue Accumulation

#### Factually correct (per parallel context)
- PC 1 (Emergency medicine): The ED queue dynamics—arrival rate, treatment rate, triage as scheduling rule—are accurate. The description of capacity saturation and backlog behavior is correct. Rating: 8
- PC 2 (Web infrastructure): Request queueing, compute-worker processing, response latency, database connection pool as bottleneck—all accurate. Load-balancing and rejection behavior are correctly characterized. Rating: 8
- PC 3 (Airport security): Security checkpoint dynamics, passenger arrival, screening rate, and lane assignment are factually sound. Rating: 8
- PC 4 (Civil litigation): Court docket, case filing, judge availability, and priority rules are accurately portrayed. The connection to capacity saturation and case deferral is correct. Rating: 8
- PC 5 (Factory production): Job release, work-in-process buffer, machine utilization, dispatch rules, and lead-time behavior are factually accurate. Rating: 8

#### Beauty
The archetype captures the fundamental nonlinearity of queueing systems—small changes near capacity produce large effects—with mathematical elegance. The five domains are well-matched in structure, making the template feel inevitable and unified. The prose in Form (b) across all five domains is direct and domain-expert in tone.
Rating: 8

#### Intelligence
Queueing theory is sophisticated and counterintuitive: the fact that waiting time grows nonlinearly (often as ~1/(1−load)) as load approaches capacity is not obvious to the untrained intuition. The observation that scheduling rules redistribute delay but cannot eliminate it when arrival exceeds service is profound. This is on par with or exceeds the Reference's sophistication.
Rating: 8

#### Domains far apart / metanyms not synonymous
Domains span healthcare operations, cloud infrastructure, transportation logistics, legal administration, and manufacturing. These are genuinely diverse contexts. Metonyms are distinct: clinical team vs. compute worker vs. screening lane vs. judge vs. machine. No synonymy.
Rating: 8

#### Impressive length
The template is approximately 120 words with 13 slots, placing it in the moderate range. It covers arrival process, queue, server, load, capacity, bottleneck, and scheduling, but is not as expansive as the longest Reference templates.
Rating: 7

---

### Archetypal context 3: Thresholded Admission

#### Factually correct (per parallel context)
- PC 1 (Spam filtering): The spam-filter threshold, false-positive (spam admission), false-negative (legitimate quarantine), and manual review are correctly characterized. Receiver-operating-curve trade-offs are implicit and accurate. Rating: 8
- PC 2 (Border admission): Admissibility standards, passport/visa evidence, false positives (bad actors admitted), false negatives (legitimate travelers refused), and secondary inspection are factually sound. Rating: 8
- PC 3 (Cancer screening): Test result thresholds, disease-risk scores, referral decisions, and the trade-off between unnecessary referrals and missed cases are medically accurate. Rating: 8
- PC 4 (Consumer lending): Default-risk scoring, approval cutoff, false positives (risky loans approved), and false negatives (creditworthy applicants denied) reflect standard lending practice accurately. Rating: 8
- PC 5 (Research grants): Merit scoring, funding cutoff, weak proposals funded vs. strong proposals rejected—accurately represents grant-review dynamics. Rating: 8

#### Beauty
The archetype elegantly captures a fundamental asymmetry: the two types of errors have unequal costs, and threshold selection should reflect this. The template is concise and focused, which lends clarity. However, it is less sweeping or structurally rich than some Reference archetypes; the concept is more narrowly scoped.
Rating: 7

#### Intelligence
The insight that threshold selection involves a value judgment (false-positive vs. false-negative cost trade-off) is important but less mathematically deep than queueing or control theory. The archetype does not delve into ROC curves, Bayes decision theory, or calibration—it remains at the intuitive level. Compared to the Reference's "Competitive Exclusion" or "Debt Accumulation," this is somewhat less sophisticated.
Rating: 7

#### Domains far apart / metanyms not synonymous
Domains span IT security, immigration law, medical diagnosis, financial services, and research administration. Strong diversity. Metonyms (spam filter, border officer, clinician, underwriting model, review panel) are distinct.
Rating: 8

#### Impressive length
The template is approximately 100 words with 12 slots. This is notably more concise than several Reference templates. The brevity serves clarity but comes at the cost of elaboration.
Rating: 6

---

### Archetypal context 4: Depleting Shared Stocks

#### Factually correct (per parallel context)
- PC 1 (Marine fishery): Fish recruitment, catch limits, stock-assessment delays, sustainability thresholds, and stock collapse are accurately portrayed. The description of recruitment overshoot and local extinction is correct. Rating: 8
- PC 2 (Groundwater basin): Aquifer recharge, pumping rates, depletion dynamics, and recovery thresholds are hydrogeologically sound. Rating: 8
- PC 3 (Shared pasture): Plant growth, grazing pressure, pasture degradation, and the tragedy of the commons are accurately described. The connection to Ostrom's commons governance is implicit and correct. Rating: 8
- PC 4 (Irrigation reservoir): Watershed inflow, irrigation release, storage dynamics, drought effects, and conservation-pool levels are accurately characterized. Rating: 8
- PC 5 (Managed forest): Tree growth, sustainable harvest, regeneration density, and the allowable-cut concept are correctly portrayed. Rating: 8

#### Beauty
This is a powerfully thematic archetype. The Tragedy of the Commons is a timeless pattern, and the five domains (fishery, aquifer, pasture, reservoir, forest) are classically resonant instantiations. The language has rhythm and weight; Form (b) passages are vivid and domain-expert. This archetype has considerable aesthetic force.
Rating: 8

#### Intelligence
The archetype distills deep insights from resource economics and institutional theory: that individual incentives can misalign with collective welfare, that feedback delays (stock assessment, drought recognition) exacerbate the problem, and that governance structures (allocation rules, monitoring, sanctions) are essential. The observation that liquidation accelerates once thresholds are crossed is profound. This rivals the Reference's sophistication.
Rating: 8

#### Domains far apart / metanyms not synonymous
The five domains are all natural-resource systems (fishery, aquifer, pasture, irrigation, forest), creating thematic coherence. However, they differ significantly in underlying mechanism (biological recruitment vs. hydrological recharge vs. pastoral plant growth), geography, and user type (fisher vs. well owner vs. herder vs. farming district vs. timber concession). The thematic clustering is stronger than in other Target archetypes, reducing domain separation slightly compared to Service-Queue or Network Cascades.
Rating: 7

#### Impressive length
The template is approximately 140 words with 14 slots, making it one of the most elaborate in the Target submission and comparable to mid-range Reference templates. It includes replenishment, withdrawal, depletion delay, governance mechanisms, recovery thresholds, yield vs. liquidation distinction, and resource economics grounding.
Rating: 8

---

### Archetypal context 5: Network Cascades

#### Factually correct (per parallel context)
- PC 1 (Infectious disease): Contact-network transmission, susceptibility thresholds, effective reproduction number, superspreader roles, household clustering, intervention via vaccination and isolation—all epidemiologically correct. Rating: 8
- PC 2 (Bank run): Depositor networks, withdrawal contagion, confidence thresholds, institutional depositors as amplifiers, regional groups as clusters, liquidity guarantees—all correct in financial-network dynamics. Rating: 8
- PC 3 (Power grid failure): Substation topology, electrical load, relay thresholds, fault propagation, heavily loaded interconnectors, electrical islands, load shedding—all power-systems engineering facts are accurate. Rating: 8
- PC 4 (Computer malware): Device networks, vulnerability thresholds, malware payload, exposed servers as amplifiers, subnets as clusters, patching and isolation interventions—all accurate in cybersecurity. Rating: 8
- PC 5 (Social rumor): Social networks, repeated exposure, credulity thresholds, influencers as amplifiers, online communities as clusters, fact-checking interventions—sociologically sound, though "belief adoption" could be more precisely operationalized. Rating: 8

#### Beauty
The archetype captures the universal phenomenon of cascades—how local spreading can become global—across astonishingly diverse domains. The template is powerful and the instantiations are vivid. The notion that small changes in a highly connected node or growth factor can toggle between local persistence and global cascade is conceptually striking.
Rating: 8

#### Intelligence
Network science and cascade theory are sophisticated. The insight that topology, thresholds, and dynamics interact to determine whether spreading remains localized or propagates globally is non-trivial. The observation that intervention targeting high-contact/central nodes can reduce the growth factor below one is practically and theoretically important. This is on par with the Reference's best archetypes.
Rating: 8

#### Domains far apart / metanyms not synonymous
Domains span epidemiology, financial networks, infrastructure systems, cybersecurity, and computational sociology—genuinely diverse. Metonyms (person, account holder, substation, device, person—though person appears twice, the contexts are distinct) are functionally far from synonymous.
Rating: 8

#### Impressive length
The template is approximately 130 words with 14 slots, making it elaborate and comprehensive. It covers network structure, triggers, transmission, amplifiers, clusters, cascades, intervention, and growth-factor dynamics.
Rating: 8

---

### Structural diversity across the submitted set

The five archetypal contexts span five distinct system structures: (1) feedback loops and error correction (Negative-Feedback Regulation), (2) arrival-service dynamics and queue accumulation (Service-Queue), (3) threshold-based decision-making with asymmetric errors (Thresholded Admission), (4) resource depletion under collective action problems (Depleting Stocks), and (5) cascade dynamics on networks (Network Cascades). These represent genuinely different dynamical systems: regulators, buffers, classifiers, commons, and spreading mechanisms. This diversity matches or exceeds the Reference submission, which includes navigation/optimization, containment/cascades, competition/coexistence, debt/recursion, and scaffolding/assembly. The Target does not feature an explicitly recursive archetype (Debt Accumulation's recursive framing across molecular–cellular–organismal–institutional–civilizational scales is a Reference innovation), but the five systems are nonetheless structurally distinct and complementary.

Rating: 8

---

```json
{
  "scores": {
    "Target": {
      "archetypal_contexts": [
        {
          "name": "Negative-Feedback Regulation",
          "factual_per_pc": [7, 7, 8, 8, 7],
          "beauty": 7,
          "intelligence": 8,
          "instantiation_distinctness": 8,
          "impressive_length": 7
        },
        {
          "name": "Service-Queue Accumulation",
          "factual_per_pc": [8, 8, 8, 8, 8],
          "beauty": 8,
          "intelligence": 8,
          "instantiation_distinctness": 8,
          "impressive_length": 7
        },
        {
          "name": "Thresholded Admission",
          "factual_per_pc": [8, 8, 8, 8, 8],
          "beauty": 7,
          "intelligence": 7,
          "instantiation_distinctness": 8,
          "impressive_length": 6
        },
        {
          "name": "Depleting Shared Stocks",
          "factual_per_pc": [8, 8, 8, 8, 8],
          "beauty": 8,
          "intelligence": 8,
          "instantiation_distinctness": 7,
          "impressive_length": 8
        },
        {
          "name": "Network Cascades",
          "factual_per_pc": [8, 8, 8, 8, 8],
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