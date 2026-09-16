# Five Archetypal Contexts

---

## Archetype Proposal: Constraint Propagation

### Template

"A [SYSTEM] contains [ELEMENT] that are subject to [CONSTRAINT]. Each [CONSTRAINT] limits the possible [STATE] of one or more [ELEMENT]. When one [ELEMENT] adopts a particular [STATE], this [INFORMATION] propagates through the network of [CONSTRAINT], progressively narrowing the [STATE] available to neighboring [ELEMENT]. [ELEMENT] that become over-constrained enter a [FAILURE] state. The process of [PROPAGATION] can either converge to a stable [CONFIGURATION], diverge into [FAILURE], or oscillate indefinitely. Understanding [PROPAGATION] is essential for predicting [OUTCOME], designing [SYSTEM] that avoid [FAILURE], and efficiently solving [PROBLEM_CLASS]. [PROPAGATION] operates identically whether [CONSTRAINT] are physical, logical, or social in nature."

### Metanym Table

| [SLOT]           | Electrical Circuit | Protein Folding    | Scheduling Problem | Ecosystem          | Social Network     |
|------------------|--------------------|--------------------|--------------------|--------------------|---------------------|
| SYSTEM           | circuit            | protein            | schedule           | ecosystem          | network             |
| ELEMENT          | node               | amino acid         | task               | species            | agent               |
| CONSTRAINT       | Kirchhoff's law    | hydrogen bond      | precedence         | predation relation | norm                |
| STATE            | voltage            | conformation       | time slot          | population size    | belief              |
| INFORMATION      | current flow       | folding pattern    | assignment         | abundance signal   | rumor               |
| PROPAGATION      | propagation        | folding            | constraint solving | trophic cascade    | social contagion    |
| CONFIGURATION    | equilibrium        | native state       | feasible schedule  | stable community   | consensus           |
| FAILURE          | short circuit      | misfolding         | infeasibility      | extinction         | polarization        |
| OUTCOME          | power dissipation  | function           | completion time    | biodiversity       | collective action   |
| PROBLEM_CLASS    | circuit analysis   | structure prediction | CSP               | community assembly | opinion dynamics    |

### Electrical Circuit

**Form (a):**
"An electrical circuit contains nodes that are subject to Kirchhoff's laws. Each law limits the possible voltages of one or more nodes. When one node adopts a particular voltage, this current flow propagates through the network of Kirchhoff's laws, progressively narrowing the voltages available to neighboring nodes. Nodes that become over-constrained enter a short-circuit state. The process of propagation can either converge to a stable equilibrium, diverge into short circuit, or oscillate indefinitely. Understanding propagation is essential for predicting power dissipation, designing circuits that avoid short circuit, and efficiently solving circuit analysis. Propagation operates identically whether Kirchhoff's laws are physical, logical, or social in nature."

**Form (b):**
"Kirchhoff's laws constrain the voltages at each node in a circuit. When a node is assigned a voltage, that constraint propagates to its neighbors, restricting their possible voltages. Over-constrained nodes short-circuit. The propagation process either reaches a stable equilibrium, fails catastrophically, or cycles. Circuit analysis depends on understanding how constraints propagate to predict power dissipation and avoid failure."

---

### Protein Folding

**Form (a):**
"A protein contains amino acids that are subject to hydrogen bonds. Each hydrogen bond limits the possible conformations of one or more amino acids. When one amino acid adopts a particular conformation, this folding pattern propagates through the network of hydrogen bonds, progressively narrowing the conformations available to neighboring amino acids. Amino acids that become over-constrained enter a misfolding state. The process of folding can either converge to a stable native state, diverge into misfolding, or oscillate indefinitely. Understanding folding is essential for predicting function, designing proteins that avoid misfolding, and efficiently solving structure prediction. Folding operates identically whether hydrogen bonds are physical, logical, or social in nature."

**Form (b):**
"A protein folds as hydrogen bonds constrain the conformations of its amino acids. Local folding decisions propagate through the chain, restricting the conformations available downstream. Amino acids that cannot satisfy their hydrogen-bonding constraints misfold. The folding process either converges to the native state (functional), fails into misfolding (often pathogenic), or gets trapped in local minima. Protein structure prediction requires understanding how local constraints propagate globally."

---

### Scheduling Problem

**Form (a):**
"A schedule contains tasks that are subject to precedence constraints. Each precedence constraint limits the possible time slots of one or more tasks. When one task adopts a particular time slot, this assignment propagates through the network of precedence constraints, progressively narrowing the time slots available to neighboring tasks. Tasks that become over-constrained enter an infeasibility state. The process of constraint solving can either converge to a stable feasible schedule, diverge into infeasibility, or oscillate indefinitely. Understanding constraint solving is essential for predicting completion time, designing schedules that avoid infeasibility, and efficiently solving CSP. Constraint solving operates identically whether precedence constraints are physical, logical, or social in nature."

**Form (b):**
"Precedence constraints in a scheduling problem restrict which tasks can be assigned to which time slots. When a task is scheduled, that constraint propagates to dependent tasks, narrowing their available slots. Over-constrained tasks make the schedule infeasible. Constraint propagation either finds a feasible schedule, detects infeasibility, or cycles. CSP solvers exploit constraint propagation to efficiently predict completion time and avoid infeasible assignments."

---

### Ecosystem

