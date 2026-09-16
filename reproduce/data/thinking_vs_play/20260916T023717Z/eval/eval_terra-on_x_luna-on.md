## Target Submission

### Archetypal context 1: Negative-Feedback Regulation

#### Factually correct (per parallel context)
- PC 1 (Building heating): This is a sound control-system account: sensing, comparison with a target, actuator response, gain-related hunting, and thermal lag are all appropriately described. The thermostat/controller distinction is slightly idealized but is clarified well in Form (b). It is materially more factually disciplined than the Reference’s typical literal substitutions. Rating: 9
- PC 2 (Glucose regulation): The account correctly identifies glucose sensing, insulin-mediated feedback, sensitivity, and hormonal delay as important elements of glucose homeostasis. However, beta cells are themselves part of the islet and directly secrete insulin rather than simply sending a glucose measurement to it; the single-loop framing also abstracts away glucagon and other counter-regulation. Still, it is stronger than the Reference’s average factual precision. Rating: 8
- PC 3 (Aircraft altitude control): The feedback-loop description is accurate and idiomatic: altimeters provide measurements, flight computers calculate corrections, elevators affect altitude through pitch control, and excessive gain or lag can produce oscillation. It simplifies the roles of thrust, airspeed, and autopilot modes, but does so responsibly. Rating: 9
- PC 4 (Spacecraft attitude control): Star trackers, guidance computers, reaction wheels, pointing errors, and solar-radiation pressure are appropriately related. The inclusion of “light-time” as a controller delay is not generally applicable to an onboard attitude-control loop, though it can matter in ground-directed operations; computation and sensing delays are sound. This remains clearly better than the Reference baseline. Rating: 8
- PC 5 (Industrial fermentation): The bioreactor example accurately describes dissolved-oxygen control through probes, controllers, aeration adjustment, microbial oxygen demand, gain, and measurement delay. It is a particularly clean technical instantiation with no substantial factual defect beyond normal simplification. Rating: 9

#### Beauty
The template is compact, balanced, and readable, moving naturally from setpoint maintenance through sensing and control to gain and delay. Its prose is cleaner and less mechanically strained than much of the Reference, although its technical directness makes it more elegant than lyrical. Rating: 8

#### Intelligence
This is a strong abstraction because it captures the essential causal structure of negative feedback rather than merely sharing vocabulary across examples. The selection of gain, delay, sensing, and actuation identifies the system features that actually govern stability. It is more conceptually coherent than the Reference’s calibration level. Rating: 8

#### Domains far apart / metanyms not synonymous
The domains span building systems, physiology, aviation, spacecraft engineering, and bioprocessing, with genuinely different metanyms for sensors, actuators, disturbances, and controllers. Aircraft and spacecraft control are relatively close cousins, which limits the breadth somewhat, but the overall spread matches the Reference well. Rating: 7

#### Impressive length
The template is substantial enough to express a complete mechanism, but it is noticeably shorter than the Reference’s generally longer archetypal templates. Its concision is a virtue stylistically, yet it is less impressive on length specifically. Rating: 6

### Archetypal context 2: Service-Queue Accumulation

#### Factually correct (per parallel context)
- PC 1 (Emergency medicine): The queuing logic is sound: near-capacity emergency departments can experience nonlinear delay growth, and triage redistributes waiting rather than creating capacity. “Patient acuity load” is not quite the same as utilization, and rejection or blocking is constrained by emergency-care obligations, but the Form (b) explanation handles the real operational point well. Rating: 8
- PC 2 (Web infrastructure): This is an accurate and practical description of API queues, worker processing, traffic spikes, load balancing, connection-pool saturation, finite buffers, and request rejection or rerouting. It is technically coherent and substantially more precise than the Reference’s average parallel context. Rating: 9
- PC 3 (Airport security): The basic queueing account is correct: passenger surges near screening capacity increase delay sharply, lane assignment redistributes waiting, and physical holding limits can constrain flow. Passport control is often organizationally separate from security screening, so the chosen bottleneck is somewhat context-dependent, but the underlying operations claim remains sound. Rating: 8
- PC 4 (Civil litigation): Dockets, hearings, judicial service capacity, case-priority rules, and delay accumulation are accurately connected. Finite docket capacity rarely means ordinary cases are simply rejected in the literal way stated, since legal systems often defer or administratively manage filings instead; nevertheless, the queueing analogy is mostly sound. Rating: 8
- PC 5 (Factory production): This is a very accurate production-operations instantiation. Work-in-process buffers, constrained machines, utilization, dispatch rules, release rates, lead time, and blocked jobs all fit standard queueing and manufacturing theory. Rating: 9

#### Beauty
The template has an admirably economical progression from arrivals and service through near-capacity nonlinearities, scheduling, bottlenecks, buffers, and the governing trade-off. It is more polished and less repetitive than the Reference’s average prose, even if it remains deliberately technical. Rating: 8

