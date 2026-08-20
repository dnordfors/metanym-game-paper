#!/usr/bin/env python3
"""Same-vendor robustness of the key-free factual axis (§5.8 -> a table).

The factual SVD assumes near-independent errors. If the truth axis were really Claude-bloc
agreement, dropping the Anthropic judges would change who the panel calls factual. This script
recomputes the GRADED generator-factuality G^F (Appendix A.2.a) under judge sub-panels with one
vendor's evaluators removed, and reports how much the factual ordering moves.

For each judge set J: build the J x item graded 1-10 factual matrix (self/missing = anchor 7),
row-centre, take the leading left singular vector f (judge competence), and read each generator's
G^F as the competence-weighted consensus of the judges in J other than itself. Compare the G^F
ordering of the generators to the full-panel ordering (Spearman).

Env: RUNS_GEN (anchor-7 run).
"""
import json, re, os, glob, statistics as st, sys
from pathlib import Path
import numpy as np
from scipy.stats import spearmanr

JR = re.compile(r"```json\s*\n(.*?)\n```", re.DOTALL)
MODELS = ["claude-opus-4.1","claude-opus-4.5","claude-opus-4.0","claude-sonnet-4",
          "gemini-3.1-pro","gemini-2.5-flash","gpt-4.1-2025-04-14","gpt-4.1-mini",
          "gpt-4.1-nano","gpt-4o","gpt-4o-2024-08-06","gpt-4o-mini"]
FK={"gpt-4.1-2025-04-14":"gpt-41-2025-04-14","gpt-4.1-mini":"gpt-41-mini","gpt-4.1-nano":"gpt-41-nano"}
def fk(m): return FK.get(m,m)
AM="claude-opus-4.5"
# Archetypes 1..5 only. Two submissions (gemini-2.5-flash, gpt-4.1-mini) carry a sixth
# archetype; its five parallel contexts are excluded so the panel stays balanced at 25
# contexts per portfolio -- 11 x 25 = 275 columns -- matching the criterion side.
SCORED_ARCHETYPES=5
ANTHROPIC={"claude-opus-4.1","claude-opus-4.5","claude-opus-4.0","claude-sonnet-4"}
GOOGLE={"gemini-3.1-pro","gemini-2.5-flash"}
OPENAI={"gpt-4.1-2025-04-14","gpt-4.1-mini","gpt-4.1-nano","gpt-4o","gpt-4o-2024-08-06","gpt-4o-mini"}

def parse(d,ev,tg):
    fp=Path(d)/f"eval_{fk(ev)}_x_{fk(tg)}.json"
    if not fp.exists(): return None
    try:
        node=json.loads(JR.search(json.load(open(fp))["Messages"][0]["Message"]["Content"]).group(1))
        node=node["scores"][list(node["scores"])[0]]
        return {ai:list(a.get("factual_per_pc") or []) for ai,a in enumerate(node["archetypal_contexts"],1)
                if ai<=SCORED_ARCHETYPES}
    except Exception:
        return None

def main():
    gen=os.environ.get("RUNS_GEN")
    if not gen: sys.exit("set RUNS_GEN")
    D={(e,t):parse(gen,e,t) for e in MODELS for t in MODELS}
    targets=[m for m in MODELS if any(D.get((e,m)) for e in MODELS)]
    # union of (target, archetype, pc) columns
    cols=set()
    for t in targets:
        for ev in MODELS:
            rec=D.get((ev,t))
            if rec:
                for ai,fl in rec.items():
                    for pi in range(len(fl)): cols.add((t,ai,pi))
    cols=sorted(cols); cidx={c:i for i,c in enumerate(cols)}
    # raw rating matrix (judge x col), NaN where absent
    R=np.full((len(MODELS),len(cols)),np.nan)
    for si,ev in enumerate(MODELS):
        for t in targets:
            rec=D.get((ev,t))
            if not rec: continue
            for ai,fl in rec.items():
                for pi,v in enumerate(fl):
                    c=(t,ai,pi)
                    if c in cidx: R[si,cidx[c]]=float(v)

    def GF(judge_set):
        idx=[i for i,m in enumerate(MODELS) if m in judge_set]
        M=R[idx,:].copy(); Mraw=M.copy()
        M=np.where(np.isnan(M),7.0,M)                 # self/missing -> anchor 7
        U,_,_=np.linalg.svd(M-M.mean(axis=1,keepdims=True),full_matrices=False)
        f=U[:,0]
        if f.sum()<0: f=-f
        f=np.clip(f,0,None)
        fj=dict(zip([MODELS[i] for i in idx],f))
        out={}
        for t in targets:
            if t==AM: out[t]=7.0; continue
            num=den=0.0
            for k,i in enumerate(idx):
                ev=MODELS[i]
                if ev==t: continue
                rs=[Mraw[k,cidx[c]] for c in cols if c[0]==t and not np.isnan(Mraw[k,cidx[c]])]
                if not rs: continue
                den+=f[k]; num+=f[k]*st.mean(rs)
            out[t]=num/den if den>0 else np.nan
        return out

    variants=[("full panel (12 judges)", set(MODELS)),
              ("drop Anthropic judges", set(MODELS)-ANTHROPIC),
              ("drop Google judges", set(MODELS)-GOOGLE),
              ("drop OpenAI judges", set(MODELS)-OPENAI),
              ("Claude-free (Google+OpenAI)", GOOGLE|OPENAI)]
    full=GF(set(MODELS))
    order=[m for m in sorted(targets,key=lambda m:-full[m])]
    print(f"{'generator':22}" + "".join(f"{v[0].split(' (')[0][:11]:>13}" for v in variants))
    res={}
    for name,js in variants: res[name]=GF(js)
    for m in order:
        print(f"{m:22}" + "".join(f"{res[n].get(m,float('nan')):>13.2f}" for n,_ in variants))
    print("\nSpearman of G^F ordering vs full panel (over the 11 generators):")
    base=[full[m] for m in targets]
    for name,js in variants:
        v=[res[name][m] for m in targets]
        rho=spearmanr(base,v).correlation
        print(f"  {name:30} rho = {rho:.3f}")
    # council-vs-inert cut: do the GPT-4o family stay at the bottom under every panel?
    inert={"gpt-4o","gpt-4o-mini","gpt-4.1-nano"}
    print("\nInert-band check (GPT-4o family + nano should stay lowest under every panel):")
    for name,js in variants:
        ranked=sorted(targets,key=lambda m:-res[name][m])
        bottom3=set(ranked[-3:])
        print(f"  {name:30} bottom-3 = {sorted(bottom3)}")

if __name__=="__main__":
    main()