**Form (a):**
"An ecosystem contains species that are subject to predation relations. Each predation relation limits the possible population sizes of one or more species. When one species adopts a particular population size, this abundance signal propagates through the network of predation relations, progressively narrowing the population sizes available to neighboring species. Species that become over-constrained enter an extinction state. The process of trophic cascade can either converge to a stable community, diverge into extinction, or oscillate indefinitely. Understanding trophic cascade is essential for predicting biodiversity, designing ecosystems that avoid extinction, and efficiently solving community assembly. Trophic cascade operates identically whether predation relations are physical, logical, or social in nature."

**Form (b):**
"Predation relations constrain the population sizes of species in an ecosystem. When one species' abundance changes, that signal cascades through the food web, altering the viable population sizes of predators and prey. Species that cannot sustain viable populations go extinct. Trophic cascades either stabilize into a persistent community structure, collapse into extinction, or cycle. Community assembly theory studies how predation constraints propagate to predict biodiversity and ecosystem stability."

Justification: "Trophic cascade" is the domain term for constraint propagation in food webs; it describes both the mechanism and the observable outcome.

---

### Social Network

**Form (a):**
"A social network contains agents that are subject to norms. Each norm limits the possible beliefs of one or more agents. When one agent adopts a particular belief, this rumor propagates through the network of norms, progressively narrowing the beliefs available to neighboring agents. Agents that become over-constrained enter a polarization state. The process of social contagion can either converge to a stable consensus, diverge into polarization, or oscillate indefinitely. Understanding social contagion is essential for predicting collective action, designing networks that avoid polarization, and efficiently solving opinion dynamics. Social contagion operates identically whether norms are physical, logical, or social in nature."

**Form (b):**
"Social norms constrain the beliefs agents can publicly hold. When one agent adopts a belief, that signal spreads through the network, narrowing the acceptable beliefs for neighbors. Agents caught between incompatible norms polarize. Social contagion either converges to consensus, fragments into polarized camps, or oscillates. Opinion dynamics research studies how norm constraints propagate to predict collective action and avoid polarization."

---

## Archetype Proposal: Boundary Dissolution

### Template

"A [SYSTEM] maintains [BOUNDARY] that separates [INTERIOR] from [EXTERIOR]. The [BOUNDARY] is permeable to [EXCHANGE], allowing controlled [FLOW] while excluding [THREAT]. Over time, [PROCESS] erodes the [BOUNDARY], increasing [PERMEABILITY]. As [PERMEABILITY] rises, [EXCHANGE] accelerates, but so does unwanted [THREAT] penetration. The [SYSTEM] can respond by reinforcing [BOUNDARY], accepting [DISSOLUTION], or adapting [INTERIOR] to tolerate [THREAT]. [DISSOLUTION] is often irreversible; once [BOUNDARY] integrity falls below a critical threshold, [SYSTEM] collapse becomes inevitable. [FIELD] studies how [SYSTEM] manage the tension between [EXCHANGE] and [PROTECTION]."

### Metanym Table

| [SLOT]           | Cell Membrane      | Nation-State        | Immune System       | Coral Reef          | Professional Guild  |
|------------------|--------------------|--------------------|--------------------|--------------------|---------------------|
| SYSTEM           | cell               | nation              | immune system       | reef                | profession          |
| BOUNDARY         | membrane           | border              | epithelial barrier  | reef structure      | credential          |
| INTERIOR         | cytoplasm          | territory           | internal tissue     | symbiotic community | membership          |
| EXTERIOR         | extracellular space| foreign land        | pathogenic environment | open ocean        | public sphere       |
| EXCHANGE         | nutrient uptake    | trade               | antigen sampling    | nutrient exchange   | knowledge sharing   |
| FLOW             | diffusion          | commerce            | immune surveillance | symbiont migration  | information flow    |
| THREAT           | toxin              | invasion            | pathogen            | bleaching agent     | credential fraud    |
| PROCESS          | oxidative stress   | globalization       | inflammation        | warming             | digitalization      |
| PERMEABILITY     | membrane fluidity  | border porosity     | barrier integrity   | structural damage   | credential inflation|
| DISSOLUTION      | lysis              | dissolution         | immunosuppression   | bleaching           | professionalization collapse |
| INTERIOR         | cytoplasm          | territory           | internal tissue     | symbiotic community | membership          |
| PROTECTION       | selective transport| border control      | immune defense      | calcification       | gatekeeping         |
| FIELD            | cell biology       | international relations | immunology      | coral biology       | sociology of professions |

### Cell Membrane

**Form (a):**
"A cell maintains a membrane that separates cytoplasm from extracellular space. The membrane is permeable to nutrient uptake, allowing controlled diffusion while excluding toxins. Over time, oxidative stress erodes the membrane, increasing membrane fluidity. As membrane fluidity rises, diffusion accelerates, but so does unwanted toxin penetration. The cell can respond by reinforcing the membrane, accepting lysis, or adapting cytoplasm to tolerate toxins. Lysis is often irreversible; once membrane integrity falls below a critical threshold, cell collapse becomes inevitable. Cell biology studies how cells manage the tension between nutrient uptake and toxin protection."

**Form (b):**
"The cell membrane maintains selective permeability, permitting nutrient diffusion while excluding toxins. Oxidative stress degrades membrane integrity, increasing fluidity and permeability. As the membrane becomes more permeable, nutrient uptake accelerates but so does toxic infiltration. Cells can reinforce the membrane, tolerate increased permeability, or adapt their cytoplasm to resist toxins. Beyond a critical threshold of membrane damage, lysis becomes inevitable. Cell biology examines how cells balance nutrient acquisition against osmotic and chemical threats."

