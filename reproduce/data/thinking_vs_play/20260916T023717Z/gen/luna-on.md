## Archetype Proposal: Negative-Feedback Regulation

### Context-template

“A [SYSTEM] maintains a desired [SETPOINT] despite [DISTURBANCE] by measuring [VARIABLE], comparing that measurement with [SETPOINT], and using the resulting [DEVIATION] to adjust [ACTUATOR]. A [SENSOR] does not alter [VARIABLE] directly; it sends a [MEASUREMENT] to a [CONTROLLER], whose [FEEDBACK] policy determines the magnitude and timing of correction. If [GAIN] is too low, correction is weak and persistent deviation remains; if [GAIN] is too high, the system may oscillate around [SETPOINT]. [DELAY] can intensify either problem by making correction depend on an outdated measurement. [CONTROL THEORY] studies how such systems preserve stability while responding to disturbance.”

### Metanym table

| Slot | Building heating | Glucose regulation | Aircraft altitude control | Spacecraft attitude control | Industrial fermentation |
|---|---|---|---|---|---|
| SYSTEM | building heating system | glucose-regulation system | aircraft flight-control system | spacecraft attitude-control system | bioreactor control system |
| SETPOINT | room temperature | plasma glucose target | assigned altitude | target orientation | dissolved-oxygen target |
| DISTURBANCE | outdoor temperature | meal | wind gust | solar-radiation pressure | microbial oxygen demand |
| VARIABLE | indoor temperature | blood glucose | aircraft altitude | spacecraft attitude | dissolved oxygen |
| DEVIATION | temperature error | glycemic error | altitude error | pointing error | oxygen error |
| ACTUATOR | burner output | insulin secretion | elevator deflection | reaction-wheel torque | aeration-valve opening |
| SENSOR | thermostat | pancreatic beta cell | altimeter | star tracker | oxygen probe |
| MEASUREMENT | temperature reading | glucose concentration | altitude reading | attitude estimate | oxygen reading |
| CONTROLLER | heating controller | pancreatic islet | flight computer | guidance computer | process controller |
| FEEDBACK | negative temperature feedback | hormonal feedback | altitude feedback | attitude feedback | oxygen feedback |
| GAIN | heating gain | insulin sensitivity | control gain | torque gain | controller gain |
| DELAY | thermal lag | hormonal delay | sensor-and-actuator lag | light-time and computation delay | measurement delay |
| CONTROL THEORY | building-control engineering | endocrine physiology | flight-control theory | spacecraft control theory | process-control engineering |

### Building heating

**Form (a)** — “A building heating system maintains a desired room temperature despite outdoor temperature by measuring indoor temperature, comparing that measurement with room temperature, and using the resulting temperature error to adjust burner output. A thermostat does not alter indoor temperature directly; it sends a temperature reading to a heating controller, whose negative temperature feedback policy determines the magnitude and timing of correction. If heating gain is too low, correction is weak and persistent deviation remains; if heating gain is too high, the system may oscillate around room temperature. Thermal lag can intensify either problem by making correction depend on an outdated measurement. Building-control engineering studies how such systems preserve stability while responding to disturbance.”

**Form (b)** — “A building’s heating plant holds the room near its temperature target by sensing indoor temperature, comparing it with the target, and changing burner output in response to the error. The thermostat is only the sensing element: it reports temperature to the heating controller, which uses negative feedback to decide how large and how rapid the adjustment should be. Too little heating gain leaves the room persistently off target, while too much can make the temperature hunt above and below the target. Thermal inertia worsens either behavior because the system is correcting on the basis of an earlier state. Building-control engineering analyzes how to maintain stable temperature under changing outdoor conditions.”

### Glucose regulation

**Form (a)** — “A glucose-regulation system maintains a desired plasma glucose target despite a meal by measuring blood glucose, comparing that measurement with plasma glucose target, and using the resulting glycemic error to adjust insulin secretion. A pancreatic beta cell does not alter blood glucose directly; it sends a glucose concentration to a pancreatic islet, whose hormonal feedback policy determines the magnitude and timing of correction. If insulin sensitivity is too low, correction is weak and persistent deviation remains; if insulin sensitivity is too high, the system may oscillate around plasma glucose target. Hormonal delay can intensify either problem by making correction depend on an outdated measurement. Endocrine physiology studies how such systems preserve stability while responding to disturbance.”

**Form (b)** — “Glucose homeostasis keeps plasma glucose near its physiological target despite the rise caused by eating. Beta cells sense glucose and communicate its concentration within the pancreatic islet, where hormonal feedback adjusts insulin secretion according to the size and timing of the glycemic error. Low insulin sensitivity produces weak, persistent correction; excessive sensitivity can produce overshoot and oscillation around the target. Hormonal delays make both problems worse because secretion is responding to an earlier glucose level. Endocrine physiology studies how this control system remains stable while handling metabolic disturbances.”

### Aircraft altitude control

