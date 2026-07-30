<!-- 2026-06-11: appendix filenames aligned with the paper's letters (A=rating estimators, B=prompts, C=anchor, D=council evaluation); stale shifted-letter duplicates removed. See commit history. -->
# Appendix B. Generation and evaluation prompts

The verbatim prompts used in the canonical run of §4. All are run with
Temperature = 0, reasoning disabled, and tools disabled.

- **B.1** is the generation prompt: each model produces its five-archetype
  portfolio from it.
- **B.2** is the evaluation prompt, shown in its **calibrated/anchored** form —
  the version used for the anchored re-evaluation and the official council
  ratings (§4.2–§4.4) and in the steady-state protocol (§3.3). It scores one
  *Target* submission against a fixed *Reference* submission pinned at
  `{ANCHOR_SCORE}` on every criterion.

The bootstrap's initial all-against-all selection (§4.1) uses the **un-anchored**
form of the same prompt — identical six criteria and JSON schema, with the
calibration machinery removed. The exact passages that are absent in the
un-anchored bootstrap pass are listed in the **Bootstrap note** after B.2, so
both forms are fully specified from the single prompt below.

Template variables appear in braces: `{SUBMISSIONS}`, `{REFERENCE_SUBMISSION}`,
`{TARGET_SUBMISSION}`, and `{ANCHOR_SCORE}` (swept across {5, 6, 7, 8}; fixed at
7 for the official ratings).

Source files in the repository:
- B.1 — `projects/active/council-of-peers-benchmark-4/prompts/generator.md`
- B.2 (anchored) — `papers/v3/experiments/17_bold_api_probe/prompts/evaluator_calibrated.md`
- B.2 (un-anchored bootstrap form) — `projects/active/council-of-peers-benchmark-4/prompts/evaluator.md`

---

## B.1 — Generation prompt

````markdown
# Make more of these. This is a contest — your submissions will be ranked.

You will propose new **archetypal contexts** — universal relational templates
that apply across multiple distant domains. Below are two worked examples,
then your task.

---

## Terminology

- **Archetypal context**: an essential context in its purest abstraction.
- **Context template**: a worded template with `[SLOT]` representing an archetypal context.
- **Parallel contexts** (also called *metaphors*): contexts that are instantiations of the same archetypal context / context template.
- **Metanyms**: words that mirror each other across parallel contexts without being synonyms.
- **Metanym set**: the set of metanyms that instantiates the context-template, producing one parallel context.
- **Metanym table**: the table whose columns are the metanym sets of the parallel contexts.

---

## Example 1

### Template

"[SIGNALING] is part of a complex system of communication that governs basic [ELEMENT] activities and coordinates [ELEMENT] actions. The ability of [ELEMENT] to perceive and correctly respond to [BOUNDARY] is the basis of development, [SUBSYSTEM] repair, and [RESILIENCE] as well as normal [SUBSYSTEM] [HOMEOSTASIS]. Errors in [ELEMENT] information processing are responsible for [FAILURE]. By understanding [SIGNALING], [FAILURE] may be treated effectively. [KNOWLEDGE SYSTEM] research helps us to understand the underlying structure of [SIGNALING] networks. [SIGNALING] is mostly thought of as signaling between [ELEMENT] of a single [SYSTEM]. However, [SIGNALING] may also occur between the [ELEMENT] of two different [SYSTEM]."

### Substitution table (metanyms in base form)

| [SLOT]            | Cell Signaling   | Organ Signaling          | Human Language   |
|-------------------|------------------|--------------------------|------------------|
| ELEMENT           | cell             | organ                    | human            |
| SIGNALING         | cell signaling   | endocrine signaling      | human language   |
| SUBSYSTEM         | tissue           | organ system             | community        |
| RESILIENCE        | immunity         | physiological resilience | resilience       |
| HOMEOSTASIS       | homeostasis      | systemic homeostasis     | equilibrium      |
| BOUNDARY          | microenvironment | internal environment     | environment      |
| FAILURE           | disease          | organ failure            | dysfunction      |
| KNOWLEDGE SYSTEM  | systems biology  | physiology               | sociology        |
| SYSTEM            | organism         | organism                 | society          |

### Cell Signaling