---

### Nation-State

**Form (a):**
"A nation maintains a border that separates territory from foreign land. The border is permeable to trade, allowing controlled commerce while excluding invasion. Over time, globalization erodes the border, increasing border porosity. As border porosity rises, commerce accelerates, but so does unwanted invasion penetration. The nation can respond by reinforcing the border, accepting dissolution, or adapting territory to tolerate invasion. Dissolution is often irreversible; once border integrity falls below a critical threshold, nation collapse becomes inevitable. International relations studies how nations manage the tension between trade and invasion protection."

**Form (b):**
"National borders maintain selective permeability, permitting trade while excluding military and political threats. Globalization erodes border control, increasing porosity and cross-border flow. As borders become more porous, commerce accelerates but so does unwanted infiltration—espionage, smuggling, irregular migration. States can reinforce borders through military or bureaucratic means, accept increased permeability, or adapt domestic institutions to resist foreign influence. Beyond a critical threshold of border erosion, state dissolution becomes inevitable. International relations theory examines how states balance economic integration against sovereignty and security."

---

### Immune System

**Form (a):**
"An immune system maintains an epithelial barrier that separates internal tissue from pathogenic environment. The barrier is permeable to antigen sampling, allowing controlled immune surveillance while excluding pathogens. Over time, inflammation erodes the barrier, increasing barrier integrity loss. As barrier integrity loss rises, immune surveillance accelerates, but so does unwanted pathogen penetration. The immune system can respond by reinforcing the barrier, accepting immunosuppression, or adapting internal tissue to tolerate pathogens. Immunosuppression is often irreversible; once barrier integrity falls below a critical threshold, immune system collapse becomes inevitable. Immunology studies how immune systems manage the tension between antigen sampling and pathogen protection."

**Form (b):**
"Epithelial barriers maintain selective permeability, permitting antigen sampling while excluding pathogens. Chronic inflammation degrades barrier integrity, increasing permeability and pathogen penetration. As barriers become compromised, immune surveillance intensifies but so does pathogenic infiltration. The immune system can reinforce barriers through tight-junction proteins, tolerate increased permeability, or adapt tissues to resist infection. Severe barrier breakdown leads to immunosuppression and systemic infection. Immunology studies how epithelial barriers balance immune surveillance against pathogenic invasion."

Justification: "Barrier integrity" is the inverse of permeability; the template uses "permeability" as the eroding quantity.

---

### Coral Reef

**Form (a):**
"A reef maintains reef structure that separates symbiotic community from open ocean. The reef structure is permeable to nutrient exchange, allowing controlled symbiont migration while excluding bleaching agents. Over time, warming erodes the reef structure, increasing structural damage. As structural damage rises, symbiont migration accelerates, but so does unwanted bleaching agent penetration. The reef can respond by reinforcing reef structure, accepting bleaching, or adapting symbiotic community to tolerate bleaching agents. Bleaching is often irreversible; once reef structure integrity falls below a critical threshold, reef collapse becomes inevitable. Coral biology studies how reefs manage the tension between nutrient exchange and bleaching agent protection."

**Form (b):**
"Coral reef structure maintains selective permeability, permitting nutrient exchange with symbionts while excluding thermal stress. Warming degrades reef structure, increasing permeability and heat penetration. As reef structure deteriorates, symbiont exchange accelerates but so does thermal stress. Corals can reinforce structure through calcification, tolerate increased heat, or adapt their symbiotic partners to resist bleaching. Beyond a critical threshold of structural damage, reef collapse and ecosystem collapse become inevitable. Coral biology examines how reef structure balances nutrient acquisition against thermal threats."

---

### Professional Guild

**Form (a):**
"A profession maintains credentials that separate membership from public sphere. Credentials are permeable to knowledge sharing, allowing controlled information flow while excluding credential fraud. Over time, digitalization erodes credentials, increasing credential inflation. As credential inflation rises, information flow accelerates, but so does unwanted credential fraud penetration. The profession can respond by reinforcing credentials, accepting professionalization collapse, or adapting membership to tolerate credential fraud. Professionalization collapse is often irreversible; once credential integrity falls below a critical threshold, profession collapse becomes inevitable. Sociology of professions studies how professions manage the tension between knowledge sharing and credential fraud protection."

**Form (b):**
"Professional credentials maintain selective permeability, permitting knowledge sharing among members while excluding fraudulent practitioners. Digitalization erodes credential barriers, increasing credential inflation and fraud. As credentials become easier to counterfeit, knowledge sharing accelerates but so does infiltration by unqualified practitioners. Professions can reinforce credentials through harder-to-forge standards, tolerate increased permeability, or adapt membership standards to resist fraud. Beyond a critical threshold of credential erosion, professional gatekeeping collapses. Sociology of professions examines how professions balance knowledge dissemination against credential fraud."

---

## Archetype Proposal: Resonance and Damping

### Template

"A [SYSTEM] exhibits [OSCILLATION] at a characteristic [FREQUENCY]. When [SYSTEM] is driven by an external [DRIVER] at or near [FREQUENCY], [AMPLITUDE] grows dramatically—a phenomenon called [RESONANCE]. [RESONANCE] can be constructive, amplifying [SIGNAL] and enabling [FUNCTION], or destructive, causing [DAMAGE]. The presence of [DAMPING] dissipates [ENERGY], reducing [AMPLITUDE] and preventing [RESONANCE] from reaching dangerous levels. [SYSTEM] with low [DAMPING] are vulnerable to [RESONANCE]; those with high [DAMPING] are stable but sluggish. Optimal [SYSTEM] design balances [DAMPING] to permit beneficial [RESONANCE] while suppressing harmful [RESONANCE]. [FIELD] studies how [SYSTEM] manage [RESONANCE] across scales."

