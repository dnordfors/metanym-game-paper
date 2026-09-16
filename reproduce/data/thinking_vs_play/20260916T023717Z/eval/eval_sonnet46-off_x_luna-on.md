## Target Submission

### Archetypal context 1: Negative-Feedback Regulation

#### Factually correct (per parallel context)
- PC 1 (Building heating): The description of a thermostat sending readings to a heating controller, with thermal lag causing outdated corrections and gain affecting oscillation, is all accurate. The claim that "too much gain can make the temperature hunt above and below the target" correctly describes limit cycling in proportional controllers. No factual errors detected. Rating: 8
- PC 2 (Glucose regulation): The description of beta cells sensing glucose, the pancreatic islet as controller, hormonal delay, and insulin sensitivity as gain is broadly accurate. Calling the beta cell the "sensor" and the islet the "controller" is a reasonable abstraction. The statement that excessive insulin sensitivity can cause oscillation is physiologically plausible (reactive hypoglycemia). No significant errors. Rating: 8
- PC 3 (Aircraft altitude control): Altimeter as sensor, flight computer as controller, elevator deflection as actuator, and sensor-and-actuator lag are all correct. The description of gain-induced oscillation (phugoid-like behavior) is accurate. No factual errors. Rating: 8
- PC 4 (Spacecraft attitude control): Star tracker as sensor, guidance computer as controller, reaction-wheel torque as actuator, and solar-radiation pressure as disturbance are all correct. Light-time delay is a real concern for deep-space spacecraft. The description of gain-induced oscillation is accurate. No factual errors. Rating: 8
- PC 5 (Industrial fermentation): Oxygen probe as sensor, process controller, aeration-valve opening as actuator, and microbial oxygen demand as disturbance are all accurate. Measurement delay causing control degradation is a well-known issue in bioprocess control. No factual errors. Rating: 8

#### Beauty
The template is clean and well-structured, capturing the essential elements of negative feedback (sensor, controller, actuator, gain, delay) with pleasing symmetry. The five parallel contexts are rendered with consistent elegance, and the Form (b) rewrites are genuinely idiomatic—the glucose and spacecraft versions in particular read naturally in domain-expert prose. However, the template is somewhat spare compared to the Reference's richer narrative texture (e.g., the Reference's gradient-navigation template has more evocative imagery). The beauty is solid but not exceptional. Rating: 7

#### Intelligence
The choice of negative-feedback regulation as an archetype is intellectually sound and the mapping is executed carefully. The identification of gain, delay, and oscillation as the key structural variables is sophisticated. However, negative feedback is perhaps the most canonical control-systems archetype imaginable—it is the textbook example—so the intellectual novelty is limited. The Reference's archetypes (gradient navigation, containment breach, competitive exclusion) show more creative reach. The execution is intelligent but the concept selection is conservative. Rating: 6

#### Domains far apart / metanyms not synonymous
The five domains (building HVAC, endocrinology, aviation, spacecraft, bioprocess) are genuinely distinct and span engineering and biology well. The metanyms are appropriately non-synonymous: "thermostat" vs. "pancreatic beta cell" vs. "altimeter" vs. "star tracker" vs. "oxygen probe" are clearly different objects serving the same structural role. The domain spread is good, though all five are fairly "technical/engineering" in flavor—none ventures into social science, economics, or humanities as the Reference does (career development, market competition, academic disciplines). Rating: 7

#### Impressive length
The template is notably short—nine sentences covering the core feedback loop. The Reference's templates are substantially longer, with more elaborated sub-cases and richer conditional structure. This template is functional but brief, and the parallel contexts, while well-written, are correspondingly compact. Rating: 5

---

### Archetypal context 2: Service-Queue Accumulation

