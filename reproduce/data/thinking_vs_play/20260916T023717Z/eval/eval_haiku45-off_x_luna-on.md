# Scoring the Target Submission

## Target Submission

### Archetypal context 1: Negative-Feedback Regulation

#### Factual correct (per parallel context)
- PC 1 (Building heating): The description of thermostat-based heating control is factually sound. Thermostats measure temperature, controllers apply negative feedback, and thermal lag is a real phenomenon that can cause oscillation. The mapping of GAIN to "heating gain" and DELAY to "thermal lag" is physically accurate. Rating: 8

- PC 2 (Glucose regulation): The glucose homeostasis description is accurate. Beta cells do sense glucose, pancreatic islets coordinate hormonal response, and insulin sensitivity is a real parameter. The mention of oscillation around setpoint reflects actual glucose dynamics. However, the phrasing "pancreatic beta cell does not alter blood glucose directly; it sends a glucose concentration to a pancreatic islet" is slightly awkward—beta cells *are* part of the islet—but the functional description remains correct. Rating: 7

- PC 3 (Aircraft altitude control): The altitude control system description is factually correct. Altimeters measure altitude, flight computers apply feedback via elevator deflection, and sensor-actuator lag is a genuine source of instability. The control-theoretic principles are sound. Rating: 8

- PC 4 (Spacecraft attitude control): The attitude control description is accurate. Star trackers measure orientation, guidance computers command reaction wheels, and light-time delay is a real constraint in spacecraft control. The description of pointing error and torque gain is correct. Rating: 8

- PC 5 (Industrial fermentation): The dissolved-oxygen control description is factually accurate. Oxygen probes measure DO, process controllers adjust aeration valves, and measurement delay is a real phenomenon in fermentation control. The mapping is sound. Rating: 8

#### Beauty
The template is elegant in its abstraction of the feedback-control principle. The parallel contexts span genuinely different scales and domains—from molecular biology to aerospace—yet all instantiate the same core structure. The Form (b) rewrites are particularly polished, using domain-expert language naturally. The template itself is concise and captures the essential tension between gain and delay. However, compared to the Reference's "Gradient-Guided Navigation," which has a more narrative flow and richer causal language ("stall, oscillate, become trapped"), this template is more mechanistic and less evocative. Rating: 7

#### Intelligence
The archetype demonstrates solid understanding of control theory and its universality. The insight that GAIN and DELAY create a fundamental trade-off is well-chosen. However, the template does not explore deeper phenomena like integral windup, nonlinear saturation, or adaptive control—concepts that would elevate the intellectual depth. The Reference's "Gradient-Guided Navigation" goes further by incorporating memory, noise filtering, and collective behavior. This archetype is competent but less intellectually ambitious. Rating: 6

#### Domains far apart / metanyms not synonymous
The five domains are reasonably well separated: building climate control, endocrine physiology, aerospace engineering, spacecraft dynamics, and bioprocess engineering. However, the metanyms are somewhat close to synonymous across domains. For example, SENSOR/MEASUREMENT/FEEDBACK are nearly identical concepts in all five contexts—they all involve measuring a variable and comparing it to a setpoint. GAIN and DELAY are also quite parallel. The Reference's "Gradient-Guided Navigation" achieves greater semantic distance: "chemoreceptor" vs. "proprioception" vs. "network contact" vs. "backpropagation" vs. "antenna" are more genuinely distinct. Rating: 6

#### Impressive length
The template is moderately long (approximately 90 words) and covers the essential elements: measurement, comparison, deviation, actuator, gain, delay, and control theory. It is comparable in length to the Reference's templates. However, it does not explore secondary phenomena (e.g., integral action, saturation, adaptive tuning) that would extend it. Rating: 7

### Archetypal context 2: Service-Queue Accumulation

#### Factual correct (per parallel context)
- PC 1 (Emergency medicine): The description of ED queueing is factually sound. Patients arrive, wait in the waiting room, and are served by clinical teams at a treatment rate. Acuity triage is a real scheduling rule. The trade-off between utilization and waiting time is correct. Rating: 8

- PC 2 (Web infrastructure): The API queueing description is accurate. Requests arrive, queue, and are processed by workers. Load balancing and queue memory are real phenomena. The description of latency and backlog is correct. Rating: 8

- PC 3 (Airport security): The security checkpoint description is factually accurate. Passengers arrive, queue, and are screened. Lane assignment and holding areas are real. The trade-off between utilization and screening time is sound. Rating: 8

- PC 4 (Civil litigation): The court docket description is factually reasonable. Cases arrive, are docketed, and are adjudicated by judges. Priority rules and docket capacity are real. However, the analogy is somewhat strained—courts do not have a single "service rate" in the same way a machine does, and the dynamics are more complex. Rating: 6