**Form (a)** — grammatical substitution (metanyms inflected as English requires):
"Cell signaling is part of a complex system of communication that governs basic cell activities and coordinates cell actions. The ability of cells to perceive and correctly respond to their microenvironment is the basis of development, tissue repair, and immunity, as well as normal tissue homeostasis. Errors in cellular information processing are responsible for disease. By understanding cell signaling, disease may be treated effectively. Systems biology research helps us to understand the underlying structure of cell-signaling networks. Cell signaling is mostly thought of as signaling between cells of a single organism. However, cell signaling may also occur between the cells of two different organisms."

**Form (b)** — idiomatic rewrite (same propositions, written as a domain expert would):
"Cell signaling is the communication apparatus that governs and coordinates cellular behavior. A cell's ability to sense and respond appropriately to its microenvironment underlies development, tissue repair, immunity, and ordinary tissue homeostasis. When that information processing fails, disease results — and conversely, a clear understanding of cell signaling enables effective therapeutic intervention. Systems biology unpacks the structure of these signaling networks. Most cell signaling occurs within a single organism, but inter-organism signaling (host–pathogen, microbiome) is well-documented."

(Two more domains would follow with their own form (a) and form (b).)

---

## Example 2

### Template

"A [AGENT] must commit [RESOURCE] under uncertainty, and once a [COMMITMENT] is observed it cannot be costlessly reversed. As [INFORMATION] arrives, the [AGENT] learns that earlier [COMMITMENT] are increasingly suboptimal. [REVERSAL_COST] grows with the depth of prior [COMMITMENT], so the [AGENT] often continues along the original [PATH] even when fresh [INFORMATION] favors a different one. [DECISION_THEORY] studies how rational [AGENT] balance the value of [INFORMATION] against the cost of [REVERSAL_COST]."

### Substitution table

| [SLOT]            | Capital Investment   | Coalition Politics   |
|-------------------|----------------------|----------------------|
| AGENT             | firm                 | coalition            |
| RESOURCE          | capital              | endorsement          |
| COMMITMENT        | investment           | public statement     |
| INFORMATION       | market signal        | polling data         |
| REVERSAL_COST     | switching cost       | reputational cost    |
| PATH              | strategy             | position             |
| DECISION_THEORY   | investment theory    | political science    |

### Capital Investment

**Form (a)**:
"A firm must commit capital under uncertainty, and once an investment has been made it cannot be costlessly reversed. As market signals arrive, the firm learns that earlier investments are increasingly suboptimal. Switching costs grow with the depth of prior investments, so the firm often continues along the original strategy even when fresh market signals favor a different one. Investment theory studies how rational firms balance the value of market signals against the cost of switching."

**Form (b)**:
"Capital investments must be made under uncertainty, and once committed they are sunk — reversal is costly. New market signals continuously update what would have been optimal, but the depth of prior commitment raises the cost of changing course. Firms therefore tend to stay with their original strategy, even when current information would favor switching. Real-options theory and other strands of investment theory characterise how rational firms trade off information value against reversal cost."

---

## Your task

Propose **five archetypal contexts**. Each archetypal context has a worded context-template, one metanym table with five metanym sets, and five parallel contexts (the instantiations of the template). The five archetypal contexts in your submission should themselves have very different system structures from each other. Surface relabelings of the worked examples above don't count.

### Note

Example 1 is **recursive**: cells - organs - humans. Recursive archetypal contexts can be observed in nature. But not all archetypal contexts are recursive. You are free to submit archetypal contexts of both kinds. If there are recursive ones in your submission, point to them. The instantiations should demonstrate the recursion.

### What to submit

For each of your five archetypal contexts, begin with:

```
## Archetype Proposal: <short name>
```

Then provide, for that archetypal context:

1. **Context-template** — a worded paragraph with `[SLOT]` placeholders. Slots use one canonical noun (e.g. `[ELEMENT]`, never `[ELEMENTS]`).
2. **Metanym table** — rows = slots, columns = 5 domains, each cell a metanym in **base form** (singular noun, infinitive verb, etc.).
3. **Five parallel contexts**, one per domain:
   - **Form (a)** — the context-template with that domain's metanym set substituted in. Inflect metanyms as English requires; Form (a) must be grammatically correct.
   - **Form (b)** — idiomatic rewrite of Form (a). Same propositions, written as a domain expert would naturally write them.
   - **Optional ≤1-sentence justification** beginning `Justification:` — only if a propositional claim might be misread by a domain expert.

