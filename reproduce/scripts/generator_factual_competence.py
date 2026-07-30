#!/usr/bin/env python3
"""G^F_svd as the right-singular-vector loading per generator, mirroring the
evaluator left-vector competence. Procedure: SVD of the verdict matrix; average the
right singular vector v over each generator's instantiations; orient so + = factual
(generating a correct instantiation); L2-normalise over the generators. Bootstrap CIs.
Also: Pearson of subjective G^F (E^F-weighted panel factual mean) vs this loading."""
import json, re, os, statistics as st
from pathlib import Path
import numpy as np
JR=re.compile(r"```json\s*\n(.*?)\n```",re.DOTALL)
M=["claude-opus-4.1","claude-opus-4.5","claude-opus-4.0","claude-sonnet-4","gemini-3.1-pro","gemini-2.5-flash","gpt-4.1-2025-04-14","gpt-4.1-mini","gpt-4.1-nano","gpt-4o","gpt-4o-2024-08-06","gpt-4o-mini"]
FK={"gpt-4.1-2025-04-14":"gpt-41-2025-04-14","gpt-4.1-mini":"gpt-41-mini","gpt-4.1-nano":"gpt-41-nano"}
fk=lambda m:FK.get(m,m);GEN=os.environ["RUNS_GEN"]
# Archetypes 1..5 only. Two submissions (gemini-2.5-flash, gpt-4.1-mini) carry a sixth
# archetype; its five parallel contexts are excluded so the panel stays balanced at 25
# contexts per portfolio -- 11 x 25 = 275 columns -- matching the criterion side.
SCORED_ARCHETYPES=5
def fa(e,t):
    fp=Path(GEN)/f"eval_{fk(e)}_x_{fk(t)}.json"
    if not fp.exists():return None
    try:
        n=json.loads(JR.search(json.load(open(fp))["Messages"][0]["Message"]["Content"]).group(1));n=n["scores"][list(n["scores"])[0]]
        return {(ai,k):v for ai,a in enumerate(n["archetypal_contexts"],1) if ai<=SCORED_ARCHETYPES for k,v in enumerate(a.get("factual_per_pc") or [])}
    except:return None
R={(e,t):fa(e,t) for e in M for t in M if e!=t}
cols=[];meta=[];ci={};V={}
for t in M:
  for e in M:
    if e==t:continue
    d=R.get((e,t))
    if not d:continue
    for key,v in d.items():
      c=(t,)+key
      if c not in ci:ci[c]=len(cols);cols.append(c);meta.append(t)
      V[(e,c)]=1.0 if v<=5 else -1.0
meta=np.array(meta)
def loading(colsel):
    Fm=-np.ones((len(M),len(colsel)))
    for jj,c in enumerate(colsel):
        for e in M:
            if (e,c) in V: Fm[M.index(e),jj]=V[(e,c)]
    Fc=Fm-Fm.mean(1,keepdims=True);U,S,Vt=np.linalg.svd(Fc,full_matrices=False);v=Vt[0,:]
    cm=Fm.mean(0)
    if np.corrcoef(v,cm)[0,1]<0: v=-v        # orient: + = false
    mt=np.array([colsel[j][0] for j in range(len(colsel))])
    gens=[g for g in M if (mt==g).any()]
    fact=np.array([-v[mt==g].mean() for g in gens])   # factuality = -falseness
    fact=fact/np.sqrt((fact**2).sum()); fact=np.clip(fact,0,None)                # L2-normalise over generators
    return dict(zip(gens,fact))
pt=loading(cols)
rng=np.random.default_rng(20260603);B=1000
acc={g:[] for g in pt}
for _ in range(B):
    sel=[cols[i] for i in rng.integers(0,len(cols),len(cols))]
    for g,val in loading(sel).items():
        if g in acc: acc[g].append(val)
from decimal import Decimal,ROUND_HALF_UP
r2=lambda x:float(Decimal(str(x)).quantize(Decimal("0.01"),ROUND_HALF_UP))
print("G^F_svd  (right-vector loading, L2-normalised, + = generates correct):")
print(f"{'Generator':22}{'G^F_svd':>9}   95% CI")
for g in sorted(pt,key=lambda g:-pt[g]):
    v=acc[g];lo,hi=r2(np.percentile(v,2.5)),r2(np.percentile(v,97.5))
    print(f"{g:22}{r2(pt[g]):>9.2f}   [{lo:.2f}, {hi:.2f}]")
# Pearson vs subjective G^F (E^F-weighted panel factual mean)
# build f+ for weights and subjective means
Fm=-np.ones((len(M),len(cols)))
for (e,c),val in V.items():Fm[M.index(e),ci[c]]=val
Fc=Fm-Fm.mean(1,keepdims=True);U,_,_=np.linalg.svd(Fc,full_matrices=False);u=U[:,0]
if u.sum()<0:u=-u
fp=dict(zip(M,np.clip(u,0,None)))
em=lambda e,t:(st.mean(R[(e,t)].values()) if R.get((e,t)) else None)
GFsub={}
for t in M:
    s=[(e,em(e,t)) for e in M if e!=t and em(e,t) is not None]
    w=sum(fp[e] for e,_ in s)
    if s and w>0: GFsub[t]=sum(fp[e]*m for e,m in s)/w
def pear(x,y):
    mx,my=st.mean(x),st.mean(y);da=sum((a-mx)**2 for a in x)**.5;db=sum((b-my)**2 for b in y)**.5
    return sum((a-mx)*(b-my) for a,b in zip(x,y))/(da*db)
C=[g for g in pt if g in GFsub]
print(f"\nPearson( subjective G^F , G^F_svd loading ) = {pear([GFsub[g] for g in C],[pt[g] for g in C]):.3f}  (n={len(C)})")