- PC 5 (Factory production): The production cell description is factually accurate. Jobs arrive, queue in WIP, and are completed by machines. Dispatch rules and buffer stock are real. The description of lead time and utilization is sound. Rating: 8

#### Beauty
The template is clean and captures the essential queueing principle. The parallel contexts are well-chosen and span different sectors. The Form (b) rewrites are natural and domain-appropriate. However, the template is somewhat mechanical and lacks the narrative richness of the Reference's "Containment Breach Cascade," which has a more dramatic arc (breach → cascade → failure). This archetype is competent but less aesthetically compelling. Rating: 7

#### Intelligence
The archetype demonstrates solid understanding of queueing theory and its universality. The insight that utilization, delay, and capacity form a fundamental trade-off is well-chosen. However, the template does not explore more sophisticated phenomena like priority queues with different service distributions, abandonment, or network effects. The Reference's "Competitive Exclusion and Niche Partitioning" goes deeper by incorporating stabilizing mechanisms and fitness differences. Rating: 6

#### Domains far apart / metanyms not synonymous
The five domains are reasonably separated: healthcare, web services, transportation, law, and manufacturing. However, the metanyms are quite parallel and nearly synonymous. QUEUE, SERVER, SERVICE RATE, WAITING TIME, and BACKLOG are nearly identical concepts across all five contexts. The Reference's "Depleting Shared Stocks" achieves greater semantic distance: "fish biomass" vs. "groundwater storage" vs. "forage biomass" vs. "stored water" vs. "standing timber" are more genuinely distinct. Rating: 5

#### Impressive length
The template is moderately long (approximately 85 words) and covers the essential elements: arrival, queue, server, service rate, load, capacity, waiting time, backlog, scheduling rule, bottleneck, buffer, and queueing theory. It is comparable to the Reference's templates. However, it does not explore secondary phenomena (e.g., abandonment, reneging, priority classes) that would extend it. Rating: 7

### Archetypal context 3: Thresholded Admission

#### Factual correct (per parallel context)
- PC 1 (Spam filtering): The spam filter description is factually accurate. Filters score messages, compare with a cutoff, and classify as spam or legitimate. Adversarial wording can cause false positives and false negatives. Manual review is a real process. Rating: 8

- PC 2 (Border admission): The border control description is factually sound. Officers evaluate documents, compare with standards, and admit or refuse. Document ambiguity can cause errors. Secondary inspection is a real process. Rating: 8

- PC 3 (Cancer screening): The screening program description is factually accurate. Tests estimate disease risk, compare with a cutoff, and refer or not refer. Measurement error can cause false positives and false negatives. Confirmatory testing is a real process. Rating: 8

- PC 4 (Consumer lending): The lending description is factually accurate. Lenders derive risk scores, compare with a cutoff, and approve or deny. Missing data can cause errors. Human review is a real process. Rating: 8

- PC 5 (Research grants): The grant selection description is factually sound. Panels evaluate proposals, compare merit scores with a cutoff, and fund or reject. Reviewer disagreement can cause errors. Rebuttal is a real process. Rating: 8

#### Beauty
The template is elegant and captures the essential threshold-decision principle. The parallel contexts are well-chosen and span very different domains. The Form (b) rewrites are natural and domain-appropriate. The template has a clear narrative arc: measurement → comparison → decision → error trade-off → review. However, compared to the Reference's "Scaffold-Dependent Assembly," which has richer causal language and explores nucleation and template information, this template is more procedural and less evocative. Rating: 7

#### Intelligence
The archetype demonstrates solid understanding of decision theory and the false-positive/false-negative trade-off. The insight that raising the threshold reduces one error while increasing the other is well-chosen. However, the template does not explore more sophisticated phenomena like ROC curves, cost-benefit analysis, or Bayesian updating. The Reference's "Debt Accumulation and Crisis" goes deeper by incorporating recursive structure and systemic propagation. Rating: 6

#### Domains far apart / metanyms not synonymous
The five domains are well separated: information technology, immigration, medicine, finance, and research administration. The metanyms are reasonably distinct: EVIDENCE ranges from "message features" to "passport and visa" to "test result" to "financial documentation" to "proposal evidence." THRESHOLD ranges from "filter cutoff" to "proof standard" to "referral cutoff" to "approval cutoff" to "funding cutoff." However, the core structure (EVIDENCE → THRESHOLD → DECISION) is quite parallel across all five contexts, and the error types (FALSE POSITIVE, FALSE NEGATIVE) are nearly synonymous. Rating: 6

