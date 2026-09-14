# A. Rating estimators

Every rating comes from one object: the scores the participants produce when each model grades the others' portfolios, swept across the anchor. No external answer key is used.

**Panel, tasks, anchor.** Twelve models, indexed $s,t\in\{1,\dots,12\}$, are each a *submission* (its portfolio is graded) and an *evaluator* (it grades the others). Every model was asked to grade every portfolio including its own, and those self-evaluations are released; but **no rating below uses a model's grade of its own portfolio** — every estimator is *leave-self-out*. A portfolio holds five *archetypes*, each realised as five *parallel contexts*. Scoring uses six axes on a 1–10 scale: a *factual* axis (once per parallel context) and five *non-factual* axes — beauty, intelligence, instantiation-distinctness, impressive-length (once per archetype) and structural-diversity (once per portfolio). Every score is relative to the **anchor** — the model $a$ whose portfolio won the un-anchored initial selection — declared to score 7 on every axis. The anchor value is swept, $\theta\in\Theta=\{5,6,7,8\}$, and $\theta^{*}=7$ is the production anchor. Write $r_{t,s,x,u}(\theta)$ for evaluator $t$'s score of unit $u$ of axis $x$ of submission $s$ at anchor $\theta$. A model earns a generation rating $G$ and an evaluation rating $E$ (A1); $E$ has two parts (A12).

## A.1 Generation rating

Evaluator $t$'s overall score of submission $s$ averages within each axis, then across axes:

$$ o_{t,s}=\frac{1}{|\mathcal{X}|}\sum_{x\in\mathcal{X}}\frac{1}{|U_x|}\sum_{u\in U_x} r_{t,s,x,u}(\theta^{*}), \tag{A2}$$

and the six-axis generation rating is the leave-self-out mean over the council $\mathcal{C}$,

$$ G_s=\frac{1}{|\mathcal{C}\setminus\{s\}|}\sum_{t\in\mathcal{C},\,t\ne s} o_{t,s}. \tag{A3}$$

