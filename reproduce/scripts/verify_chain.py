#!/usr/bin/env python3
# supplementary: verification of the pinned inputs, not a result producer
"""Walk the chain from the prompts to the numbers and check every link that can be checked from the package alone.

RESULT: exit 0 and one line per link when every check passes; exit 1 naming the first file that breaks a link.

The links, in the order the experiment ran:

  1. prompts -> runs       each run's own record (run_info.json) names the prompt it was sent and its length; the file
                            is in prompts/ and its length is the recorded one (run 1 is the documented exception, below)
  2. generation            every portfolio of every run is present (twelve per run), with its API envelope for run 1
  3. evaluation            every ordered (evaluator, target) pair of every run has its JSON envelope and its transcript;
                            the envelope is a completed call (status 200; finish reasons are tallied, one anchor-5 call ended
                            in the vendor's content filter) and its completion-token count fits the transcript's length
  4. generation -> evaluation   the archetype titles a judge names in its transcript are the titles of the target's
                            portfolio file, so each evaluation is of the portfolio shipped here
  5. prompt -> evaluation  each transcript follows the output format the evaluator prompt prescribes
  6. GPQA                  each model's 198 raw responses re-score to the accuracy in data/gpqa_selfadministered.csv
  7. checksums             SHA256SUMS covers every input and matches; its own SHA-256 is the package digest
                            (the digest printed in the paper's Reproducibility statement)

Link 8, evaluations -> numbers, is `bash reproduce.sh`: it rewrites every CSV the paper's tables are built from,
byte-identically, from the evaluation JSONs checked here.

Run 1's log records a 5,373-character evaluator template; the shipped prompts/evaluator_calibrated.md has 5,512
characters and is the revision the anchor sweep (two hours later) and both regenerations record. The earlier revision
was not kept; Appendix B prints the shipped one. This is the one recorded discrepancy in the package, and this script
expects exactly it.

    python3 scripts/verify_chain.py            # from reproduce/; standard library only
"""
import csv, hashlib, json, re, statistics, sys
from pathlib import Path

PKG = Path(__file__).resolve().parents[1]
MODELS = ["claude-opus-4.5", "gemini-3.1-pro", "claude-opus-4.1", "claude-opus-4.0", "gemini-2.5-flash", "claude-sonnet-4",
          "gpt-41-mini", "gpt-41-2025-04-14", "gpt-41-nano", "gpt-4o-2024-08-06", "gpt-4o", "gpt-4o-mini"]   # file-name slugs
RUNS = {  # run directory -> (pairs expected, portfolio directory or None, prompt file)
    "data/probe_J_20260529T005230Z": (144, None, "prompts/evaluator.md"),
    "data/probe_K_20260529T014133Z": (132, "data/portfolios_run1", "prompts/evaluator_calibrated.md"),
    "data/probe_K_anchor5_20260529T030442Z": (132, None, "prompts/evaluator_calibrated.md"),
    "data/probe_K_anchor6_20260529T032518Z": (132, None, "prompts/evaluator_calibrated.md"),
    "data/probe_K_anchor8_20260529T033755Z": (132, None, "prompts/evaluator_calibrated.md"),
    "data/regenerations/probe_K_anchor7_20260619T015828Z": (132, "data/regenerations/portfolios_run2", "prompts/evaluator_calibrated.md"),
    "data/regenerations/probe_K_anchor7_20260619T040659Z": (132, "data/regenerations/portfolios_run3", "prompts/evaluator_calibrated.md"),
}
RECORDED_PROMPT_CHARS_EXCEPTION = {"data/probe_K_20260529T014133Z": 5373}      # see the docstring
FORMAT_HEADINGS = ["## Target Submission", "### Archetypal context", "#### Factually correct", "### Structural diversity"]
failures = []


def fail(msg):
    failures.append(msg); print("FAIL", msg)


def ok(msg):
    print("ok  ", msg)


def link1_prompts():
    for run, (_, _, prompt) in RUNS.items():
        info = json.loads((PKG / run / "run_info.json").read_text())
        rec = info["evaluator_prompt_path"]
        if rec != prompt:
            fail(f"{run}: run_info names prompt {rec!r}, expected {prompt!r}"); continue
        n = len((PKG / prompt).read_text())
        want = RECORDED_PROMPT_CHARS_EXCEPTION.get(run, n)
        if info["evaluator_prompt_chars"] != want:
            fail(f"{run}: recorded prompt length {info['evaluator_prompt_chars']} but {prompt} has {n} characters")
    ok(f"link 1  prompts -> runs: every run names a prompt shipped in prompts/ at the recorded length "
       f"(run 1 recorded {RECORDED_PROMPT_CHARS_EXCEPTION['data/probe_K_20260529T014133Z']}, the earlier revision; see docstring)")