#### Factually correct (per parallel context)
- PC 1 (Emergency medicine): The description of patient flow, triage as scheduling rule, resuscitation bay as bottleneck, and diversion when capacity is exceeded is accurate. The nonlinear relationship between load and waiting time (Little's Law territory) is correctly described. Rating: 8
- PC 2 (Web infrastructure): API gateway, compute workers, database connection pool as bottleneck, and queue memory as buffer are all accurate. The description of latency spikes near capacity is correct. Rating: 8
- PC 3 (Airport security): Screening lanes, passport-control desk as bottleneck, and holding area as buffer are accurate. The description of disproportionate queue growth near capacity is correct. Rating: 8
- PC 4 (Civil litigation): Court docket, judges as servers, specialized courtroom as bottleneck, and docket capacity as buffer are accurate. The description of filing surges causing disproportionate delays is correct. Rating: 8
- PC 5 (Factory production): Work-in-process buffer, machine as server, constrained machine as bottleneck, and dispatch rules are all accurate manufacturing operations concepts. Rating: 8

#### Beauty
The template is well-crafted and the five domains are rendered with consistent quality. The Form (b) rewrites are genuinely idiomatic—the emergency medicine and civil litigation versions in particular feel like authentic domain-expert prose. The structural parallel between a hospital waiting room and a court docket is aesthetically pleasing. However, like the first archetype, the template is somewhat terse and the beauty is competent rather than striking. Rating: 7

#### Intelligence
Queueing theory as an archetype is a smart choice—it is less obvious than feedback control and the nonlinear behavior near capacity (the M/M/1 queue's hyperbolic waiting-time curve) is a genuinely interesting structural feature. The identification of the bottleneck, buffer, and scheduling rule as the key control points shows good understanding. The five domains are well-chosen to illustrate different manifestations. This is slightly more intellectually creative than the feedback archetype. Rating: 7

#### Domains far apart / metanyms not synonymous
Emergency medicine, web infrastructure, airport security, civil litigation, and factory production are genuinely diverse. The metanyms are non-synonymous: "clinical team" vs. "compute worker" vs. "screening lane" vs. "judge" vs. "machine" are clearly different. The spread includes both physical and informational systems, and both human-service and automated contexts. This is comparable to the Reference. Rating: 7

#### Impressive length
The template is again relatively short—eight sentences. The Reference's templates are longer and more elaborated. This is a consistent weakness across the submission. Rating: 5

---

### Archetypal context 3: Thresholded Admission

#### Factually correct (per parallel context)
- PC 1 (Spam filtering): The description of feature extraction, score comparison with cutoff, false positives/negatives, and the trade-off from threshold adjustment is accurate. Manual review as override is correct. Rating: 8
- PC 2 (Border admission): The description of passport/visa as evidence, admissibility score, secondary inspection as review, and the trade-off between inadmissible admissions and admissible refusals is accurate. Rating: 8
- PC 3 (Cancer screening): The description of test results, referral cutoff, unnecessary referrals vs. missed referrals, confirmatory testing, and the threshold trade-off is accurate and well-grounded in medical screening literature. Rating: 8
- PC 4 (Consumer lending): Default-risk score, approval cutoff, underwriting model, human review, and the trade-off between risky approvals and creditworthy denials are all accurate. Rating: 8
- PC 5 (Research grants): Merit score, funding cutoff, reviewer disagreement as noise, applicant rebuttal as review, and the trade-off between weak awards and strong rejections are all accurate. Rating: 8

#### Beauty
The template is elegant in its simplicity—the false-positive/false-negative trade-off is a beautiful structural duality, and the five domains instantiate it cleanly. The Form (b) rewrites are consistently idiomatic. The cancer screening and research grants versions are particularly well-rendered. The archetype has a pleasing logical symmetry. Rating: 7

#### Intelligence
Signal detection theory / statistical decision theory as an archetype is a smart choice. The identification of noise, threshold, and asymmetric error costs as the key structural variables is sophisticated. The five domains are well-chosen to span very different consequence structures (missing cancer vs. funding a weak proposal). This is intellectually solid. Rating: 7

#### Domains far apart / metanyms not synonymous
Spam filtering, border control, cancer screening, consumer lending, and research grants are genuinely diverse domains spanning computer science, law enforcement, medicine, finance, and academia. The metanyms are non-synonymous: "classifier" vs. "border officer" vs. "clinician" vs. "underwriting model" vs. "review panel" are clearly different. This is good domain diversity. Rating: 8

#### Impressive length
The template is again short—eight sentences. This is a consistent pattern across the submission and represents a clear weakness relative to the Reference. Rating: 5

---

### Archetypal context 4: Depleting Shared Stocks

#### Factually correct (per parallel context)
- PC 1 (Marine fishery): Fish recruitment, harvest, spawning biomass threshold, and the role of delayed stock assessments are all accurate. The description of sustainable yield vs. stock collapse is correct. Rating: 8
- PC 2 (Groundwater basin): Aquifer recharge, pumping, minimum aquifer level, and delayed water-level measurement are all accurate. The description of sustainable extraction vs. depletion is correct. Rating: 8
- PC 3 (Shared pasture): Forage biomass, plant growth, livestock grazing, stocking limits, and seasonal grazing lag are all accurate. The description of pasture degradation is correct. Rating: 8
- PC 4 (Irrigation reservoir): Watershed inflow, irrigation release, conservation pool, and delayed drought recognition are all accurate. The description of reservoir exhaustion is correct. Rating: 8
- PC 5 (Managed forest): Standing timber, tree growth, timber harvest, annual allowable cut, and forest-inventory lag are all accurate. The description of clear-cut liquidation vs. sustainable yield is correct. Rating: 8

#### Beauty
This is the strongest archetype in the submission aesthetically. The commons-dilemma structure is rich and the five domains (fishery, aquifer, pasture, reservoir, forest) are all natural-resource systems that feel genuinely parallel. The Form (b) rewrites are consistently excellent—the fishery and groundwater versions in particular read like authentic resource-economics prose. The depletion delay as a structural feature is an elegant addition. Rating: 8

#### Intelligence
The commons/common-pool resource archetype is intellectually rich, drawing on Ostrom's work and resource economics. The identification of the depletion delay as a key structural variable (hiding decline until it is too late) is a sophisticated insight. The recovery threshold adds further depth. This is the most intellectually impressive archetype in the submission. Rating: 8

#### Domains far apart / metanyms not synonymous
Marine fishery, groundwater basin, shared pasture, irrigation reservoir, and managed forest are all natural-resource systems—they are genuinely parallel but also somewhat clustered in the same broad domain (natural resource management). The metanyms are non-synonymous ("fisher" vs. "well owner" vs. "herder" vs. "farming district" vs. "timber concession"), but the domain spread is narrower than the Reference's archetypes, which span biology, engineering, economics, and social science. Rating: 6

#### Impressive length
The template is again short—eight sentences. This is the consistent weakness of the submission. Rating: 5

---

### Archetypal context 5: Network Cascades

#### Factually correct (per parallel context)
- PC 1 (Infectious disease): Contact network, superspreader, household clustering, effective reproduction number, and the role of vaccination/isolation are all accurate. The description of threshold-based infection is correct. Rating: 8
- PC 2 (Bank run): Depositor network, institutional depositors as amplifiers, regional depositor groups as clusters, liquidity guarantee as intervention, and withdrawal propagation ratio are all accurate. Rating: 8
- PC 3 (Power grid failure): Substations, transmission lines, relay threshold, protective tripping, load shedding, and outage branching factor are all accurate power-systems concepts. Rating: 8
- PC 4 (Computer malware): Device network, vulnerability threshold, exposed server as amplifier, subnet as cluster, patching/isolation as intervention, and effective infection rate are all accurate. Rating: 8
- PC 5 (Social rumor): Social network, credulity threshold, influencer as amplifier, online community as cluster, fact-checking as intervention, and sharing ratio are all accurate. Rating: 8

#### Beauty
The network cascade archetype is well-executed and the five domains are rendered with consistent quality. The Form (b) rewrites are idiomatic. The structural parallel between an epidemic and a bank run is aesthetically pleasing and intellectually satisfying. The identification of the growth factor (R-number equivalent) as the key control variable across all five domains is elegant. Rating: 8

#### Intelligence
Network cascade theory is a sophisticated archetype. The identification of amplifiers, clusters, growth factor, and intervention timing as the key structural variables shows deep understanding of network dynamics. The five domains are well-chosen to span biological, financial, physical, digital, and social systems. The growth factor concept (effective reproduction number, withdrawal propagation ratio, outage branching factor) is a particularly intelligent unifying variable. Rating: 8

#### Domains far apart / metanyms not synonymous
Infectious disease, bank run, power grid failure, computer malware, and social rumor are genuinely diverse domains spanning epidemiology, finance, engineering, cybersecurity, and social science. The metanyms are non-synonymous: "superspreader" vs. "institutional depositor" vs. "heavily loaded interconnector" vs. "exposed server" vs. "influencer" are clearly different. This is excellent domain diversity. Rating: 8

#### Impressive length
The template is again short—eight sentences. This is the consistent weakness across all five archetypes. Rating: 5

---

### Structural diversity across the submitted set

The five archetypes—negative feedback, queue accumulation, threshold classification, stock depletion, and network cascade—are genuinely structurally distinct. Negative feedback is a continuous regulatory loop; queue accumulation is a flow-and-inventory system; threshold classification is a binary decision process; stock depletion is a commons-governance problem; network cascade is a propagation-on-graph problem. These five system structures are meaningfully different from one another and cover a good range of dynamical archetypes. The Reference's five archetypes (gradient navigation, containment breach, competitive exclusion, debt accumulation, scaffold assembly) are also structurally diverse, and the Reference additionally includes a recursive archetype (debt accumulation) with explicit nested-scale demonstration. The Target submission explicitly disclaims recursion. The structural diversity of the Target is comparable to the Reference, perhaps slightly better in that the five structures are more cleanly orthogonal (feedback, queue, threshold, stock, cascade are well-separated concepts), but the absence of any recursive structure and the consistent brevity of templates slightly reduces the overall impression. Rating: 8

---

```json
{
  "scores": {
    "Target": {
      "archetypal_contexts": [
        {
          "name": "Negative-Feedback Regulation",
          "factual_per_pc":           [8, 8, 8, 8, 8],
          "beauty":                   7,
          "intelligence":             6,
          "instantiation_distinctness": 7,
          "impressive_length":        5
        },
        {
          "name": "Service-Queue Accumulation",
          "factual_per_pc":           [8, 8, 8, 8, 8],
          "beauty":                   7,
          "intelligence":             7,
          "instantiation_distinctness": 7,
          "impressive_length":        5
        },
        {
          "name": "Thresholded Admission",
          "factual_per_pc":           [8, 8, 8, 8, 8],
          "beauty":                   7,
          "intelligence":             7,
          "instantiation_distinctness": 8,
          "impressive_length":        5
        },
        {
          "name": "Depleting Shared Stocks",
          "factual_per_pc":           [8, 8, 8, 8, 8],
          "beauty":                   8,
          "intelligence":             8,
          "instantiation_distinctness": 6,
          "impressive_length":        5
        },
        {
          "name": "Network Cascades",
          "factual_per_pc":           [8, 8, 8, 8, 8],
          "beauty":                   8,
          "intelligence":             8,
          "instantiation_distinctness": 8,
          "impressive_length":        5
        }
      ],
      "structural_diversity": 8
    }
  }
}
```