**Form (a)** — “An aircraft flight-control system maintains a desired assigned altitude despite a wind gust by measuring aircraft altitude, comparing that measurement with assigned altitude, and using the resulting altitude error to adjust elevator deflection. An altimeter does not alter aircraft altitude directly; it sends an altitude reading to a flight computer, whose altitude feedback policy determines the magnitude and timing of correction. If control gain is too low, correction is weak and persistent deviation remains; if control gain is too high, the system may oscillate around assigned altitude. Sensor-and-actuator lag can intensify either problem by making correction depend on an outdated measurement. Flight-control theory studies how such systems preserve stability while responding to disturbance.”

**Form (b)** — “An aircraft’s flight-control system holds the aircraft near its assigned altitude by measuring altitude, comparing it with the commanded value, and deflecting the elevator in proportion to the altitude error. The altimeter supplies the flight computer with the measurement but does not change altitude itself. A low control gain leaves the aircraft slow to recover, whereas a high gain can cause repeated climbs and descents through the target. Sensor and actuator lag aggravate both effects because the computer is acting on stale information. Flight-control theory determines how to obtain a stable response to gusts and other disturbances.”

### Spacecraft attitude control

**Form (a)** — “A spacecraft attitude-control system maintains a desired target orientation despite solar-radiation pressure by measuring spacecraft attitude, comparing that measurement with target orientation, and using the resulting pointing error to adjust reaction-wheel torque. A star tracker does not alter spacecraft attitude directly; it sends an attitude estimate to a guidance computer, whose attitude feedback policy determines the magnitude and timing of correction. If torque gain is too low, correction is weak and persistent deviation remains; if torque gain is too high, the system may oscillate around target orientation. Light-time and computation delay can intensify either problem by making correction depend on an outdated measurement. Spacecraft control theory studies how such systems preserve stability while responding to disturbance.”

**Form (b)** — “A spacecraft maintains its commanded orientation by comparing star-tracker measurements with the desired attitude and changing reaction-wheel torque according to the pointing error. The star tracker provides the attitude estimate; the guidance computer turns that estimate into a feedback command. Insufficient torque gain leaves pointing errors unresolved, while excessive gain can make the vehicle oscillate about its commanded orientation. Delays in sensing and computation worsen either response because the command is based on an earlier attitude. Spacecraft control theory studies how to stabilize attitude despite disturbances such as solar-radiation pressure.”

### Industrial fermentation

**Form (a)** — “A bioreactor control system maintains a desired dissolved-oxygen target despite microbial oxygen demand by measuring dissolved oxygen, comparing that measurement with dissolved-oxygen target, and using the resulting oxygen error to adjust aeration-valve opening. An oxygen probe does not alter dissolved oxygen directly; it sends an oxygen reading to a process controller, whose oxygen feedback policy determines the magnitude and timing of correction. If controller gain is too low, correction is weak and persistent deviation remains; if controller gain is too high, the system may oscillate around dissolved-oxygen target. Measurement delay can intensify either problem by making correction depend on an outdated measurement. Process-control engineering studies how such systems preserve stability while responding to disturbance.”

**Form (b)** — “A controlled fermenter keeps dissolved oxygen near its target by measuring oxygen concentration and adjusting the aeration valve in response to the error created by microbial demand. The probe supplies the measurement, while the process controller applies oxygen feedback and determines the size and timing of the aeration change. A low controller gain gives sluggish recovery; a high gain can produce oscillation around the target. Delayed oxygen measurements make either response worse because the controller is correcting an earlier condition. Process-control engineering examines how to maintain stable fermentation conditions under changing biological demand.”

---

## Archetype Proposal: Service-Queue Accumulation

### Context-template

“A [QUEUEING SYSTEM] receives a [WORK ITEM] through its [ARRIVAL PROCESS] and places it in the [QUEUE] before service by the [SERVER]. The [SERVER] removes items at a [SERVICE RATE], while [LOAD] measures how heavily available service is being used. As [LOAD] approaches [CAPACITY], small bursts in arrivals produce disproportionate increases in [WAITING TIME] and [BACKLOG]. A [SCHEDULING RULE] can redistribute delay among items, but it cannot eliminate a persistent excess of arrivals over service. When the [BOTTLENECK] is saturated, a finite [BUFFER] forces some items to be rejected, deferred, diverted, or blocked. [QUEUEING THEORY] studies the trade-off among utilization, delay, priority, and capacity.”

### Metanym table

| Slot | Emergency medicine | Web infrastructure | Airport security | Civil litigation | Factory production |
|---|---|---|---|---|---|
| QUEUEING SYSTEM | emergency department | API service | security checkpoint | court registry | production cell |
| WORK ITEM | patient | request | passenger | case | production job |
| ARRIVAL PROCESS | patient-arrival stream | traffic-arrival stream | passenger-arrival stream | case-filing stream | job-release stream |
| QUEUE | waiting room | request queue | security line | court docket | work-in-process buffer |
| SERVER | clinical team | compute worker | screening lane | judge | machine |
| SERVICE RATE | treatment rate | processing rate | screening rate | adjudication rate | completion rate |
| LOAD | patient acuity load | traffic intensity | passenger load | filing load | machine utilization |
| CAPACITY | treatment capacity | processing capacity | screening capacity | hearing capacity | machine capacity |
| WAITING TIME | time to treatment | response latency | time to screening | time to hearing | job lead time |
| BACKLOG | untreated patient list | pending-request backlog | un screened passenger line | pending docket | unfinished work |
| SCHEDULING RULE | acuity triage | load-balancing policy | lane-assignment rule | case-priority rule | dispatch rule |
| BOTTLENECK | resuscitation bay | database connection pool | passport-control desk | specialized courtroom | constrained machine |
| BUFFER | treatment space | queue memory | holding area | docket capacity | buffer stock |
| QUEUEING THEORY | health-care operations research | performance engineering | airport operations research | court administration | manufacturing operations research |

