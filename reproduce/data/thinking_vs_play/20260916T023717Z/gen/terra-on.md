## Archetype Proposal: Cascading Load Redistribution

### Context-template

“A [NETWORK] conveys [FLOW] among interconnected [NODE]. Every [NODE] has a finite [CAPACITY], normally bears a [LOAD], and relies on [RESERVE] to absorb ordinary fluctuations. When a [SHOCK] removes a [NODE] or sharply increases its [LOAD], some of that [LOAD] is redistributed through remaining connections. If the transferred [LOAD] drives another [NODE] beyond its [CAPACITY], that [NODE] also ceases to carry [FLOW], and a [CASCADE] can follow. [PROTECTION] detects stress and sheds, reroutes, or isolates [LOAD] before propagation; nevertheless, tight coupling and small [RESERVE] make a [NETWORK] efficient in quiet conditions yet fragile under correlated [SHOCK]. [NETWORK] analysis therefore asks not only which [NODE] is likely to fail, but how the pattern of connections converts a local [SHOCK] into system-wide loss of [FLOW].”

### Metanym table

| [SLOT] | Power Grid | Internet | Road Network | Hospital System | Supply Chain |
|---|---|---|---|---|---|
| NETWORK | power grid | internet | road network | hospital system | supply chain |
| FLOW | electricity | data | vehicle | patient | material |
| NODE | substation | router | intersection | hospital | facility |
| CAPACITY | transmission capacity | forwarding capacity | throughput capacity | bed capacity | throughput capacity |
| LOAD | power load | traffic load | traffic load | patient load | order load |
| RESERVE | operating reserve | spare bandwidth | spare capacity | surge capacity | safety stock |
| SHOCK | line outage | denial-of-service attack | road closure | mass-casty event | plant shutdown |
| CASCADE | blackout | service outage | gridlock | care disruption | shortage cascade |
| PROTECTION | relay protection | congestion control | traffic management | surge management | inventory management |

### Power Grid

**Form (a)**  
“A power grid conveys electricity among interconnected substations. Every substation has a finite transmission capacity, normally bears a power load, and relies on operating reserve to absorb ordinary fluctuations. When a line outage removes a substation or sharply increases its power load, some of that power load is redistributed through remaining connections. If the transferred power load drives another substation beyond its transmission capacity, that substation also ceases to carry electricity, and a blackout can follow. Relay protection detects stress and sheds, reroutes, or isolates power load before propagation; nevertheless, tight coupling and small operating reserves make a power grid efficient in quiet conditions yet fragile under correlated line outages. Power-grid analysis therefore asks not only which substation is likely to fail, but how the pattern of connections converts a local line outage into system-wide loss of electricity.”

**Form (b)**  
“A grid moves electricity through interconnected substations, each with limited transmission capacity, ordinary loading, and operating reserves for routine variation. A line outage can remove a substation or force extra power onto others; that burden is then redistributed across the surviving network. If the added loading exceeds another substation’s transmission capacity, it too drops out, potentially initiating a blackout. Relay protection attempts to shed, reroute, or isolate stressed power before failure propagates, but tightly coupled grids with little reserve are efficient in normal operation and vulnerable to correlated outages. Accordingly, grid analysis examines both the first likely failure and the network pathways by which one outage becomes a system-wide loss of supply.”

### Internet

**Form (a)**  
“The internet conveys data among interconnected routers. Every router has a finite forwarding capacity, normally bears a traffic load, and relies on spare bandwidth to absorb ordinary fluctuations. When a denial-of-service attack removes a router or sharply increases its traffic load, some of that traffic load is redistributed through remaining connections. If the transferred traffic load drives another router beyond its forwarding capacity, that router also ceases to carry data, and a service outage can follow. Congestion control detects stress and sheds, reroutes, or isolates traffic load before propagation; nevertheless, tight coupling and small spare bandwidth make the internet efficient in quiet conditions yet fragile under correlated denial-of-service attacks. Internet analysis therefore asks not only which router is likely to fail, but how the pattern of connections converts a local denial-of-service attack into system-wide loss of data.”

**Form (b)**  
“The internet carries data through routers that have finite forwarding capacity and depend on spare bandwidth to absorb ordinary demand variation. A denial-of-service attack can disable a router or sharply raise its traffic burden, pushing traffic onto alternate paths. When that transferred traffic overwhelms another router, the second router also stops forwarding data and the disruption can become a service outage. Congestion-control mechanisms try to shed, reroute, or isolate traffic before the disturbance spreads, yet tightly coupled networks with little spare bandwidth trade normal efficiency for vulnerability to coordinated attacks. The central question is therefore not merely which router fails first, but how topology turns a local attack into broad data loss.”

### Road Network

**Form (a)**  
“A road network conveys vehicles among interconnected intersections. Every intersection has a finite throughput capacity, normally bears a traffic load, and relies on spare capacity to absorb ordinary fluctuations. When a road closure removes an intersection or sharply increases its traffic load, some of that traffic load is redistributed through remaining connections. If the transferred traffic load drives another intersection beyond its throughput capacity, that intersection also ceases to carry vehicles, and gridlock can follow. Traffic management detects stress and sheds, reroutes, or isolates traffic load before propagation; nevertheless, tight coupling and small spare capacity make a road network efficient in quiet conditions yet fragile under correlated road closures. Road-network analysis therefore asks not only which intersection is likely to fail, but how the pattern of connections converts a local road closure into system-wide loss of vehicle movement.”

