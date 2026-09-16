## Target Submission

### Archetypal context 1: Negative-Feedback Regulation

#### Factually correct (per parallel context)
- PC 1 (Building heating): The control-loop account is accurate and the idiomatic rewrite improves on the mechanically substituted form. Minor simplifications—such as treating “room temperature” as both setpoint wording and measured variable—do not undermine the core claims. It is more consistently correct than several reference instantiations. Rating: 8
- PC 2 (Glucose regulation): The broad negative-feedback description is sound, including glucose sensing, insulin-mediated correction, delay, and instability under excessive gain. However, beta cells do not simply “send a glucose concentration” to an islet, and insulin sensitivity is not cleanly equivalent to controller gain; the reference has comparable but somewhat more frequent biological mapping errors. Rating: 7
- PC 3 (Aircraft altitude control): This is a strong and technically coherent feedback-control instantiation. Altimeter measurement, flight-computer control, elevator actuation, gain-induced sluggishness or oscillation, and lag are all appropriately described. Rating: 8
- PC 4 (Spacecraft attitude control): The account is largely correct: star trackers estimate attitude and reaction wheels apply torque under feedback control. “Light-time” delay is not ordinarily an onboard attitude-control delay, though computation and sensing delays are relevant; this is a minor factual overextension. Rating: 8
- PC 5 (Industrial fermentation): Dissolved-oxygen control through probe measurement and aeration adjustment is accurate, as are the effects of gain and measurement delay. In practice agitation is often another major actuator, but its omission is not an error. Rating: 8

#### Beauty
The template is compact, lucid, and rhythmically organized around the causal logic of a feedback loop. Its prose is less ornate than the reference but more disciplined and less burdened by awkward substitutions, yielding a modest improvement in elegance.  
Rating: 8

#### Intelligence
This archetype identifies a foundational systems structure and maps its key formal elements—setpoint, sensor, controller, gain, delay, and stability—cleanly across biological and engineered domains. The mappings are unusually structurally faithful, though the abstraction is familiar rather than surprising.  
Rating: 8

#### Domains far apart / metanyms not synonymous
The domains span domestic engineering, endocrinology, aviation, spacecraft engineering, and bioprocessing. They are genuinely distinct, although four are explicitly control systems and the metanyms remain close functional analogues by design; this is still stronger and cleaner than much of the reference’s domain variation.  
Rating: 8

#### Impressive length
The template is a coherent medium-length paragraph with several interacting control concepts, but it is substantially shorter than the reference’s longest templates and does not sustain as many relational slots.  
Rating: 6

### Archetypal context 2: Service-Queue Accumulation

#### Factually correct (per parallel context)
- PC 1 (Emergency medicine): The queueing analogy is broadly accurate, especially regarding triage, near-capacity nonlinear delay, and diversion. “Patient acuity load” is not a standard utilization measure and resuscitation-bay saturation does not generally force all listed outcomes, but the rewrite appropriately conveys operational reality. Rating: 7
- PC 2 (Web infrastructure): The description accurately captures request queues, processing limits, latency growth near saturation, load balancing’s limits, and finite-buffer rejection or rerouting. The database connection pool is a plausible bottleneck. Rating: 8
- PC 3 (Airport security): The queueing claims are sound, but passport control is often organizationally separate from security screening, making it a somewhat awkward bottleneck within this particular checkpoint model. The core operational logic remains correct. Rating: 7
- PC 4 (Civil litigation): Dockets, filing pressure, hearing capacity, priority rules, and delay accumulation are accurately represented. The claim that finite docket capacity forces cases to be refused is less generally true than deferral or reassignment, but it is plausible in constrained procedural settings. Rating: 7
- PC 5 (Factory production): This is a strong and conventional queueing instantiation: WIP buffers, machine utilization, dispatching, bottlenecks, and finite-buffer blocking are all accurately connected. Rating: 8

#### Beauty
The prose has a clear escalation from arrivals to saturation to buffer failure, and the rewrites are concise and readable. It is more functional than evocative, but its conceptual economy makes it slightly more polished than the reference average.  
Rating: 8

#### Intelligence
The archetype captures a deep and transferable queueing principle: utilization near capacity produces nonlinear delay, while scheduling redistributes rather than abolishes scarcity. The distinction between transient bursts and persistent overload is particularly intelligent and well expressed.  
Rating: 9

#### Domains far apart / metanyms not synonymous
Emergency care, APIs, airport operations, courts, and manufacturing are materially different institutional domains. The mappings preserve queueing roles without collapsing into synonyms, although all five are recognizable service systems. Rating: 8

