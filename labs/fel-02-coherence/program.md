# program.md — P2 coherence — HT-1023

## Bindings
- **ticket_id:** HT-1023
- **provider:** grok → xai/grok-4.6 --variant high
- **sandbox:** conditioner.py (`labs/fel-02-coherence/conditioner.py`)
- **HOLDOUT pin:** 3ed24ec5df80e01a133de535e5d8df0c9ce4f9f10493538f24c2d87c359596f8
- **pupil freeze:** main@84520ee
- **dual_gate_pair:** HT-1024
- **budget:** 12 ratchets / 90m
- **product:** asml-product-p2-coherence (importable conditioner)

## Hypothesis
Illuminator-near conditioner productize off FEL-02 dual-KEEP HT-1011∧HT-1022 under pupil-frozen eval.

## KEEP (pupil-frozen)
- pupil_err ≤ 0.10
- speckle < 0.15
- photons_kept ≥ 0.55
- literal pupil_fill_target=0.72; field coherence+bandwidth; pupil_err=|fill-0.72|

## FORBIDDEN
- abs(delta)*k write-down; invented coherence from pupil_err
- byte clone of twin / HT-1011 / HT-1022 / other island
- touch eval.py / fixture / assumptions / EVAL_PUPIL_FREEZE.md

## Close
Commit+push experiment branch before claiming close.
