#!/usr/bin/env python3
"""Appendix H (ICLR version) — the thinking-vs-play experiment (2026-09-16, official Anthropic and OpenAI APIs): four models
as two players each, thinking off at temperature 0 and thinking on; each plays the generator prompt once and judges the six
non-kin players and the two ballasts against the anchor pinned at 7. Reads data/thinking_vs_play/20260916T023717Z/{gen,eval}/
and reports: per target the factual mean over its judges; on-minus-off per model with a bootstrap (judges resampled with
replacement, then each portfolio's five archetypes; percentile 95% intervals); judge agreement with the others' consensus;
what the thinking was spent on (title and domain overlap between kin; drafting of slotted template text in the thinking;
similarity of each final template to its closest draft). No API calls. Record: archetypal-contexts
projects/completed/thinking-vs-play/FINAL_REPORT.md."""
import sys, json, re, statistics as st, difflib, io, contextlib
from pathlib import Path
import numpy as np
PKG = Path(__file__).resolve().parent.parent
run = PKG / "data/thinking_vs_play/20260916T023717Z"
PLAYERS = ["sonnet46-off", "sonnet46-on", "haiku45-off", "haiku45-on", "terra-off", "terra-on", "luna-off", "luna-on"]
MODELS = ["haiku45", "luna", "sonnet46", "terra"]
JR = re.compile(r"```json\s*\n(.*?)\n```", re.S); NF = ("beauty", "intelligence", "instantiation_distinctness", "impressive_length")

def parse_eval(fp):
    try:
        node = json.loads(JR.search(json.load(open(fp))["Messages"][0]["Message"]["Content"]).group(1))["scores"]
        node = node[list(node)[0]]; A = node["archetypal_contexts"][:5]
        return dict(fact=[x for a in A for x in a.get("factual_per_pc", [])], nf=[a[k] for a in A for k in NF if isinstance(a.get(k), (int, float))])
    except Exception: return None
R = {}
for fp in sorted((run / "eval").glob("eval_*.json")):
    e, t = re.match(r"eval_(.+)_x_(.+)\.json", fp.name).groups(); r = parse_eval(fp)
    if r: R[(e, t)] = r
targets = sorted({t for _, t in R}); judges = sorted({e for e, _ in R})
print(f"parsed {len(R)} evaluations; {len(judges)} judges, {len(targets)} targets\n")
print(f"{'target':22} {'judges':>6} {'factual':>8} {'other axes':>10} {'from thinking judges':>21} {'from non-thinking':>18}")
for t in targets:
    js = [e for e, tt in R if tt == t]; f = lambda es: st.mean(x for e in es for x in R[(e, t)]["fact"]) if es else float("nan")
    print(f"{t:22} {len(js):6} {f(js):8.2f} {st.mean(x for e in js for x in R[(e, t)]['nf']):10.2f} {f([e for e in js if e.endswith('-on')]):21.2f} {f([e for e in js if e.endswith('-off')]):18.2f}")

print("\nbootstrap (B = 4000, seed 0): judges resampled with replacement, then each portfolio's five archetypes; percentile 95% intervals")
rng = np.random.default_rng(0); B = 4000
def by_arch(e, t):
    f = R[(e, t)]["fact"]; return [f[i * 5:(i + 1) * 5] for i in range(len(f) // 5)]
def port_mean(t, js, idx): return st.mean(x for e in js for a in idx for x in by_arch(e, t)[a])
print(f"{'model':10} {'off [95% CI]':>22} {'on [95% CI]':>22} {'on - off [95% CI]':>24}")
for m in MODELS:
    on, off = f"{m}-on", f"{m}-off"; J = sorted({e for e, t in R if t == on} & {e for e, t in R if t == off})
    na, nb = min(len(by_arch(e, on)) for e in J), min(len(by_arch(e, off)) for e in J); d, xo, xf = [], [], []
    for _ in range(B):
        js = list(rng.choice(J, len(J))); a, b = port_mean(on, js, rng.integers(0, na, na)), port_mean(off, js, rng.integers(0, nb, nb)); xo.append(a); xf.append(b); d.append(a - b)
    q = lambda v: (float(np.percentile(v, 2.5)), float(np.percentile(v, 97.5)))
    print(f"{m:10} {port_mean(off, J, range(nb)):6.2f} [{q(xf)[0]:.2f}, {q(xf)[1]:.2f}]   {port_mean(on, J, range(na)):6.2f} [{q(xo)[0]:.2f}, {q(xo)[1]:.2f}]   {st.mean(d):+6.2f} [{q(d)[0]:+.2f}, {q(d)[1]:+.2f}]  P(on>off)={np.mean(np.array(d) > 0):.2f}")

print("\njudges: agreement of each judge's factual ratings with the other judges' consensus (Pearson over shared parallel contexts):")
for e in judges:
    xs, ys = [], []
    for t in targets:
        if (e, t) not in R: continue
        rows = [R[(o, t)]["fact"] for o in judges if o != e and (o, t) in R and len(R[(o, t)]["fact"]) == len(R[(e, t)]["fact"])]
        if rows: xs += list(R[(e, t)]["fact"]); ys += list(np.mean(rows, axis=0))
    print(f"  {e:12} r={np.corrcoef(xs, ys)[0,1]:.2f}  n={len(xs)}  mean given={st.mean(xs):.2f}")

print("\nwhat the thinking was spent on:")
sys.path.insert(0, str(PKG / "scripts"))
with contextlib.redirect_stdout(io.StringIO()):
    from portfolio_divergence import parse
for m in MODELS:
    A, Bp = parse((run / f"gen/{m}-off.md").read_text()), parse((run / f"gen/{m}-on.md").read_text())
    da = {d for _, ds, _ in A.values() for d in ds}; db = {d for _, ds, _ in Bp.values() for d in ds}
    T = (run / f"gen/{m}-on.reasoning.md").read_text(); paras = [p for p in re.split(r"\n\s*\n", T) if p.strip()]
    drafting = [p for p in paras if re.search(r"\[[A-Z_]{3,}\]", p)]
    sims = [max((difflib.SequenceMatcher(None, p, tmpl).ratio() for p in drafting), default=0) for tmpl, _, _ in Bp.values()]
    print(f"  {m:9} kin share {len(set(A) & set(Bp))}/{len(Bp)} titles, {len(da & db)}/{len(db)} domains; thinking {len(T.split())} words, {sum(len(p.split()) for p in drafting)} of them drafting slotted template text; final templates resembling a draft (similarity >= 0.3): {sum(s >= 0.3 for s in sims)} of {len(sims)}")
