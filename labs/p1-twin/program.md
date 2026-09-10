# program.md — P1 twin — HT-1025

## Bindings
- **ticket_id:** HT-1025
- **session:** ticket-HT-1016-p1-deepen-mistral-r3 (NOT -r2)
- **provider:** mock-mistral → xai/grok-4.20-0309-non-reasoning
- **sandbox:** twin.py (`labs/p1-twin/twin.py`)
- **HOLDOUT pin:** 2c398448a78b496b871794ad27d644d7a14b174426b538f1af7807f75bcc603c
- **dual_gate_pair:** HT-1015
- **replaces:** HT-1020 (VOID comment-fork)
- **budget:** 12 ratchets / 90m
- **start:** fresh SEED (not HT-1015 paste); twin.py.1015ref reference only

## Hypothesis
Independent mock-mistral twin with executable coef/structure change on HOLDOUT 2c398448 that clears holdout_nrmse<0.30 and trap_nrmse>holdout+0.05 with holdout prediction vector materially different from HT-1015 (max abs diff > 1e-3) — not a comment/sha-only fork or metric paste.

## KEEP bar
- holdout_nrmse < 0.30
- trap_nrmse > holdout + 0.05
- IF_COUPLING & MIRROR_LOAD nonzero
- max abs pred diff vs HT-1015 > 1e-3 (`python3 /workspace/tmp/check-pred-diff-vs-1015.py`)

## VOID if
- preds ≈ HT-1015 (diff ≤1e-3)
- comment-only fork
- truth_v2 / gen_fixtures.truth clone
- restart 1016 / reuse r2 / paste 1015 twin

## Must not touch
eval.py, fixture/*, assumptions/*, gen_fixtures.py