#### Impressive length
The template is moderately long and contains a complete causal sequence—arrival, queue, service, utilization, nonlinear delay, scheduling, bottleneck, buffer, and theory. It is shorter than the reference’s most elaborate templates but comparably substantive.  
Rating: 7

### Archetypal context 3: Thresholded Admission

#### Factually correct (per parallel context)
- PC 1 (Spam filtering): The classification framework and false-positive/false-negative trade-off are accurate. The direction of “raising the filter cutoff” depends on score convention, but the rewrite clarifies the intended stricter-versus-looser threshold interpretation. Rating: 8
- PC 2 (Border admission): The decision-theoretic framing is broadly correct, including ambiguity, secondary inspection, and asymmetric error costs. “Passport and visa” is grammatically awkward as extracted evidence, but not materially false. Rating: 8
- PC 3 (Cancer screening): The account correctly describes screening thresholds, measurement error, confirmatory testing, and the referral trade-off. Calling a false positive an “unnecessary referral” is reasonable, though referral is not identical to treatment. Rating: 8
- PC 4 (Consumer lending): The lending example is mostly accurate, but the threshold direction is potentially inverted: if the score is default risk, raising an approval cutoff would ordinarily permit more risky applicants unless the rule is explicitly defined inversely. This ambiguity weakens an otherwise solid mapping. Rating: 7
- PC 5 (Research grants): The grant-selection analogy accurately captures noisy evaluation, cutoff trade-offs, review, and asymmetric consequences. Applicant rebuttal is not universally available, but it is plausible in some grant systems. Rating: 8

#### Beauty
This template is exceptionally clean: it introduces classification, error types, review, and the threshold trade-off in a compact logical progression. The language is precise rather than lyrical, but it is more elegant and less strained than the reference’s average archetype prose.  
Rating: 8

#### Intelligence
The abstraction successfully transfers statistical decision theory across automated filtering, law and administration, medicine, finance, and peer review. Its explicit treatment of asymmetric error costs and revisability through review gives it more conceptual depth than a simple binary-choice analogy.  
Rating: 9

#### Domains far apart / metanyms not synonymous
The domains range from machine classification to immigration, clinical screening, lending, and research governance. The roles are structurally parallel but semantically distant, making this one of the submission’s strongest metanym tables. Rating: 9

#### Impressive length
The template is concise but complete, covering evidence, criterion, decision, noise, both error types, review, threshold adjustment, and unequal costs. It is somewhat shorter than the reference’s longer templates.  
Rating: 7

### Archetypal context 4: Depleting Shared Stocks

#### Factually correct (per parallel context)
- PC 1 (Marine fishery): The fishery account is accurate and well grounded in recruitment, harvest pressure, delayed assessment, quotas, closures, spawning biomass, and rebuilding uncertainty. It is stronger and more coherent than many reference factual mappings. Rating: 8
- PC 2 (Groundwater basin): Recharge, pumping, delayed observation, allocation, penalties, threshold effects, and slow recovery are accurately represented. The wording “natural aquifer recharge may restore it only slowly or uncertainly” is sensible, though recovery depends heavily on hydrogeology. Rating: 8
- PC 3 (Shared pasture): The tragedy-of-the-commons structure is accurately applied to forage growth, grazing pressure, seasonal lags, stocking limits, and restoration. “Natural pasture rest and reseeding” mixes natural recovery with active intervention, but the substantive point remains sound. Rating: 8
- PC 4 (Irrigation reservoir): The reservoir mapping is broadly correct, including inflow, releases, drought-recognition delay, allocation, conservation pools, and refill uncertainty. A reservoir is managed storage rather than a naturally replenishing common stock in exactly the same sense as fish or pasture, but the analogy remains valid. Rating: 8
- PC 5 (Managed forest): The forest example accurately captures standing timber, growth, harvest, inventory lags, harvest limits, regeneration thresholds, and liquidation. It is among the strongest factual contexts in the submission. Rating: 8

#### Beauty
The template has a satisfying moral and causal arc from individual extraction to collective depletion and institutional correction. Its language is clear and balanced, though less stylistically distinctive than the strongest reference prose.  
Rating: 8

#### Intelligence
This is a sophisticated common-pool-resource archetype that integrates stock-flow dynamics, delayed feedback, threshold effects, governance mechanisms, and incentive alignment. It is more analytically complete than a generic “tragedy of the commons” formulation.  
Rating: 9