### Rules

- The **context-template** uses base-form slot placeholders — `[ELEMENT]` not `[ELEMENTS]`. One token per slot, used consistently.
- The **metanym table** lists metanyms in **base form** — `cell`, `human`, etc.
- The **parallel contexts** (Form (a) and Form (b)) must use the **correct grammatical form** of each metanym for the sentence — `cell` in the table becomes `cells` or `cell's` in the PC as English grammar requires.
- Every proposition in Form (a) must appear in Form (b), and vice versa. Do not add or drop claims between the two forms.

### How you will be ranked

A submission contains **five archetypal contexts**. Evaluators score on six criteria, each rated 1–10. The scope tag tells you the unit of judgment:

1. **(Each parallel context)** Each sentence is factually correct
2. **(Each archetypal context)** Beauty
3. **(Each archetypal context)** Intelligence
4. **(Each archetypal context)** The parallel contexts from the template span very different domains. Metanyms are far from synonymous
5. **(Each archetypal context)** The archetypal template has impressive length
6. **(Each submitted set of archetypal contexts)** The archetypal contexts have very different system structures
````

---

## B.2 — Evaluation prompt (calibrated/anchored)

````markdown
# Score this submission against a calibration reference.

You are evaluating one contest submission ("Target Submission") against a fixed
reference ("Reference Submission") that has been pre-scored at **{ANCHOR_SCORE}/10 on every
criterion**. Score the Target Submission only — the Reference is your yardstick.

For each criterion below, ask: *is the Target's quality on this criterion better
or worse than the Reference, and by how much?*

- Equal quality to the Reference → **{ANCHOR_SCORE}**
- Clearly better than the Reference → **above {ANCHOR_SCORE}** (with magnitude reflecting how much better, up to 10)
- Clearly worse than the Reference → **below {ANCHOR_SCORE}** (with magnitude reflecting how much worse, down to 1)

Use the full 1–10 scale relative to the calibration anchor. Do not score the
Reference Submission itself — its scores are fixed at {ANCHOR_SCORE}.

## Terminology

- **Archetypal context**: an essential context in its purest abstraction.
- **Context template**: a worded template with `[SLOT]` representing an archetypal context.
- **Parallel contexts** (also called *metaphors*): contexts that are instantiations of the same archetypal context / context template.
- **Metanyms**: words that mirror each other across parallel contexts without being synonyms.
- **Metanym set**: the set of metanyms that instantiates the context-template, producing one parallel context.
- **Metanym table**: the table whose columns are the metanym sets of the parallel contexts.

---

Each submission contains **five archetypal contexts**. Each archetypal context has:

- A **context-template** — a worded paragraph with `[SLOT]` placeholders.
- A **metanym table** — five metanym sets, one per parallel context. Rows = slots, columns = domains.
- **Five parallel contexts** (the five instantiations of the template), each consisting of:
  - **Form (a)** — the template with one metanym set substituted in, grammatically correct.
  - **Form (b)** — an idiomatic rewrite of Form (a), same propositions in domain-expert prose.
  - Optionally a **Justification** sentence.

Score the Target Submission on **six criteria**, each rated 1–10 relative to the Reference (which is fixed at {ANCHOR_SCORE} on every criterion). The scope tag at the start of each criterion — `(Each parallel context)`, `(Each archetypal context)`, or `(Each submitted set of archetypal contexts)` — tells you the unit of judgment. For each scored unit, write one paragraph justifying the rating relative to the Reference, then give the number.

---

## The six criteria

### 1. (Each parallel context) Each sentence is factually correct (1–10)

### 2. (Each archetypal context) Beauty (1–10)

### 3. (Each archetypal context) Intelligence (1–10)

### 4. (Each archetypal context) The parallel contexts from the template span very different domains. Metanyms are far from synonymous (1–10)

### 5. (Each archetypal context) The archetypal template has impressive length (1–10)

### 6. (Each submitted set of archetypal contexts) The archetypal contexts have very different system structures (1–10)

---

## Note on recursion

Some submissions may be **recursive** — the same archetypal context manifesting at multiple nested scales (cells → organs → humans, the canonical example). Contestants are invited to identify recursion in their submission and show the instantiations that demonstrate it. Recursion is a valued property when present and correctly identified, but is not required. Take it into account where appropriate.

---