**Form (b)**  
“A road system moves vehicles through intersections whose throughput is limited and whose spare capacity absorbs everyday variation. A closure can eliminate an intersection or divert additional traffic onto nearby streets. If those transfers exceed another intersection’s throughput, that junction also becomes unable to pass vehicles, allowing gridlock to spread. Traffic management can meter, reroute, or isolate traffic before congestion propagates, but a tightly coupled network with little spare capacity is efficient in calm conditions and brittle during multiple closures. Transport analysis therefore studies both the initial bottleneck and the connection pattern that turns one closure into network-wide immobility.”

### Hospital System

**Form (a)**  
“A hospital system conveys patients among interconnected hospitals. Every hospital has a finite bed capacity, normally bears a patient load, and relies on surge capacity to absorb ordinary fluctuations. When a mass-casualty event removes a hospital or sharply increases its patient load, some of that patient load is redistributed through remaining connections. If the transferred patient load drives another hospital beyond its bed capacity, that hospital also ceases to carry patients, and care disruption can follow. Surge management detects stress and sheds, reroutes, or isolates patient load before propagation; nevertheless, tight coupling and small surge capacity make a hospital system efficient in quiet conditions yet fragile under correlated mass-casualty events. Hospital-system analysis therefore asks not only which hospital is likely to fail, but how the pattern of connections converts a local mass-casualty event into system-wide loss of patient care.”

**Form (b)**  
“A hospital system distributes patients across hospitals with finite beds, ordinary occupancy, and some surge capacity for routine fluctuations. A mass-casualty event can incapacitate one hospital or abruptly increase its demand, forcing patients toward the remaining facilities. If those transfers exceed another hospital’s bed capacity, that facility too may be unable to receive patients, producing wider care disruption. Surge management seeks to divert, defer, or isolate patient flows before overload spreads, but systems designed with little slack are efficient in ordinary periods and vulnerable to simultaneous emergencies. The relevant systems question is therefore both where overload begins and how referral connections transform a local emergency into a regional loss of care.”

### Supply Chain

**Form (a)**  
“A supply chain conveys material among interconnected facilities. Every facility has a finite throughput capacity, normally bears an order load, and relies on safety stock to absorb ordinary fluctuations. When a plant shutdown removes a facility or sharply increases its order load, some of that order load is redistributed through remaining connections. If the transferred order load drives another facility beyond its throughput capacity, that facility also ceases to carry material, and a shortage cascade can follow. Inventory management detects stress and sheds, reroutes, or isolates order load before propagation; nevertheless, tight coupling and small safety stocks make a supply chain efficient in quiet conditions yet fragile under correlated plant shutdowns. Supply-chain analysis therefore asks not only which facility is likely to fail, but how the pattern of connections converts a local plant shutdown into system-wide loss of material.”

**Form (b)**  
“A supply chain moves material among facilities with limited throughput, normal order burdens, and safety stocks for routine variation. A plant shutdown can remove a facility or concentrate orders on the surviving ones. If the transferred demand exceeds another facility’s throughput, that facility can also stop moving material, creating a shortage cascade. Inventory management can ration, reroute, or isolate orders before the disturbance propagates, but tightly coupled chains with thin safety stocks are efficient in normal periods and fragile when shutdowns are correlated. Supply-chain analysis thus asks not only which site breaks first, but how network structure converts one shutdown into widespread material unavailability.”

---

## Archetype Proposal: Negative-Feedback Regulation

### Context-template

“A [SYSTEM] regulates [VARIABLE] around a [TARGET] despite [DISTURBANCE]. A [SENSOR] samples [VARIABLE], and a [CONTROLLER] compares the measurement with [TARGET] to compute a [COMMAND]. An [ACTUATOR] changes [VARIABLE] in response to that [COMMAND]; the changed [VARIABLE] is then measured again, closing a negative-feedback loop. The loop works only within its [RANGE], and its effectiveness is limited by measurement noise, [DELAY], and the strength of the [RESPONSE]. If [DELAY] is long or [RESPONSE] too strong, corrections can overshoot and produce [OSCILLATION] rather than stable regulation. [DISCIPLINE] designs or studies this trade-off between rapid disturbance rejection and stability.”

### Metanym table

| [SLOT] | Climate-Control System | Human Body | Automobile | Economy | Project Organization |
|---|---|---|---|---|---|
| SYSTEM | climate-control system | human body | automobile | economy | project organization |
| VARIABLE | room temperature | blood glucose | road speed | inflation | work backlog |
| TARGET | temperature setpoint | glucose setpoint | speed setpoint | inflation target | backlog target |
| DISTURBANCE | outdoor weather | meal | road grade | demand shock | demand surge |
| SENSOR | thermometer | glucose-sensing cell | speed sensor | price index | work-tracking dashboard |
| CONTROLLER | thermostat | pancreas | cruise controller | central bank | operations manager |
| COMMAND | heating signal | insulin signal | throttle command | policy-rate change | staffing adjustment |
| ACTUATOR | heating unit | insulin release | throttle | interest-rate mechanism | staffing process |
| RANGE | operating range | physiological range | operating range | policy range | staffing range |
| DELAY | thermal lag | hormonal delay | actuator lag | policy lag | hiring delay |
| RESPONSE | heating gain | insulin response | control gain | policy response | staffing response |
| OSCILLATION | temperature cycling | glycemic oscillation | speed hunting | inflation volatility | backlog oscillation |
| DISCIPLINE | control engineering | endocrinology | control engineering | macroeconomics | operations management |

