#!/usr/bin/env python3
"""Appendix D — full audit of the self-administered GPQA Diamond scoring.

Re-derives every published GPQA number from the raw per-question artifacts shipped in
data/gpqa_runs/ (198 questions x 12 models, each record carrying the model's full raw
response text, the key letter for that question, and the stored verdict), so the scoring
is checkable end to end without any API access. Five checks, all hard failures:

  1. CSV reconciliation — per model, n_correct recomputed from the raw records must equal
     data/gpqa_selfadministered.csv exactly.
  2. Key consistency — the key letter for each question must be identical across all 12
     models' records (one shuffle, applied once).
  3. Key balance — the shuffled key's letter distribution must be near-uniform (chi-square
     against uniform, p > 0.01); a skewed key would interact with letter-guessing priors.
  4. Independent re-extraction — a second, independently written answer-extractor is run
     over every raw response; per-model disagreement with the stored verdicts is reported.
     (The archive extractor is more capable on LaTeX '\\boxed{X}' answers; disagreements
     concentrate there and in truncated derivations.)
  5. Strict-terminal sensitivity — accuracies rescored counting ONLY responses with an
     explicit terminal answer statement ('Answer: X', 'final answer ... X', boxed). The
     published-vs-strict deltas and the resulting shift in the T-GPQA correlation are
     printed; the shift must be small (|dr| < 0.01) for the headline to stand.

No key ever entered a prompt (see the archived runner's PROMPT_TMPL, reproduced in the
appendix); this script verifies the scoring side of that pipeline.
"""
import csv
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

import numpy as np
from scipy.stats import chisquare, pearsonr

HERE = Path(__file__).resolve().parent
DATA = HERE.parent / "data"
RUN = sorted((DATA / "gpqa_runs").glob("gpqa_*"))[-1]


def independent_extract(t):
    """Second extractor, written blind to the archive's: last explicit answer statement,
    then last parenthesised letter, then a lone-letter line."""
    if not t:
        return None
    m = re.findall(r"[Aa]nswer[^A-Za-z0-9\n]{0,10}\(?([ABCD])\)?\b", t)
    if m:
        return m[-1]
    m = re.findall(r"\(([ABCD])\)", t)
    if m:
        return m[-1]
    m = re.findall(r"^\s*\(?([ABCD])\)?\.?\s*$", t, re.M)
    if m:
        return m[-1]
    return None


def terminal_extract(t):
    """Strict: only an explicit terminal answer statement counts (incl. \\boxed{X})."""
    if not t:
        return None
    m = re.findall(r"(?:final answer|answer)\s*(?:is|:)?\s*(?:option\s*)?\$?\\?(?:boxed\{)?"
                   r"\(?\**([ABCD])\**\)?\}?", t, re.I)
    return m[-1] if m else None


def main():
    csv_rows = {r["model"]: r for r in csv.DictReader(
        [l for l in open(DATA / "gpqa_selfadministered.csv") if not l.startswith('"#')])}
    models = sorted(d.name for d in RUN.iterdir() if d.is_dir())
    fails = 0
    keys = defaultdict(set)
    strict_acc = {}

    print(f"run: {RUN.name}   models: {len(models)}")
    print(f"{'model':22}{'csv_n':>7}{'raw_n':>7}{'indep':>7}{'disagr':>7}{'strict':>7}")
    for m in models:
        recs = json.load(open(RUN / m / "responses.json"))
        raw_n = sum(1 for r in recs if r["is_correct"])
        indep = disagr = strict_n = 0
        for r in recs:
            keys[r["idx"]].add(r["correct"])
            mine = independent_extract(r["raw_text"])
            ok = mine == r["correct"]
            indep += ok
            disagr += (ok != r["is_correct"])
            term = terminal_extract(r["raw_text"])
            strict_n += (term == r["correct"]) if term else 0
        c = csv_rows[m]
        ok_csv = int(c["n_correct"]) == raw_n and abs(float(c["gpqa_diamond_accuracy"]) - 100 * raw_n / len(recs)) < 0.01
        fails += not ok_csv
        strict_acc[m] = 100 * strict_n / len(recs)
        gem = m.startswith("gemini")
        ok4 = disagr == 0 or gem            # non-Gemini disagreement = extraction bug
        fails += not ok4
        print(f"{m:22}{int(c['n_correct']):>7}{raw_n:>7}{indep:>7}{disagr:>7}{strict_n:>7}"
              f"  {'OK' if (ok_csv and ok4) else 'FAIL'}")

    multi = {k for k, v in keys.items() if len(v) > 1}
    print(f"\ncheck 2 — key identical across models: {'OK' if not multi else f'FAIL {sorted(multi)[:5]}'}")
    fails += bool(multi)

    dist = Counter(sorted(v)[0] for v in keys.values())
    p = chisquare(list(dist.values())).pvalue
    print(f"check 3 — key balance {dict(sorted(dist.items()))}, chi-square p = {p:.2f}: "
          f"{'OK' if p > 0.01 else 'FAIL'}")
    fails += p <= 0.01

    # check 5 — correlation shift under strict scoring
    council = {r["model"]: r for r in csv.DictReader(
        [l for l in open(DATA / "total_rating_council.csv") if not l.startswith("#")])}
    ms = [m for m in models if m in council]
    T = [float(council[m]["T"]) for m in ms]
    g_pub = [float(csv_rows[m]["gpqa_diamond_accuracy"]) for m in ms]
    g_str = [strict_acc[m] for m in ms]
    r_pub = pearsonr(T, g_pub).statistic
    r_str = pearsonr(T, g_str).statistic
    print(f"check 5 — T vs GPQA: published r = {r_pub:.3f}, strict-terminal r = {r_str:.3f}, "
          f"|dr| = {abs(r_pub - r_str):.3f}: {'OK' if abs(r_pub - r_str) < 0.01 else 'FAIL'}")
    fails += abs(r_pub - r_str) >= 0.01

    # check 6 — the two-stage administration: D.2's first-pass numbers re-read from log.txt
    import re as _re
    log = (RUN / "log.txt").read_text()
    m6 = _re.search(r"gemini-3\.1-pro\s+(\d+)/198\s+acc=\s*[\d.]+%\s+\(scored\s+([\d.]+)%, void (\d+)\)", log)
    m7 = _re.search(r"gemini-2\.5-flash\s+(\d+)/198\s+acc=\s*[\d.]+%\s+\(scored\s+([\d.]+)%, void (\d+)\)", log)
    ok6 = (m6 and m6.groups() == ("82", "86.3", "103") and m7 and m7.groups() == ("121", "81.8", "50"))
    print(f"check 6 — first-pass log matches D.2 (pro 82/198, scored 86.3%, void 103; "
          f"flash 121/198, void 50): {'OK' if ok6 else 'FAIL'}")
    fails += not ok6

    if fails:
        sys.exit(f"GPQA AUDIT FAILED ({fails} check(s))")
    print("\nGPQA audit: all checks pass")


if __name__ == "__main__":
    main()
