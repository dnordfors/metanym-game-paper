# D. Auditing the metanym–GPQA correlation

## D.1 The correlation, decomposed

**The aggregation ladder is monotone.** Council-basis official values against GPQA, three runs pooled, $n = 12$ throughout:

| Quantity | Pearson $r$ | Spearman $\rho$ | Fisher-$z$ 95% | BCa bootstrap 95% |
|---|---:|---:|---|---|
| $E^{C}$ alone | 0.81 | 0.82 | [0.45, 0.95] | [0.42, 0.94] |
| $G^{F}$ alone | 0.89 | 0.84 | [0.64, 0.97] | [0.72, 0.95] |
| $E^{F}$ alone | 0.87 | 0.97 | [0.60, 0.96] | [0.76, 0.93] |
| $G^{C}$ alone | 0.95 | 0.84 | [0.82, 0.99] | [0.82, 0.98] |
| $G = \tfrac12(G^{F}+G^{C})$ — generation half | 0.94 | 0.87 | [0.81, 0.98] | [0.84, 0.98] |
| $E = \tfrac12(E^{F}+E^{C})$ — evaluation half | 0.94 | 0.95 | [0.80, 0.98] | [0.83, 0.98] |
| $\tfrac12(E^{F}+G^{F})$ — the factual pair | 0.94 | 0.96 | [0.80, 0.98] | [0.89, 0.97] |
| $T = \tfrac14(G^{F}+G^{C}+E^{F}+E^{C})$ | **0.98** | **0.96** | **[0.93, 1.00]** | **[0.95, 0.99]** |

Table: The aggregation ladder. Two interval constructions are reported because each covers the other's weakness at $n = 12$: Fisher-$z$ assumes bivariate normality but unbends the skew of a bounded statistic; the BCa bootstrap is assumption-lighter and corrects the bias that makes the naive percentile bootstrap anti-conservative here. Where they disagree, the wider bound is the honest one.