### Climate-Control System

**Form (a)**  
“A climate-control system regulates room temperature around a temperature setpoint despite outdoor weather. A thermometer samples room temperature, and a thermostat compares the measurement with the temperature setpoint to compute a heating signal. A heating unit changes room temperature in response to that heating signal; the changed room temperature is then measured again, closing a negative-feedback loop. The loop works only within its operating range, and its effectiveness is limited by measurement noise, thermal lag, and the strength of the heating gain. If thermal lag is long or heating gain too strong, corrections can overshoot and produce temperature cycling rather than stable regulation. Control engineering designs or studies this trade-off between rapid disturbance rejection and stability.”

**Form (b)**  
“A climate-control system holds room temperature near its setpoint despite changes in outdoor weather. The thermometer measures temperature, the thermostat compares that reading with the setpoint, and it issues a heating signal. The heating unit changes the temperature, which is measured again to close the negative-feedback loop. Regulation is limited by the equipment’s operating range, sensor noise, thermal lag, and heating gain; excessive lag or gain can cause overshoot and temperature cycling instead of stability. Control engineering studies the resulting trade-off between fast rejection of weather disturbances and stable operation.”

### Human Body

**Form (a)**  
“A human body regulates blood glucose around a glucose setpoint despite a meal. A glucose-sensing cell samples blood glucose, and the pancreas compares the measurement with the glucose setpoint to compute an insulin signal. Insulin release changes blood glucose in response to that insulin signal; the changed blood glucose is then measured again, closing a negative-feedback loop. The loop works only within its physiological range, and its effectiveness is limited by measurement noise, hormonal delay, and the strength of the insulin response. If hormonal delay is long or insulin response too strong, corrections can overshoot and produce glycemic oscillation rather than stable regulation. Endocrinology designs or studies this trade-off between rapid disturbance rejection and stability.”

**Form (b)**  
“The body regulates blood glucose around a physiological setpoint despite disturbances such as a meal. Glucose-sensing cells detect blood glucose, and the pancreas uses that information relative to the setpoint to generate an insulin signal. Insulin release alters glucose concentration, which is sensed again and thereby closes the negative-feedback loop. This regulation is bounded by physiological range and constrained by measurement noise, hormonal delay, and insulin responsiveness; excessive delay or response can produce overshoot and glycemic oscillation rather than stability. Endocrinology studies how the system balances rapid correction of disturbances against stable glucose control.”

### Automobile

**Form (a)**  
“An automobile regulates road speed around a speed setpoint despite road grade. A speed sensor samples road speed, and a cruise controller compares the measurement with the speed setpoint to compute a throttle command. A throttle changes road speed in response to that throttle command; the changed road speed is then measured again, closing a negative-feedback loop. The loop works only within its operating range, and its effectiveness is limited by measurement noise, actuator lag, and the strength of the control gain. If actuator lag is long or control gain too strong, corrections can overshoot and produce speed hunting rather than stable regulation. Control engineering designs or studies this trade-off between rapid disturbance rejection and stability.”

**Form (b)**  
“Cruise control holds an automobile near its selected road speed despite disturbances such as a changing road grade. A speed sensor supplies the measurement, the cruise controller compares it with the speed setpoint, and the controller sends a throttle command. Throttle action changes speed, which is measured again to close the negative-feedback loop. Performance is limited by operating range, sensor noise, actuator lag, and control gain; excessive lag or gain can make the vehicle overshoot and hunt around the target speed. Control engineering analyzes the trade-off between quickly rejecting grade disturbances and maintaining stable speed.”

### Economy

**Form (a)**  
“An economy regulates inflation around an inflation target despite a demand shock. A price index samples inflation, and a central bank compares the measurement with the inflation target to compute a policy-rate change. An interest-rate mechanism changes inflation in response to that policy-rate change; the changed inflation is then measured again, closing a negative-feedback loop. The loop works only within its policy range, and its effectiveness is limited by measurement noise, policy lag, and the strength of the policy response. If policy lag is long or policy response too strong, corrections can overshoot and produce inflation volatility rather than stable regulation. Macroeconomics designs or studies this trade-off between rapid disturbance rejection and stability.”

**Form (b)**  
“In a monetary-policy framework, the economy is steered toward an inflation target despite demand shocks. A price index measures inflation, and the central bank compares that measurement with the target before changing policy rates. Interest-rate transmission then influences inflation, which is measured again, forming a negative-feedback loop. The process operates within a policy range and is limited by noisy measurement, policy lags, and the strength of the policy response; long lags or excessive response can overshoot and generate inflation volatility. Macroeconomics studies the trade-off between rapid stabilization of shocks and stable inflation control.”

