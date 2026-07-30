#!/usr/bin/env python3
"""Generation-factuality validation (soft SVD), following Appendix A.2.a EXACTLY.

The factual ratings are used directly on the 1-10 scale -- NO binarisation. We build
the evaluator x instantiation matrix F (A5, self/missing entries = anchor 7), row-centre
it (A6), take the leading SVD triple, read evaluator factual competence off the left
vector f (A7) and the competence-weighted consensus instantiation rating off the right
vector v (A8), and average per generator for G^F_svd (A9). Three generator measures over
the same anchored factual scores (anchor 7, RUNS_GEN):

  G^F      (equal)        = full-panel equal-weight leave-self-out mean of the soft scores
  G^F'     (E^F-weighted) = full-panel mean weighted by evaluator competence f+ (= E^F_svd)
  G^F_svd  (A8-A9)        = competence-weighted consensus rating C + kappa*v, per generator

Reported with Pearson r only. Env: RUNS_GEN (anchor-7 generation run).
"""
import json, re, os, statistics as st
from pathlib import Path
import numpy as np

JR = re.compile(r"```json\s*\n(.*?)\n```", re.DOTALL)
MODELS = ["claude-opus-4.1","claude-opus-4.5","claude-opus-4.0","claude-sonnet-4","gemini-3.1-pro",
 "gemini-2.5-flash","gpt-4.1-2025-04-14","gpt-4.1-mini","gpt-4.1-nano","gpt-4o","gpt-4o-2024-08-06","gpt-4o-mini"]
FK = {"gpt-4.1-2025-04-14":"gpt-41-2025-04-14","gpt-4.1-mini":"gpt-41-mini","gpt-4.1-nano":"gpt-41-nano"}
def fk(m): return FK.get(m, m)
GEN = os.environ["RUNS_GEN"]
ANCHOR = 7.0
ANCHOR_MODEL = "claude-opus-4.5"   # the reference portfolio; ungraded as a generator
# Archetypes 1..5 only. Two submissions (gemini-2.5-flash, gpt-4.1-mini) carry a sixth
# archetype; its five parallel contexts are excluded so the panel stays balanced at 25
# contexts per portfolio -- 11 x 25 = 275 columns -- matching the criterion side, which
# is built over archetypes 1..5 throughout.
SCORED_ARCHETYPES = 5

def facts(ev, tg):
    fp = Path(GEN)/f"eval_{fk(ev)}_x_{fk(tg)}.json"
    if not fp.exists(): return None
    try:
        n = json.loads(JR.search(json.load(open(fp))["Messages"][0]["Message"]["Content"]).group(1))
        n = n["scores"][list(n["scores"])[0]]
        return {(ai,k): v for ai,a in enumerate(n["archetypal_contexts"],1) if ai<=SCORED_ARCHETYPES
                for k,v in enumerate(a.get("factual_per_pc") or [])}
    except Exception:
        return None

R = {(e,t): facts(e,t) for e in MODELS for t in MODELS if e != t}
R = {k:v for k,v in R.items() if v}

# instantiation columns (each carries its generator)
cols=[]; cidx={}; gen_of=[]
for tg in MODELS:
    for ev in MODELS:
        if ev==tg or (ev,tg) not in R: continue
        for key in R[(ev,tg)]:
            c=(tg,)+key
            if c not in cidx: cidx[c]=len(cols); cols.append(c); gen_of.append(tg)
gen_of=np.array(gen_of)
mi={m:i for i,m in enumerate(MODELS)}

def svd_triplet(colsel, ref=None):
    """A5-A7: build F (soft, fill=anchor), row-centre, leading SVD triple.
    Returns f, f+, oriented v, sigma1, rowmean. If ref (full-sample f) is given,
    lock onto the competence axis (the component best matching ref) and align its
    sign to ref, so bootstrap replicates track the same axis (no component/sign swap)."""
    ci={c:j for j,c in enumerate(colsel)}
    F=np.full((len(MODELS),len(colsel)),ANCHOR)        # A5: self/missing entries = anchor 7
    for (ev,tg),d in R.items():
        for key,val in d.items():
            c=(tg,)+key
            if c in ci: F[mi[ev],ci[c]]=float(val)
    rowmean=F.mean(1)
    Fc=F-rowmean[:,None]                                # A6: row-centre
    U,S,Vt=np.linalg.svd(Fc,full_matrices=False)
    if ref is None:
        k=0
        u=U[:,0]; v=Vt[0,:]; s1=S[0]
        if u.sum()<0: u=-u; v=-v                        # A7: sign so sum_s f_s > 0
    else:                                               # lock to the competence axis matching ref
        k=max(range(min(3,U.shape[1])), key=lambda j:abs(np.corrcoef(U[:,j],ref)[0,1]))
        u=U[:,k]; v=Vt[k,:]; s1=S[k]
        if np.corrcoef(u,ref)[0,1]<0: u=-u; v=-v
    fpos=np.clip(u,0,None)                              # f+ = max(f,0)
    if np.corrcoef(v,Fc.mean(0))[0,1]<0: v=-v           # orient v: positive = factually stronger
    return u, fpos, v, s1, rowmean

f, fpos, v, s1, rowmean = svd_triplet(cols)
EF = dict(zip(MODELS, fpos))                            # E^F_svd (raw loading, clipped)

# full-sample top-2 left subspace, for Procrustes-aligned bootstrap (the leading axis is
# near-degenerate between the Anthropic and Google blocs, so a single-vector bootstrap swaps)
def centered(colsel):
    cix={c:j for j,c in enumerate(colsel)}
    Fm=np.full((len(MODELS),len(colsel)),ANCHOR)
    for (ev,tg),d in R.items():
        for key,val in d.items():
            c=(tg,)+key
            if c in cix: Fm[mi[ev],cix[c]]=float(val)
    return Fm-Fm.mean(1,keepdims=True)