#### Intelligence
This is among the strongest archetypes in the Target. It identifies the important non-obvious feature of queueing systems—exploding delay near saturation—and correctly distinguishes priority redistribution from actual capacity relief. That is a sophisticated and useful systems abstraction, stronger than the Reference anchor. Rating: 9

#### Domains far apart / metanyms not synonymous
Emergency medicine, web services, airport operations, courts, and factories are meaningfully different institutional and technical settings. Their queue, server, bottleneck, and scheduling terms are not merely synonyms, giving this context broader domain separation than the Reference baseline. Rating: 8

#### Impressive length
The template covers a complete queueing mechanism and its policy implications, but it is shorter than the Reference’s more extended templates. It earns credit for density rather than sheer length. Rating: 6

### Archetypal context 3: Thresholded Admission

#### Factually correct (per parallel context)
- PC 1 (Spam filtering): The general false-positive/false-negative framework is correct, as are the roles of adversarial wording and manual review. However, with a quantity explicitly called a “spam score,” raising the stated cutoff would normally admit more spam rather than reduce spam admission, unless the score’s direction is defined oppositely; the claimed cutoff direction is therefore materially ambiguous or wrong. Rating: 6
- PC 2 (Border admission): This is a sound decision-theoretic abstraction of border screening. Higher evidentiary standards can reduce inadmissible entries while increasing mistaken refusals, and secondary inspection can revise an initial decision. It simplifies the legal and discretionary complexity of immigration law but remains factually robust. Rating: 9
- PC 3 (Cancer screening): The example correctly presents screening as a threshold trade-off between unnecessary referrals and missed cases, with confirmatory testing able to revise an initial classification. “Treatment referral” is somewhat broader than many screening pathways, which typically refer for diagnostic workup, but the substantive logic is correct. Rating: 9
- PC 4 (Consumer lending): The broad lending example is appropriate, but the cutoff direction is problematic. For a score explicitly described as default risk, raising an approval cutoff ordinarily allows riskier applicants to qualify and would increase risky approvals, contrary to the text; it would work only if the score were defined as creditworthiness instead. Rating: 6
- PC 5 (Research grants): The grants example accurately captures imperfect merit assessment, reviewer disagreement, appeals or rebuttal, and the trade-off between weak awards and rejecting strong proposals. Its claims are appropriately qualified and clearer than the Reference baseline. Rating: 9

#### Beauty
The template is exceptionally clear in its use of paired opposites—accepted/rejected, false positive/false negative, higher/lower threshold—and makes an abstract classification problem accessible across domains. It is more stylistically controlled than the Reference, though its formal framing is somewhat dry. Rating: 8

#### Intelligence
The archetype intelligently isolates a core decision-theoretic structure: noisy evidence, a binary threshold, asymmetric errors, review, and unequal consequences. The score-direction errors in two instantiations modestly undermine execution, but the underlying abstraction remains stronger than the Reference’s calibration level. Rating: 8

#### Domains far apart / metanyms not synonymous
The examples range across information systems, immigration, medicine, finance, and research governance. They are diverse, but all are recognizably evaluative gatekeeping systems, and the Reference’s strongest domain-spanning contexts are at least as broad. Rating: 7

#### Impressive length
The template is complete and well organized but comparatively short relative to the Reference’s longer archetypal paragraphs. Its precision compensates somewhat, yet it does not surpass the Reference on length. Rating: 6

### Archetypal context 4: Depleting Shared Stocks

#### Factually correct (per parallel context)
- PC 1 (Marine fishery): The fishery account accurately connects recruitment, harvesting, delayed assessment, collective overuse, quotas, closures, spawning biomass, and stock rebuilding. It is a strong and conventional representation of common-pool resource management. Rating: 9
- PC 2 (Groundwater basin): Recharge, pumping, delayed water-level information, allotments, penalties, depletion, and slow recovery are correctly presented. Recovery rates depend strongly on geology and continued extraction, but the qualification that they “may” be slow or uncertain is sound. Rating: 9
- PC 3 (Shared pasture): The pasture example correctly captures overgrazing, seasonal information lags, stocking limits, exclusion, and the difficulty of recovery after ground-cover loss. Calling reseeding part of “natural” recovery is slightly imprecise because reseeding is an intervention, but the central ecology and governance claims are sound. Rating: 8
- PC 4 (Irrigation reservoir): The account correctly describes storage, inflows, releases, drought-recognition delays, allocations, conservation pools, and the danger of exhausting reserves. Watershed inflow varies substantially and is not a simple replenishment process, but the abstraction is accurate for reservoir management. Rating: 9
- PC 5 (Managed forest): Forest growth, harvesting, inventory lags, harvest limits, penalties, and regeneration concerns are accurately linked. The relation between standing-timber stock and a “minimum regeneration density” is slightly loose, but the example remains substantively correct. Rating: 8

#### Beauty
The template is lucid and morally resonant without becoming rhetorical: immediate private gain, hidden collective decline, governance, thresholds, and long-term stewardship form a clear arc. It is more graceful and coherent than the Reference’s average archetypal wording. Rating: 8