### Metanym Table

| [SLOT]           | Mechanical Oscillator | Electromagnetic Wave | Population Dynamics | Neural Circuit      | Financial Market    |
|------------------|----------------------|----------------------|--------------------|--------------------|---------------------|
| SYSTEM           | oscillator           | cavity               | population          | circuit             | market              |
| OSCILLATION      | vibration            | electromagnetic mode | population cycle   | oscillation         | boom-bust cycle     |
| FREQUENCY        | natural frequency    | resonant frequency   | generation time    | oscillation frequency | business cycle frequency |
| DRIVER           | external force       | electromagnetic field | environmental forcing | input signal       | exogenous shock     |
| AMPLITUDE        | displacement         | field strength       | population size    | firing rate         | price volatility    |
| RESONANCE        | resonance            | resonance            | population resonance | resonance           | market resonance    |
| SIGNAL           | vibration            | radiation            | population growth  | neural signal       | price signal        |
| FUNCTION         | energy transfer      | radiation emission   | population stability | information processing | price discovery    |
| DAMAGE           | structural failure   | dielectric breakdown | population crash   | seizure             | market crash        |
| DAMPING          | friction             | resistance           | density dependence  | inhibitory synapse  | circuit breaker     |
| ENERGY           | kinetic energy       | electromagnetic energy | metabolic energy   | neural activity     | capital             |
| FIELD            | mechanics            | electromagnetism     | ecology             | neuroscience        | finance             |

### Mechanical Oscillator

**Form (a):**
"A mechanical oscillator exhibits vibration at a characteristic natural frequency. When the oscillator is driven by an external force at or near the natural frequency, displacement grows dramatically—a phenomenon called resonance. Resonance can be constructive, amplifying vibration and enabling energy transfer, or destructive, causing structural failure. The presence of friction dissipates kinetic energy, reducing displacement and preventing resonance from reaching dangerous levels. Oscillators with low friction are vulnerable to resonance; those with high friction are stable but sluggish. Optimal oscillator design balances friction to permit beneficial resonance while suppressing harmful resonance. Mechanics studies how oscillators manage resonance across scales."

**Form (b):**
"Mechanical systems oscillate at their natural frequency. When driven by an external force near that frequency, displacement amplifies dramatically—resonance. Resonance can constructively amplify useful vibrations (energy transfer in machinery) or destructively cause structural failure. Friction damps oscillations by dissipating kinetic energy, reducing amplitude and preventing dangerous resonance. Low-friction systems are resonance-prone; high-friction systems are stable but inefficient. Engineering balances damping to exploit beneficial resonance while avoiding destructive resonance."

---

### Electromagnetic Wave

**Form (a):**
"An electromagnetic cavity exhibits an electromagnetic mode at a characteristic resonant frequency. When the cavity is driven by an electromagnetic field at or near the resonant frequency, field strength grows dramatically—a phenomenon called resonance. Resonance can be constructive, amplifying radiation and enabling radiation emission, or destructive, causing dielectric breakdown. The presence of resistance dissipates electromagnetic energy, reducing field strength and preventing resonance from reaching dangerous levels. Cavities with low resistance are vulnerable to resonance; those with high resistance are stable but sluggish. Optimal cavity design balances resistance to permit beneficial resonance while suppressing harmful resonance. Electromagnetism studies how cavities manage resonance across scales."

**Form (b):**
"Electromagnetic cavities support standing waves at discrete resonant frequencies. When driven by an external field near a resonant frequency, field strength amplifies dramatically—resonance. Resonance can constructively enhance radiation emission (lasers, antennas) or destructively cause dielectric breakdown. Resistance in cavity walls dissipates electromagnetic energy, damping oscillations and preventing dangerous resonance. Low-loss cavities are resonance-prone; high-loss cavities are stable but inefficient. Cavity design balances loss to exploit beneficial resonance while avoiding destructive resonance."

---

### Population Dynamics

**Form (a):**
"A population exhibits a population cycle at a characteristic generation time. When the population is driven by environmental forcing at or near the generation time, population size grows dramatically—a phenomenon called population resonance. Population resonance can be constructive, amplifying population growth and enabling population stability, or destructive, causing population crash. The presence of density dependence dissipates metabolic energy, reducing population size and preventing population resonance from reaching dangerous levels. Populations with low density dependence are vulnerable to population resonance; those with high density dependence are stable but sluggish. Optimal population design balances density dependence to permit beneficial population resonance while suppressing harmful population resonance. Ecology studies how populations manage population resonance across scales."

**Form (b):**
"Populations exhibit intrinsic cycles driven by generation time and reproduction rate. When environmental forcing (resource availability, predation) oscillates near the population's natural cycle frequency, population size amplifies dramatically—population resonance. Resonance can constructively stabilize populations (periodic resource pulses matching breeding cycles) or destructively cause population crashes (predator-prey misalignment). Density dependence damps population oscillations by dissipating metabolic energy, reducing amplitude and preventing dangerous resonance. Populations with weak density dependence are resonance-prone; those with strong density dependence are stable but less responsive. Ecology studies how density dependence balances population responsiveness against crash risk."

