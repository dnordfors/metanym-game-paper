<!-- 2026-06-11: appendix filenames aligned with the paper's letters (A=rating estimators, B=prompts, C=council evaluation, D=GPQA audit); stale shifted-letter duplicates removed. See commit history. -->
# Appendix A. Rating estimators

Every rating comes from one object: the scores the participants produces when each model grades the others' portfolios, swept across the anchor. No external answer key is used. This appendix defines that object and the estimators built on it.

**Panel and tasks.** Twelve models are the participants, indexed by $s,t\in\{1,\dots,12\}$. Each is both a *submission* (its portfolio is graded) and an *evaluator* (it grades the others). Every model was in fact asked to grade every portfolio including its own, and those self-evaluations are in the released run data; but **no rating below uses a model's grade of its own portfolio** — every estimator here is *leave-self-out*. The two criteria implement that exclusion differently, and the difference is deliberate: the factual-competence estimator (A.2.a) keeps the self-entry as a column of its matrix and sets it to the anchor value (A5), so the factorisation stays on one rectangular matrix; the rating-consistency estimator (A.2.b) and the generation rating (A.1) drop the self-pair from the unit set outright. Below, $s,t$ denote a model in whichever role an equation needs — the graded submission in A.1, the grading evaluator in A.2. A portfolio holds five *archetypes* — the templates a model produced — each realised as several *parallel contexts*, the same template instantiated in different domains. A model is rated on the two tasks of the game (§2.b): to **generate** archetypal context templates *and* their instantiations, and to **evaluate** others' portfolios. It earns, correspondingly,

$$ G=\text{generation rating},\qquad E=\text{evaluation rating}. \tag{A1}$$

These yield the total rating (A14), and $E$ has two parts (A12); each is constructed below.

**Rubric and anchor.** Scoring uses six axes, each rated on a $1$–$10$ scale: a *factual* axis (scored once per parallel context) and five *non-factual* axes — beauty, intelligence, instantiation-distinctness and impressive-length (once per archetype) and structural-diversity among the archetypes (once per portfolio). Every score is given relative to a fixed reference portfolio, the **anchor** — the model $a$ whose portfolio won the un-anchored initial selection (§4.1), declared to score $7$ on every axis. Because $a$ is a participant it also evaluates; the anchor is required to be a council member (A.3), so its factual competence $f_a>0$ and rating consistency $\bar r_a>0$ (A.2). The anchor value is swept, $\theta\in\Theta=\{5,6,7,8\}$ — each value a separate scoring pass with the reference declared at that value — and $\theta^{*}=7$ is the production anchor. Write $r_{t,s,x,u}(\theta)$ for evaluator $t$'s score of unit $u$ of axis $x$ of submission $s$ at anchor $\theta$.

## A.1 Generation rating

Evaluator $t$'s overall score of submission $s$ averages within each axis, then across axes (so axes weigh equally although a per-portfolio axis has one unit and the factual axis has many):

$$ o_{t,s}=\frac{1}{|\mathcal{X}|}\sum_{x\in\mathcal{X}}\frac{1}{|U_x|}\sum_{u\in U_x} r_{t,s,x,u}(\theta^{*}), \tag{A2}$$

where $\mathcal{X}$ is the axis set and $U_x$ the units of axis $x$. Production ratings use only the production anchor $\theta^{*}$; the sweep $\Theta$ enters the benchmark solely through rating consistency (A.2.b). The generation rating is the leave-self-out mean over the council $\mathcal{C}$ (A.3):

$$ G_s=\frac{1}{|\mathcal{C}\setminus\{s\}|}\sum_{t\in\mathcal{C},\,t\ne s} o_{t,s}. \tag{A3}$$