#### Impressive length
The template is moderately long (approximately 80 words) and covers the essential elements: gate, candidate, evidence, threshold, criterion, decision maker, accepted, rejected, noise, false positive, false negative, review, and field. It is comparable to the Reference's templates. However, it does not explore secondary phenomena (e.g., cost asymmetry, sequential testing, Bayesian updating) that would extend it. Rating: 7

### Archetypal context 4: Depleting Shared Stocks

#### Factual correct (per parallel context)
- PC 1 (Marine fishery): The fishery description is factually accurate. Fish biomass is replenished by recruitment and depleted by harvest. Delayed stock assessments can hide decline. Fishery management uses quotas and closures. The description of minimum spawning biomass and stock collapse is sound. Rating: 8

- PC 2 (Groundwater basin): The aquifer description is factually accurate. Groundwater is replenished by recharge and depleted by pumping. Delayed water-level measurements can hide decline. Groundwater authorities use allotments and penalties. The description of minimum aquifer level and depletion is sound. Rating: 8

- PC 3 (Shared pasture): The pasture description is factually accurate. Forage is replenished by plant growth and depleted by grazing. Seasonal lags can hide decline. Pasture associations use stocking limits and exclusion. The description of minimum ground cover and degradation is sound. Rating: 8

- PC 4 (Irrigation reservoir): The reservoir description is factually accurate. Water is replenished by inflow and depleted by irrigation release. Delayed drought recognition can hide decline. Reservoir authorities use allocation and penalties. The description of conservation pool and exhaustion is sound. Rating: 8

- PC 5 (Managed forest): The forest description is factually accurate. Timber is replenished by tree growth and depleted by harvest. Delayed forest inventories can hide decline. Forestry administrations use harvest limits and penalties. The description of minimum regeneration density and liquidation is sound. Rating: 8

#### Beauty
The template is elegant and captures the essential tragedy-of-the-commons principle. The parallel contexts are exceptionally well-chosen and span genuinely different resource systems. The Form (b) rewrites are particularly polished and use domain-expert language naturally. The template has a clear narrative arc: replenishment → withdrawal → depletion delay → governance → recovery threshold → crisis. This is one of the strongest archetypes in the Target submission. Rating: 8

#### Intelligence
The archetype demonstrates sophisticated understanding of resource economics and the commons dilemma. The insight that depletion delays hide decline, and that governance must combine monitoring, allocation, and sanction, is intellectually rich. The distinction between sustainable yield and liquidation is well-chosen. However, the template does not explore more sophisticated phenomena like dynamic optimization, discount rates, or heterogeneous user types. The Reference's "Debt Accumulation and Crisis" goes deeper by incorporating recursive structure. Rating: 7

#### Domains far apart / metanyms not synonymous
The five domains are exceptionally well separated: marine biology, hydrogeology, pastoral ecology, water engineering, and forestry. The metanyms are genuinely distinct: STOCK ranges from "fish biomass" to "groundwater storage" to "forage biomass" to "stored water" to "standing timber." REPLENISHMENT ranges from "fish recruitment" to "aquifer recharge" to "plant growth" to "watershed inflow" to "tree growth." WITHDRAWAL ranges from "fish harvest" to "groundwater pumping" to "livestock grazing" to "irrigation release" to "timber harvest." These are far from synonymous. Rating: 9

#### Impressive length
The template is moderately long (approximately 85 words) and covers the essential elements: resource system, stock, replenishment, withdrawal, user, depletion delay, governance, monitoring, allocation rule, sanction, recovery threshold, recovery, yield, and liquidation. It is comparable to the Reference's templates. However, it does not explore secondary phenomena (e.g., heterogeneous users, discount rates, dynamic optimization) that would extend it. Rating: 7

### Archetypal context 5: Network Cascades

#### Factual correct (per parallel context)
- PC 1 (Infectious disease): The epidemiological description is factually accurate. Disease spreads through contact networks, transmission depends on exposure and susceptibility thresholds, and superspreaders amplify spread. Vaccination and isolation can reduce the effective reproduction number. Rating: 8

- PC 2 (Bank run): The bank-run description is factually sound. Withdrawals propagate through depositor networks, confidence thresholds determine behavior, and institutional depositors can amplify runs. Liquidity guarantees can reduce propagation. Rating: 8

- PC 3 (Power grid failure): The power-grid description is factually accurate. Faults propagate through transmission networks, relay thresholds determine protective trips, and heavily loaded interconnectors amplify cascades. Load shedding can reduce branching. Rating: 8

- PC 4 (Computer malware): The malware description is factually accurate. Malware spreads through computer networks, vulnerability thresholds determine infection, and exposed servers amplify spread. Patching and isolation can reduce infection rates. Rating: 8