### Project Organization

**Form (a)**  
“A project organization regulates work backlog around a backlog target despite a demand surge. A work-tracking dashboard samples work backlog, and an operations manager compares the measurement with the backlog target to compute a staffing adjustment. A staffing process changes work backlog in response to that staffing adjustment; the changed work backlog is then measured again, closing a negative-feedback loop. The loop works only within its staffing range, and its effectiveness is limited by measurement noise, hiring delay, and the strength of the staffing response. If hiring delay is long or staffing response too strong, corrections can overshoot and produce backlog oscillation rather than stable regulation. Operations management designs or studies this trade-off between rapid disturbance rejection and stability.”

**Form (b)**  
“A project organization tries to hold its work backlog near a target even when demand surges. A work-tracking dashboard measures the backlog, an operations manager compares it with the target, and the manager makes a staffing adjustment. Staffing changes the backlog, which is then measured again to close the negative-feedback loop. This process is limited by available staffing range, measurement noise, hiring delay, and the size of the staffing response; delayed or excessive hiring can overshoot and create backlog oscillation. Operations management studies how to balance rapid response to demand shocks against stable workload control.”

---

## Archetype Proposal: Recursive Modular Composition

**Recursive archetype:** a module at one scale may itself be a composite of modules at a lower scale.

### Context-template

“A [SYSTEM] achieves [FUNCTION] by arranging [MODULE] into a [ARCHITECTURE]. Each [MODULE] presents an [INTERFACE] that specifies the [SERVICE] it will provide while concealing its internal [IMPLEMENTATION]. A [COMPOSITE] can therefore combine [MODULE] by depending on their [INTERFACE], and a [MODULE] at one scale can itself be a [COMPOSITE] at a lower scale. This layering permits [CHANGE] inside a [MODULE] without redesigning every [COMPOSITE] that uses it, provided its [INTERFACE] remains compatible. It also localizes many [FAULT], although an [INTERFACE] mismatch can disable otherwise sound [MODULE] across the [SYSTEM]. [DISCIPLINE] studies how to choose boundaries, interfaces, and layers so that coordination is possible without exposing needless detail.”

### Metanym table

| [SLOT] | Software System | Electronic Device | Multicellular Organism | Firm | Manufactured Product |
|---|---|---|---|---|---|
| SYSTEM | software system | electronic device | multicellular organism | firm | manufactured product |
| FUNCTION | computation | signal processing | physiological function | production | mechanical function |
| MODULE | software module | circuit block | cell | team | component |
| ARCHITECTURE | software architecture | circuit architecture | tissue architecture | organizational structure | product architecture |
| INTERFACE | application programming interface | terminal interface | membrane interface | role interface | mechanical interface |
| SERVICE | operation | signal function | regulated exchange | deliverable | motion |
| IMPLEMENTATION | code | circuitry | molecular machinery | internal workflow | internal mechanism |
| COMPOSITE | application | subsystem | tissue | department | subassembly |
| CHANGE | refactoring | component revision | molecular change | process change | design revision |
| FAULT | bug | electrical fault | cell defect | coordination failure | defect |
| DISCIPLINE | software engineering | electrical engineering | systems biology | organization design | systems engineering |

### Software System

**Form (a)**  
“A software system achieves computation by arranging software modules into a software architecture. Each software module presents an application programming interface that specifies the operation it will provide while concealing its internal code. An application can therefore combine software modules by depending on their application programming interfaces, and a software module at one scale can itself be an application at a lower scale. This layering permits refactoring inside a software module without redesigning every application that uses it, provided its application programming interface remains compatible. It also localizes many bugs, although an application programming interface mismatch can disable otherwise sound software modules across the software system. Software engineering studies how to choose boundaries, interfaces, and layers so that coordination is possible without exposing needless detail.”

**Form (b)**  
“A software system performs computation through modules arranged in an architecture. A module exposes an application programming interface that defines its operation while hiding its code. Applications can compose modules by relying on those interfaces, and what counts as a module at one level can itself be an application composed from lower-level modules. This layering permits internal refactoring without redesigning every dependent application, as long as the interface remains compatible. It contains many bugs locally, though an API mismatch can disable otherwise sound modules throughout the system. Software engineering concerns the selection of boundaries, interfaces, and layers that enable coordination without unnecessary exposure of implementation detail.”

### Electronic Device

**Form (a)**  
“An electronic device achieves signal processing by arranging circuit blocks into a circuit architecture. Each circuit block presents a terminal interface that specifies the signal function it will provide while concealing its internal circuitry. A subsystem can therefore combine circuit blocks by depending on their terminal interfaces, and a circuit block at one scale can itself be a subsystem at a lower scale. This layering permits component revision inside a circuit block without redesigning every subsystem that uses it, provided its terminal interface remains compatible. It also localizes many electrical faults, although a terminal-interface mismatch can disable otherwise sound circuit blocks across the electronic device. Electrical engineering studies how to choose boundaries, interfaces, and layers so that coordination is possible without exposing needless detail.”

