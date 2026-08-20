# Appendix D. Auditing the Metanym Game–GPQA correlation: No Leaks Found

The total rating $T$ tracks self-administered GPQA Diamond at Pearson $r = 0.97$ — closer
than any of its components, the factual pair $\tfrac12(E^{F}+G^{F})$ included (the ladder below). A correlation that strong between a key-free peer rating and an externally keyed
benchmark invites the suspicion that something leaked. This appendix records the audit that
looked for the leak and did not find one, the administration detail the audit surfaced and
the paper must disclose, the decompositions that make the number unremarkable in hindsight,
and the artifacts shipped so that anyone can repeat the search. Statistics are reported at
the caution $n = 12$ demands: intervals are Fisher-$z$ unless marked, and differences
between the strong correlations below are point-estimate observations — none of them is
individually resolved at this sample size.

## D.1 The correlation, decomposed

**The aggregation ladder is monotone.** Council-basis official values vs GPQA, $n = 12$
throughout (Pearson $r$ measures agreement of the values on a line; Spearman $\rho$,
agreement of the rankings alone):

| Quantity | Pearson $r$ | Spearman $\rho$ | Fisher-$z$ 95% | BCa bootstrap 95% |
|---|---:|---:|---|---|
| $E^{C}$ alone | 0.81 | 0.82 | [0.45, 0.95] | [0.43, 0.94] |
| $G^{F}$ alone | 0.83 | 0.86 | [0.48, 0.95] | [0.66, 0.94] |
| $E^{F}$ alone | 0.83 | 0.88 | [0.49, 0.95] | [0.68, 0.93] |
| $G^{C}$ alone | 0.92 | 0.88 | [0.73, 0.98] | [0.51, 0.98] |
| $G = \tfrac12(G^{F}+G^{C})$ — generation half | 0.91 | 0.86 | [0.70, 0.97] | [0.73, 0.97] |
| $E = \tfrac12(E^{F}+E^{C})$ — evaluation half | 0.92 | 0.93 | [0.73, 0.98] | [0.78, 0.98] |
| $\tfrac12(E^{F}+G^{F})$ — §4.7's factual pair | 0.92 | 0.92 | [0.73, 0.98] | [0.84, 0.97] |
| $T = \tfrac14(G^{F}+G^{C}+E^{F}+E^{C})$ | **0.97** | **0.93** | **[0.90, 0.99]** | **[0.92, 0.99]** |

Two interval constructions are reported because each covers the other's weakness at
$n = 12$: Fisher-$z$ assumes bivariate normality but unbends the skew of a bounded
statistic; the BCa bootstrap is assumption-lighter and corrects the bias and skew that
make the naive percentile bootstrap anti-conservative here (the earlier percentile
interval on $T$, $[0.94, 0.99]$, was too narrow for exactly that reason and is retired).
Where the two constructions disagree ($G^{C}$: Fisher $[0.73, 0.98]$ vs BCa
$[0.51, 0.98]$), the BCa is detecting leverage sensitivity and the wider bound is the
honest one. Read as validation: every component's interval sits well clear of zero —
GPQA corroborates $T$ and, with varying strength, each of its components as capability
measures — with $T$'s interval the tightest under both constructions.

**Measurement error, propagated (sensitivity).** All correlations above are computed on
point estimates. Both coordinates carry known measurement distributions — each model's $T$
has its A.5 replicate distribution (shipped in `total_rating_council_replicates.csv`), and
GPQA accuracy is binomial — so the fit can be re-derived with them propagated
(`scripts/slope_full_bootstrap.py`; slope point estimate 8.0 GPQA points per $T$ unit):

| Uncertainty propagated | slope 95% | $r$ 95% |
|---|---|---|
| sampling of models only (pairs bootstrap) | [7.1, 9.4] | [0.94, 0.99] |
| measurement only (coordinate draws, models fixed) | [6.5, 9.2] | [0.88, 0.98] |
| both simultaneously | [6.1, 9.8] | [0.83, 0.98] |