#### Domains far apart / metanyms not synonymous
All five contexts are natural-resource systems—fish, groundwater, pasture, reservoirs, and forests—so their domains are closely related compared with the reference’s broader cross-domain tables. The metanyms are appropriately non-synonymous but not especially distant. Rating: 6

#### Impressive length
The template is a substantial paragraph with multiple linked mechanisms: replenishment, withdrawal, delayed depletion, governance, thresholds, recovery, yield, and liquidation. It is comparable to the reference’s medium-to-long templates.  
Rating: 8

### Archetypal context 5: Network Cascades

#### Factually correct (per parallel context)
- PC 1 (Infectious disease): The network framing, thresholded transmission, superspreading, household clustering, targeted intervention, and effective reproduction number are broadly accurate. “An infected person can move from one person to another” is an awkward substitution for pathogen transmission, but Form (b) corrects it. Rating: 8
- PC 2 (Bank run): The contagion analogy is plausible and captures confidence thresholds, institutional amplification, clustering, guarantees, and delay. However, withdrawal requests do not literally transmit in the same way as pathogens, and targeted guarantees to individual exposed account holders are less standard than institution-wide guarantees. Rating: 7
- PC 3 (Power grid failure): Cascading overloads, relay trips, topology, interconnectors, islands, and load shedding are accurately invoked. The wording that an overload “moves” between substations is simplified, but the rewrite correctly describes propagation through network flows. Rating: 8
- PC 4 (Computer malware): The malware mapping is generally accurate, including network topology, vulnerable devices, exposed servers, patching, isolation, and delayed response. “Payload exceeds a vulnerability threshold” is a simplified causal model but acceptable at this abstraction level. Rating: 8
- PC 5 (Social rumor): The account accurately captures repeated exposure, credibility thresholds, influencers, communities, fact-checking, and delayed intervention. Fact-checking a single high-reach account does not reliably reduce sharing below one, but it is a plausible targeted intervention. Rating: 8

#### Beauty
The template is vivid without becoming melodramatic, and its progression from local trigger to amplification, clustering, intervention, and delay is well shaped. It is more readable and coherent than several reference templates.  
Rating: 8

#### Intelligence
The archetype combines contagion thresholds, topology, clustering, amplification, intervention targeting, and reproduction-like growth factors in a unified network-science frame. It is conceptually strong, though it risks flattening important differences between physical failures, beliefs, and biological infection.  
Rating: 8

#### Domains far apart / metanyms not synonymous
Disease, banking, electrical infrastructure, malware, and rumor are highly distinct domains, and the table maps roles across them with considerable semantic distance. This is clearly stronger than the reference’s average domain spread. Rating: 9

#### Impressive length
The template is moderately long and densely structured, with enough slots to express topology, thresholds, amplification, clustering, intervention, and growth. It is shorter than the reference’s most expansive templates but still impressive.  
Rating: 7

### Structural diversity across the submitted set
The five archetypes represent genuinely different system structures: stabilizing feedback loops, congestion under service constraints, binary classification under uncertainty, common-pool stock depletion, and contagion-like network propagation. This is more structurally diverse than the reference set, whose archetypes include several broad process/cascade structures and a recursive debt framework, although the target lacks the reference’s valuable recursive demonstration.  
Rating: 9

```json
{
  "scores": {
    "Target": {
      "archetypal_contexts": [
        {
          "name": "Negative-Feedback Regulation",
          "factual_per_pc": [8, 7, 8, 8, 8],
          "beauty": 8,
          "intelligence": 8,
          "instantiation_distinctness": 8,
          "impressive_length": 6
        },
        {
          "name": "Service-Queue Accumulation",
          "factual_per_pc": [7, 8, 7, 7, 8],
          "beauty": 8,
          "intelligence": 9,
          "instantiation_distinctness": 8,
          "impressive_length": 7
        },
        {
          "name": "Thresholded Admission",
          "factual_per_pc": [8, 8, 8, 7, 8],
          "beauty": 8,
          "intelligence": 9,
          "instantiation_distinctness": 9,
          "impressive_length": 7
        },
        {
          "name": "Depleting Shared Stocks",
          "factual_per_pc": [8, 8, 8, 8, 8],
          "beauty": 8,
          "intelligence": 9,
          "instantiation_distinctness": 6,
          "impressive_length": 8
        },
        {
          "name": "Network Cascades",
          "factual_per_pc": [8, 7, 8, 8, 8],
          "beauty": 8,
          "intelligence": 8,
          "instantiation_distinctness": 9,
          "impressive_length": 7
        }
      ],
      "structural_diversity": 9
    }
  }
}
```