**Form (b)**  
“An electronic device processes signals through circuit blocks arranged in a circuit architecture. Each block exposes terminals that define its signal function while hiding its circuitry. A subsystem can combine blocks by relying on those terminal interfaces, and a block at one scale may itself be a lower-level subsystem. That layering allows a component revision within a block without redesigning every dependent subsystem, provided the terminal interface stays compatible. It localizes many electrical faults, although an incompatible terminal interface can disable sound blocks across the device. Electrical engineering studies the boundary, interface, and layer choices that permit coordination without revealing unnecessary circuit detail.”

### Multicellular Organism

**Form (a)**  
“A multicellular organism achieves physiological function by arranging cells into a tissue architecture. Each cell presents a membrane interface that specifies the regulated exchange it will provide while concealing its internal molecular machinery. A tissue can therefore combine cells by depending on their membrane interfaces, and a cell at one scale can itself be a tissue at a lower scale. This layering permits molecular change inside a cell without redesigning every tissue that uses it, provided its membrane interface remains compatible. It also localizes many cell defects, although a membrane-interface mismatch can disable otherwise sound cells across the multicellular organism. Systems biology studies how to choose boundaries, interfaces, and layers so that coordination is possible without exposing needless detail.”

**Form (b)**  
“A multicellular organism performs physiological functions by organizing cells into tissues. Cells expose membrane interfaces through which they provide regulated exchange while keeping their molecular machinery internal. Tissues can combine cells by relying on those interfaces, and a cell itself is a lower-level composite of organized molecular machinery. This layered organization permits molecular change within a cell without requiring every tissue that uses the cell to be redesigned, so long as membrane interactions remain compatible. It also confines many cell defects, although incompatible membrane interactions can disable otherwise functional cells throughout an organism. Systems biology investigates the boundaries, interfaces, and layers that make such coordination possible without exposing every internal molecular detail.”

### Firm

**Form (a)**  
“A firm achieves production by arranging teams into an organizational structure. Each team presents a role interface that specifies the deliverable it will provide while concealing its internal workflow. A department can therefore combine teams by depending on their role interfaces, and a team at one scale can itself be a department at a lower scale. This layering permits process change inside a team without redesigning every department that uses it, provided its role interface remains compatible. It also localizes many coordination failures, although a role-interface mismatch can disable otherwise sound teams across the firm. Organization design studies how to choose boundaries, interfaces, and layers so that coordination is possible without exposing needless detail.”

**Form (b)**  
“A firm produces by arranging teams within an organizational structure. Each team offers a role interface: it commits to a deliverable while retaining control of its internal workflow. Departments can therefore coordinate teams through those role interfaces, and a team at one organizational scale can itself be a department made from lower-level teams. This layering allows a team to change its process without redesigning every dependent department, provided that its role interface remains compatible. It contains many coordination failures locally, but incompatible role interfaces can disable otherwise capable teams across the firm. Organization design studies how boundaries, interfaces, and layers make coordination possible without forcing every unit to expose its internal work.”

### Manufactured Product

**Form (a)**  
“A manufactured product achieves mechanical function by arranging components into a product architecture. Each component presents a mechanical interface that specifies the motion it will provide while concealing its internal mechanism. A subassembly can therefore combine components by depending on their mechanical interfaces, and a component at one scale can itself be a subassembly at a lower scale. This layering permits design revision inside a component without redesigning every subassembly that uses it, provided its mechanical interface remains compatible. It also localizes many defects, although a mechanical-interface mismatch can disable otherwise sound components across the manufactured product. Systems engineering studies how to choose boundaries, interfaces, and layers so that coordination is possible without exposing needless detail.”

**Form (b)**  
“A manufactured product performs mechanical functions through components arranged in a product architecture. A component exposes a mechanical interface that defines the motion it provides while hiding its internal mechanism. Subassemblies can combine components by depending on those interfaces, and a component at one scale can itself be a subassembly made from lower-level components. This layered structure permits a design revision within one component without redesigning every subassembly that uses it, as long as the mechanical interface remains compatible. It isolates many defects, though an incompatible interface can disable otherwise sound components throughout the product. Systems engineering studies how to choose boundaries, interfaces, and layers that permit coordination without needless disclosure of internal detail.”

---

## Archetype Proposal: Inference from Imperfect Evidence

### Context-template

“An [INVESTIGATOR] seeks to infer an unobserved [CAUSE] from observable [SIGN]. At the outset, several [HYPOTHESIS] are plausible, and their [PRIOR] need not be equal. A [TEST] is valuable when competing [HYPOTHESIS] predict meaningfully different [RESULT], but no [TEST] is perfect: both [FALSEPOSITIVE] and [FALSENEGATIVE] can occur. As [EVIDENCE] accumulates, the [INVESTIGATOR] updates the relative support for each [HYPOTHESIS] and chooses further [TEST] by balancing expected discrimination against [COST]. A final [JUDGMENT] should therefore reflect the total pattern of [EVIDENCE], not a single striking [SIGN]. [DISCIPLINE] formalizes or disciplines this movement from signs to causes.”

### Metanym table