- PC 5 (Social rumor): The rumor description is factually sound. Rumors spread through social networks, credulity thresholds determine adoption, and influencers amplify spread. Fact-checking can reduce sharing ratios. Rating: 8

#### Beauty
The template is elegant and captures the essential cascade principle. The parallel contexts are well-chosen and span very different domains. The Form (b) rewrites are natural and domain-appropriate. The template has a clear narrative arc: network → trigger → threshold → transmission → amplifier → cascade → intervention. However, compared to the Reference's "Gradient-Guided Navigation," which has richer causal language and explores memory and collective behavior, this template is more structural and less evocative. Rating: 7

#### Intelligence
The archetype demonstrates solid understanding of network science and cascade dynamics. The insight that connectivity, thresholds, clustering, and intervention shape cascades is well-chosen. However, the template does not explore more sophisticated phenomena like percolation theory, critical thresholds, or phase transitions. The Reference's "Competitive Exclusion and Niche Partitioning" goes deeper by incorporating stabilizing mechanisms and fitness differences. Rating: 6

#### Domains far apart / metanyms not synonymous
The five domains are well separated: epidemiology, finance, power systems, cybersecurity, and sociology. The metanyms are reasonably distinct: NODE ranges from "person" to "account holder" to "substation" to "device" to "person." TRIGGER ranges from "infected person" to "withdrawal request" to "line overload" to "infected device" to "rumor post." However, the core structure (NETWORK → NODE → LINK → TRIGGER → STATE → TRANSMISSION) is quite parallel across all five contexts, and concepts like THRESHOLD, AMPLIFIER, and CASCADE are nearly synonymous. Rating: 6

#### Impressive length
The template is moderately long (approximately 85 words) and covers the essential elements: network, node, link, trigger, state, exposure, threshold, transmission, amplifier, cluster, cascade, intervention, target, growth factor, and network science. It is comparable to the Reference's templates. However, it does not explore secondary phenomena (e.g., percolation, critical thresholds, phase transitions) that would extend it. Rating: 7

### Structural diversity across the submitted set

The Target submission presents five archetypal contexts with distinct system structures: (1) Negative-Feedback Regulation—a control system with measurement, comparison, and actuation; (2) Service-Queue Accumulation—a queueing system with arrivals, service, and delay; (3) Thresholded Admission—a classification system with evidence, threshold, and decision; (4) Depleting Shared Stocks—a resource system with replenishment, withdrawal, and governance; (5) Network Cascades—a propagation system with nodes, links, and transmission. These five structures are genuinely different: feedback control, queueing, classification, resource management, and network dynamics. However, compared to the Reference submission, which includes Gradient-Guided Navigation (local sensing and adjustment), Containment Breach Cascade (boundary failure and propagation), Competitive Exclusion (niche partitioning), Debt Accumulation (recursive hierarchical structure), and Scaffold-Dependent Assembly (template-guided construction), the Target's structures are somewhat less diverse. The Reference includes a recursive archetype (Debt Accumulation), which the Target does not. The Reference's structures span a wider range of system types: gradient-following, boundary dynamics, competition, hierarchical accumulation, and assembly. The Target's structures are more focused on control, queueing, classification, resource management, and cascades—a somewhat narrower range. Rating: 6

---

```json
{
  "scores": {
    "Target": {
      "archetypal_contexts": [
        {
          "name": "Negative-Feedback Regulation",
          "factual_per_pc": [8, 7, 8, 8, 8],
          "beauty": 7,
          "intelligence": 6,
          "instantiation_distinctness": 6,
          "impressive_length": 7
        },
        {
          "name": "Service-Queue Accumulation",
          "factual_per_pc": [8, 8, 8, 6, 8],
          "beauty": 7,
          "intelligence": 6,
          "instantiation_distinctness": 5,
          "impressive_length": 7
        },
        {
          "name": "Thresholded Admission",
          "factual_per_pc": [8, 8, 8, 8, 8],
          "beauty": 7,
          "intelligence": 6,
          "instantiation_distinctness": 6,
          "impressive_length": 7
        },
        {
          "name": "Depleting Shared Stocks",
          "factual_per_pc": [8, 8, 8, 8, 8],
          "beauty": 8,
          "intelligence": 7,
          "instantiation_distinctness": 9,
          "impressive_length": 7
        },
        {
          "name": "Network Cascades",
          "factual_per_pc": [8, 8, 8, 8, 8],
          "beauty": 7,
          "intelligence": 6,
          "instantiation_distinctness": 6,
          "impressive_length": 7
        }
      ],
      "structural_diversity": 6
    }
  }
}
```