Every component's interval sits well clear of zero — GPQA corroborates $T$ and, with varying strength, each component — with $T$'s interval the tightest under both constructions. The four quarters are four *differently distorted* reads of capability: $G^{F}$ **ceilings at the top** (the leading eight compress into 6.23–7.00 while GPQA still spreads them across 19 points) and **offers a refuge at the bottom** (the GPT-4o family holds $G^{F}\approx5.2$ on safe, simple, true portfolios while GPQA reads 46–48% and $G^{C}$ reads 3.5 — truth rewards playing safe, beauty punishes it); $E^{F}$ is judging in form but answering in content; $E^{C}$ is a disposition that saturates once a model is competent enough to have a standard (gpt-4.1-mini's $E^{C}$ of 6.97 sits above every Opus but the anchor). Equal-weight averaging cancels substantially independent distortions (Spearman–Brown); dropping even the weakest quarter lowers the aggregate ($\tfrac13(G^{F}+G^{C}+E^{F})$ reads 0.97), and no sub-combination we examined beats the full average — the best two-quarter pairing, $\tfrac12(G^{C}+E^{F})$, reads 0.95. $T$ is also the only compound with a pre-registered justification: it is the benchmark's official total, defined before any GPQA comparison, whereas any other weighting chosen for its GPQA agreement at $n = 12$ would be curve-fitting.

**Measurement error, propagated.** Both coordinates carry known measurement distributions — each model's $T$ its replicate distribution, GPQA accuracy binomial — so the fit can be re-derived with them propagated (slope point estimate 8.4 GPQA points per unit of $T$):

| Uncertainty propagated | slope 95% | $r$ 95% |
|---|---|---|
| sampling of models only (pairs bootstrap) | [7.7, 9.7] | [0.96, 1.00] |
| measurement only (coordinate draws, models fixed) | [6.9, 9.7] | [0.90, 0.98] |
| both simultaneously | [6.6, 10.3] | [0.86, 0.98] |

Table: The $T$–GPQA fit with measurement uncertainty propagated. The last row is conservative (the observed scatter already contains one realisation of each point's noise); the correlation does not fall below 0.86. Measurement error in $x$ attenuates a correlation rather than inflating it, so the point estimates are themselves conservative.

**The regimes invert — $T$ is the only regime-invariant indicator.** Restricting to the leading eight reverses the single-quarter ordering:

| Quantity | Full roster ($n=12$) | Leading eight ($n=8$) |
|---|---:|---:|
| $G^{F}$ | 0.89 | 0.67 |
| $G^{C}$ | **0.95** | 0.81 |
| $E^{F}$ | 0.87 | **0.89** |
| $E^{C}$ | 0.81 | 0.37 |
| $\tfrac12(E^{F}+G^{F})$ | 0.94 | 0.92 |
| $\tfrac12(G^{C}+E^{F})$ | 0.95 | 0.94 |
| $T$ | **0.98** | **0.94** |

Table: Pearson $r$ against GPQA on the full roster and on the leading eight (point estimates on eight points).

Across the full roster the capability cliff gives the subjective making axis its discriminating range; among the elite every model is a competent maker (gemini-3.1-pro tops GPQA yet is a middling maker), and what still separates frontier models is knowledge, which is $E^{F}$'s content: detecting errors in others' work stays hard after producing clean work has become easy, so $E^{F}$ keeps its spread (7.78 down to 0.77 across the eight) exactly where $G^{F}$ compresses. Within the Anthropic family alone ($n = 4$) the rank agreement is $\rho = 0.80$ — where the evaluators leave the ordering unresolved, the agreement with GPQA coarsens too. Recomputing every quantity on the twelve-evaluator basis instead of the contest basis moves $T$'s correlation from 0.982 to 0.976; the one real difference is $E^{C}$ (0.81 contest vs 0.89 twelve-evaluator), the contest's easier consistency test inflating inert-band judges in a way an external instrument can see. Taken apart, the three runs read $r = 0.97, 0.97, 0.92$ ($\rho = 0.93, 0.95, 0.88$), the dip being run 3, whose factual axis is unidentified ($\sigma_1/\sigma_2 = 1.29$); pooled, 0.98 ($\rho = 0.96$); excluding the anchor changes nothing (0.97, 0.97, 0.91; pooled 0.98).

**What it does and does not corroborate.** $T$ and GPQA are both broad capability measures, so their agreement corroborates the benchmark as a whole. It does not by itself certify that the factual axis recovered *truth* rather than capability-correlated quality: with $G^{C}$ alone at 0.95, GPQA concordance is not an axis-specific claim.

## D.2 The administration, disclosed

GPQA Diamond (198 questions) was administered 2026-06-13 — two weeks *after* the generation run (2026-05-29), so no direction exists for the benchmark's content to have been shaped by GPQA. All twelve models were queried through the same gateway and protocol as the council run (Temperature 0, no dedicated reasoning channel, no tools), with the question and four shuffled options only — no key ever enters a prompt:

```
Answer the following multiple choice question. The last line of your reply
must be exactly 'Answer: $LETTER' where $LETTER is one of A, B, C, D.

{question}

A) {A}
B) {B}
C) {C}
D) {D}
```

Option order is shuffled deterministically per question (seeded by question index, identically for every model).

**The administration was two-stage.** "No dedicated reasoning channel" is not deliberation-off: models write visible derivations of vendor-idiosyncratic length before the answer line, and under the initial 2,048-token cap the two Gemini seats were massively truncated — the first pass (preserved in the run's log) scored gemini-3.1-pro at 82/198 with 103 unparseable responses and gemini-2.5-flash at 121/198 with 50, voids counted as wrong. The cap was raised to 8,192 and the void responses — only the void ones — were re-asked; the published records are the patched set (13 residual voids per Gemini seat, still counted as wrong). Two facts bound the bias: retries targeted only *unparseable* responses, never parsed-but-wrong answers; and the retry success rate did not exceed the first pass's scored-only accuracy on either seat (gemini-3.1-pro: 78/90 retried items correct, 86.7%, vs 86.3% on its 95 parseable first-pass responses — above the published 80.81%; gemini-2.5-flash: 22/37, 59%, vs 81.8%). Both stages' evidence ships with the package.

## D.3 The audit: no leak found

An audit script re-derives the published table from the raw records and hard-fails on any mismatch. Its checks, all passing:

1. **CSV reconciliation** — per-model correct counts recomputed from raw equal the published accuracies exactly, all twelve models.
2. **Key consistency** — the key letter is identical across all twelve models' records for every question.
3. **Key balance** — shuffled key distribution A/B/C/D = 48/51/47/52, chi-square vs uniform $p = 0.95$.
4. **Independent re-extraction** — a second answer extractor, written without sight of the first, agrees with the stored verdicts on every response for ten of twelve models; the Gemini disagreements are almost entirely the independent extractor failing on the LaTeX `\boxed{X}` answer style. Genuinely questionable credits — granted with no terminal answer statement — number 2 (gemini-2.5-flash) and 6 (gemini-3.1-pro) of 198.
5. **Strict-terminal sensitivity** — rescoring with only explicit terminal answer statements counted moves three models (gemini-2.5-flash 72.22 → 70.71, gemini-3.1-pro 80.81 → 77.27, gpt-4.1-mini 63.13 → 60.10) and the $T$–GPQA correlation from 0.982 to 0.972. Scored the opposite way — voids excluded rather than counted wrong — it reads 0.975.
6. **First-pass log reconciliation** — the archived first-pass log reconciles exactly with the shipped two-stage records.

**What the audit cannot rule out.** It certifies the path from raw records to published numbers; it cannot re-run the models. Both instruments share the gateway, so capability-correlated properties of that path touch both, and the gateway's `thinkingBudget: 0` for the Gemini seats is passed but not verified by assertion. And GPQA is public: *uniform* training contamination would inflate accuracies without inflating a correlation against freshly generated items, but *differential* contamination — exposure increasing with training recency and scale, which correlate with capability — would inflate the slope itself. That channel cannot be excluded with the shipped data and is the specific residual threat.

<a id="tab-gpqa-values"></a>

| Model | $T$ | GPQA Diamond (%) |
|---|---:|---:|
| ★ claude-opus-4.5 (anchor) | 7.00 | 78.79 |
| gemini-3.1-pro | 6.92 | 80.81 |
| claude-opus-4.1 | 6.02 | 76.77 |
| claude-opus-4.0 | 5.81 | 71.21 |
| gemini-2.5-flash | 5.75 | 72.22 |
| claude-sonnet-4 | 5.34 | 72.22 |
| gpt-4.1-mini | 5.03 | 63.13 |
| gpt-4.1-2025-04-14 | 4.66 | 61.62 |
| gpt-4.1-nano | 3.68 | 55.05 |
| gpt-4o-2024-08-06 | 3.34 | 46.46 |
| gpt-4o | 2.95 | 48.48 |
| gpt-4o-mini | 2.39 | 43.94 |

Table: The two instruments side by side — the key-free total $T$ (three runs pooled) and self-administered GPQA Diamond accuracy (voids counted as wrong), sorted by $T$.