Justification: "Population resonance" is not standard terminology; it describes the amplification of population cycles when environmental forcing matches intrinsic population frequency.

---

### Neural Circuit

**Form (a):**
"A neural circuit exhibits oscillation at a characteristic oscillation frequency. When the circuit is driven by an input signal at or near the oscillation frequency, firing rate grows dramatically—a phenomenon called resonance. Resonance can be constructive, amplifying neural signal and enabling information processing, or destructive, causing seizure. The presence of inhibitory synapse dissipates neural activity, reducing firing rate and preventing resonance from reaching dangerous levels. Circuits with low inhibitory synapse are vulnerable to resonance; those with high inhibitory synapse are stable but sluggish. Optimal circuit design balances inhibitory synapse to permit beneficial resonance while suppressing harmful resonance. Neuroscience studies how circuits manage resonance across scales."

**Form (b):**
"Neural circuits oscillate at intrinsic frequencies determined by membrane properties and synaptic time constants. When driven by input signals near a circuit's resonant frequency, firing rates amplify dramatically—neural resonance. Resonance can constructively enhance information processing (selective frequency tuning) or destructively trigger seizures (pathological synchronization). Inhibitory synapses damp oscillations by dissipating neural activity, reducing amplitude and preventing dangerous resonance. Circuits with weak inhibition are seizure-prone; those with strong inhibition are stable but less responsive. Neural circuit design balances inhibition to exploit beneficial resonance while preventing pathological resonance."

---

### Financial Market

**Form (a):**
"A financial market exhibits a boom-bust cycle at a characteristic business cycle frequency. When the market is driven by an exogenous shock at or near the business cycle frequency, price volatility grows dramatically—a phenomenon called market resonance. Market resonance can be constructive, amplifying price signal and enabling price discovery, or destructive, causing market crash. The presence of a circuit breaker dissipates capital, reducing price volatility and preventing market resonance from reaching dangerous levels. Markets with low circuit breaker are vulnerable to market resonance; those with high circuit breaker are stable but sluggish. Optimal market design balances circuit breaker to permit beneficial market resonance while suppressing harmful market resonance. Finance studies how markets manage market resonance across scales."

**Form (b):**
"Financial markets exhibit boom-bust cycles at frequencies determined by credit cycles and investor sentiment. When exogenous shocks (policy changes, external crises) arrive near the market's natural cycle frequency, price volatility amplifies dramatically—market resonance. Resonance can constructively enhance price discovery (efficient information incorporation) or destructively trigger crashes (cascading margin calls, liquidity evaporation). Circuit breakers and trading halts dissipate capital and momentum, damping oscillations and preventing dangerous resonance. Markets with weak circuit breakers are crash-prone; those with strong circuit breakers are stable but less price-responsive. Market design balances circuit breaker strength to exploit beneficial resonance while preventing systemic crashes."

---

## Archetype Proposal: Nesting and Emergence

### Template

"[SYSTEM] at scale N consists of [COMPONENT] at scale N−1, which themselves consist of [COMPONENT] at scale N−2. Each [COMPONENT] at scale N−1 exhibits [PROPERTY_LOCAL], but when aggregated into [SYSTEM] at scale N, a new [PROPERTY_GLOBAL] emerges that is not present in any individual [COMPONENT]. This [PROPERTY_GLOBAL] cannot be predicted from [PROPERTY_LOCAL] alone; it arises from [INTERACTION] between [COMPONENT]. The [PROPERTY_GLOBAL] often feeds back to constrain [PROPERTY_LOCAL], creating a [FEEDBACK_LOOP]. [SYSTEM] that exhibit strong [FEEDBACK_LOOP] are more robust to perturbations at scale N−1 but less flexible. [FIELD] studies how [PROPERTY_GLOBAL] emerges from [INTERACTION] and how [FEEDBACK_LOOP] stabilize [SYSTEM] across scales."

### Metanym Table

| [SLOT]           | Multicellular Organism | Ecosystem           | Language            | Immune System       | Economic System     |
|------------------|----------------------|----------------------|--------------------|--------------------|---------------------|
| SYSTEM           | organism             | ecosystem           | language            | immune system       | economy             |
| COMPONENT        | cell                 | organism            | word                | lymphocyte          | firm                |
| PROPERTY_LOCAL   | metabolism           | reproduction        | meaning             | antigen specificity | profit motive       |
| PROPERTY_GLOBAL  | consciousness        | biodiversity        | grammar             | immune tolerance    | market efficiency   |
| INTERACTION      | synaptic connection  | predation           | syntax              | immune regulation   | market competition  |
| FEEDBACK_LOOP    | neuroendocrine loop  | trophic feedback    | semantic constraint | regulatory T cell   | price feedback      |
| FIELD            | neurobiology         | ecology             | linguistics         | immunology          | economics           |

### Multicellular Organism

**Form (a):**
"A multicellular organism at scale N consists of cells at scale N−1, which themselves consist of organelles at scale N−2. Each cell at scale N−1 exhibits metabolism, but when aggregated into an organism at scale N, a new consciousness emerges that is not present in any individual cell. This consciousness cannot be predicted from metabolism alone; it arises from synaptic connections between cells. The consciousness often feeds back to constrain metabolism, creating a neuroendocrine loop. Organisms that exhibit strong neuroendocrine loops are more robust to perturbations at scale N−1 but less flexible. Neurobiology studies how consciousness emerges from synaptic connections and how neuroendocrine loops stabilize organisms across scales."