### Emergency medicine

**Form (a)** — “An emergency department receives a patient through its patient-arrival stream and places it in the waiting room before service by the clinical team. The clinical team removes patients at a treatment rate, while patient acuity load measures how heavily available treatment is being used. As patient acuity load approaches treatment capacity, small bursts in arrivals produce disproportionate increases in time to treatment and the untreated patient list. Acuity triage can redistribute delay among patients, but it cannot eliminate a persistent excess of arrivals over treatment. When the resuscitation bay is saturated, finite treatment space forces some patients to be rejected, deferred, diverted, or blocked. Health-care operations research studies the trade-off among utilization, delay, priority, and capacity.”

**Form (b)** — “An emergency department places arriving patients in the waiting room until the clinical team can treat them. Treatment capacity is consumed especially heavily by high-acuity patients, so a department operating near capacity can experience large increases in treatment times after even a small arrival surge. Acuity-based triage changes who waits, but it cannot resolve a continuing mismatch in which patients arrive faster than they can be treated. When the resuscitation bay is full, limited treatment space requires patients to be deferred, diverted, or otherwise prevented from immediate service. Health-care operations research analyzes this balance among utilization, delay, priority, and capacity.”

### Web infrastructure

**Form (a)** — “An API service receives a request through its traffic-arrival stream and places it in the request queue before service by the compute worker. The compute worker removes requests at a processing rate, while traffic intensity measures how heavily available processing is being used. As traffic intensity approaches processing capacity, small bursts in arrivals produce disproportionate increases in response latency and the pending-request backlog. A load-balancing policy can redistribute delay among requests, but it cannot eliminate a persistent excess of arrivals over processing. When the database connection pool is saturated, finite queue memory forces some requests to be rejected, deferred, diverted, or blocked. Performance engineering studies the trade-off among utilization, delay, priority, and capacity.”

**Form (b)** — “An API gateway holds incoming requests in a queue until compute workers can process them. Near the service’s processing limit, a brief traffic spike can cause response latency and the pending-request backlog to grow sharply. Load balancing can distribute the resulting delay across requests, but it cannot compensate for a sustained arrival rate above processing capacity. Once the database connection pool is exhausted, finite queue memory means that requests must be refused, delayed, rerouted, or blocked. Performance engineering studies how utilization, latency, priority, and capacity interact.”

### Airport security

**Form (a)** — “A security checkpoint receives a passenger through its passenger-arrival stream and places the passenger in the security line before service by the screening lane. The screening lane removes passengers at a screening rate, while passenger load measures how heavily available screening is being used. As passenger load approaches screening capacity, small bursts in arrivals produce disproportionate increases in time to screening and the unscreened passenger line. A lane-assignment rule can redistribute delay among passengers, but it cannot eliminate a persistent excess of arrivals over screening. When the passport-control desk is saturated, finite holding area forces some passengers to be rejected, deferred, diverted, or blocked. Airport operations research studies the trade-off among utilization, delay, priority, and capacity.”

**Form (b)** — “At an airport security checkpoint, arriving passengers wait in line until a screening lane can process them. When passenger volume is close to the checkpoint’s screening capacity, even a modest burst can greatly lengthen the time to screening and extend the unscreened line. Assigning passengers among lanes changes the distribution of waiting, but it cannot solve a persistent excess of arrivals. If the passport-control desk becomes the bottleneck, limited holding space requires passengers to be delayed, redirected, or prevented from proceeding. Airport operations research examines the relationship between utilization, delay, priority, and capacity.”

### Civil litigation

**Form (a)** — “A court registry receives a case through its case-filing stream and places it in the court docket before service by the judge. The judge removes cases at an adjudication rate, while filing load measures how heavily available hearings are being used. As filing load approaches hearing capacity, small bursts in filings produce disproportionate increases in time to hearing and the pending docket. A case-priority rule can redistribute delay among cases, but it cannot eliminate a persistent excess of filings over adjudication. When the specialized courtroom is saturated, finite docket capacity forces some cases to be rejected, deferred, diverted, or blocked. Court administration studies the trade-off among utilization, delay, priority, and capacity.”

**Form (b)** — “A court registry adds newly filed cases to a docket until judges and courtrooms can hear them. As filings approach the system’s hearing capacity, a small surge can cause both time to hearing and the pending docket to expand disproportionately. Priority rules determine which litigants wait longest, but they cannot remove a sustained excess of filings over adjudications. If a specialized courtroom is full, limited docket capacity requires some matters to be deferred, redirected, or refused at that stage. Court administration studies the resulting trade-off between utilization, delay, priority, and capacity.”