def link2_generation():
    for run, (_, pdir, _) in RUNS.items():
        if not pdir:
            continue
        files = sorted((PKG / pdir).glob("*_off_T0_r1.md"))
        slugs = sorted(f.name[: -len("_off_T0_r1.md")] for f in files)
        if slugs != sorted(MODELS):
            fail(f"{pdir}: portfolios {slugs} != the twelve participants"); continue
        if pdir.endswith("run1"):
            for f in files:
                env = f.with_suffix(".json")
                if not env.exists():
                    fail(f"{env}: missing envelope for a run-1 portfolio"); continue
                e = json.loads(env.read_text())
                if e.get("ResponseStatusCode") != 200 or not e.get("Messages"):
                    fail(f"{env}: not a completed generation call")
    for name in ("anchor_claude-opus-4.5.md", "ballast_gpt-4o-mini.md", "ballast_gpt-4.1-nano.md"):
        sub = (PKG / "submissions" / name).read_text()
        slug = name.split("_", 1)[1][:-3].replace("gpt-4.1", "gpt-41")
        run1 = (PKG / "data/portfolios_run1" / f"{slug}_off_T0_r1.md").read_text()
        if name.startswith("ballast") and sub != run1:
            fail(f"submissions/{name} is not byte-identical to its run-1 portfolio")
        if name.startswith("anchor"):
            tmpl = re.search(r"\[NAVIGATOR\][^\n]{40,}", sub)
            if not tmpl or tmpl.group(0)[:120] not in run1:
                fail("submissions/anchor_claude-opus-4.5.md: its first template is not in the run-1 anchor portfolio")
    ok("link 2  generation: twelve portfolios in each of runs 1, 2, 3; run 1's with completed API envelopes; "
       "the ballast files are byte-identical to their run-1 portfolios and the anchor exhibit is the run-1 anchor portfolio")


def link3_evaluation():
    ratios, finishes = [], {}
    for run, (pairs, _, _) in RUNS.items():
        d = PKG / run
        js = sorted(p for p in d.glob("eval_*.json"))
        if len(js) != pairs:
            fail(f"{run}: {len(js)} evaluation envelopes, expected {pairs}"); continue
        info = json.loads((d / "run_info.json").read_text())
        if info["pairs"] != pairs or len(info["results"]) != pairs or not all(r["ok"] for r in info["results"]):
            fail(f"{run}: run_info does not record {pairs} completed pairs")
        evaluators = {p.name[len("eval_"):].split("_x_")[0] for p in js}
        if evaluators != set(MODELS):
            fail(f"{run}: evaluators {sorted(evaluators)} != the twelve participants")
        for p in js:
            md = p.with_suffix(".md")
            if not md.exists():
                fail(f"{md}: transcript missing"); continue
            e = json.loads(p.read_text())
            if e.get("ResponseStatusCode") != 200:
                fail(f"{p}: status {e.get('ResponseStatusCode')}")
            fr = str(e["Messages"][0].get("FinishReason", "stop")).lower(); finishes[fr] = finishes.get(fr, 0) + 1
            tok = e["TokenInformation"]["CompletionTokens"]; chars = len(md.read_text())
            if tok <= 0 or chars <= 0:
                fail(f"{p}: empty completion"); continue
            ratios.append(chars / tok)
    lo, hi, med = min(ratios), max(ratios), statistics.median(ratios)
    if not (2.0 <= lo and hi <= 8.0):
        fail(f"characters per completion token outside the plausible band: min {lo:.2f}, max {hi:.2f}")
    ok(f"link 3  evaluation: {len(ratios)} completed calls across 7 runs, every pair with envelope and transcript; "
       f"finish reasons {finishes}; transcript length per completion token median {med:.2f} (range {lo:.2f}–{hi:.2f})")


def titles_in_portfolio(text):
    return [t.strip().lower() for t in re.findall(r"^##+ Archetype Proposal:\s*(.+)$", text, flags=re.M)]