The last row modestly overstates total uncertainty — the observed scatter already contains
one realization of each point's measurement noise, and jittering observed values adds a
second — so it is a conservative bound, under which the correlation still does not fall
below 0.83. Two notes keep every approximation's direction honest: the figure retains the
classical confidence band by convention (per-point uncertainties are drawn as bars, not
folded into the band); and measurement error in the $x$ coordinate *attenuates* a
correlation rather than inflating it, so the point estimates above are themselves
conservative — the classical disattenuation correction (reliabilities $\approx 0.98$ for
$T$ and $\approx 0.94$ for GPQA, from the shipped intervals) places the latent-quantity
correlation at the measurement ceiling, reported here as context, not as a claim.

**Why the single quarters order the way they do.** GPQA is an answering test — capability
expressed in graded performance — so a quantity couples to it in proportion to two things:
how much *performance content* it carries, and how much *discriminating range* it retains
across the roster.

- $G^{C}$ (0.92) has both. Producing a portfolio the council rates beautiful and
  structurally intelligent requires marshalling knowledge, invention, and control at once —
  output quality is a high-bandwidth readout of capability — and the subjective axes keep
  discriminating across the whole roster (council-basis spread 3.4–7.2).
- $G^{F}$ (0.83) has the content but loses the range twice. It **ceilings at the top**: the
  leading eight compress into 6.15–7.00 — frontier models rarely write false sentences into
  templates they chose themselves — while GPQA still spreads those eight across 19 points.
  And it **offers a refuge at the bottom**: factual cleanliness is achievable through
  conservatism — the GPT-4o family holds $G^{F} \approx 5.0$ on safe, simple, true
  portfolios while GPQA reads 46–48% and $G^{C}$ reads 3.4. Truth rewards playing safe;
  beauty punishes it.
- $E^{F}$ (0.83) is judging in form but answering in content: detecting a false claim
  requires the same knowledge GPQA tests, which is why it ties $G^{F}$ rather than sinking
  to $E^{C}$'s level.
- $E^{C}$ (0.81) is a disposition, not a performance: holding a firm rating standard
  requires enough competence to have a standard, then saturates — a mid-capability model
  can hold one in full measure (gpt-4.1-mini's $E^{C}$ of 6.97 sits above every Opus but
  the anchor), which is precisely the pairs on which GPQA disagrees.

**The subjective quarters, by estimator.** The making-vs-judging asymmetry above is not an
estimator artifact. $G^{C}$'s 0.92 is carried by the ratings' content (the A12b reliability
weights only set each judge's influence, and the council's weights are near-uniform);
judging couples weakly to GPQA under *either* available estimator:

| Subjective quarter | Estimator | $r$ | $\rho$ |
|---|---|---:|---:|
| $G^{C}$ (official) | reliability-weighted council mean of the model's *output* quality | 0.92 | 0.88 |
| $E^{C}$ (official) | anchor-sweep consistency of the model's own *judging* | 0.81 | 0.82 |
| $E^{C}_{\text{svd}}$ (declined; §4.4) | alignment with the participants' collective taste (twelve-evaluator basis) | 0.80 | 0.76 |

The two $E$-side estimators are statistically indistinguishable as GPQA predictors; the
weak coupling belongs to the quantity, not the choice between them. This is the paper's
central dissociation replicated on a third instrument: making tracks answering; judging is
its own trait, and no keyed answering benchmark measures it. Had $E$-side quantities
tracked GPQA at 0.95, the evaluation half of $T$ would be redundant with existing benchmarks.