**Form (b):**
"Organisms are hierarchical: cells compose tissues, tissues compose organs, organs compose systems. Individual cells exhibit metabolic activity, but the organism as a whole exhibits consciousness—subjective experience, intentionality, unified perception—that no single cell possesses. Consciousness emerges from synaptic connectivity and neural integration, not from any cell's intrinsic properties. Consciousness feeds back to regulate cellular metabolism through neuroendocrine signaling, creating homeostatic loops. Organisms with tight neuroendocrine feedback are metabolically stable but behaviorally rigid. Neurobiology examines how consciousness emerges from neural interaction and how feedback loops integrate the organism across scales."

---

### Ecosystem

**Form (a):**
"An ecosystem at scale N consists of organisms at scale N−1, which themselves consist of cells at scale N−2. Each organism at scale N−1 exhibits reproduction, but when aggregated into an ecosystem at scale N, a new biodiversity emerges that is not present in any individual organism. This biodiversity cannot be predicted from reproduction alone; it arises from predation between organisms. The biodiversity often feeds back to constrain reproduction, creating a trophic feedback. Ecosystems that exhibit strong trophic feedback are more robust to perturbations at scale N−1 but less flexible. Ecology studies how biodiversity emerges from predation and how trophic feedback stabilizes ecosystems across scales."

**Form (b):**
"Ecosystems are hierarchical: cells compose organisms, organisms compose communities, communities compose ecosystems. Individual organisms exhibit reproductive drive, but the ecosystem as a whole exhibits biodiversity—species richness, functional redundancy, structural complexity—that no single organism determines. Biodiversity emerges from predator-prey interactions and competition, not from any organism's intrinsic traits. Biodiversity feeds back to regulate organism reproduction through trophic cascades, creating stability. Ecosystems with tight trophic feedback are resistant to invasion but less productive. Ecology examines how biodiversity emerges from ecological interaction and how trophic feedback stabilizes ecosystems across scales."

---

### Language

**Form (a):**
"A language at scale N consists of words at scale N−1, which themselves consist of phonemes at scale N−2. Each word at scale N−1 exhibits meaning, but when aggregated into a language at scale N, a new grammar emerges that is not present in any individual word. This grammar cannot be predicted from meaning alone; it arises from syntax between words. The grammar often feeds back to constrain meaning, creating a semantic constraint. Languages that exhibit strong semantic constraint are more robust to perturbations at scale N−1 but less flexible. Linguistics studies how grammar emerges from syntax and how semantic constraint stabilizes languages across scales."

**Form (b):**
"Languages are hierarchical: phonemes compose words, words compose sentences, sentences compose discourse. Individual words carry meaning, but the language as a whole exhibits grammar—systematic rules for combining words, agreement patterns, word order constraints—that no single word determines. Grammar emerges from syntactic combination and historical convention, not from any word's intrinsic properties. Grammar feeds back to constrain word meaning through semantic fields and collocational patterns, creating coherence. Languages with tight semantic constraints are more stable but less innovative. Linguistics examines how grammar emerges from syntactic interaction and how semantic feedback stabilizes languages across scales."

---

### Immune System

**Form (a):**
"An immune system at scale N consists of lymphocytes at scale N−1, which themselves consist of genes at scale N−2. Each lymphocyte at scale N−1 exhibits antigen specificity, but when aggregated into an immune system at scale N, a new immune tolerance emerges that is not present in any individual lymphocyte. This immune tolerance cannot be predicted from antigen specificity alone; it arises from immune regulation between lymphocytes. The immune tolerance often feeds back to constrain antigen specificity, creating a regulatory T cell. Immune systems that exhibit strong regulatory T cell are more robust to perturbations at scale N−1 but less flexible. Immunology studies how immune tolerance emerges from immune regulation and how regulatory T cell stabilizes immune systems across scales."

**Form (b):**
"Immune systems are hierarchical: genes compose lymphocytes, lymphocytes compose clones, clones compose the immune repertoire. Individual lymphocytes exhibit antigen specificity, but the immune system as a whole exhibits tolerance—the ability to distinguish self from non-self, to mount proportionate responses, to avoid autoimmunity—that no single lymphocyte determines. Tolerance emerges from regulatory interactions between helper, effector, and regulatory T cells, not from any lymphocyte's intrinsic properties. Tolerance feeds back to suppress autoreactive lymphocytes through regulatory T cell signaling, creating homeostasis. Immune systems with tight regulatory feedback are stable but less responsive to novel pathogens. Immunology examines how tolerance emerges from immune regulation and how regulatory feedback stabilizes the immune system across scales."

---

### Economic System

**Form (a):**
"An economic system at scale N consists of firms at scale N−1, which themselves consist of workers at scale N−2. Each firm at scale N−1 exhibits profit motive, but when aggregated into an economy at scale N, a new market efficiency emerges that is not present in any individual firm. This market efficiency cannot be predicted from profit motive alone; it arises from market competition between firms. The market efficiency often feeds back to constrain profit motive, creating a price feedback. Economies that exhibit strong price feedback are more robust to perturbations at scale N−1 but less flexible. Economics studies how market efficiency emerges from market competition and how price feedback stabilizes economies across scales."