## The submissions

### Reference Submission (fixed at {ANCHOR_SCORE}/10 on every criterion)

{REFERENCE_SUBMISSION}

---

### Target Submission (to be scored relative to the Reference)

{TARGET_SUBMISSION}

---

## Output

Produce a section in this exact form (for the Target only — do not re-score the Reference):

```
## Target Submission

### Archetypal context 1: <short name>

#### Factually correct (per parallel context)
- PC 1 (<domain>): <one paragraph, relative to Reference>. Rating: N
- PC 2 (<domain>): <one paragraph, relative to Reference>. Rating: N
- PC 3 (<domain>): <one paragraph, relative to Reference>. Rating: N
- PC 4 (<domain>): <one paragraph, relative to Reference>. Rating: N
- PC 5 (<domain>): <one paragraph, relative to Reference>. Rating: N

#### Beauty
<one paragraph relative to Reference>
Rating: N

#### Intelligence
<one paragraph relative to Reference>
Rating: N

#### Domains far apart / metanyms not synonymous
<one paragraph relative to Reference>
Rating: N

#### Impressive length
<one paragraph relative to Reference>
Rating: N

### Archetypal context 2: <short name>
… (same five blocks)

### Archetypal context 3: <short name>
…

### Archetypal context 4: <short name>
…

### Archetypal context 5: <short name>
…

### Structural diversity across the submitted set
<one paragraph relative to Reference>
Rating: N
```

After the markdown, end with a single fenced JSON block (Target scores only):

```json
{
  "scores": {
    "Target": {
      "archetypal_contexts": [
        {
          "name": "<short name>",
          "factual_per_pc":           [N, N, N, N, N],
          "beauty":                   N,
          "intelligence":             N,
          "instantiation_distinctness": N,
          "impressive_length":        N
        }
        /* five entries in this list, one per archetypal context */
      ],
      "structural_diversity": N
    }
  }
}
```

All ratings are integers 1–10 inclusive. Equal to the Reference = {ANCHOR_SCORE}.
````

### Bootstrap note — the un-anchored form (§4.1 initial selection)

The bootstrap's initial all-against-all leaderboard (§4.1, stage 1 of §3.4) is
produced with the **same six criteria, output format, and JSON schema** as B.2,
but with the calibration machinery removed. Relative to the anchored prompt
above, the un-anchored form **omits** the following, and makes the substitutions
noted:

1. **Title line.** "Score this submission against a calibration reference."
   becomes "Score these. You are evaluating contest submissions."
2. **The entire calibration preamble is removed** — i.e. everything from "You
   are evaluating one contest submission (\"Target Submission\") against a fixed
   reference…" down to and including "…Do not score the Reference Submission
   itself — its scores are fixed at {ANCHOR_SCORE}." (the opening paragraph, the
   three "Equal / Clearly better / Clearly worse" bullets, and the "Use the full
   1–10 scale relative to the calibration anchor" sentence).
3. **The scoring-instruction sentence drops its reference clause.** "Score the
   Target Submission on six criteria, each rated 1–10 relative to the Reference
   (which is fixed at {ANCHOR_SCORE} on every criterion)… justifying the rating
   relative to the Reference" becomes "Score each submission on six criteria,
   each rated 1–10… justifying the rating" (all "relative to the Reference"
   qualifiers dropped).
4. **The Reference Submission block is removed.** The "## The submissions →
   ### Reference Submission (fixed at {ANCHOR_SCORE}/10…) {REFERENCE_SUBMISSION}
   → ### Target Submission … {TARGET_SUBMISSION}" section is replaced by a
   single batch: "## The proposals to evaluate" followed by `{SUBMISSIONS}`.
5. **The output is per-submission, not per-target.** "## Target Submission"
   becomes "## Submission <ID>" repeated for each submission; all
   "<…relative to Reference>" annotations in the output template are dropped;
   and the JSON top-level key changes from the single `"Target"` to one entry
   per `"<submission_id>"`.
6. **The closing line drops its anchor clause.** "All ratings are integers 1–10
   inclusive. Equal to the Reference = {ANCHOR_SCORE}." becomes "All ratings are
   integers 1–10 inclusive."

Everything else — the six criteria and their scope tags, the terminology block,
the recursion note, and the per-archetype/per-PC/per-portfolio output structure
— is identical between the two forms.