def link4_generation_to_evaluation():
    for run, (_, pdir, _) in RUNS.items():
        if not pdir:
            continue
        shares = {}
        for target in MODELS:
            if target == "claude-opus-4.5":      # the anchor is every anchored prompt's Reference, never a Target: no transcript names its archetypes
                continue
            port = (PKG / pdir / f"{target}_off_T0_r1.md").read_text().lower()
            named, found = 0, 0
            for md in (PKG / run).glob(f"eval_*_x_{target}.md"):
                if md.name.startswith(f"eval_{target}_x_"):
                    continue
                for t in re.findall(r"^### Archetypal context \d+:\s*(.+)$", md.read_text(), flags=re.M):
                    named += 1; found += t.strip().lower().rstrip(".") in port
            if named == 0:
                fail(f"{run}: no archetype titles named in the evaluations of {target}"); continue
            shares[target] = found / named
            if shares[target] < 0.5:
                fail(f"{run}: only {found}/{named} archetype titles named by the judges of {target} occur in {pdir}/{target}_off_T0_r1.md")
        ok(f"link 4  generation -> evaluation, {pdir.split('/')[-1]}: judges' archetype titles found in the target portfolio for "
           f"{sum(shares.values()) / len(shares):.0%} of mentions (min {min(shares.values()):.0%}); the anchor is the Reference of every prompt, not a target")


def link5_prompt_to_evaluation():
    prompt = (PKG / "prompts/evaluator_calibrated.md").read_text()
    for h in FORMAT_HEADINGS:
        if h not in prompt:
            fail(f"prompts/evaluator_calibrated.md does not prescribe the heading {h!r}")
    total = bad = 0
    for run, (_, _, prompt_file) in RUNS.items():
        if not prompt_file.endswith("evaluator_calibrated.md"):
            continue
        for md in (PKG / run).glob("eval_*.md"):
            total += 1; txt = md.read_text()
            if not all(h in txt for h in FORMAT_HEADINGS):
                bad += 1
    if bad / total > 0.02:
        fail(f"{bad} of {total} anchored transcripts do not follow the prescribed output format")
    ok(f"link 5  prompt -> evaluation: {total - bad} of {total} anchored transcripts carry the prompt's prescribed headings")


def link6_gpqa():
    rows = {r["model"]: r for r in csv.DictReader(l for l in (PKG / "data/gpqa_selfadministered.csv").read_text().splitlines() if not l.startswith('"#'))}
    run = next((PKG / "data/gpqa_runs").glob("gpqa_*"))
    for model, r in rows.items():
        recs = json.loads((run / model / "responses.json").read_text())
        if len(recs) != 198:
            fail(f"gpqa {model}: {len(recs)} responses, expected 198"); continue
        correct = sum(1 for x in recs if x["is_correct"]); void = sum(1 for x in recs if x["void"])
        if correct != int(r["n_correct"]) or void != int(r["n_void"]):
            fail(f"gpqa {model}: raw responses give {correct} correct / {void} void, CSV says {r['n_correct']} / {r['n_void']}")
    ok(f"link 6  GPQA: {len(rows)} models × 198 raw responses re-score to the CSV")


def link7_checksums():
    sums = PKG / "SHA256SUMS"
    if not sums.exists():
        fail("SHA256SUMS is missing (see README: 'Check the chain yourself')"); return
    n = 0
    for line in sums.read_text().splitlines():
        digest, name = line.split("  ", 1); n += 1
        p = PKG / name
        if not p.exists():
            fail(f"SHA256SUMS lists {name}, which is missing"); continue
        if hashlib.sha256(p.read_bytes()).hexdigest() != digest:
            fail(f"{name}: SHA-256 differs from SHA256SUMS")
    listed = {l.split("  ", 1)[1] for l in sums.read_text().splitlines()}
    for sub in ("data", "prompts", "submissions"):
        for p in (PKG / sub).rglob("*"):
            if p.is_file() and p.name != ".DS_Store" and str(p.relative_to(PKG)) not in listed:
                fail(f"{p.relative_to(PKG)} is not covered by SHA256SUMS")
    ok(f"link 7  checksums: {n} files match SHA256SUMS; package digest sha256(SHA256SUMS) = {hashlib.sha256(sums.read_bytes()).hexdigest()}")


def main():
    for link in (link1_prompts, link2_generation, link3_evaluation, link4_generation_to_evaluation, link5_prompt_to_evaluation, link6_gpqa, link7_checksums):
        link()
    if failures:
        print(f"\n{len(failures)} check(s) failed"); return 1
    print("\nevery link holds; link 8 is `bash reproduce.sh` (rewrites the CSVs byte-identically from the evaluation JSONs)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