**Form (b):**
"Economies are hierarchical: workers compose firms, firms compose industries, industries compose markets. Individual firms pursue profit, but the economy as a whole exhibits market efficiency—prices that reflect scarcity, allocation of resources to high-value uses, innovation incentives—that no single firm determines. Market efficiency emerges from competitive interaction and price signals, not from any firm's intrinsic strategy. Market efficiency feeds back to constrain firm profit through price competition and creative destruction, creating dynamic equilibrium. Economies with tight price feedback are stable but less entrepreneurial. Economics examines how market efficiency emerges from competitive interaction and how price feedback stabilizes economies across scales."

---

## Archetype Proposal: Threshold and Tipping

### Template

"A [SYSTEM] exhibits [BEHAVIOR_A] when [PARAMETER] is below a critical [THRESHOLD]. As [PARAMETER] increases, [SYSTEM] remains in [BEHAVIOR_A] due to [STABILIZATION], which actively resists change. However, once [PARAMETER] crosses [THRESHOLD], [STABILIZATION] fails and [SYSTEM] rapidly transitions to [BEHAVIOR_B]. This transition is often [IRREVERSIBILITY], meaning that even if [PARAMETER] decreases, [SYSTEM] does not return to [BEHAVIOR_A]. The region near [THRESHOLD] is characterized by [INSTABILITY], where small perturbations can trigger premature transition. [SYSTEM] that have already transitioned to [BEHAVIOR_B] often exhibit [HYSTERESIS], requiring [PARAMETER] to fall well below [THRESHOLD] before [BEHAVIOR_A] can be restored. [FIELD] studies [THRESHOLD] dynamics to predict [TIPPING_POINT] and design interventions that prevent unwanted [TRANSITION]."

### Metanym Table

| [SLOT]           | Climate System      | Ecosystem Collapse  | Neural Firing       | Social Movement     | Organizational Change |
|------------------|--------------------|--------------------|--------------------|--------------------|----------------------|
| SYSTEM           | climate             | ecosystem          | neuron              | society             | organization        |
| PARAMETER        | CO2 concentration  | resource depletion | input current       | grievance intensity | organizational stress |
| BEHAVIOR_A       | stable climate      | thriving ecosystem | quiescence          | social order        | status quo           |
| BEHAVIOR_B       | runaway warming    | barren landscape   | firing              | revolution          | organizational collapse |
| THRESHOLD        | tipping point       | critical threshold | firing threshold    | revolutionary threshold | breaking point      |
| STABILIZATION    | negative feedback   | ecosystem resilience | resting potential   | social control       | organizational inertia |
| IRREVERSIBILITY  | irreversible        | irreversible       | irreversible        | irreversible        | irreversible        |
| INSTABILITY      | critical slowing   | critical transition | subthreshold noise  | pre-revolutionary tension | organizational fragility |
| HYSTERESIS       | hysteresis          | hysteresis         | hysteresis          | hysteresis          | hysteresis          |
| TIPPING_POINT    | tipping point       | tipping point      | firing threshold    | revolutionary moment | organizational collapse |
| TRANSITION       | transition          | collapse           | action potential    | revolution          | collapse             |
| FIELD            | climate science     | ecology            | neuroscience        | political science   | organizational theory |

### Climate System

**Form (a):**
"A climate exhibits stable climate when CO2 concentration is below a critical tipping point. As CO2 concentration increases, the climate remains in stable climate due to negative feedback, which actively resists change. However, once CO2 concentration crosses the tipping point, negative feedback fails and the climate rapidly transitions to runaway warming. This transition is often irreversible, meaning that even if CO2 concentration decreases, the climate does not return to stable climate. The region near the tipping point is characterized by critical slowing, where small perturbations can trigger premature transition. Climates that have already transitioned to runaway warming often exhibit hysteresis, requiring CO2 concentration to fall well below the tipping point before stable climate can be restored. Climate science studies tipping point dynamics to predict tipping points and design interventions that prevent unwanted transitions."

**Form (b):**
"The climate system exhibits stable conditions when CO2 remains below critical thresholds. Negative feedbacks—increased cloud cover, enhanced weathering—resist warming. But once CO2 crosses a tipping point, these stabilizing mechanisms fail and warming accelerates catastrophically. The transition to runaway warming is often irreversible; carbon sequestration cannot restore the prior climate state. Near tipping points, critical slowing occurs: recovery from perturbations slows, and small disturbances can trigger collapse. Systems already in runaway warming exhibit hysteresis: CO2 must fall far below the original threshold before stable conditions return. Climate science uses tipping-point theory to identify dangerous thresholds and design mitigation strategies."

---

### Ecosystem Collapse

**Form (a):**
"An ecosystem exhibits thriving ecosystem when resource depletion is below a critical critical threshold. As resource depletion increases, the ecosystem remains in thriving ecosystem due to ecosystem resilience, which actively resists change. However, once resource depletion crosses the critical threshold, ecosystem resilience fails and the ecosystem rapidly transitions to barren landscape. This transition is often irreversible, meaning that even if resource depletion decreases, the ecosystem does not return to thriving ecosystem. The region near the critical threshold is characterized by critical transition, where small perturbations can trigger premature transition. Ecosystems that have already transitioned to barren landscape often exhibit hysteresis, requiring resource depletion to fall well below the critical threshold before thriving ecosystem can be restored. Ecology studies critical threshold dynamics to predict tipping points and design interventions that prevent unwanted collapses."

