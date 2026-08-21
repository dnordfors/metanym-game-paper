#!/usr/bin/env bash
# Reproduce every table and figure in the paper from the pinned evaluation data in ./data.
# Deterministic, no API (Levels 2-3 of "reproduce"). Each step names the paper exhibit it makes;
# all runs are pinned from experiment papers/v3/experiments/17_bold_api_probe.
# Level 1 (full LLM re-run, N+=1, budget-gated, non-deterministic) is NOT this script.
set -euo pipefail
cd "$(dirname "$0")"

# Pick an interpreter that can actually import the analysis dependencies. After
# `conda activate metanym-game` the bare name `python3` may still resolve to a system
# interpreter outside the environment, so the active environment's own python is tried
# before the bare names. An explicitly set $PYTHON is used as given, never substituted.
has_deps() { "$1" -c 'import numpy, scipy, matplotlib' >/dev/null 2>&1; }

no_interpreter() {
  echo "ERROR: '$1' cannot import numpy, scipy and matplotlib." >&2
  echo "  Create the environment:  conda env create -f environment.yml && conda activate metanym-game" >&2
  echo "  Or select an interpreter: PYTHON=/path/to/python bash reproduce.sh" >&2
  exit 1
}

if [ -n "${PYTHON:-}" ]; then
  PY="$PYTHON"
  has_deps "$PY" || no_interpreter "$PY"
else
  CANDIDATES=()
  if [ -n "${CONDA_PREFIX:-}" ]; then CANDIDATES+=("$CONDA_PREFIX/bin/python"); fi
  CANDIDATES+=(python3 python)
  PY=""
  for cand in "${CANDIDATES[@]}"; do
    if command -v "$cand" >/dev/null 2>&1 && has_deps "$cand"; then PY="$cand"; break; fi
  done
  [ -n "$PY" ] || no_interpreter "python3"
fi

export RUNS_GEN="data/probe_K_20260529T014133Z"     # run 1 (bootstrap) -> published leaderboard
export RUNS_SWEEP="data"                             # parent of probe_K_anchor{5,6,8}
export RUNS="data"                                   # anchor sweep parent (criterion B / anchor sweep)
export RUNS_UNANCHORED="data/probe_J_20260529T005230Z"  # un-anchored run, all twelve participants (§4.1)
REGEN2="data/regenerations/probe_K_anchor7_20260619T015828Z"   # run 2 (§4.9)
REGEN3="data/regenerations/probe_K_anchor7_20260619T040659Z"   # run 3 (§4.9)

echo "##### §4.1 — un-anchored leaderboard and the one break #####"
"$PY" scripts/section_4_1_unanchored.py              # emits data/section_4_1_unanchored.csv
echo; echo "##### §4.2 factual competence — E^F + G^F #####"
"$PY" scripts/generation_factuality_validation.py        # emits data/criterion_a_ef_gf.csv
echo; echo "##### §4.2 — generator G^F_svd (spectral) #####"
"$PY" scripts/generator_factual_competence.py
echo; echo "##### §4.4 rating consistency — per-axis ρ + council ρ̄ 95% CI #####"
"$PY" scripts/criterion_b_stability.py   # cross-checks build_paper1_tables.py
echo; echo "##### §4.4 — alignment cos(G,E) 95% CI #####"
"$PY" scripts/alignment_cosine.py
echo; echo "##### §4.2 — same-vendor robustness #####"
"$PY" scripts/vendor_robustness.py
echo; echo "##### §4.2/§5.7 — graded-vs-binary SVD #####"
RUNS="$RUNS_GEN" "$PY" scripts/graded_vs_binary_svd.py   # RUNS = the anchor-7 run dir here
echo; echo "##### §4.4 exhibits + §4.7 total T and official leaderboard #####"
"$PY" scripts/build_paper1_tables.py                     # emits data/total_rating_leaderboard.csv
                                                         #   and data/section_4_4_criterion_b.csv
echo; echo "##### §4.7 — total T 95% joint bootstrap CI (A.5) #####"
"$PY" scripts/bootstrap_total.py      # emits data/total_rating_bootstrap.csv
echo; echo "##### §5.7 — leaderboard across the anchor sweep (N=4) #####"
"$PY" scripts/anchor_sweep_leaderboard.py
echo; echo "##### §4.8 + Appendix D — GPQA exhibits and audit #####"
"$PY" scripts/combined_factual_bootstrap.py              # emits data/combined_factual_bootstrap.csv (fig 1 x-bars)
"$PY" scripts/gpqa_audit.py                              # Appendix D: 6 hard-fail checks on the raw GPQA artifacts
"$PY" scripts/t_gpqa_ladder.py                           # Appendix D.1: ladder/compounds/regimes/bases/per-run
"$PY" scripts/slope_full_bootstrap.py                    # Appendix D.1: slope/r under propagated measurement error
"$PY" scripts/plot_total_validation.py                   # -> figures/total_validation.png (the 4.8 figure, T vs GPQA)
"$PY" scripts/plot_anchoring_resolution.py               # -> figures/anchoring_resolution.png (the 4.2 figure + both F values)
"$PY" scripts/plot_council_evaluation.py                # -> figures/council_evaluation_pc1.png (the 3.2 exhibit, verbatim from Appendix C)
echo; echo "##### §4.9 — robustness to regeneration (N=3) #####"
"$PY" scripts/compare_runs.py "$RUNS_GEN" "$REGEN2" "$REGEN3" --sweep "$RUNS_SWEEP"
echo; echo "##### §4.6 — sizing the ballast (why two) #####"
"$PY" scripts/ballast_sizing.py
"$PY" scripts/plot_ballast_heatmap.py                   # -> figures/ballast_heatmap.png (the 4.6 exhibit)
echo; echo "##### §5.6 / §5.7 — consensus limits and the multi-council reading #####"
"$PY" scripts/consensus_limits.py
echo; echo "##### manuscript consistency checks #####"
"$PY" scripts/check_manuscript.py
echo; echo "##### reproduce.sh complete #####"