Intervals: 95% percentile bootstrap over the per-(submission, archetype) units; a gap $G_s-G_{s'}$ is *resolvable* when the paired bootstrap puts its interval clear of 0. The official leaderboard's $G$ is the split form (A13), $G=\tfrac12(G^{F}+G^{C})$, not (A3).

## A.2 Factual competence and generation factuality (SVD)

Stack the factual scores into $F$ (evaluators × instantiations), each entry the 1–10 rating used **directly**, no thresholding. Self-entries and the rare missing entries are set to the anchor value:

$$ F_{sj}=r_{s,j}\in\{1,\dots,10\}\qquad(\text{self-entries }=\theta^{*}=7). \tag{A5}$$

Centre each row (subtract the evaluator's mean, removing its leniency) and keep the leading triple:

$$ \tilde F = F-\bar r\,\mathbf 1^{\top}=U\Sigma V^{\top},\qquad \sigma_1,\quad u\equiv U_{\cdot 1},\quad v\equiv V_{\cdot 1}. \tag{A6}$$

The left singular vector is factual competence,

$$ f\equiv u,\qquad \text{signed so } \textstyle\sum_s f_s>0,\qquad f^{+}_s=\max(f_s,0), \tag{A7}$$

clamped at zero so an evaluator anti-correlated with the consensus carries no weight. Centering is essential: raw scores cluster at the anchor, so on the un-centred matrix the leading axis is the shared level and ranks the most lenient evaluators highest. Equivalently $u$ is the leading eigenvector of the row-centred inter-evaluator Gram $\tilde F\tilde F^{\top}$. Because every row of $\tilde F$ sums to zero, $v$ sums to zero and is oriented so that positive means factually stronger ($\operatorname{corr}(v,\ \text{column means of }\tilde F)>0$).

The **competence-weighted consensus rating** of instantiation $j$ reads $v$ back on the 1–10 scale,

$$ \hat r_j \;=\; C+\kappa\,v_j,\qquad C=\frac{\sum_s f^{+}_s\,\bar r_s}{\sum_s f^{+}_s},\quad \kappa=\sigma_1\,\frac{\sum_s f^{+}_s\,u_s}{\sum_s f^{+}_s}>0, \tag{A8}$$

the rank-one approximation of the competence-weighted mean rating (the two agree within 0.14 on the canonical run, $r = 1.00$). Averaging over a generator's own instantiations $J_g$ gives the key-free **generation-factuality** rating

$$ G^{F}_{g} \;=\; \frac1{|J_g|}\sum_{j\in J_g}\hat r_j, \tag{A9}$$

already on the 1–10 scale: clean instantiations sit at $v_j\approx0$, hence at $C\approx7$. Its interval resamples the generator's own $\hat r_j$ with the consensus $(C,\kappa,v)$ held fixed. The one assumption: the only thing the evaluators share is the truth — a same-vendor bloc with a common bias would add a spurious shared component, which is why competence is read off a vendor-diverse panel with the shared-bias check of §4.2.

<a id="tab-criterion-a"></a>

| Model | $E^{F}$ loading | $E^{F}$ anchored | 95% CI | $G^{F}$ | 95% CI |
|---|---:|---:|---|---:|---|
| gemini-3.1-pro | 0.61 | 8.24 | [7.33, 9.30] | 6.78 | [6.62, 6.89] |
| claude-opus-4.5 | 0.52 | 7.00 | [7.00, 7.00] | 7.00 | (anchor) |
| claude-opus-4.0 | 0.35 | 4.69 | [3.45, 6.04] | 6.93 | [6.89, 6.97] |
| claude-opus-4.1 | 0.35 | 4.65 | [3.56, 5.96] | 6.99 | [6.91, 7.07] |
| gemini-2.5-flash | 0.26 | 3.47 | [1.62, 5.05] | 6.49 | [6.27, 6.68] |
| claude-sonnet-4 | 0.18 | 2.37 | [1.53, 3.36] | 6.96 | [6.92, 7.00] |
| gpt-4.1-mini | 0.10 | 1.34† | — | 6.26 | [6.07, 6.43] |
| gpt-4.1-2025-04-14 | 0.06 | 0.79 | [0.39, 1.53] | 6.56 | [6.39, 6.69] |
| gpt-4o | 0.04 | 0.47 | [0.28, 0.70] | 5.33 | [5.12, 5.53] |
| gpt-4o-2024-08-06 | 0.03 | 0.35 | [0.18, 0.61] | 5.39 | [5.16, 5.62] |
| gpt-4.1-nano | 0.02 | 0.28† | — | 4.82 | [4.01, 5.38] |
| gpt-4o-mini | -0.00 | -0.00† | — | 4.14 | [3.60, 4.69] |

Table: Evaluator factual competence $E^{F}$ (left singular vector; "anchored" $= 7f/f_a$) and generator factuality $G^{F}$ (right vector, per generator), twelve-evaluator basis, three runs pooled (805 items). † loading interval includes zero; no interval printed.

## A.3 Rating consistency

For evaluator $s$ and axis $x$, let $v_{s,x}(\theta)$ be $s$'s axis-$x$ scores across that axis's units at anchor $\theta$, leave-self-out (50 units for the four per-archetype axes, 250 for factual, 10 for structural diversity; 55 / 275 / 11 for the anchor, whose own portfolio is not among the graded eleven). The per-axis consistency is the mean Pearson correlation over the anchor pairs on which both vectors are non-constant,

$$ r_{s,x}=\frac{1}{|\mathcal P_{s,x}|}\sum_{(\theta,\theta')\in\mathcal P_{s,x}}\operatorname{corr}\!\big(v_{s,x}(\theta),v_{s,x}(\theta')\big). \tag{A10}$$

The **collapsed** score that gates the council averages the four per-archetype non-factual axes into one value per (submission, archetype) before correlating,

$$ \bar r_s=\frac{1}{|\mathcal P_{s}|}\sum_{(\theta,\theta')\in\mathcal P_{s}}\operatorname{corr}\!\big(v_{s}(\theta),v_{s}(\theta')\big), \tag{A11}$$

so axis-idiosyncratic noise partially cancels (gemini-2.5-flash: row mean of Table \ref{tab-criterion-b} ≈ 0.70, collapsed 0.81). Factual is A.2's job and is excluded; structural diversity, one score per portfolio, is too coarse and is excluded too. Design counts are met for eight of twelve evaluators; a missing grading call costs units, not correctness (dropped pairwise).

<a id="tab-criterion-b"></a>

| Evaluator | factual | beauty | intelligence | distinctness | length | struct |
|---|---:|---:|---:|---:|---:|---:|
| gemini-3.1-pro | 0.88 | 0.83 | 0.90 | 0.87 | 0.90 | 0.89 |
| claude-opus-4.5 | 0.90 | 0.86 | 0.85 | 0.84 | 0.91 | 0.85 |
| claude-opus-4.1 | 0.83 | 0.84 | 0.85 | 0.72 | 0.84 | 0.92 |
| claude-opus-4.0 | 0.78 | 0.83 | 0.84 | 0.69 | 0.83 | 0.86 |
| gpt-4.1-mini | 0.87 | 0.77 | 0.75 | 0.76 | 0.84 | 0.81 |
| claude-sonnet-4 | 0.70 | 0.75 | 0.77 | 0.75 | 0.78 | 0.81 |
| gpt-4.1-2025-04-14 | 0.24 | 0.64 | 0.73 | 0.74 | 0.82 | 0.84 |
| gemini-2.5-flash | 0.31 | 0.77 | 0.66 | 0.50 | 0.82 | 0.85 |
| gpt-4.1-nano | 0.65 | 0.63 | 0.64 | 0.44 | 0.37 | 0.36 |
| gpt-4o-2024-08-06 | 0.59 | 0.58 | 0.55 | 0.38 | 0.53 | 0.69 |
| gpt-4o | 0.13 | 0.32 | 0.24 | 0.12 | 0.40 | 0.34 |
| gpt-4o-mini | n/a | 0.25 | 0.36 | 0.27 | 0.10 | 0.23 |

Table: Anchor-sweep consistency per evaluator and axis (A10): mean pairwise Pearson correlation of scores across anchor values 5/6/7/8. It measures self-consistency, not accuracy; the factual column is distinct from the factual-competence loading. gpt-4o-mini's factual entry is undefined (near-zero variance). The initial council's collapsed values $\bar r$ (A11) with 95% CIs: gemini-3.1-pro 0.94 [0.92, 0.96], claude-opus-4.5 0.93 [0.89, 0.96], gemini-2.5-flash 0.81 [0.75, 0.86], claude-opus-4.0 0.85 [0.80, 0.89], claude-opus-4.1 0.87 [0.82, 0.91]; their factual loadings with CIs: 0.58 [0.56, 0.60], 0.55 [0.54, 0.58], 0.37 [0.31, 0.40], 0.35 [0.32, 0.35], 0.28 [0.27, 0.30].

## A.4 The council and the total

The sweep keeps the anchor interior to the 1–10 scale. At its ends, 5 and 8, the room on one side of the anchor shrinks, so part of the residual disagreement between anchor values is compression of the scale rather than reordering; the consistency values are conservative to that extent.

A model is **reliable** when its competence sits clear of the inert band — its 95% bootstrap interval on $f$ separates it from the near-zero cluster — and $\bar r_s\ge0.78$. Eight of twelve clear the consistency gate; five clear both, and that conjunction seats the council. Each evaluator index is rescaled so the anchor scores 7,

$$ E^{F}_s=7\,\frac{f_s}{f_a},\qquad E^{C}_s=7\,\frac{\bar r_s}{\bar r_a}, \tag{A12}$$

so the singular vector's arbitrary scale cancels. Generation splits the same way: $G^{F}$ (A9) and the criterion quality $G^{C}$, the council's mean over the five non-factual axes, **reliability-weighted** — each judge's vote on axis $x$ weighted by its own $r_{t,x}$:

$$ G^{C}_s=\frac{1}{|\mathcal{X}_{5}|}\sum_{x\in\mathcal{X}_{5}}\frac{\sum_{t\in\mathcal{C}\setminus\{s\}}\max(r_{t,x},0)\,\bar r_{t,s,x}}{\sum_{t\in\mathcal{C}\setminus\{s\}}\max(r_{t,x},0)}, \tag{A12b}$$

with $\bar r_{t,s,x}$ judge $t$'s mean score of $s$ on axis $x$ at the production anchor. Then

$$ G_s=\tfrac12\big(G^{F}_s+G^{C}_s\big),\qquad E_s=\tfrac12\big(E^{F}_s+E^{C}_s\big), \tag{A13}$$

$$ T_s=\tfrac12\big(G_s+E_s\big)=\tfrac14\big(G^{F}_s+G^{C}_s+E^{F}_s+E^{C}_s\big). \tag{A14}$$

**Intervals.** Every rating carries a 95% percentile bootstrap ($10^3$–$10^4$ replicates). Units: $G$ — the per-(run, submission, archetype) units; $f$ — the 805 parallel contexts of the pooled matrix, each replicate's top-2 left subspace Procrustes-aligned to the full sample before the leading loading is read (the leading axis is near-degenerate between the Anthropic and Google blocs); $\bar r$ — the 55 (submission, archetype) atoms of run 1's anchor sweep. $E$ and $T$ are **not** combined analytically: they are bootstrapped jointly on the 165-atom (run, submission, archetype) grid, the run-1 atoms of each draw feeding $\bar r$, leave-self-out applied after the resample, every component including $f_a,\bar r_a$ recomputed on each replicate. Because a regenerated portfolio moves all of its atoms together, the interval contains run-to-run dispersion as well as item dispersion: pooling three runs did not narrow the intervals of run 1 (mean width ratio 1.06), and the two-run pool sits at 1.01 (Appendix F). The council is held at its selected membership rather than re-selected inside each replicate (the gate is itself defined by a bootstrap interval), so the interval is conditional on that selection.

## A.5 Per-criterion generator quality versus evaluator consistency

For each non-factual criterion $x$, $G_{s,x}$ is the reliability-weighted council estimator (A12b) on that axis and $E_{s,x}=7\,r_{s,x}/r_{a,x}$; both anchored to 7. Their agreement is the **anchored cosine**,

$$ \mathrm{cos}(G,E)_x=\frac{\sum_{s}(G_{s,x}-7)\,(E_{s,x}-7)}{\sqrt{\sum_{s}(G_{s,x}-7)^2}\;\sqrt{\sum_{s}(E_{s,x}-7)^2}}, \tag{A15}$$

centred on the anchor point rather than each vector's mean so values are comparable across axes. It is a diagnostic and feeds nothing in $T$.

<a id="tab-per-criterion"></a>

| Model | beauty $G$ | beauty $E$ | intel $G$ | intel $E$ | dist $G$ | dist $E$ | len $G$ | len $E$ | struct $G$ | struct $E$ |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| ★ claude-opus-4.5 | 7.0 | 7.0 | 7.0 | 7.0 | 7.0 | 7.0 | 7.0 | 7.0 | 7.0 | 7.0 |
| claude-opus-4.1 | 7.1 | 6.8 | 7.2 | 7.0 | 7.4 | 6.0 | 6.7 | 6.5 | 7.3 | 7.6 |
| claude-opus-4.0 | 6.9 | 6.7 | 6.9 | 7.0 | 7.0 | 5.7 | 6.8 | 6.3 | 7.3 | 7.1 |
| claude-sonnet-4 | 6.3 | 6.1 | 6.3 | 6.4 | 6.5 | 6.2 | 6.1 | 6.0 | 6.4 | 6.7 |
| gemini-3.1-pro | 5.8 | 6.8 | 5.7 | 7.4 | 6.0 | 7.3 | 5.5 | 6.9 | 5.7 | 7.4 |
| gemini-2.5-flash | 5.4 | 6.2 | 5.5 | 5.5 | 6.2 | 4.2 | 5.7 | 6.3 | 5.8 | 7.0 |
| gpt-4.1-mini | 4.8 | 6.3 | 5.0 | 6.2 | 5.9 | 6.3 | 4.2 | 6.5 | 5.4 | 6.7 |
| gpt-4.1-2025-04-14 | 5.1 | 5.2 | 5.0 | 6.0 | 6.0 | 6.2 | 3.6 | 6.3 | 5.6 | 7.0 |
| gpt-4.1-nano | 3.5 | 5.1 | 3.7 | 5.3 | 4.2 | 3.7 | 3.5 | 2.8 | 3.2 | 2.9 |
| gpt-4o-2024-08-06 | 3.5 | 4.7 | 3.3 | 4.5 | 4.1 | 3.1 | 3.3 | 4.0 | 3.0 | 5.7 |
| gpt-4o | 3.4 | 2.6 | 3.4 | 2.0 | 4.7 | 1.0 | 2.6 | 3.1 | 3.2 | 2.8 |
| gpt-4o-mini | 3.5 | 2.1 | 3.5 | 3.0 | 3.3 | 2.3 | 3.8 | 0.8 | 3.0 | 1.9 |
| **cos(G,E)** | **0.91** | [.83,.95] | **0.90** | [.80,.93] | **0.89** | [.82,.92] | **0.84** | [.80,.87] | **0.87** | [.86,.87] |

Table: Per-criterion generator quality $G$ versus evaluator consistency $E$, both anchored to claude-opus-4.5 (★) = 7; last row the anchored cosine with its joint-bootstrap 95% CI.

## A.6 The contest, the ballast, and the guards

The official leaderboard is issued on the **contest** basis: a contest for model $c$ convenes the five council seats and $c$ itself as evaluators over the incumbents' portfolios, the two ballast blocks and $c$'s own — every estimator above unchanged, leave-self-out throughout, the anchor's $f_a,\bar r_a$ the contest's own. Two **guards** decide whether the contest's factual axis is identified: $\sigma_1/\sigma_2\in[2.0,5.0]$ and a spread of the seats' anchored $E^{F}$ above 2.5 points; if either fails, no seat changes hands and the contest's totals carry the caveat. The upper bound marks the range within which the sizing below was validated, not a failure in itself.

A contest convenes the top of the field, and with the weak submissions gone the factual axis breaks: the seats' anchored $E^{F}$ come out wrong in scale and in order, swinging by up to 8.8 points with the contestant. The **ballast** — the weakest archived submissions, added to every contest's graded set and held fixed through anchor replacements and council rotations — repairs this; two suffice.

<a id="tab-ballast"></a>

| Seat | council alone | +1 ballast | +2 ballast | +3 ballast | all 12 |
|---|---:|---:|---:|---:|---:|
| gemini-3.1-pro | 7.19 | 6.94 | 7.84 | 8.13 | 8.24 |
| ★ claude-opus-4.5 | 7.00 | 7.00 | 7.00 | 7.00 | 7.00 |
| claude-opus-4.0 | 6.98 | 3.58 | 3.66 | 4.14 | 4.69 |
| claude-opus-4.1 | 7.42 | 4.26 | 3.79 | 4.20 | 4.65 |
| gemini-2.5-flash | 1.41 | 2.75 | 4.18 | 3.95 | 3.47 |

Table: Each seat's anchored $E^{F}$ by contest composition — 0–3 ballast blocks (mean over the seven possible contestants) beside the twelve-participant reference, three runs pooled. Council alone, the column is scrambled; from two ballast on, the contest reproduces the reference (mean $|\Delta|$ 0.60 over the seven contests at two blocks, 0.37 at three; the same seat lowest in six of the seven). Two blocks is the protocol's configuration.

Why two and not one: with a single block the axis narrows toward *did this judge notice the one bad portfolio*, and the guards fail in 6% of bootstrap resamples; two blocks carry two independent error patterns, the guards hold in every resample, $\sigma_1/\sigma_2 = 2.87$ [2.50, 3.03] on the pooled corpus with both interval ends inside the band; a third tightens the seats' fidelity further (0.37) at twenty-five more columns of grading per run, and the protocol keeps two. Taken apart, the runs behave differently: the sizing holds on run 1 (two-ballast separation 2.99 [2.71, 3.48], guards holding in every resample), is marginal on run 2 (2.01 [1.87, 2.40], holding in 65% of resamples), and fails on run 3 at every ballast size (1.53 [1.31, 1.73], holding in none): no column set can single out an axis the judges did not share. Against a per-evaluator permutation null (each evaluator's ratings shuffled across the columns), $\sigma_1$ stands 1.48× above the 95th-percentile noise edge on the pooled corpus, where the second pattern lies within noise; on run 3 alone it stands 1.29× above the edge and the second pattern also exceeds it, while the leading direction is stable under the column bootstrap (`scripts/spectral_gap_checks.py`): run 3 has a shared factual axis, but not a single one, and pooling it with two clean runs restores one.

## A.7 Authority versus consistency on the subjective axes

Computed on run 1 alone. Peer centrality can be run on the subjective axes too: one SVD per non-factual axis yields an **authority** rating — each judge's alignment with the participants' collective taste. On the five subjective axes authority and consistency correlate at Pearson 0.70–0.90; on factual — the one axis with a truth to be right about — they diverge (0.50, CI [−0.08, 0.84]), because only there can a judge be stable yet wrong. Consistency credits a judge's whole stable standard, personal taste included, penalising only flimsiness; authority credits the collective share alone, so stable-but-partly-private judges drop under authority (Spearman between the twelve orderings 0.83). Council membership is invariant to the choice: the top five by either estimator are the five seats. Substituting authority for consistency in the total preserves the ordering (Spearman 0.986) with one headline change: authority is not bounded by the anchor's own loading, so gemini-3.1-pro's total (7.86) overtakes the pinned 7. The official rating uses consistency; adopting authority inside $T$ would convert alignment into authority on axes where no truth licenses the conversion (§6).

**Limits of a consensus-defined competence** (run 1). Because $E^{F}$ is read off agreement, a judge that departs from the panel is scored down whether it is wrong or right. A synthetic evaluator built to reproduce the panel's competence-weighted consensus exactly reads $E^{F} = 5.15$; inverting its verdict on 5% of the items drops it to 4.84, on 20% to 3.79 (`scripts/consensus_limits.py`). Substituting authority for consistency in the total preserves the ordering (Spearman 0.986) save Gemini 3.1 Pro overtaking the anchor (7.86).

## A.8 The two estimators compared

<a id="tab-estimators"></a>

| | Peer centrality (graded SVD) | Rating consistency (anchor sweep) |
|---|---|---|
| Character | *collective*: each judge weighted by the other judges' agreement with it | *individual*: each judge measured only against itself across the sweep |
| Licensing assumption | the only thing competent judges share is the truth | a stable standard is the only competence a subjective axis can show |
| Use for | fact-checking — replaces the golden key ($E^{F}$, $G^{F}$) | axes with no right or wrong ($E^{C}$; the per-axis weights in $G^{C}$) |
| Blind spot | a misunderstanding *shared* by the judges reads as truth (§6) | a *private* misconception, held consistently, passes as a standard |
| Why it stops there | agreement on taste would convert alignment into authority (A.7) | consistency cannot certify truth: a consistent judge can be consistently *wrong* |

Table: The two estimators and their division of labour (source §4.2).