**Form (b):**
"Ecosystems exhibit thriving conditions when resource extraction remains below critical thresholds. Ecosystem resilience—biodiversity, functional redundancy, regenerative capacity—resists degradation. But once extraction crosses a tipping point, these stabilizing mechanisms fail and ecosystem collapse accelerates. The transition to barren landscape is often irreversible; restoration cannot recover the prior ecosystem state. Near tipping points, critical transitions occur: recovery from disturbances slows, and small perturbations trigger collapse. Ecosystems already collapsed exhibit hysteresis: resource extraction must fall far below the original threshold before recovery begins. Ecology uses critical-transition theory to identify dangerous thresholds and design conservation strategies."

---

### Neural Firing

**Form (a):**
"A neuron exhibits quiescence when input current is below a critical firing threshold. As input current increases, the neuron remains in quiescence due to resting potential, which actively resists change. However, once input current crosses the firing threshold, resting potential fails and the neuron rapidly transitions to firing. This transition is often irreversible, meaning that even if input current decreases, the neuron does not return to quiescence. The region near the firing threshold is characterized by subthreshold noise, where small perturbations can trigger premature transition. Neurons that have already transitioned to firing often exhibit hysteresis, requiring input current to fall well below the firing threshold before quiescence can be restored. Neuroscience studies firing threshold dynamics to predict firing thresholds and design interventions that prevent unwanted action potentials."

**Form (b):**
"Neurons exhibit quiescence when input current remains below the firing threshold. The resting potential—maintained by ion pumps and leak channels—resists depolarization. But once input current crosses the threshold, voltage-gated channels open and the neuron rapidly fires an action potential. The transition is irreversible during the action potential; the neuron cannot return to rest until repolarization completes. Near threshold, subthreshold noise can trigger premature firing, and small current fluctuations destabilize the resting state. Neurons exhibit hysteresis: after firing, the threshold temporarily rises, requiring input current to fall well below the original threshold before the neuron can fire again. Neuroscience uses threshold dynamics to understand neural coding and design neuroprosthetics."

---

### Social Movement

**Form (a):**
"A society exhibits social order when grievance intensity is below a critical revolutionary threshold. As grievance intensity increases, the society remains in social order due to social control, which actively resists change. However, once grievance intensity crosses the revolutionary threshold, social control fails and the society rapidly transitions to revolution. This transition is often irreversible, meaning that even if grievance intensity decreases, the society does not return to social order. The region near the revolutionary threshold is characterized by pre-revolutionary tension, where small perturbations can trigger premature transition. Societies that have already transitioned to revolution often exhibit hysteresis, requiring grievance intensity to fall well below the revolutionary threshold before social order can be restored. Political science studies revolutionary threshold dynamics to predict tipping points and design interventions that prevent unwanted revolutions."

**Form (b):**
"Societies exhibit social order when grievance intensity remains below critical thresholds. Social control—police, ideology, institutional legitimacy—resists mobilization. But once grievance intensity crosses a tipping point, these stabilizing mechanisms fail and revolution accelerates. The transition to revolution is often irreversible; institutional collapse cannot restore prior order. Near tipping points, pre-revolutionary tension occurs: small disturbances trigger large responses, and society becomes fragile. Societies already in revolution exhibit hysteresis: order must be restored through force or institutional rebuilding; grievance reduction alone cannot restore prior stability. Political science uses tipping-point theory to identify revolutionary thresholds and design conflict-prevention strategies."

---

### Organizational Change

**Form (a):**
"An organization exhibits status quo when organizational stress is below a critical breaking point. As organizational stress increases, the organization remains in status quo due to organizational inertia, which actively resists change. However, once organizational stress crosses the breaking point, organizational inertia fails and the organization rapidly transitions to organizational collapse. This transition is often irreversible, meaning that even if organizational stress decreases, the organization does not return to status quo. The region near the breaking point is characterized by organizational fragility, where small perturbations can trigger premature transition. Organizations that have already transitioned to organizational collapse often exhibit hysteresis, requiring organizational stress to fall well below the breaking point before status quo can be restored. Organizational theory studies breaking point dynamics to predict tipping points and design interventions that prevent unwanted collapses."

**Form (b):**
"Organizations exhibit stability when internal stress remains below critical thresholds. Organizational inertia—established routines, institutional culture, sunk costs—resists change. But once stress crosses a breaking point, these stabilizing mechanisms fail and organizational collapse accelerates. The transition is often irreversible; restructuring cannot restore the prior organization. Near breaking points, organizational fragility occurs: small disruptions trigger large responses, and the organization becomes unstable. Organizations already collapsed exhibit hysteresis: recovery requires rebuilding from scratch; stress reduction alone cannot restore prior stability. Organizational theory uses tipping-point dynamics to identify critical thresholds and design change-management strategies."

---

## Summary

**Recursive archetypal contexts in this submission:**
- **Archetype 1 (Constraint Propagation)**: Not recursive in the strict sense, but exhibits self-similarity across domains.
- **Archetype 3 (Nesting and Emergence)**: **Explicitly recursive**. Each domain instantiation shows N → N−1 → N−2 nesting (e.g., organism → cell → organelle; ecosystem → organism → cell; language → word → phoneme).

**System structure diversity:**
1. **Constraint Propagation**: Network constraint satisfaction; convergence/divergence dynamics.
2. **Boundary Dissolution**: Permeable barrier maintenance; erosion and collapse.
3. **Resonance and Damping**: Driven oscillatory systems; frequency-matching amplification.
4. **Nesting and Emergence**: Hierarchical composition; downward causation via feedback.
5. **Threshold and Tipping**: Bistable systems; critical transitions and hysteresis.