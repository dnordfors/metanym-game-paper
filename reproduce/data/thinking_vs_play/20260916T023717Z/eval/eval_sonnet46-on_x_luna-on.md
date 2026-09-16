## Target Submission

### Archetypal context 1: Negative-Feedback Regulation

#### Factually correct (per parallel context)
- PC 1 (Building heating): The description is factually clean: thermostat as sensor, heating controller as decision element, burner output as actuator, thermal lag as a genuine delay mechanism. All propositions are accurate and the Form (b) rewrite correctly introduces thermal inertia. Comparable to the Reference in accuracy. Rating: 7
- PC 2 (Glucose regulation): The broad outline is correct, but "a pancreatic beta cell sends a glucose concentration to a pancreatic islet" is awkward: beta cells are constituent members of the islet, not upstream reporters to it. The islet does coordinate paracrine feedback (alpha cells, delta cells), so the framing is defensible, but it strains biological accuracy slightly more than the Reference's parallel contexts do. Rating: 6
- PC 3 (Aircraft altitude control): All propositions are accurate. Altimeter as sensor, flight computer as controller, elevator deflection as actuator, and sensor-actuator lag as the delay mechanism are all standard flight-control engineering. Form (b) clarifies clearly. Comparable to the Reference. Rating: 7
- PC 4 (Spacecraft attitude control): Accurate and notably specific—star tracker, reaction-wheel torque, solar-radiation pressure as disturbance, and light-time plus computation delay are all correct elements of spacecraft attitude control, especially for deep-space missions. Slightly more domain-precise than most Reference PCs. Rating: 8
- PC 5 (Industrial fermentation): Accurate throughout. Dissolved oxygen controlled by aeration-valve opening, oxygen probe as sensor, process controller, and measurement delay are all standard in bioprocess engineering. Form (b) adds biological context (microbial demand). Rating: 7

#### Beauty
The template prose is crisp and logically sequenced, capturing the gain-instability-delay triangle of control theory in compact sentences. However, the language is more textbook than evocative, and the Form (b) rewrites, while fluent, rarely rise above technical paraphrase. The Reference's Gradient-Guided Navigation template had analogous discipline but slightly richer imagery ("stall, oscillate, or become trapped in local attractors" resonates across scales). The Target is comparable in functional elegance, not quite matching the Reference in expressive texture.
Rating: 7

#### Intelligence
Representing control theory through a five-slot sensor–controller–actuator pipeline is intellectually correct, and the gain/delay instability insight is genuine. However, four of the five domains chosen (building, aircraft, spacecraft, fermentation) are all engineered closed-loop systems that share very similar internal structure. The biological domain (glucose regulation) is the only conceptual departure. The Reference's analogous archetypes tended to span more structurally distinct manifestations of their abstract principle. The archetype is competently executed but not as intellectually surprising as the best Reference archetypes.
Rating: 6

#### Domains far apart / metanyms not synonymous
This is the clearest weakness of this archetype. Building heating, aircraft altitude control, spacecraft attitude control, and industrial fermentation are all engineered feedback-control systems; glucose regulation is biological but structurally identical. As a result, the metanyms converge: "heating gain," "control gain," "torque gain," and "controller gain" are nearly synonymous, and "thermal lag," "sensor-and-actuator lag," "measurement delay," and "hormonal delay" differ only terminologically. The Reference archetypes (e.g., chemotaxis–gradient descent–career development–ant foraging) achieved far greater semantic distance. This is noticeably below the Reference standard.
Rating: 4

#### Impressive length
The template runs approximately 110 words across nine sentences with 13 slots—shorter in word count than all five Reference templates, which ranged from roughly 130 to 190 words. The Form (a) and (b) instances are correspondingly compact. While the 13-slot table is reasonable, the template's sentences are brief and do not elaborate on secondary consequences the way the Reference templates did (e.g., the "Some [NAVIGATOR] emit their own [SIGNAL]" clause adds genuine complexity). Below the Reference benchmark on this criterion.
Rating: 6

---

### Archetypal context 2: Service-Queue Accumulation