| [SLOT] | Clinical Medicine | Equipment Maintenance | Cybersecurity | Astronomy | Criminal Investigation |
|---|---|---|---|---|---|
| INVESTIGATOR | clinician | technician | security analyst | astronomer | detective |
| CAUSE | disease | equipment fault | intrusion | astronomical source | crime |
| SIGN | symptom | warning indicator | alert | signal | clue |
| HYPOTHESIS | diagnosis | failure mode | attack scenario | source model | case theory |
| PRIOR | prevalence | base rate | base rate | occurrence rate | base rate |
| TEST | diagnostic test | inspection | scan | observation | forensic examination |
| RESULT | test result | inspection finding | scan finding | measurement | forensic finding |
| FALSEPOSITIVE | false positive | false alarm | false alert | false detection | false match |
| FALSENEGATIVE | false negative | missed fault | missed intrusion | non-detection | missed match |
| EVIDENCE | clinical evidence | diagnostic evidence | telemetry | observational data | case evidence |
| COST | testing cost | downtime cost | investigation cost | telescope time | investigative cost |
| JUDGMENT | diagnosis | fault assessment | incident assessment | source classification | case assessment |
| DISCIPLINE | medical diagnosis | reliability engineering | cybersecurity | astrophysics | criminal investigation |

### Clinical Medicine

**Form (a)**  
“A clinician seeks to infer an unobserved disease from observable symptoms. At the outset, several diagnoses are plausible, and their prevalences need not be equal. A diagnostic test is valuable when competing diagnoses predict meaningfully different test results, but no diagnostic test is perfect: both false positives and false negatives can occur. As clinical evidence accumulates, the clinician updates the relative support for each diagnosis and chooses further diagnostic tests by balancing expected discrimination against testing cost. A final diagnosis should therefore reflect the total pattern of clinical evidence, not a single striking symptom. Medical diagnosis formalizes or disciplines this movement from signs to causes.”

**Form (b)**  
“A clinician infers an unseen disease from observable symptoms. Several diagnoses may initially be plausible, but their prevalences are not necessarily equal. A diagnostic test is useful when rival diagnoses predict different results, although every test can yield both false positives and false negatives. As clinical evidence accumulates, the clinician revises support for each diagnosis and selects additional tests by weighing discriminatory value against testing cost. The final diagnosis should rest on the overall pattern of evidence rather than one dramatic symptom. Medical diagnosis structures this movement from signs to underlying causes.”

### Equipment Maintenance

**Form (a)**  
“A technician seeks to infer an unobserved equipment fault from observable warning indicators. At the outset, several failure modes are plausible, and their base rates need not be equal. An inspection is valuable when competing failure modes predict meaningfully different inspection findings, but no inspection is perfect: both false alarms and missed faults can occur. As diagnostic evidence accumulates, the technician updates the relative support for each failure mode and chooses further inspections by balancing expected discrimination against downtime cost. A final fault assessment should therefore reflect the total pattern of diagnostic evidence, not a single striking warning indicator. Reliability engineering formalizes or disciplines this movement from signs to causes.”

**Form (b)**  
“A technician infers an unseen equipment fault from warning indicators. Multiple failure modes may fit initially, but their base rates differ. An inspection is valuable when competing failure modes imply different findings, yet inspections can produce false alarms and miss real faults. As diagnostic evidence accumulates, the technician updates the support for each failure mode and chooses further inspections by trading expected discrimination against downtime cost. A fault assessment should therefore depend on the complete evidence pattern, not one conspicuous indicator. Reliability engineering gives disciplined methods for reasoning from observed symptoms of equipment to their causes.”

### Cybersecurity

**Form (a)**  
“A security analyst seeks to infer an unobserved intrusion from observable alerts. At the outset, several attack scenarios are plausible, and their base rates need not be equal. A scan is valuable when competing attack scenarios predict meaningfully different scan findings, but no scan is perfect: both false alerts and missed intrusions can occur. As telemetry accumulates, the security analyst updates the relative support for each attack scenario and chooses further scans by balancing expected discrimination against investigation cost. A final incident assessment should therefore reflect the total pattern of telemetry, not a single striking alert. Cybersecurity formalizes or disciplines this movement from signs to causes.”

**Form (b)**  
“A security analyst infers a possible intrusion from observable alerts. Several attack scenarios can initially fit, but they do not have equal base rates. A scan is useful when rival scenarios predict different findings, although scans can generate false alerts and miss genuine intrusions. As telemetry accumulates, the analyst updates support for each scenario and chooses additional scans by balancing discriminating value against investigation cost. The incident assessment should therefore reflect the full telemetry pattern rather than one alarming alert. Cybersecurity provides disciplined methods for moving from observable indicators to their probable causes.”

### Astronomy

**Form (a)**  
“An astronomer seeks to infer an unobserved astronomical source from observable signals. At the outset, several source models are plausible, and their occurrence rates need not be equal. An observation is valuable when competing source models predict meaningfully different measurements, but no observation is perfect: both false detections and non-detections can occur. As observational data accumulates, the astronomer updates the relative support for each source model and chooses further observations by balancing expected discrimination against telescope time. A final source classification should therefore reflect the total pattern of observational data, not a single striking signal. Astrophysics formalizes or disciplines this movement from signs to causes.”