### Factory production

**Form (a)** — “A production cell receives a production job through its job-release stream and places it in the work-in-process buffer before service by the machine. The machine removes jobs at a completion rate, while machine utilization measures how heavily available machine service is being used. As machine utilization approaches machine capacity, small bursts in releases produce disproportionate increases in job lead time and unfinished work. A dispatch rule can redistribute delay among jobs, but it cannot eliminate a persistent excess of releases over completion. When the constrained machine is saturated, finite buffer stock forces some jobs to be rejected, deferred, diverted, or blocked. Manufacturing operations research studies the trade-off among utilization, delay, priority, and capacity.”

**Form (b)** — “A production cell stores released jobs in a work-in-process buffer until the machine can complete them. As machine utilization nears its capacity, even a short burst of releases can sharply increase lead times and unfinished work. Dispatching determines which jobs receive the delay, but it cannot overcome a release rate that persistently exceeds the machine’s completion rate. Once the constrained machine is saturated, limited buffer stock causes jobs to be postponed, rerouted, refused, or blocked. Manufacturing operations research analyzes the balance among utilization, delay, priority, and capacity.”

---

## Archetype Proposal: Thresholded Admission

### Context-template

“A [GATE] evaluates each [CANDIDATE] by extracting [EVIDENCE] and comparing it with a [THRESHOLD] on a [CRITERION]. The [DECISION MAKER] assigns the candidate to [ACCEPTED] or [REJECTED]. Because [NOISE] can distort evidence, a [FALSE POSITIVE] admits an unsuitable candidate, whereas a [FALSE NEGATIVE] excludes a suitable one. [REVIEW] can overturn an initial assignment when additional evidence or a better interpretation becomes available. Raising [THRESHOLD] usually reduces [FALSE POSITIVE] but increases [FALSE NEGATIVE], while lowering it has the opposite trade-off. [FIELD] studies how thresholds should be selected when the two errors have unequal consequences.”

### Metanym table

| Slot | Spam filtering | Border admission | Cancer screening | Consumer lending | Research grants |
|---|---|---|---|---|---|
| GATE | spam filter | border-control procedure | screening program | lending institution | grant-selection process |
| CANDIDATE | incoming message | traveler | patient | loan applicant | research proposal |
| EVIDENCE | message features | passport and visa | test result | financial documentation | proposal evidence |
| THRESHOLD | filter cutoff | proof standard | referral cutoff | approval cutoff | funding cutoff |
| CRITERION | spam score | admissibility score | disease-risk score | default-risk score | merit score |
| DECISION MAKER | classifier | border officer | clinician | underwriting model | review panel |
| ACCEPTED | inbox delivery | entry authorization | treatment referral | loan approval | grant funding |
| REJECTED | spam quarantine | entry refusal | no referral | loan denial | proposal rejection |
| NOISE | adversarial wording | document ambiguity | measurement error | missing financial data | reviewer disagreement |
| FALSE POSITIVE | spam admission | inadmissible admission | unnecessary referral | risky approval | weak proposal funding |
| FALSE NEGATIVE | legitimate quarantine | admissible refusal | missed referral | creditworthy denial | strong proposal rejection |
| REVIEW | manual review | secondary inspection | confirmatory testing | human underwriting review | applicant rebuttal |
| FIELD | statistical decision theory | immigration administration | medical screening | credit-risk analysis | research evaluation |

### Spam filtering

**Form (a)** — “A spam filter evaluates each incoming message by extracting message features and comparing them with a filter cutoff on a spam score. The classifier assigns the message to inbox delivery or spam quarantine. Because adversarial wording can distort evidence, a spam admission admits an unsuitable message, whereas a legitimate quarantine excludes a suitable one. Manual review can overturn an initial assignment when additional evidence or a better interpretation becomes available. Raising the filter cutoff usually reduces spam admission but increases legitimate quarantine, while lowering it has the opposite trade-off. Statistical decision theory studies how thresholds should be selected when the two errors have unequal consequences.”

**Form (b)** — “A spam filter scores messages from their features and compares those scores with a cutoff. Messages above or below the cutoff are sent either to the inbox or to quarantine. Obfuscated or adversarial wording can make the classifier accept spam or quarantine legitimate mail. Manual review can reverse that initial decision when more evidence or a better interpretation is available. A stricter cutoff generally blocks more spam but also traps more legitimate messages; a looser cutoff reverses those error rates. Statistical decision theory analyzes which trade-off is appropriate when the costs differ.”

### Border admission

**Form (a)** — “A border-control procedure evaluates each traveler by extracting passport and visa and comparing them with a proof standard on an admissibility score. The border officer assigns the traveler to entry authorization or entry refusal. Because document ambiguity can distort evidence, an inadmissible admission admits an unsuitable traveler, whereas an admissible refusal excludes a suitable one. Secondary inspection can overturn an initial assignment when additional evidence or a better interpretation becomes available. Raising the proof standard usually reduces inadmissible admission but increases admissible refusal, while lowering it has the opposite trade-off. Immigration administration studies how thresholds should be selected when the two errors have unequal consequences.”