#### Factually correct (per parallel context)
- PC 1 (Emergency medicine): Accurate. Waiting room, clinical team, triage, resuscitation bay as bottleneck, and diversion when treatment space is exhausted are all consistent with emergency-department operations research. "Patient acuity load" is nonstandard terminology for utilization but captures the concept. Rating: 7
- PC 2 (Web infrastructure): Accurate. The database connection pool as a common bottleneck, queue memory limits, and the nonlinear relationship between traffic intensity and latency near capacity are all standard in performance engineering. Rating: 7
- PC 3 (Airport security): Accurate. Screening lanes, passport-control desk as downstream bottleneck, and the holding-area constraint are factually sound. The arrival-burst-to-queue-length nonlinearity is correctly stated. Rating: 7
- PC 4 (Civil litigation): Accurate. Court dockets, adjudication rates, and specialized courtrooms as bottlenecks are well-known features of court administration. Priority rules shifting delay without eliminating it is correct. Rating: 7
- PC 5 (Factory production): Accurate. Work-in-process buffers, constrained machines, dispatch rules, and the nonlinear utilization-to-leadtime relationship are all standard manufacturing operations research concepts (Theory of Constraints, Little's Law). Rating: 7

#### Beauty
The template is logically tight, correctly capturing the nonlinear surge behavior near capacity saturation. The phrase "small bursts in arrivals produce disproportionate increases in waiting time and backlog" is an elegant one-sentence summary of the M/M/1 heavy-traffic phenomenon. Form (b) rewrites are readable and domain-appropriate. Slightly formulaic in structure but well-crafted. Comparable to the Reference.
Rating: 7

#### Intelligence
Queueing theory is a genuine and underused conceptual lens, and the archetype successfully imports Little's Law, utilization-vs-delay nonlinearity, bottleneck identification, and scheduling-rule limitations into a unified template. The insight that scheduling rules redistribute but cannot eliminate persistent overload is particularly well-articulated. Comparable to the Reference's better archetypes in analytical depth.
Rating: 7

#### Domains far apart / metanyms not synonymous
The five domains—emergency medicine, web infrastructure, airport security, civil litigation, factory production—span healthcare, computing, transportation, law, and manufacturing, which is genuinely diverse. Metanyms diverge meaningfully: "acuity triage" vs. "load-balancing policy" vs. "lane-assignment rule" vs. "case-priority rule" vs. "dispatch rule" are related but not synonymous, and the bottlenecks (resuscitation bay, database connection pool, passport-control desk, specialized courtroom, constrained machine) are quite distinct objects. On par with the Reference.
Rating: 7

#### Impressive length
The template runs approximately 130 words with 14 slots. This is close to the shorter Reference templates (Scaffold-Dependent Assembly was ~130 words) but below the longer ones. The table is well-populated. Form (a) and (b) instances are appropriately developed. Comparable to the midpoint of the Reference range.
Rating: 7

---

### Archetypal context 3: Thresholded Admission

#### Factually correct (per parallel context)
- PC 1 (Spam filtering): Accurate. False positive (ham classified as spam) and false negative (spam in inbox) are correctly distinguished. Manual review overriding classifier decisions is a real practice. The threshold–error-rate trade-off is correctly stated. Rating: 7
- PC 2 (Border admission): Accurate. Secondary inspection as a review mechanism, the trade-off between inadmissible admissions and admissible refusals at different proof standards, and document ambiguity as noise are all correct. Rating: 7
- PC 3 (Cancer screening): Accurate. The referral cutoff, unnecessary referral (false positive), missed referral (false negative), confirmatory testing as a review step, and the asymmetric cost argument for threshold setting are all correct and clinically appropriate. Rating: 7
- PC 4 (Consumer lending): Accurate. Default-risk scoring, underwriting model, human underwriting review as an override mechanism, and the creditworthy-denial vs. risky-approval trade-off are all standard in credit-risk practice. Rating: 7
- PC 5 (Research grants): Accurate. Merit scoring, review-panel decisions, applicant rebuttal as a review step, and the weak-proposal-funded vs. strong-proposal-rejected trade-off are all realistic representations of grant evaluation. Rating: 7

#### Beauty
The template efficiently encodes signal detection theory's core structure: evidence extraction, threshold comparison, binary assignment, noise, two error types, review, and the threshold trade-off, plus the asymmetric-cost motivation. The symmetry of false positive and false negative within a single template sentence is elegant. Form (b) rewrites are concise and natural. Comparable to the Reference.
Rating: 7

#### Intelligence
Signal detection theory as an archetypal context is a sophisticated and underused lens. The recognition that the same threshold-trade-off logic governs spam filters, border control, medical screening, lending, and grant panels is a genuinely non-obvious intellectual insight. The archetype correctly identifies that [FIELD] studies the optimal threshold under asymmetric error costs—a real and important research question in all five domains. Slightly above the Reference on intelligence.
Rating: 8

#### Domains far apart / metanyms not synonymous
Spam filtering (computational), border admission (governmental security), cancer screening (medical), consumer lending (financial), research grants (academic)—these span five distinct institutional spheres. Metanyms differ meaningfully: "classifier" vs. "border officer" vs. "clinician" vs. "underwriting model" vs. "review panel" are genuinely distinct decision-making entities. "Adversarial wording" vs. "document ambiguity" vs. "measurement error" vs. "missing financial data" vs. "reviewer disagreement" are distinct noise mechanisms. On par with the Reference's better domain-diversity examples.
Rating: 7

#### Impressive length
The template is approximately 100 words—the shortest among the Target's five templates and noticeably shorter than all Reference templates. While the 13-slot table is adequate, the template sentences are lean and do not introduce secondary dynamics the way the Reference templates did. This is a clear shortcoming on this criterion relative to the Reference.
Rating: 5

---

### Archetypal context 4: Depleting Shared Stocks

#### Factually correct (per parallel context)
- PC 1 (Marine fishery): Accurate. Minimum spawning biomass as a recovery threshold, delayed stock assessments as the informational lag, and the distinction between sustainable catch and stock collapse are all correct fisheries science. Rating: 7
- PC 2 (Groundwater basin): Accurate. Delayed water-level measurements, minimum aquifer levels, and the distinction between sustainable extraction and aquifer depletion are all correct hydrogeology. The slow or uncertain recharge of depleted aquifers (especially fossil aquifers) is correctly flagged. Rating: 8
- PC 3 (Shared pasture): Accurate. Seasonal grazing lags, minimum ground-cover thresholds for range recovery, and the stocking-limit mechanism are all correct range management. The archetype directly maps the classic commons structure. Rating: 7
- PC 4 (Irrigation reservoir): Accurate. Conservation-pool level as a recovery threshold, delayed drought recognition, and the distinction between reliable yield and exhaustion are all correct reservoir operations. Rating: 7
- PC 5 (Managed forest): Accurate. Annual allowable cut vs. clear-cut liquidation, minimum regeneration density as a threshold, and forest-inventory lags are all correct forestry management concepts. Rating: 7

#### Beauty
The template captures the tragedy-of-commons structure with clean precision: individual incentive divergence, depletion delay, governance response, recovery threshold, and the sustainable-yield vs. liquidation distinction all appear in a compressed but complete narrative. Form (b) rewrites are fluent and domain-appropriate, sometimes improving on (a) (the fishery Form (b) is particularly clean). Comparable to the Reference.
Rating: 7

#### Intelligence
Ostrom-style common-pool resource theory is a genuine and important intellectual framework, and the template correctly represents its key structural elements: stock, replenishment, withdrawal, depletion lag, governance triad (monitoring–allocation–sanction), recovery threshold, and the sustainable-yield/liquidation distinction. The parallel between fish, water, pasture, water (again), and timber is well-structured. Slightly above the Reference on intelligence for correctly identifying governance as a composite of three distinct mechanisms.
Rating: 7

#### Domains far apart / metanyms not synonymous
This is the most significant weakness in the entire submission. All five domains are natural-resource commons: marine fishery, groundwater basin, shared pasture, irrigation reservoir, managed forest. They differ in substrate but share almost identical institutional and ecological structures. The metanyms reflect this: "fish harvest," "groundwater pumping," "livestock grazing," "irrigation release," and "timber harvest" are all extraction activities that are nearly synonymous at the abstract level. "Fish recruitment," "aquifer recharge," "plant growth," "watershed inflow," and "tree growth" are all replenishment processes that differ only in substrate. The Reference maintained much greater domain diversity even within thematically related archetypes. This is substantially below the Reference.
Rating: 3

#### Impressive length
The template runs approximately 120 words with 14 slots. This is in the lower range of Reference templates but not far below the median. The distinction between sustainable yield and liquidation, and the governance triad, add structural complexity that partially compensates for shorter prose. Slightly below the Reference median.
Rating: 6

---

### Archetypal context 5: Network Cascades

#### Factually correct (per parallel context)
- PC 1 (Infectious disease): Accurate and precise. Superspreader as high-degree amplifier, household as clustering unit, effective reproduction number, and the threshold condition R < 1 from targeted intervention are all correct epidemiology. Rating: 8
- PC 2 (Bank run): Accurate in substance. The propagation of withdrawal behavior through depositor networks, institutional depositors as amplifiers, and liquidity guarantees as interventions targeting the propagation ratio are all correct. The phrasing "a withdrawal request can move from one account holder to another" is slightly mechanically awkward but not factually wrong. Rating: 7
- PC 3 (Power grid failure): Accurate. Protective relay trips as the state change, relay thresholds, heavily loaded interconnectors as amplifiers, electrical islands as clustering units, load shedding as intervention, and the outage branching factor as the growth measure are all correct power-systems engineering. Rating: 7
- PC 4 (Computer malware): Accurate. Vulnerability thresholds, exposed servers as amplifiers, subnets as clusters, patching and isolation as interventions, and effective infection rate are all correct cybersecurity concepts. Rating: 7
- PC 5 (Social rumor): Accurate. Credulity threshold, influencers as amplifiers, online communities as clustering units, fact-checking as intervention, and sharing ratio as the growth factor are all conceptually sound. The repeated-claim framing for exposure is appropriate. Rating: 7

#### Beauty
The template compresses network cascade theory into a single coherent paragraph that correctly identifies nodes, links, triggers, thresholds, transmission, amplification, clustering, cascades, interventions, and growth factors. The sentence "Once a [CASCADE] begins, targeted [INTERVENTION] at a [TARGET] can lower the effective [GROWTH FACTOR] below one" is particularly elegant—the threshold-crossing at 1 is a unifying mathematical insight across all five domains. Form (b) rewrites are fluent and suitably technical. Slightly above the Reference average on beauty.
Rating: 7

#### Intelligence
The archetype successfully unifies epidemic SIR dynamics, bank run contagion, grid-fault propagation, malware diffusion, and social information cascades under a single network-theoretic template. The identification of "growth factor" as the unifying threshold quantity (R₀ in epidemiology, branching factor in grid failures, sharing ratio in social networks) is a genuinely non-obvious intellectual insight that spans multiple disciplines. The amplifier/cluster distinction (degree heterogeneity vs. community structure) is also conceptually precise. Above the Reference on intelligence.
Rating: 8

#### Domains far apart / metanyms not synonymous
Infectious disease (public health/biology), bank run (finance), power grid failure (electrical engineering), computer malware (cybersecurity), social rumor (social science/computational sociology)—five genuinely distinct domains spanning biological, financial, physical, digital, and social systems. Metanyms diverge substantially: "superspreader" vs. "institutional depositor" vs. "heavily loaded interconnector" vs. "exposed server" vs. "influencer" are distinct real-world entities. "Vaccination and isolation" vs. "liquidity guarantee" vs. "load shedding" vs. "patching and isolation" vs. "fact-checking" are meaningfully different interventions. Above the Reference on this criterion.
Rating: 8

#### Impressive length
The template runs approximately 130 words with 15 slots—the most slots of any Target archetype and comparable to the mid-length Reference templates. The Form (a) and (b) instances are fully developed. Comparable to the Reference median.
Rating: 7

---

### Structural diversity across the submitted set

The five archetypes represent five genuinely distinct dynamical systems: closed-loop negative feedback (archetype 1), queue accumulation with nonlinear congestion (archetype 2), binary threshold classification with error-type trade-offs (archetype 3), stock depletion under commons incentive structures (archetype 4), and network cascade propagation with growth-factor thresholds (archetype 5). These five abstract structures are logically independent and do not reduce to one another: feedback regulation is not queuing, queuing is not classification, classification is not depletion, and depletion is not network propagation. The coverage spans control theory, operations research, statistical decision theory, resource economics, and network science—five distinct scientific disciplines. The Reference achieved comparable structural diversity across its five archetypes, though it benefited additionally from an explicitly recursive archetype (Debt Accumulation) that added a nested-scale dimension the Target lacks. The Target's diversity is genuine and well-articulated, landing slightly above the Reference.
Rating: 8

---

```json
{
  "scores": {
    "Target": {
      "archetypal_contexts": [
        {
          "name": "Negative-Feedback Regulation",
          "factual_per_pc":           [7, 6, 7, 8, 7],
          "beauty":                   7,
          "intelligence":             6,
          "instantiation_distinctness": 4,
          "impressive_length":        6
        },
        {
          "name": "Service-Queue Accumulation",
          "factual_per_pc":           [7, 7, 7, 7, 7],
          "beauty":                   7,
          "intelligence":             7,
          "instantiation_distinctness": 7,
          "impressive_length":        7
        },
        {
          "name": "Thresholded Admission",
          "factual_per_pc":           [7, 7, 7, 7, 7],
          "beauty":                   7,
          "intelligence":             8,
          "instantiation_distinctness": 7,
          "impressive_length":        5
        },
        {
          "name": "Depleting Shared Stocks",
          "factual_per_pc":           [7, 8, 7, 7, 7],
          "beauty":                   7,
          "intelligence":             7,
          "instantiation_distinctness": 3,
          "impressive_length":        6
        },
        {
          "name": "Network Cascades",
          "factual_per_pc":           [8, 7, 7, 7, 7],
          "beauty":                   7,
          "intelligence":             8,
          "instantiation_distinctness": 8,
          "impressive_length":        7
        }
      ],
      "structural_diversity": 8
    }
  }
}
```