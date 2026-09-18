# Score these. You are evaluating contest submissions.

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

Score each submission on **six criteria**, each rated 1–10. The scope tag at the start of each criterion — `(Each parallel context)`, `(Each archetypal context)`, or `(Each submitted set of archetypal contexts)` — tells you the unit of judgment. For each scored unit, write one paragraph justifying the rating, then give the number.

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

## The proposals to evaluate

{SUBMISSIONS}

---

## Output

For each submission, produce a section in this exact form:

```
## Submission <ID>

### Archetypal context 1: <short name>

#### Factually correct (per parallel context)
- PC 1 (<domain>): <one paragraph>. Rating: N
- PC 2 (<domain>): <one paragraph>. Rating: N
- PC 3 (<domain>): <one paragraph>. Rating: N
- PC 4 (<domain>): <one paragraph>. Rating: N
- PC 5 (<domain>): <one paragraph>. Rating: N

#### Beauty
<one paragraph>
Rating: N

#### Intelligence
<one paragraph>
Rating: N

#### Domains far apart / metanyms not synonymous
<one paragraph>
Rating: N

#### Impressive length
<one paragraph>
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
<one paragraph>
Rating: N
```

After all submissions, end with a single fenced JSON block:

```json
{
  "scores": {
    "<submission_id>": {
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

All ratings are integers 1–10 inclusive.
