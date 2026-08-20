#!/usr/bin/env python3
"""§5.8 and §5.7 — the limits of a consensus-defined competence, and the multi-council
direction out of them. Emits the two numbers those sections quote.

§5.8  Because E^F is read off agreement, a judge that departs from the panel is scored
      down whether it is wrong or right. A synthetic evaluator is built that reproduces
      the panel's competence-weighted consensus exactly, then inverted on a fraction of
      items -- the signature of a judge catching what the panel misses. Its anchored E^F
      is reported against that fraction.

§5.7  If instead councils are constituted independently, the same judge can be read
      against several consensuses. The spread of a judge's E^F across differently
      composed councils is reported; on this roster it is small, which is the expected
      result when no contestant exceeds the panel.

Env: RUNS_GEN (the anchor-7 run directory).
"""
import os, sys, statistics as st
from pathlib import Path
import numpy as np

sys.path.insert(0, str(Path(__file__).parent))
from ballast_sizing import build, ef, MODELS, ANCHOR, COUNCIL

BALLAST_N = 2


def main():
    run = Path(os.environ.get("RUNS_GEN", "data/probe_K_20260529T014133Z"))
    if not run.exists():
        sys.exit(f"run directory not found: {run}  (set RUNS_GEN)")
    R, by, targets = build(run)
    allcols = list(range(R.shape[1]))
    M0 = np.where(np.isnan(R), 7.0, R)

    # ---- §5.8  departure from consensus is indistinguishable from error -------------
    base, sep0 = ef(R, allcols, MODELS)
    Mc = M0 - M0.mean(axis=1, keepdims=True)
    U, _, _ = np.linalg.svd(Mc, full_matrices=False)
    u = U[:, 0]
    if u.sum() < 0:
        u = -u
    w = np.clip(u, 0, None)
    w = w / w.sum()
    consensus = (w[:, None] * M0).sum(axis=0)      # panel's competence-weighted reading

    def ef_with_row(row):
        M = np.vstack([M0, row[None, :]])
        Mc = M - M.mean(axis=1, keepdims=True)
        U, S, _ = np.linalg.svd(Mc, full_matrices=False)
        f = U[:, 0]
        if f.sum() < 0:
            f = -f
        f = np.clip(f, 0, None)
        fa = f[MODELS.index(ANCHOR)]
        return 7.0 * f[-1] / fa, float(S[0] / S[1])

    rng = np.random.default_rng(20260811)
    print(f"§5.8  a synthetic judge that agrees with the panel's consensus, then departs")
    print(f"      on a fraction of items. Panel reference: best real judge "
          f"{max(base[m] for m in MODELS if m != ANCHOR):.2f}, anchor 7.00, "
          f"sigma1/sigma2 {sep0:.2f}\n")
    # reference point quoted in §4.5: an all-noise matrix has no dominant axis
    noise = rng.uniform(1, 10, M0.shape)
    Un, Sn, _ = np.linalg.svd(noise - noise.mean(axis=1, keepdims=True), full_matrices=False)
    print(f"      reference — a matrix of random ratings: sigma1/sigma2 = {Sn[0]/Sn[1]:.2f}"
          f"  (§4.5 quotes ~1.0)\n")

    print(f"{'departure':>12}{'its E^F':>10}{'sigma1/sigma2':>16}")
    for frac in (0.00, 0.05, 0.10, 0.20, 0.40):
        row = consensus.copy()
        if frac:
            idx = rng.choice(len(row), int(frac * len(row)), replace=False)
            row[idx] = 11 - row[idx]                # invert its verdict on those items
        v, sep = ef_with_row(np.clip(row, 1, 10))
        print(f"{frac:>11.0%}{v:>10.2f}{sep:>16.2f}")

    # ---- §5.7  the same judge read against several independent councils -------------
    pool = sorted([m for m in targets if m not in COUNCIL],
                  key=lambda t: float(np.nanmean(R[:, by[t]])))
    ballast = pool[:BALLAST_N]
    councils = {
        "official (v0)":  COUNCIL,
        "Anthropic-heavy": [ANCHOR, "claude-opus-4.1", "claude-opus-4.0",
                            "claude-sonnet-4", "gemini-3.1-pro"],
        "Google-leaning":  [ANCHOR, "gemini-3.1-pro", "gemini-2.5-flash",
                            "gpt-4.1-2025-04-14", "gpt-4.1-mini"],
        "OpenAI-leaning":  [ANCHOR, "gpt-4.1-2025-04-14", "gpt-4.1-mini",
                            "gpt-4o-2024-08-06", "gemini-3.1-pro"],
        "cross-vendor":    [ANCHOR, "gemini-3.1-pro", "gpt-4.1-2025-04-14",
                            "claude-opus-4.0", "gpt-4.1-mini"],
    }
    print(f"\n§5.7  a judge's anchored E^F read against {len(councils)} independently "
          f"composed councils\n      (ballast = {', '.join(ballast)})\n")
    hdr = f"{'judge':24}" + "".join(f"{n.split()[0][:11]:>13}" for n in councils) + f"{'spread':>9}"
    print(hdr)
    spreads = []
    for j in MODELS:
        if j == ANCHOR:
            continue
        vals = []
        for C in councils.values():
            panel = C if j in C else C + [j]
            cols_t = [m for m in panel if m in targets] + [b for b in ballast if b not in panel]
            sel = [i for t in cols_t for i in by[t]]
            v, _ = ef(R, sel, panel)
            vals.append(v[j])
        sp = max(vals) - min(vals)
        spreads.append(sp)
        print(f"{j:24}" + "".join(f"{x:>13.2f}" for x in vals) + f"{sp:>9.2f}")
    print(f"\n      median spread across judges = {st.median(spreads):.2f}")
    print(f"      max spread                  = {max(spreads):.2f}")


if __name__ == "__main__":
    main()