U0,_,_=np.linalg.svd(centered(cols),full_matrices=False); ref2=U0[:,:2]

# A8: competence-weighted consensus rating  r_hat_j = C + kappa * v_j
W=fpos.sum()
C   = float((fpos*rowmean).sum()/W)
kap = float(s1*(fpos*f).sum()/W)
rhat = C + kap*v
# A9: G^F_svd per generator (opus-4.5 is the reference, ungraded)
gens=[g for g in MODELS if (gen_of==g).any() and g!=ANCHOR_MODEL]
GFsvd={g: float(rhat[gen_of==g].mean()) for g in gens}

# subjective generator factuality on the soft scale
def evmean(ev,tg):
    d=R.get((ev,tg)); return st.mean(d.values()) if d else None
GFeq={}; GFwt={}
for tg in gens:
    soft=[(ev,evmean(ev,tg)) for ev in MODELS if ev!=tg and evmean(ev,tg) is not None]
    GFeq[tg]=st.mean([m for _,m in soft])              # G^F  (equal weight)
    w=sum(EF[ev] for ev,_ in soft)
    GFwt[tg]=sum(EF[ev]*m for ev,m in soft)/w          # G^F' (E^F-weighted)

# E^F_svd CI: resample columns, recompute the SVD, align the top-2 left subspace to the
#   full-sample one by 2-component Procrustes, read off the aligned leading loading.
# G^F_svd CI: resample each generator's own instantiation ratings (A.5 unit), holding
#   the panel consensus (C, kappa, v) fixed -- the dominant source of a generator's
#   uncertainty is the spread of its own instantiations.
rng=np.random.default_rng(20260606); B=1000
accEF={m:[] for m in MODELS}; accGF={g:[] for g in gens}
for _ in range(B):
    sel=[cols[i] for i in rng.integers(0,len(cols),len(cols))]
    Ub=np.linalg.svd(centered(sel),full_matrices=False)[0][:,:2]
    Uu,_,Vt2=np.linalg.svd(ref2.T@Ub); fb=(Ub@(Vt2.T@Uu.T))[:,0]   # Procrustes-aligned leading vector
    if np.corrcoef(fb,f)[0,1]<0: fb=-fb
    for i,m in enumerate(MODELS): accEF[m].append(np.clip(fb[i],0,None))
rhat_by_gen={g: rhat[gen_of==g] for g in gens}
for _ in range(B):
    for g in gens:
        a=rhat_by_gen[g]
        accGF[g].append(float(a[rng.integers(0,len(a),len(a))].mean()))
from decimal import Decimal, ROUND_HALF_UP
r2=lambda x:float(Decimal(str(x)).quantize(Decimal("0.01"),ROUND_HALF_UP))
def ci(a): return r2(np.percentile(a,2.5)), r2(np.percentile(a,97.5))

def pearson(x,y):
    mx,my=st.mean(x),st.mean(y)
    da=sum((a-mx)**2 for a in x)**.5; db=sum((b-my)**2 for b in y)**.5
    return sum((a-mx)*(b-my) for a,b in zip(x,y))/(da*db)

print(f"E^F_svd (left singular vector f+, clipped)   anchor={int(ANCHOR)}, columns={len(cols)}")
print(f"{'evaluator':22}{'E^F_svd':>9}   95% CI")
for m in sorted(MODELS,key=lambda m:-EF[m]):
    lo,hi=ci(accEF[m]); print(f"{m:22}{r2(EF[m]):>9.2f}   [{lo:.2f}, {hi:.2f}]")

print(f"\nGenerator factuality on the 1-10 scale   (C={C:.2f}, kappa={kap:.2f})")
print(f"{'generator':22}{'G^F':>7}{'G^F-prime':>11}{'G^F_svd':>9}   G^F_svd 95% CI")
for g in sorted(gens,key=lambda g:-GFsvd[g]):
    lo,hi=ci(accGF[g])
    print(f"{g:22}{GFeq[g]:>7.2f}{GFwt[g]:>11.2f}{GFsvd[g]:>9.2f}   [{lo:.2f}, {hi:.2f}]")

print(f"\nPearson r (n={len(gens)}):")
print(f"  G^F (equal)  vs  G^F' (E^F-weighted) : {pearson([GFeq[g] for g in gens],[GFwt[g] for g in gens]):.3f}")
print(f"  G^F' (E^F-weighted) vs G^F_svd       : {pearson([GFwt[g] for g in gens],[GFsvd[g] for g in gens]):.3f}")
print(f"  G^F (equal)  vs  G^F_svd             : {pearson([GFeq[g] for g in gens],[GFsvd[g] for g in gens]):.3f}")

# --- emit the §4.3 Criterion-A table (E^F, G^F + CIs) as CSV for downstream figures (Fig 1) ---
import os as _os
_dd = _os.path.join(_os.path.dirname(_os.path.dirname(_os.path.abspath(__file__))), "data")
_fa = EF[ANCHOR_MODEL]                                    # anchor loading -> anchored E^F = 7f/f_a (1-10)
with open(_os.path.join(_dd, "criterion_a_ef_gf.csv"), "w") as _f:
    _f.write("model,ef,ef_lo,ef_hi,gf,gf_lo,gf_hi\n")
    for g in gens:
        elo, ehi = ci(accEF[g]); glo, ghi = ci(accGF[g])
        _f.write(f"{g},{r2(7*EF[g]/_fa)},{r2(7*elo/_fa)},{r2(7*ehi/_fa)},{r2(GFsvd[g])},{glo},{ghi}\n")
print("wrote", _os.path.join(_dd, "criterion_a_ef_gf.csv"))