#### Intelligence
This is a well-formed common-pool-resource archetype, integrating stock-flow dynamics, delayed information, incentive misalignment, threshold effects, and institutional remedies. It is conceptually strong, though less unusually ambitious than the Reference’s recursive debt proposal. Rating: 8

#### Domains far apart / metanyms not synonymous
All five domains are natural-resource systems governed through common-pool institutions: fisheries, groundwater, pasture, reservoir water, and forests. The metanyms are appropriate, but the examples are substantially closer to one another than those in the Reference’s broadest tables. Rating: 6

#### Impressive length
The template is compact and covers the necessary stock-flow and governance mechanisms, but it is appreciably less lengthy than the Reference templates. Its content density is good, while its raw length is below the calibration anchor. Rating: 6

### Archetypal context 5: Network Cascades

#### Factually correct (per parallel context)
- PC 1 (Infectious disease): The epidemiological network framing is fundamentally sound: contacts, exposure thresholds, clustering, superspreading, targeted intervention, and the effective reproduction number are all relevant. The wording that an infected person “moves” to another person should more properly refer to transmission of a pathogen, but Form (b) resolves the intended meaning well. Rating: 8
- PC 2 (Bank run): The account captures contagion in withdrawal behavior, confidence thresholds, institutional depositors, guarantees, and intervention timing. However, “banking relationships” are a weaker analogue of the social, informational, and contractual links through which runs usually spread, making this less exact than the stronger Target contexts. Rating: 7
- PC 3 (Power grid failure): The description appropriately connects overloaded lines, protective relays, topology, interconnectedness, islands, load shedding, and cascading outages. “Local persistence” is a slightly awkward description for recurring grid trips, but the power-systems mechanism is otherwise accurate. Rating: 8
- PC 4 (Computer malware): Malware propagation, vulnerable devices, exposed servers, subnets, patching, isolation, and time-sensitive intervention are all represented plausibly. The “payload exceeds vulnerability threshold” phrasing is schematic rather than technically literal, but the network-security claims remain sound. Rating: 8
- PC 5 (Social rumor): The example correctly describes repeated exposure, belief adoption, social ties, influencers, local online communities, fact-checking, and delayed intervention. Credulity thresholds and a sharing ratio are simplified constructs, yet they are legitimate network-science abstractions. Rating: 8

#### Beauty
The template is tightly structured and vivid: triggers, thresholds, amplifiers, clusters, interventions, and delay create a compelling cascade narrative. Its prose is more concise and consistently idiomatic than the Reference’s average context templates. Rating: 8

#### Intelligence
This archetype captures several genuinely important network-science distinctions: topology, threshold activation, local clustering, amplification, intervention targeting, and subcritical growth. It is a coherent high-level model rather than a superficial shared-network metaphor, making it stronger than the Reference baseline. Rating: 8

#### Domains far apart / metanyms not synonymous
Infectious disease, finance, electric-power engineering, cybersecurity, and social communication are highly distinct systems. The metanyms differ materially in their triggers, states, links, amplifiers, and interventions, exceeding the Reference’s calibration level for cross-domain distance. Rating: 8

#### Impressive length
The template has enough length to state a sophisticated cascade mechanism, but it is still more compressed than the Reference’s longer archetypes. It falls modestly below the Reference on this criterion. Rating: 6

### Structural diversity across the submitted set
The five archetypes represent genuinely different system structures: stabilizing feedback loops, queueing congestion, threshold classification, common-pool stock depletion, and propagating network cascades. They are not recursive, but their separation is deliberate and clean, with little structural overlap beyond a general systems perspective. The Reference also offers diverse structures and gains some value from recursion, yet the Target’s set is more consistently differentiated at the mechanism level. Rating: 8

```json
{
  "scores": {
    "Target": {
      "archetypal_contexts": [
        {
          "name": "Negative-Feedback Regulation",
          "factual_per_pc": [9, 8, 9, 8, 9],
          "beauty": 8,
          "intelligence": 8,
          "instantiation_distinctness": 7,
          "impressive_length": 6
        },
        {
          "name": "Service-Queue Accumulation",
          "factual_per_pc": [8, 9, 8, 8, 9],
          "beauty": 8,
          "intelligence": 9,
          "instantiation_distinctness": 8,
          "impressive_length": 6
        },
        {
          "name": "Thresholded Admission",
          "factual_per_pc": [6, 9, 9, 6, 9],
          "beauty": 8,
          "intelligence": 8,
          "instantiation_distinctness": 7,
          "impressive_length": 6
        },
        {
          "name": "Depleting Shared Stocks",
          "factual_per_pc": [9, 9, 8, 9, 8],
          "beauty": 8,
          "intelligence": 8,
          "instantiation_distinctness": 6,
          "impressive_length": 6
        },
        {
          "name": "Network Cascades",
          "factual_per_pc": [8, 7, 8, 8, 8],
          "beauty": 8,
          "intelligence": 8,
          "instantiation_distinctness": 8,
          "impressive_length": 6
        }
      ],
      "structural_diversity": 8
    }
  }
}
```