**Form (b)** — “Border control compares a traveler’s passport and visa evidence with the required standard of admissibility. The officer must authorize entry or refuse it. Ambiguous documents can lead to an inadmissible person being admitted or an admissible person being refused. Secondary inspection can reverse the first decision when further evidence or a better reading of the evidence appears. A higher evidentiary standard reduces mistaken admissions but increases mistaken refusals; a lower standard does the reverse. Immigration administration studies how to choose that threshold when the consequences of the two mistakes differ.”

### Cancer screening

**Form (a)** — “A screening program evaluates each patient by extracting test result and comparing it with a referral cutoff on a disease-risk score. The clinician assigns the patient to treatment referral or no referral. Because measurement error can distort evidence, an unnecessary referral refers an unsuitable patient, whereas a missed referral excludes a suitable one. Confirmatory testing can overturn an initial assignment when additional evidence or a better interpretation becomes available. Raising the referral cutoff usually reduces unnecessary referral but increases missed referral, while lowering it has the opposite trade-off. Medical screening studies how thresholds should be selected when the two errors have unequal consequences.”

**Form (b)** — “A screening program uses a test result to estimate a patient’s disease risk and compares that estimate with the referral cutoff. The clinician either refers the patient for treatment or does not refer them. Measurement error can produce unnecessary referrals as well as missed referrals. Confirmatory testing can change the initial classification when further evidence or a more accurate interpretation is obtained. Raising the cutoff generally reduces unnecessary referrals but increases missed cases; lowering it has the opposite effect. Medical screening studies how to set the cutoff when those two errors do not carry equal costs.”

### Consumer lending

**Form (a)** — “A lending institution evaluates each loan applicant by extracting financial documentation and comparing it with an approval cutoff on a default-risk score. The underwriting model assigns the applicant to loan approval or loan denial. Because missing financial data can distort evidence, a risky approval approves an unsuitable applicant, whereas a creditworthy denial excludes a suitable one. Human underwriting review can overturn an initial assignment when additional evidence or a better interpretation becomes available. Raising the approval cutoff usually reduces risky approval but increases creditworthy denial, while lowering it has the opposite trade-off. Credit-risk analysis studies how thresholds should be selected when the two errors have unequal consequences.”

**Form (b)** — “A lender derives a default-risk score from an applicant’s financial documentation and compares it with the approval cutoff. The underwriting model then approves or denies the loan. Incomplete information can cause the lender to approve a risky borrower or deny a creditworthy one. Human underwriting review can reverse the first decision when additional evidence or a better interpretation is available. A higher cutoff reduces risky approvals but also denies more creditworthy applicants; a lower cutoff produces the opposite trade-off. Credit-risk analysis studies how to choose the cutoff when the losses from the two errors differ.”

### Research grants

**Form (a)** — “A grant-selection process evaluates each research proposal by extracting proposal evidence and comparing it with a funding cutoff on a merit score. The review panel assigns the proposal to grant funding or proposal rejection. Because reviewer disagreement can distort evidence, weak proposal funding funds an unsuitable proposal, whereas strong proposal rejection excludes a suitable one. Applicant rebuttal can overturn an initial assignment when additional evidence or a better interpretation becomes available. Raising the funding cutoff usually reduces weak proposal funding but increases strong proposal rejection, while lowering it has the opposite trade-off. Research evaluation studies how thresholds should be selected when the two errors have unequal consequences.”

**Form (b)** — “A grant panel evaluates the evidence in each proposal and compares its merit score with the funding cutoff. It then funds the proposal or rejects it. Disagreement among reviewers can lead to a weak proposal being funded or a strong proposal being rejected. An applicant’s rebuttal can change the initial outcome when it supplies additional evidence or clarifies the proposal. Raising the cutoff reduces weak awards but increases the number of strong proposals rejected; lowering it reverses that trade-off. Research evaluation studies how to set the cutoff when the consequences of the two mistakes are unequal.”

---

## Archetype Proposal: Depleting Shared Stocks

### Context-template

“A [RESOURCE SYSTEM] contains a shared [STOCK] that changes through [REPLENISHMENT] and [WITHDRAWAL]. Each [USER] can gain immediate benefit by increasing [WITHDRAWAL], but collective withdrawal can exceed replenishment, especially when a [DEPLETION DELAY] hides decline. Because the condition of the stock affects future users, [GOVERNANCE] combines [MONITORING], [ALLOCATION RULE], and [SANCTION]. If the stock falls below its [RECOVERY THRESHOLD], natural [RECOVERY] may be slow or uncertain. [RESOURCE ECONOMICS] distinguishes sustainable [YIELD] from [LIQUIDATION] and studies how institutions can align individual use with long-term stock maintenance.”

### Metanym table