Confidence intervals: 95% percentile bootstrap over the per-(submission, archetype) scoring units; a gap $G_s-G_{s'}$ is *resolvable* when the paired bootstrap (resampling the same units for both models) puts its 95% interval clear of $0$. This six-axis $G_s$ is §4.3's generation rating and the statistic the §5.8 anchor-sweep invariance check re-ranks; the official leaderboard's $G$ is the split form (A13), $G=\tfrac12(G^{F}+G^{C})$, not (A3).

## A.2 Evaluation ratings

The evaluation rating $E$ measures how good a judge a model is, in two independent parts: how accurately it detects factual errors (A.2.a) and how stably it ranks work as the anchor moves (A.2.b).

### A.2.a Factual competence and instantiation falseness (SVD)

With no key, we must find both which evaluators judge factuality well and which instantiations are factually weak. One factorisation gives both.

Stack the participants' factual scores into a matrix $F$ (evaluators $\times$ instantiations): $F_{sj}$ is evaluator $s$'s $1$–$10$ factual rating of pooled parallel context $j$, used **directly** — with no thresholding into a true/false verdict, so the full graded judgement is kept. A model does not grade its own submission; those self-entries — and the rare missing evaluator–target entries — are set to the anchor value (treated as reference-clean):

$$ F_{sj}=r_{s,j}\in\{1,\dots,10\}\qquad(\text{self-entries }=\theta^{*}=7). \tag{A5}$$

(The equation numbering carries a historical gap: there is no (A4).)

Centre each row (subtract the evaluator's mean over its $N$ entries, removing its overall leniency); only the leading triple is used:

$$ \tilde F = F-\bar r\,\mathbf 1^{\top}=U\Sigma V^{\top},\qquad \sigma_1,\quad u\equiv U_{\cdot 1},\quad v\equiv V_{\cdot 1}. \tag{A6}$$

This is the rank-one model $\tilde F_{sj}\approx \sigma_1\,u_s v_j$. The hypothesis is that competent evaluators **agree on the centred pattern** — which instantiations are weaker, once each evaluator's own leniency is subtracted — and the leading axis of that agreement is the competence axis. The left singular vector is factual competence,

$$ f\equiv u,\qquad \text{signed so } \textstyle\sum_s f_s>0,\qquad f^{+}_s=\max(f_s,0), \tag{A7}$$

the quantity the council gate uses (A.3) and that $E^{F}$ rescales (A12), clamped at zero so an evaluator anti-correlated with the consensus carries no weight. Centering is essential, not cosmetic: the raw scores cluster at the anchor (most contexts are clean, near $7$), so on the *un*-centred matrix the leading axis is simply that shared level and ranks the most lenient — non-detecting — evaluators highest; subtracting each row's mean removes the level so the leading axis becomes agreement-on-pattern. (Equivalently $u$ is the leading eigenvector of the row-centred inter-evaluator Gram $\tilde F\tilde F^{\top}$.) Competence is a continuum, not a hard cliff: an evaluator whose centred scores are flat or idiosyncratic lands near zero, and the council gate (A.3) reads the gap above that inert band.

Because every row of $\tilde F$ sums to zero, the all-ones vector lies in its null space, so each right singular vector is orthogonal to it and itself sums to zero: $v$ is therefore signed, and we orient it to agree with the participants ($\operatorname{corr}(v,\ \text{column means of }\tilde F)>0$, so positive means *factually stronger* — a cleaner instantiation, scored above the evaluators' norm). The left vector $u$ is sign-fixed by (A7) and clamped to $f^{+}$; on soft ratings it is not guaranteed non-negative (an evaluator can be anti-correlated with the consensus), so the clamp is an explicit convention rather than an automatic property.

The right singular vector $v$ orders the instantiations by factual standing; to read it back on the native $1$–$10$ scale we reconstruct each instantiation's rating from the rank-one model and a competence-weighted baseline. The **competence-weighted consensus rating** of instantiation $j$ is

$$ \hat r_j \;=\; C+\kappa\,v_j,\qquad C=\frac{\sum_s f^{+}_s\,\bar r_s}{\sum_s f^{+}_s},\quad \kappa=\sigma_1\,\frac{\sum_s f^{+}_s\,u_s}{\sum_s f^{+}_s}>0, \tag{A8}$$

an affine read-off of the right vector ($C$ the competence-weighted clean level, $\kappa$ the rank-one scale). It is exactly the rank-one approximation of the competence-weighted mean rating $\big(\sum_s f^{+}_s F_{sj}\big)/\sum_s f^{+}_s$, the two differing only by the discarded higher-rank residual — on the canonical run they agree within $0.14$ on the anchored scale ($r = 1.00$; `generation_factuality_validation.py`). Averaging over a generator's own instantiations $J_g$ gives the key-free **generation-factuality** rating

$$ G^{F}_{\text{svd},g} \;=\; \frac1{|J_g|}\sum_{j\in J_g}\hat r_j. \tag{A9}$$

No $\times7$ rescaling is needed — the rating is already on the $1$–$10$ scale: clean instantiations sit at $v_j\approx0$, hence at $C\approx7$, so a reference-clean portfolio scores $\approx7$ by construction (the declared-clean reference scores $7$ exactly, not measured). $G^{F}_{\text{svd}}$ is the benchmark's generation-side factual rating $G^{F}$: it enters the total $T$ through $G=\tfrac12(G^{F}+G^{C})$ (A13–A14). It is no part of the evaluation rating $E$.

This is the exact dual of (A7): the **left** singular vector rates an evaluator's competence at *spotting* a factually weak instantiation; the **right**, aggregated to generators through (A8)–(A9), rates a generator's competence at *producing a sound* one — both from the one factorisation, with no key. $G^{F}_{\text{svd}}$ carries a 95% bootstrap CI computed by resampling each generator's own instantiation ratings $\hat r_j$ — one unit per parallel context — with the participants consensus $(C,\kappa,v)$ held fixed — the dominant source of a generator's uncertainty being the spread of its own instantiations.

*Why it works.* Better judges converge on the same relative assessment; their shared axis is that consensus; on a vendor-diverse participant set with no common bias, the consensus is the truth. The lone assumption is that the only thing the evaluators share is the truth — a same-vendor bloc with a common bias would add a spurious shared component — so competence is read off a vendor-diverse participant set with a shared-bias check (§4.2). $f$ carries a 95% bootstrap CI over the $N$ contexts; the council (A.3) admits $s$ only when that CI sits clear of the inert band.

### A.2.b Rating consistency

An evaluator's **rating consistency** is its capacity to hold a stable standard for each non-factual criterion; we measure it with the **anchor sweep**. A reliable evaluator ranks portfolios the same way wherever the anchor sits; only the absolute numbers should move. The anchor is set to each of the four swept values $5, 6, 7, 8$ in turn ($7$ is the value used in production), and we ask whether the evaluator's ranking survives the shift. The Pearson correlation captures exactly this: it is unchanged by a common shift or stretch, so the harmless rise from raising the anchor costs nothing and only a genuine reordering does.

For evaluator $s$ and axis $x$, let $v_{s,x}(\theta)$ be $s$'s axis-$x$ scores across that axis's units at anchor $\theta$. Eleven portfolios are graded — the anchor's own is the fixed reference, not a graded free-generation submission — so an evaluator that is itself one of the eleven is scored, leave-self-out, on the other **ten**: $50=10\times5$ units for the four per-archetype non-factual axes, $250=10\times25$ parallel contexts for factual, and $10$ portfolios for structural-diversity. The anchor $a$ is the exception: its portfolio is not among the eleven, so it grades all of them and its unit counts are $55$, $275$ and $11$. (Throughout, the two submissions that returned a sixth archetype contribute their first five archetypes only, so every portfolio weighs $5$ archetypes and $25$ contexts — this is the same balancing that gives the factual-competence estimator its $275$ columns. These are design counts; observed coverage meets them for eight of the twelve evaluators and falls short where a grading call did not return — by one archetype for claude-sonnet-4 and gpt-4o-mini, and by two whole portfolios for gpt-4.1-nano, which grades $8$ rather than $10$. A missing entry is dropped pairwise by the correlation in (A10)–(A11), so a shortfall costs units, not correctness.) The per-axis rating consistency — its rating consistency on that axis — is the average Pearson correlation over the anchor pairs on which it is defined,

$$ r_{s,x}=\frac{1}{|\mathcal P_{s,x}|}\sum_{(\theta,\theta')\in\mathcal P_{s,x}}\operatorname{corr}\!\big(v_{s,x}(\theta),v_{s,x}(\theta')\big), \tag{A10}$$

where $\mathcal P_{s,x}$ is the subset of the $\binom{4}{2}=6$ anchor pairs for which both score vectors are non-constant (a constant vector makes the correlation undefined, so that pair is dropped). This per-axis breakdown is the diagnostic per-axis rating consistency $r_{s,x}$ (§4.4 reports it anchored, $E^{C}_a = 7\,r_{s,x}/r_{a,x}$; A12, A.6). The single **collapsed rating-consistency** score $\bar r_s$ that gates the council is not the mean of (A10) but a single collapsed score: average the four non-factual per-archetype axes (beauty, intelligence, instantiation-distinctness, impressive-length) into one value per (submission, archetype), giving a vector $v_{s}(\theta)$ over $s$'s $50$ leave-self-out units ($55$ for the anchor), and take

$$ \bar r_s=\frac{1}{|\mathcal P_{s}|}\sum_{(\theta,\theta')\in\mathcal P_{s}}\operatorname{corr}\!\big(v_{s}(\theta),v_{s}(\theta')\big), \tag{A11}$$

with $\mathcal P_s$ the anchor pairs on which $v_s$ is non-constant. Factual is A.2.a's job and is excluded; structural-diversity, one score per portfolio, is too coarse for a per-archetype vector and is excluded too. The council gate (A.3) uses $\bar r_s\ge0.78$. These statistics use only $s$'s own scores, so they are independent of the rest of the participants — which is why the leave-self-out convention here cannot cascade into A.2.a. $\bar r_s$ is reported with a bootstrap CI resampled over the full $55$-atom (submission, archetype) grid of A.5, the same grid every CI in this paper uses; each evaluator then contributes whichever of the resampled atoms are among its own $50$ (the anchor's $55$). The two numbers are distinct and both are needed: $55$ is the shared resampling grid, $50$ is one graded evaluator's effective sample.

## A.3 The council

The ratings are formed in two passes. First, factual competence $f$ (A7) and rating consistency $\bar r$ (A11) are computed over all twelve evaluators. Second, the **council** $\mathcal{C}$ is taken as the *reliable* subset, and the generation rating $G$ (A3) is then recomputed using only $\mathcal{C}$ as evaluators.

Being right (A.2.a) and being self-consistent (A.2.b) are different virtues, and a trustworthy judge needs both. A model is **reliable** when its competence sits clear of the inert band — its 95% bootstrap CI (A.2.a) separates it from the near-zero cluster of flat or idiosyncratic raters — and its rating consistency satisfies $\bar r_s\ge0.78$. Here **eight** of the twelve clear the reliability gate $\bar r_s\ge0.78$, but only **five** clear it *and* the factual-competence gate, and it is that conjunction that seats the council. The two gates are independent, and the three models that clear one but not the other are the proof: a precise-but-inaccurate rater can clear $\bar r_s\ge0.78$ yet have $f_s$ indistinguishable from $0$ (gpt-4.1-mini is the clean case, $\bar r_s=0.86$ with a loading in the inert band). Selecting evaluators this way does not bias the ratings they feed, because $f_s$ is essentially invariant to participant membership (A.2.a): the council-only and full-participant orderings coincide.

## A.4 The total rating

The components sit on different scales — generation ($G^{F}$, $G^{C}$) on the $1$–$10$ rubric, $f$ a singular-vector entry, $\bar r$ a correlation in $[0,1]$. We place them on one scale by the rule that already fixes generation: the anchor model scores $7$. Since $a$ is a participant it has a factual competence $f_a>0$ and rating consistency $\bar r_a>0$, and we rescale each evaluator index so that $a$ scores $7$:

$$ E^{F}_s=7\,\frac{f_s}{f_a},\qquad E^{C}_s=7\,\frac{\bar r_s}{\bar r_a}. \tag{A12}$$

Because $f_s$ enters only through the ratio $f_s/f_a$, the singular vector's arbitrary scale cancels — $f$ never needs normalising. Generation splits the same way evaluation does: the generator's factual competence $G^{F}$ (the SVD generation factuality, A9) and its criterion quality $G^{C}$, the council's mean over the five non-factual axes of its scores of $s$ — but **reliability-weighted**: on each axis $x$ a judge's vote is weighted by its own per-axis rating consistency $r_{t,x}$ (A10), so a judge with a firm standard on $x$ counts fully and one with none counts little, mirroring the way the SVD weights the factual side by competence,

$$ G^{C}_s=\frac{1}{|\mathcal{X}_{5}|}\sum_{x\in\mathcal{X}_{5}}\frac{\sum_{t\in\mathcal{C}\setminus\{s\}}\max(r_{t,x},0)\,\bar r_{t,s,x}}{\sum_{t\in\mathcal{C}\setminus\{s\}}\max(r_{t,x},0)}, \tag{A12b}$$

with $\mathcal{X}_{5}$ the five non-factual axes, $\bar r_{t,s,x}$ judge $t$'s mean score of $s$ on axis $x$ at the production anchor, and the anchor scoring $7$ on each axis by construction; $G^{F}$ and $G^{C}$ are both already on the anchored rubric. The two halves of each side combine equally,

$$ G_s=\tfrac12\big(G^{F}_s+G^{C}_s\big),\qquad E_s=\tfrac12\big(E^{F}_s+E^{C}_s\big), \tag{A13}$$

and generation and evaluation weigh equally in turn, so the total is the mean of the four anchored competences — a symmetric $2\times2$ of {generator, evaluator} $\times$ {factual, criterion}:

$$ T_s=\tfrac12\big(G_s+E_s\big)=\tfrac14\big(G^{F}_s+G^{C}_s+E^{F}_s+E^{C}_s\big). \tag{A14}$$

The anchor scores $7$ on every component, hence $\approx7$ on $T$: each rating reads against one reference — $7$ is the anchor portfolio, as producer and as judge — and beating it on a task lifts that component above $7$. A model that detects nothing sits at the inert floor, $E^{F}_s\approx0$, forfeiting its full quarter for factual judging and dropping below the council, but not erased, since the other three components remain. Two conventions keep the arithmetic honest: a worse-than-chance loading is clamped to $0$ before its ratio in (A12), and a negative per-axis weight likewise where it enters (A12b); no negative $\bar r$ occurs in the data — the anchor itself is a council member, so $f_a,\bar r_a>0$ — and the singular-vector sign is fixed as in (A7). The combination weights in $T$ are not free — the three equalities ($G^{F}$ with $G^{C}$, $E^{F}$ with $E^{C}$, generation with evaluation) and the anchor-$7$ convention fix every weight and scale; the council gates of A.3, the self-entry and centering conventions in (A5)–(A6), and the sweep values are reliability and protocol choices, separate from these weights. The leaderboard is §4.7.

## A.5 Confidence intervals

Every rating is reported with a 95% **percentile bootstrap** interval: the rating's resampling unit is drawn with replacement, the rating is recomputed, and the 2.5th and 97.5th percentiles of the replicates form the interval ($\sim10^3$–$10^4$ replicates). [The unit](#tab-bootstrap-units) is the natural independent observation for each rating:

<a id="tab-bootstrap-units"></a>

| Rating | Resampled unit | Notes |
|---|---|---|
| $G$ (A3) | the per-(submission, archetype) scoring units | paired across two models for a *resolvable* gap (interval of $G_s-G_{s'}$ excludes $0$) |
| $f$, hence $E^{F}$ (A7, A12) | the $N$ parallel contexts | align each replicate's top-2 left subspace to the full-sample one by 2-component Procrustes, then read the aligned leading loading — the leading axis is near-degenerate between the Anthropic and Google blocs, so a single-vector resample would swap components |
| $\bar r$, hence $E^{C}$ (A11, A12) | the $55$ (submission, archetype) atoms of the shared grid | the evaluator reads only the resampled atoms that are not its own ($50$ of the $55$; all $55$ for the anchor); a constant (zero-variance) anchor pair is dropped |

Table: The bootstrap resampling unit for each rating, with the convention each one applies.

The evaluation rating $E$ and the total $T$ are **not** obtained by combining the component intervals with an analytic (independent-variance) formula. The components are computed from the same evaluation data and are therefore correlated — $G$, $E^{F}$ and $E^{C}$ all derive from the free-generation evaluations, so their sampling errors move together — and an independent-variance sum would misstate the interval. Instead $E$ and $T$ are bootstrapped **jointly**, resampling on the coarsest shared grid so a single draw serves all three free-generation components: the **(submission, archetype) atom**. The grid holds $55$ atoms — eleven graded portfolios $\times$ five archetypes — and they are resampled with replacement once per replicate; each atom carries the parallel contexts inside it, so the resampled atoms *induce* both the factual rating columns of $f$ (A5–A7) and the score vectors of $\bar r$ (A11), while $G$ averages over the resampled atoms of each submission. Leave-self-out is applied *after* the resample, so a graded evaluator's replicate vector is built from whichever draws fall outside its own portfolio (in expectation $50$ of the $55$) and the anchor's from all of them; the grid is shared, the per-evaluator sample is not. Every component — including the anchor's $f_a,\bar r_a$ — is recomputed on that one resample, $T$ is formed, and the percentiles of the $T$ replicates give the interval; the joint resample captures the inter-component covariance automatically. The council is the one exception: it is held at its selected membership rather than re-selected within each replicate, because the gate of A.3 is itself defined by a bootstrap CI on $f$ and re-selecting inside a replicate would require a nested bootstrap. The interval is therefore conditional on that selection.

## A.6 Generation–evaluation alignment

§4.4 asks, criterion by criterion, how closely a model's skill as a *generator* tracks its competence as a *judge* across the participants, on the five non-factual criteria (factual competence is the factual-competence estimator's separate, key-free measure, A.2.a, and is not an anchor-sweep criterion). For each criterion $x$ we hold two vectors over the models $s$: the generator competence $G_{s,x}$ — the per-axis generation rating, formed by the **reliability-weighted** council estimator (A12b), not the unweighted mean of (A3): the council's leave-self-out mean of its members' scores of $s$ on axis $x$, each member's vote weighted by its own $\max(r_{t,x},0)$ on that axis, with the anchor pinned at $7$. This is the same weighting §4.7 applies to $G^{C}$, so the per-axis table and the aggregate agree by construction, and $E$ both scores the judge and sets its weight in $G$. Against it we hold the evaluator competence $E_{s,x}=7\,r_{s,x}/r_{a,x}$, the per-axis rating consistency (A10, A12). Both are anchored so the anchor model reads $7$ on each ($G_a\equiv7$ by the anchor convention — A12b pins the anchor at $7$ on each axis — and $E_a\equiv7$ by A12), and both are carried unrounded into (A15) and rounded once for display. Their agreement is the **anchored cosine** — the cosine taken after subtracting the anchor point $(7,7)$, i.e. of each model's deviation-from-anchor as generator against its deviation-from-anchor as evaluator,

$$ \mathrm{cos}(G,E)_x=\frac{\sum_{s}(G_{s,x}-7)\,(E_{s,x}-7)}{\sqrt{\sum_{s}(G_{s,x}-7)^2}\;\sqrt{\sum_{s}(E_{s,x}-7)^2}}. \tag{A15} $$

Centering on the anchor rather than on each vector's own mean is deliberate: $7$ is one fixed external reference shared by all six criteria, so the values are comparable across axes, and the anchor — at $(7,7)$ by construction — contributes nothing to either sum. Because (A15) is scale-free in each argument, it is invariant to the (A12) rescaling; the raw competences $r$ and $G$ give the same value. The score is $1$ when generation and evaluation deviate from the anchor in lockstep and falls as the two profiles diverge: it is high across all five criteria (cosine $0.84$–$0.91$), so being a strong generator and a sharp evaluator are largely the same capability on the aesthetic and structural axes. The interval is the joint (submission, archetype) bootstrap of A.5 — each replicate recomputes $G$ and the per-axis $r$ on the resampled atoms and re-forms (A15) — and is reported alongside the point value in the §4.4 table; both come from the one code path (`build_paper1_tables.py` for the point, `alignment_cosine.py` for the interval, the latter importing the former). The statistic is a diagnostic of §4.4 and does not feed the total $T$.

## A.7 The contest and its guards

The official leaderboard (§4.7) is issued on the **contest** basis. A contest for model $c$ convenes the five council seats and $c$ itself as evaluators, over a graded set of the incumbents' portfolios, the two ballast blocks (§4.6), and $c$'s own — every estimator above unchanged: the factual factorisation (A5–A9) on the contest's columns, the consistency statistics (A10–A11) on its graded units, the anchored components and total (A12–A14), leave-self-out throughout. The anchor's $f_a$ and $\bar r_a$ are the contest's own. The $T$ interval is the A.5 joint bootstrap run on the contest's (submission, archetype) atoms.

Two **guards** decide whether the contest's factual axis is identified: the separation $\sigma_1/\sigma_2$ of (A6) must lie in $[2.0, 5.0]$, and the seats' anchored $E^{F}$ (A12) must spread by more than $2.5$ points; if either fails, the contest abstains (§4.5). Both thresholds are sized by re-analysis of the pinned run in §4.6 (`ballast_sizing.py`); the guards-hold rate is the fraction of bootstrap resamples — parallel contexts within portfolios — in which both pass.

The **authority** variant of §4.4 runs the construction (A5–A7) unchanged, one SVD per non-factual axis, reading each judge's alignment with the collective standard on that axis; it is a disclosed diagnostic and feeds nothing in (A12)–(A14).