**Form (b)**  
“An astronomer infers an unseen astronomical source from measured signals. Different source models may be plausible at first, but their occurrence rates are not equal. An observation has diagnostic value when competing models predict different measurements, although observations can produce false detections and non-detections. As observational data grows, the astronomer revises relative support for each model and chooses further observations by weighing expected discrimination against telescope time. A source classification should rely on the entire data pattern, not one remarkable signal. Astrophysics disciplines the inference from observed signals to their underlying sources.”

### Criminal Investigation

**Form (a)**  
“A detective seeks to infer an unobserved crime from observable clues. At the outset, several case theories are plausible, and their base rates need not be equal. A forensic examination is valuable when competing case theories predict meaningfully different forensic findings, but no forensic examination is perfect: both false matches and missed matches can occur. As case evidence accumulates, the detective updates the relative support for each case theory and chooses further forensic examinations by balancing expected discrimination against investigative cost. A final case assessment should therefore reflect the total pattern of case evidence, not a single striking clue. Criminal investigation formalizes or disciplines this movement from signs to causes.”

**Form (b)**  
“A detective infers an unobserved crime from observable clues. Several case theories can initially fit the clues, but their base rates may differ. A forensic examination is valuable when rival theories predict distinct findings, though false matches and missed matches remain possible. As case evidence accumulates, the detective updates support for each theory and orders further examinations by balancing expected discrimination against investigative cost. A case assessment should consequently reflect the full evidence pattern rather than one dramatic clue. Criminal investigation disciplines the movement from clues to underlying criminal events.”

---

## Archetype Proposal: Evolutionary Search Through Variation and Selection

### Context-template

“A [SEARCH] maintains a [POPULATION] of [CANDIDATE] that differ in heritable [TRAIT]. Each [CANDIDATE] is evaluated in an [ENVIRONMENT], yielding a measure of [FITNESS] that affects its chance of [RETENTION]. [VARIATION] introduces new [TRAIT], while [INHERITANCE] preserves some successful [TRAIT] in descendants or successors. Repeated [SELECTION] can adapt the [POPULATION] to its current [ENVIRONMENT], but it can also concentrate too quickly on a local [OPTIMUM] and lose [DIVERSITY]. Because [ENVIRONMENT] may change and evaluation may be noisy, a capable [SEARCH] retains enough [DIVERSITY] to explore alternatives while exploiting high-[FITNESS] [CANDIDATE]. [DISCIPLINE] studies how variation, inheritance, selection, and diversity determine long-run adaptation.”

### Metanym table

| [SLOT] | Natural Evolution | Crop Breeding | Directed Enzyme Evolution | Evolutionary Algorithm | Technological Innovation |
|---|---|---|---|---|---|
| SEARCH | evolutionary process | breeding program | directed-evolution campaign | evolutionary algorithm | innovation ecosystem |
| POPULATION | population | breeding population | library | population | design population |
| CANDIDATE | organism | plant line | enzyme variant | solution | product design |
| TRAIT | phenotypic trait | agronomic trait | molecular trait | encoded trait | design feature |
| ENVIRONMENT | ecological environment | field environment | assay environment | problem landscape | market environment |
| FITNESS | reproductive fitness | breeding value | assay fitness | objective fitness | commercial fitness |
| RETENTION | reproduction | parent selection | advancement | retention | market retention |
| VARIATION | mutation | crossing | mutagenesis | mutation | prototyping |
| INHERITANCE | genetic inheritance | genetic inheritance | sequence inheritance | copying | design reuse |
| SELECTION | natural selection | breeder selection | screening selection | fitness selection | market selection |
| OPTIMUM | adaptive peak | yield plateau | activity peak | local optimum | dominant design |
| DIVERSITY | genetic diversity | germplasm diversity | library diversity | population diversity | design diversity |
| DISCIPLINE | evolutionary biology | plant breeding | protein engineering | evolutionary computation | innovation studies |

### Natural Evolution

**Form (a)**  
“An evolutionary process maintains a population of organisms that differ in heritable phenotypic traits. Each organism is evaluated in an ecological environment, yielding a measure of reproductive fitness that affects its chance of reproduction. Mutation introduces new phenotypic traits, while genetic inheritance preserves some successful phenotypic traits in descendants or successors. Repeated natural selection can adapt the population to its current ecological environment, but it can also concentrate too quickly on an adaptive peak and lose genetic diversity. Because the ecological environment may change and evaluation may be noisy, a capable evolutionary process retains enough genetic diversity to explore alternatives while exploiting high-reproductive-fitness organisms. Evolutionary biology studies how variation, inheritance, selection, and diversity determine long-run adaptation.”

**Form (b)**  
“Natural evolution operates on populations of organisms that differ in heritable phenotypic traits. Organisms are evaluated by their ecological environment, and reproductive fitness influences their chance of reproduction. Mutation creates new traits, while genetic inheritance carries some successful traits into descendants. Repeated natural selection can adapt a population to its current environment, but rapid concentration on one adaptive peak can reduce genetic diversity. Because environments change and fitness evaluation is noisy, evolutionary processes retain diversity that explores alternatives while high-fitness organisms are exploited through reproduction. Evolutionary biology studies how variation, inheritance, selection, and diversity shape long-run adaptation.”