| Slot | Marine fishery | Groundwater basin | Shared pasture | Irrigation reservoir | Managed forest |
|---|---|---|---|---|---|
| RESOURCE SYSTEM | coastal fishery | aquifer system | communal pasture | irrigation reservoir | managed forest |
| STOCK | fish biomass | groundwater storage | forage biomass | stored water | standing timber |
| REPLENISHMENT | fish recruitment | aquifer recharge | plant growth | watershed inflow | tree growth |
| WITHDRAWAL | fish harvest | groundwater pumping | livestock grazing | irrigation release | timber harvest |
| USER | fisher | well owner | herder | farming district | timber concession |
| DEPLETION DELAY | delayed stock assessment | delayed water-level measurement | seasonal grazing lag | delayed drought recognition | forest-inventory lag |
| GOVERNANCE | fishery management | groundwater authority | pasture association | reservoir authority | forestry administration |
| MONITORING | catch-and-stock survey | water-level monitoring | grazing-pressure survey | reservoir-level monitoring | forest inventory |
| ALLOCATION RULE | catch quota | pumping allotment | stocking limit | water allocation | harvest limit |
| SANCTION | fishing closure | pumping penalty | grazing exclusion | excess-use penalty | logging penalty |
| RECOVERY THRESHOLD | minimum spawning biomass | minimum aquifer level | minimum ground cover | conservation-pool level | minimum regeneration density |
| RECOVERY | stock rebuilding | aquifer recharge | pasture rest and reseeding | reservoir refill | forest regeneration |
| YIELD | sustainable catch | sustainable extraction | sustainable stocking | reliable water yield | annual allowable cut |
| LIQUIDATION | stock collapse | aquifer depletion | pasture degradation | reservoir exhaustion | clear-cut liquidation |

### Marine fishery

**Form (a)** — “A coastal fishery contains a shared fish biomass that changes through fish recruitment and fish harvest. Each fisher can gain immediate benefit by increasing fish harvest, but collective harvest can exceed recruitment, especially when a delayed stock assessment hides decline. Because the condition of the stock affects future fishers, fishery management combines catch-and-stock survey, catch quota, and fishing closure. If the stock falls below its minimum spawning biomass, natural stock rebuilding may be slow or uncertain. Resource economics distinguishes sustainable catch from stock collapse and studies how institutions can align individual use with long-term stock maintenance.”

**Form (b)** — “A fishery depends on a shared biomass that is replenished by recruitment and reduced by harvesting. Any fisher can benefit immediately from catching more, but the fleet as a whole can remove fish faster than the population replaces them. Delayed stock assessments can conceal that decline. Fishery management therefore uses surveys, quotas, and closures. Once spawning biomass falls below a critical level, rebuilding may be slow or uncertain. Resource economics distinguishes a sustainable catch from liquidating the stock and asks how institutions can make individual incentives compatible with long-term maintenance.”

### Groundwater basin

**Form (a)** — “An aquifer system contains a shared groundwater storage that changes through aquifer recharge and groundwater pumping. Each well owner can gain immediate benefit by increasing groundwater pumping, but collective pumping can exceed recharge, especially when a delayed water-level measurement hides decline. Because the condition of the stock affects future well owners, groundwater authority combines water-level monitoring, pumping allotment, and pumping penalty. If the stock falls below its minimum aquifer level, natural aquifer recharge may be slow or uncertain. Resource economics distinguishes sustainable extraction from aquifer depletion and studies how institutions can align individual use with long-term stock maintenance.”

**Form (b)** — “An aquifer stores groundwater that is replenished by recharge and depleted by pumping. Each well owner benefits immediately from pumping more, but the basin’s users can collectively withdraw water faster than it is replenished. Delayed water-level measurements may hide the decline. A groundwater authority consequently relies on monitoring, pumping allotments, and penalties. If the aquifer falls below its minimum level, natural recharge may restore it only slowly or uncertainly. Resource economics distinguishes sustainable extraction from depletion and studies institutions that align private pumping with the basin’s long-term condition.”

### Shared pasture

**Form (a)** — “A communal pasture contains a shared forage biomass that changes through plant growth and livestock grazing. Each herder can gain immediate benefit by increasing livestock grazing, but collective grazing can exceed plant growth, especially when a seasonal grazing lag hides decline. Because the condition of the stock affects future herders, pasture association combines grazing-pressure survey, stocking limit, and grazing exclusion. If the stock falls below its minimum ground cover, natural pasture rest and reseeding may be slow or uncertain. Resource economics distinguishes sustainable stocking from pasture degradation and studies how institutions can align individual use with long-term stock maintenance.”

**Form (b)** — “A communal pasture supports a shared stock of forage, which plant growth replenishes and livestock grazing depletes. Each herder gains in the short term by grazing more animals, but all herders together can consume forage faster than it grows. Seasonal lags can conceal the deterioration until the pasture is already stressed. A pasture association uses grazing surveys, stocking limits, and exclusion rules to govern use. If ground cover falls below its minimum level, resting and reseeding the pasture may recover it only slowly or uncertainly. Resource economics distinguishes sustainable stocking from degrading the pasture and studies institutions that reconcile individual and collective interests.”

### Irrigation reservoir