**Why $T$ beats every part: diversity, not construct-matching.** If construct-matching
governed, the generation half would lead; it does not ($G$ 0.91 vs $E$ 0.92). The compounds are
governed by error-diversity: the four quarters are four *differently distorted* reads of
capability — one ceilinged, one refuge-prone, one knowledge-loaded, one saturating — with
substantially independent distortions, so equal-weight averaging cancels them
(Spearman–Brown). The leave-one-out pattern confirms it: dropping even the weakest quarter
lowers the aggregate ($\tfrac13(G^{F}+G^{C}+E^{F})$ reads 0.95 against $T$'s 0.97), and no
sub-combination we examined beats the full average ($\tfrac12(G^{C}+E^{F})$, the
best-single-quarters pairing, reads 0.93). $T$ is also the only compound with a
pre-registered justification — it is the benchmark's official total, defined before any
GPQA comparison — whereas any other weighting chosen for its GPQA agreement at $n = 12$
would be curve-fitting. These comparisons are point estimates; their differences are not
individually resolvable at this $n$.

**The regimes invert — and $T$ is the only regime-invariant indicator.** Restricting to the
leading eight (the roster above the GPT-4o-family cliff) reverses the single-quarter
ordering:

| Quantity | Full roster ($n=12$) | Leading eight ($n=8$) |
|---|---:|---:|
| $G^{F}$ | 0.83 | 0.60 |
| $G^{C}$ | **0.92** | 0.66 |
| $E^{F}$ | 0.83 | **0.84** |
| $E^{C}$ | 0.81 | 0.37 |
| $\tfrac12(E^{F}+G^{F})$ | 0.92 | 0.88 |
| $\tfrac12(G^{C}+E^{F})$ | 0.93 | 0.91 |
| $T$ | **0.97** | **0.91** |

The mechanism is the same law with the *range* term changing owners. Across the full
roster, the capability cliff gives the subjective making axis its discriminating range, so
$G^{C}$ carries the agreement. Among the elite, every model is a competent maker — making
quality decouples from knowledge (gemini-3.1-pro tops GPQA yet is a middling maker, so
$G^{C}$ falls to 0.66) — and what still separates frontier models is knowledge, which is
$E^{F}$'s content: detecting errors in others' work stays hard after producing clean work
has become easy, so $E^{F}$ keeps its spread (7.27 down to 0.00 across the eight) exactly
where $G^{F}$ compresses into 6.15–7.00. $E^{C}$, a pure disposition, saturates among the
competent and collapses to 0.37. Among frontier models, the best key-free predictor of a
keyed knowledge benchmark is how well a model judges *other models'* truth — §5.4's
dissociation thesis in empirical form. $T$ leads or ties in both regimes because the
equal-weight aggregate always contains whichever quarter is currently doing the
discriminating; any single quarter is the best proxy only in the population where its
range lives. (Leading-eight values are point estimates on eight points.)

**It is not the cluster gap — but fine ordering is beyond it.** Within the leading eight
alone, $T$ vs GPQA reads $r = 0.91$ ($\rho = 0.79$), so the correlation is not carried by
the division between the leading eight and the GPT-4o-family cliff. The honest boundary:
within the Anthropic family alone ($n = 4$) the rank agreement is $\rho = 0.40$ — where
ordering is genuinely unresolved by the
evaluators (§4.2), the agreement with GPQA dissolves
too. The two instruments agree on coarse capability structure, not on fine ranks; the
trailing four alone ($r = 0.71$, $n = 4$) are too few to inform either way. This is
consistent with §4.9's position that the benchmark's reliable products are membership and
rank order, not fine placement.

**It survives the basis change that makes the benchmark scalable.** Recomputing every
quantity on the twelve-evaluator bootstrap basis instead of the official council+ballast
contests moves $T$'s correlation from 0.972 to 0.969 and leaves $G^{F}$, $G^{C}$, $E^{F}$
and the factual pair within 0.02 of themselves. The one real difference is $E^{C}$: 0.81
on the contest basis against 0.89 on the twelve-evaluator basis — the contest's easier
consistency test (§4.7's scope note) inflates inert-band judges in a way an external
capability instrument can see. $T$ absorbs the distortion (a quarter of four), so the
switch to the standing-service basis costs the headline nothing.

**It survives regeneration — with one flagged run.** Across the three full re-runs of
§4.9: $r = 0.97, 0.97, 0.92$ ($\rho = 0.93, 0.95, 0.88$). The dip is run 3, whose factual
axis the §4.6 diagnostic reports as unidentified ($\sigma_1/\sigma_2 = 1.28$); $T$'s three
healthy quarters buffer the broken one (the factual pair alone falls to 0.83 there).
Excluding the anchor changes nothing ($r = 0.97, 0.97, 0.91$; run 1 anchor-excluded 0.971).

**What it does and does not corroborate.** $T$ and GPQA are both broad capability
measures, so their agreement corroborates the benchmark as a whole — its one number tracks
real capability. It is distinct from, and does not strengthen, an axis-specific claim: with
$G^{C}$ alone at 0.92, GPQA concordance cannot by itself certify that the factual axis
recovered *truth* rather than capability-correlated quality.

## D.2 The administration, disclosed

GPQA Diamond (198 questions) was administered 2026-06-13 — two weeks *after* the council
generation run (2026-05-29), so no direction exists for the benchmark's content to have
been shaped by GPQA. All twelve models were queried through the same gateway and protocol
as the council run (Temperature 0, no dedicated reasoning channel, no tools), with the
question and four shuffled options only — no key ever enters a prompt:

```
Answer the following multiple choice question. The last line of your reply
must be exactly 'Answer: $LETTER' where $LETTER is one of A, B, C, D.

{question}

A) {A}
B) {B}
C) {C}
D) {D}
```

Option order is shuffled deterministically per question (seeded by question index, one
shuffle applied identically for every model).

**The administration was two-stage, and the first stage is in the shipped log.** "No
dedicated reasoning channel" is not deliberation-off: models write visible derivations of
vendor-idiosyncratic length before the answer line, and under the initial 2,048-token cap
the two Gemini seats were massively truncated — the original pass (preserved in the run's
`log.txt`) scored gemini-3.1-pro at 82/198 with 103 unparseable responses and
gemini-2.5-flash at 121/198 with 50, truncation voids counted as wrong. The cap was raised
to 8,192 and the void responses — only the void ones — were re-asked; the published
records are the patched set (13 residual voids per Gemini seat, still counted as wrong).
Two facts bound the bias this asymmetric repair could introduce: retries targeted only
*unparseable* responses, never parsed-but-wrong answers; and the retry success rate
(≈87% correct) matches the original pass's scored-only accuracy (gemini-3.1-pro 86.3% on
its 95 parseable responses — *above* the published 80.81%), so the second pass did not
score better than the first pass's readable fraction. The single-pass description of §3.1
therefore holds for the council run but not for the GPQA administration, which was
single-pass-with-void-retry; both stages' evidence ships in `data/gpqa_runs/`.

## D.3 The audit: no leak found

`scripts/gpqa_audit.py` re-derives the published table from the raw records and hard-fails
on any mismatch. Its checks, all passing:

1. **CSV reconciliation** — per-model `n_correct` recomputed from raw equals
   `gpqa_selfadministered.csv` exactly, all twelve models.
2. **Key consistency** — the key letter is identical across all twelve models' records for
   every question.
3. **Key balance** — shuffled key distribution A/B/C/D = 48/51/47/52, chi-square vs
   uniform $p = 0.95$.
4. **Independent re-extraction** — a second answer-extractor, written without sight of the
   first, agrees with the stored verdicts on every response for ten of twelve models; the
   Gemini disagreements are almost entirely the independent extractor failing on the LaTeX
   `\boxed{X}` answer style. The genuinely questionable credits — granted with no terminal
   answer statement, the letter recovered from a truncated derivation — number 2
   (gemini-2.5-flash) and 6 (gemini-3.1-pro) of 198.
5. **Strict-terminal sensitivity** — rescoring with only explicit terminal answer
   statements counted moves three models: gemini-2.5-flash 72.22 → 70.71, gemini-3.1-pro
   80.81 → 77.27, and gpt-4.1-mini 63.13 → 60.10. The $T$–GPQA correlation moves from
   0.972 to 0.966. Scored the opposite way — voids excluded rather than counted wrong —
   it reads 0.967. The headline survives both directions of the scoring convention.

**What the audit cannot rule out.** It certifies the path from raw records to published
numbers; it cannot re-run the models. Two residual channels remain. Both instruments share
the gateway, so capability-correlated properties of that path (truncation behaviour,
context handling) touch both; the gateway's `thinkingBudget: 0` for the Gemini seats is
passed but not verified by assertion. And GPQA is public: *uniform* training contamination
would inflate accuracies without inflating a correlation against freshly generated items,
but *differential* contamination — exposure increasing with training recency and scale,
which correlate with capability — would inflate the slope itself. That channel cannot be
excluded with the shipped data and is the specific residual threat.

## D.4 Publicly reported GPQA values, and why they differ

Public GPQA Diamond figures for the frontier seats are substantially higher than this
protocol's — and are themselves inconsistent across sources: for claude-opus-4.5 the
November 2025 system card reports 87.0 while a 2026 leaderboard snapshot lists 94.1
(thinking configuration unconfirmed); for gemini-3.1-pro public sources report 94.3 against
this protocol's 80.81. The gap has a protocol explanation — public evaluations run with
reasoning enabled, large budgets, and heterogeneous answer extraction (public GPT-4o
figures move from ${\sim}46$ to ${\sim}54$ with the extraction method alone), while this
administration is deliberately reasoning-channel-off, T=0, harness-matched — but the
per-model public record is too poorly sourced to reconcile cell by cell: of the twelve
models, only six have citable public values (`data/external_benchmarks.csv` records the
sourcing state). On those six, public vs self-administered agreement is $r = 0.86$
($\rho = 0.81$, $n = 6$) — real but visibly weaker than any correlation in D.1, which is
the expected signature of two administrations under different protocols. [The two administrations are plotted against each other below](#fig-gpqa-two-admins): the relation is smooth and monotone with the reasoning-budget offset above the diagonal — corroboration that the self-administered numbers measure the same capability under a leaner protocol.

<a id="fig-gpqa-two-admins"></a>

![Two administrations of the same test: publicly reported GPQA Diamond (typically reasoning-on) against this protocol's self-administered accuracy (T=0, reasoning off), for the six models with a citable public value. Pearson $r = 0.86$, Spearman $\rho = 0.81$. The offset above the diagonal is the reasoning budget. Produced by `scripts/plot_gpqa_public_vs_measured.py`.](../reproduce/figures/gpqa_public_vs_measured.png)

## D.5 Artifacts

| Artifact | Path |
|---|---|
| Raw per-question responses, all models, both stages' outcome + first-pass log | `reproduce/data/gpqa_runs/` |
| Published accuracy table | `reproduce/data/gpqa_selfadministered.csv` |
| Scoring audit (hard-fail checks) | `reproduce/scripts/gpqa_audit.py` |
| Official council-basis totals + CIs | `reproduce/data/total_rating_council.csv` |
| The §4.8 figure | `reproduce/scripts/plot_total_validation.py` |
| Every D.1 number (ladder, compounds, regimes, bases, per-run) | `reproduce/scripts/t_gpqa_ladder.py` |
| Bootstrap-basis components; per-run council-basis totals; the declined $E^{C}_{\text{svd}}$ | `reproduce/data/total_rating_twelve.csv`, `total_rating_runs.csv`, `ec_svd_twelve.csv` |
| Public-value sourcing state | `reproduce/data/external_benchmarks.csv` |

Every number in this appendix recomputes from the shipped data: `scripts/gpqa_audit.py`
(six hard-fail checks, including the first-pass log reconciliation) and
`scripts/t_gpqa_ladder.py` (all of D.1, with headline assertions).