### Crop Breeding

**Form (a)**  
“A breeding program maintains a breeding population of plant lines that differ in heritable agronomic traits. Each plant line is evaluated in a field environment, yielding a measure of breeding value that affects its chance of parent selection. Crossing introduces new agronomic traits, while genetic inheritance preserves some successful agronomic traits in descendants or successors. Repeated breeder selection can adapt the breeding population to its current field environment, but it can also concentrate too quickly on a yield plateau and lose germplasm diversity. Because the field environment may change and evaluation may be noisy, a capable breeding program retains enough germplasm diversity to explore alternatives while exploiting high-breeding-value plant lines. Plant breeding studies how variation, inheritance, selection, and diversity determine long-run adaptation.”

**Form (b)**  
“A breeding program works with populations of plant lines that vary in heritable agronomic traits. Each line is evaluated in field conditions, and its breeding value affects whether it is chosen as a parent. Crossing generates new trait combinations, while genetic inheritance preserves desirable traits in later lines. Repeated breeder selection can adapt the population to current field conditions, but premature concentration on one yield plateau can erode germplasm diversity. Because field conditions can change and trial results are noisy, a strong program preserves enough diversity to explore alternatives while exploiting high-value lines. Plant breeding studies how variation, inheritance, selection, and diversity govern long-run adaptation.”

### Directed Enzyme Evolution

**Form (a)**  
“A directed-evolution campaign maintains a library of enzyme variants that differ in heritable molecular traits. Each enzyme variant is evaluated in an assay environment, yielding a measure of assay fitness that affects its chance of advancement. Mutagenesis introduces new molecular traits, while sequence inheritance preserves some successful molecular traits in descendants or successors. Repeated screening selection can adapt the library to its current assay environment, but it can also concentrate too quickly on an activity peak and lose library diversity. Because the assay environment may change and evaluation may be noisy, a capable directed-evolution campaign retains enough library diversity to explore alternatives while exploiting high-assay-fitness enzyme variants. Protein engineering studies how variation, inheritance, selection, and diversity determine long-run adaptation.”

**Form (b)**  
“A directed-evolution campaign searches a library of enzyme variants that differ in heritable molecular traits. Variants are tested in an assay environment, and assay fitness determines which ones advance. Mutagenesis creates new traits, while sequence inheritance carries successful traits into successor variants. Repeated screening selection can adapt the library to the current assay, but rapid concentration on one activity peak can exhaust library diversity. Since assay conditions can change and measurements are noisy, an effective campaign keeps enough diversity to explore alternatives while advancing high-fitness variants. Protein engineering studies how variation, inheritance, selection, and diversity determine long-run molecular adaptation.”

### Evolutionary Algorithm

**Form (a)**  
“An evolutionary algorithm maintains a population of solutions that differ in heritable encoded traits. Each solution is evaluated in a problem landscape, yielding a measure of objective fitness that affects its chance of retention. Mutation introduces new encoded traits, while copying preserves some successful encoded traits in descendants or successors. Repeated fitness selection can adapt the population to its current problem landscape, but it can also concentrate too quickly on a local optimum and lose population diversity. Because the problem landscape may change and evaluation may be noisy, a capable evolutionary algorithm retains enough population diversity to explore alternatives while exploiting high-objective-fitness solutions. Evolutionary computation studies how variation, inheritance, selection, and diversity determine long-run adaptation.”

**Form (b)**  
“An evolutionary algorithm searches a population of solutions that vary in heritable encoded traits. Each solution is scored against a problem landscape, and objective fitness affects whether it is retained. Mutation creates new traits, while copying preserves successful traits in descendant solutions. Repeated fitness selection can adapt the population to the current landscape, but premature concentration on a local optimum can eliminate population diversity. Since landscapes may change and evaluations may be noisy, a capable algorithm preserves enough diversity to explore alternatives while exploiting high-fitness solutions. Evolutionary computation studies how variation, inheritance, selection, and diversity shape long-run adaptation.”

### Technological Innovation

**Form (a)**  
“An innovation ecosystem maintains a design population of product designs that differ in heritable design features. Each product design is evaluated in a market environment, yielding a measure of commercial fitness that affects its chance of market retention. Prototyping introduces new design features, while design reuse preserves some successful design features in descendants or successors. Repeated market selection can adapt the design population to its current market environment, but it can also concentrate too quickly on a dominant design and lose design diversity. Because the market environment may change and evaluation may be noisy, a capable innovation ecosystem retains enough design diversity to explore alternatives while exploiting high-commercial-fitness product designs. Innovation studies studies how variation, inheritance, selection, and diversity determine long-run adaptation.”

**Form (b)**  
“An innovation ecosystem contains product designs that vary in heritable design features. Markets evaluate each design, and commercial fitness affects whether the design is retained. Prototyping introduces new features, while design reuse carries successful features into successor products. Repeated market selection can adapt the design population to current market conditions, but rapid concentration on a dominant design can reduce design diversity. Because markets change and commercial evaluation is noisy, a capable innovation ecosystem retains enough diversity to explore alternatives while exploiting highly fit product designs. Innovation studies examines how variation, inheritance, selection, and diversity determine long-run technological adaptation.”