**Form (a)** — “An irrigation reservoir contains a shared stored water that changes through watershed inflow and irrigation release. Each farming district can gain immediate benefit by increasing irrigation release, but collective release can exceed inflow, especially when a delayed drought recognition hides decline. Because the condition of the stock affects future farming districts, reservoir authority combines reservoir-level monitoring, water allocation, and excess-use penalty. If the stock falls below its conservation-pool level, natural reservoir refill may be slow or uncertain. Resource economics distinguishes reliable water yield from reservoir exhaustion and studies how institutions can align individual use with long-term stock maintenance.”

**Form (b)** — “An irrigation reservoir stores water supplied by watershed inflow and depleted by irrigation releases. Each farming district benefits immediately from releasing more water, but the districts together can release more than the watershed replaces. If drought is recognized late, the falling storage level may remain hidden until reserves are seriously reduced. The reservoir authority therefore monitors levels, allocates water, and penalizes excess use. Once storage falls below the conservation pool, natural refill may be slow or uncertain. Resource economics distinguishes a reliable yield from exhausting the reservoir and studies institutions that coordinate use over time.”

### Managed forest

**Form (a)** — “A managed forest contains a shared standing timber that changes through tree growth and timber harvest. Each timber concession can gain immediate benefit by increasing timber harvest, but collective harvest can exceed tree growth, especially when a forest-inventory lag hides decline. Because the condition of the stock affects future timber concessions, forestry administration combines forest inventory, harvest limit, and logging penalty. If the stock falls below its minimum regeneration density, natural forest regeneration may be slow or uncertain. Resource economics distinguishes annual allowable cut from clear-cut liquidation and studies how institutions can align individual use with long-term stock maintenance.”

**Form (b)** — “A managed forest is a shared stock of standing timber, replenished by tree growth and reduced by logging. Each concession can profit immediately from cutting more, but all concessions together can harvest faster than the forest grows. Delays in forest inventories can conceal the decline. Forestry administration uses inventories, harvest limits, and logging penalties to govern the stock. If regeneration density falls below its minimum, natural recovery may be slow or uncertain. Resource economics distinguishes an annual allowable cut from liquidating the forest and studies institutions that make concession-level decisions compatible with long-term maintenance.”

---

## Archetype Proposal: Network Cascades

### Context-template

“A [NETWORK] consists of [NODE] linked by [LINK]. A [TRIGGER] can move from one node to another, causing the receiving node to enter [STATE] when [EXPOSURE] exceeds a [THRESHOLD]; the resulting [TRANSMISSION] depends on topology and timing. A highly connected [AMPLIFIER] can increase spread, while a [CLUSTER] can sustain local persistence even when distant nodes are unaffected. Once a [CASCADE] begins, targeted [INTERVENTION] at a [TARGET] can lower the effective [GROWTH FACTOR] below one. Delay, however, allows more [NODE] to enter [STATE]. [NETWORK SCIENCE] studies how connectivity, thresholds, clustering, and intervention shape collective cascades.”

### Metanym table

| Slot | Infectious disease | Bank run | Power grid failure | Computer malware | Social rumor |
|---|---|---|---|---|---|
| NETWORK | contact network | depositor network | electric grid | computer network | social network |
| NODE | person | account holder | substation | device | person |
| LINK | physical contact | banking relationship | transmission line | network connection | social tie |
| TRIGGER | infected person | withdrawal request | line overload | infected device | rumor post |
| STATE | infection | withdrawal | protective trip | compromise | belief adoption |
| EXPOSURE | infectious dose | withdrawal signal | electrical load | malicious payload | repeated claim |
| THRESHOLD | susceptibility threshold | confidence threshold | relay threshold | vulnerability threshold | credulity threshold |
| TRANSMISSION | pathogen spread | depositor imitation | fault propagation | malware propagation | social sharing |
| AMPLIFIER | superspreader | institutional depositor | heavily loaded interconnector | exposed server | influencer |
| CLUSTER | household | regional depositor group | electrical island | subnet | online community |
| CASCADE | outbreak | bank run | blackout cascade | malware outbreak | viral rumor |
| INTERVENTION | vaccination and isolation | liquidity guarantee | load shedding | patching and isolation | fact-checking |
| TARGET | high-contact person | exposed account holder | overloaded line | vulnerable device | high-reach account |
| GROWTH FACTOR | effective reproduction number | withdrawal propagation ratio | outage branching factor | effective infection rate | sharing ratio |
| NETWORK SCIENCE | epidemiology | financial-network analysis | power-systems engineering | cybersecurity | computational sociology |

### Infectious disease

**Form (a)** — “A contact network consists of people linked by physical contact. An infected person can move from one person to another, causing the receiving person to enter infection when infectious dose exceeds a susceptibility threshold; the resulting pathogen spread depends on topology and timing. A highly connected superspreader can increase spread, while a household can sustain local persistence even when distant people are unaffected. Once an outbreak begins, targeted vaccination and isolation at a high-contact person can lower the effective reproduction number below one. Delay, however, allows more people to enter infection. Epidemiology studies how connectivity, thresholds, clustering, and intervention shape collective cascades.”

**Form (b)** — “Infectious disease spreads through a contact network of people connected by physical contact. An infected person can infect another when the exposure exceeds that person’s susceptibility threshold, and the resulting pathogen spread depends on who contacts whom and when. Superspreaders can accelerate transmission, while households can maintain local transmission even without affecting distant groups. Once an outbreak is underway, vaccinating or isolating high-contact people can reduce the effective reproduction number below one. Delayed intervention permits more people to become infected. Epidemiology studies how network structure, thresholds, clustering, and intervention determine outbreaks.”

### Bank run

**Form (a)** — “A depositor network consists of account holders linked by banking relationships. A withdrawal request can move from one account holder to another, causing the receiving account holder to enter withdrawal when withdrawal signal exceeds a confidence threshold; the resulting depositor imitation depends on topology and timing. A highly connected institutional depositor can increase spread, while a regional depositor group can sustain local persistence even when distant account holders are unaffected. Once a bank run begins, targeted liquidity guarantee at an exposed account holder can lower the effective withdrawal propagation ratio below one. Delay, however, allows more account holders to enter withdrawal. Financial-network analysis studies how connectivity, thresholds, clustering, and intervention shape collective cascades.”

**Form (b)** — “A bank run can propagate through a network of account holders connected by banking relationships. One withdrawal request can prompt another account holder to withdraw when the withdrawal signal exceeds that person’s confidence threshold. Institutional depositors can amplify the process, while a regional group of depositors can maintain a local run even when distant customers remain calm. Once the run has begun, a liquidity guarantee directed at exposed account holders can reduce the withdrawal propagation ratio below one. Delaying that intervention allows more account holders to withdraw. Financial-network analysis studies how depositor connectivity, confidence thresholds, clusters, and interventions shape runs.”

### Power grid failure

**Form (a)** — “An electric grid consists of substations linked by transmission lines. A line overload can move from one substation to another, causing the receiving substation to enter protective trip when electrical load exceeds a relay threshold; the resulting fault propagation depends on topology and timing. A highly connected heavily loaded interconnector can increase spread, while an electrical island can sustain local persistence even when distant substations are unaffected. Once a blackout cascade begins, targeted load shedding at an overloaded line can lower the effective outage branching factor below one. Delay, however, allows more substations to enter protective trip. Power-systems engineering studies how connectivity, thresholds, clustering, and intervention shape collective cascades.”

**Form (b)** — “In an electric grid, substations are connected by transmission lines, and an overload can propagate through those connections. A receiving substation trips when its electrical load exceeds the relevant relay threshold; the pattern and timing of the resulting fault propagation depend on grid topology. A heavily loaded interconnector can amplify failures, while an electrical island can continue experiencing local trips without immediately affecting distant parts of the grid. Once a blackout cascade starts, shedding load around an overloaded line can reduce the outage branching factor below one. Delayed shedding allows more substations to trip. Power-systems engineering studies how grid structure, protection thresholds, clustering, and intervention shape cascading failures.”

### Computer malware

**Form (a)** — “A computer network consists of devices linked by network connections. An infected device can move from one device to another, causing the receiving device to enter compromise when malicious payload exceeds a vulnerability threshold; the resulting malware propagation depends on topology and timing. An exposed server can increase spread, while a subnet can sustain local persistence even when distant devices are unaffected. Once a malware outbreak begins, targeted patching and isolation at a vulnerable device can lower the effective infection rate below one. Delay, however, allows more devices to enter compromise. Cybersecurity studies how connectivity, thresholds, clustering, and intervention shape collective cascades.”

**Form (b)** — “Malware spreads through a computer network whose devices are connected by network links. An infected device can compromise another when the malicious payload exceeds that device’s vulnerability threshold. The propagation pattern depends on the network’s topology and on timing. An exposed server can amplify the outbreak, while a subnet can sustain local compromise without immediately affecting distant devices. Once an outbreak begins, patching or isolating vulnerable devices can reduce the effective infection rate below one; delay lets more devices become compromised. Cybersecurity studies how connectivity, thresholds, clustering, and intervention shape malware cascades.”

### Social rumor

**Form (a)** — “A social network consists of people linked by social ties. A rumor post can move from one person to another, causing the receiving person to enter belief adoption when repeated claim exceeds a credulity threshold; the resulting social sharing depends on topology and timing. An influential influencer can increase spread, while an online community can sustain local persistence even when distant people are unaffected. Once a viral rumor begins, targeted fact-checking at a high-reach account can lower the effective sharing ratio below one. Delay, however, allows more people to enter belief adoption. Computational sociology studies how connectivity, thresholds, clustering, and intervention shape collective cascades.”

**Form (b)** — “A rumor spreads through a social network of people connected by social ties. Repeated exposure to a rumor post can lead another person to adopt the belief once it exceeds that person’s credulity threshold. Sharing depends on who is connected to whom and on the timing of the exposures. An influencer can amplify the rumor, while an online community can keep it circulating locally even when distant users are unaffected. Once the rumor becomes viral, fact-checking a high-reach account can reduce the sharing ratio below one. Delayed fact-checking allows more people to adopt the belief. Computational sociology studies how network structure, thresholds, clusters, and interventions shape rumor cascades.”

None of these five archetypes is recursive in the cell–organ–human sense; they are distinct nonrecursive structures: feedback regulation, queue accumulation, threshold classification, stock depletion, and network cascade.