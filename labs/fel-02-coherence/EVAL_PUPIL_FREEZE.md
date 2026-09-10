# FEL-02 / P2 eval pupil freeze (2026-09-10)

**Owner:** Eval Integrity  
**Authority:** `tickets/IF_SPEC_PUPIL_BOUND.md` (IF Spec Owner)  
**Trigger:** CoS — DUAL-KEEP HT-1011∧HT-1022 stamped; P2 blocked until pupil in frozen KEEP.

## Freeze
`labs/fel-02-coherence/eval.py` KEEP requires **all**:
- holdout mean `speckle` `< 0.15`
- holdout mean `photons_kept` `≥ 0.55` (`PHOTON_FLOOR`)
- holdout mean `pupil_fill_error` `≤ 0.10` (`PUPIL_ERR_MAX`) — **NEW**

HOLDOUT unchanged: `3ed24ec5df80e01a133de535e5d8df0c9ce4f9f10493538f24c2d87c359596f8`

## Non-changes
- Assumption card `coherence-if-v1` / `pupil_fill_target=0.72` untouched
- Fixtures untouched
- Ticket-level `photons_kept==1.0` remains Critic/docket hard where stamped; eval floor stays 0.55 per IF Spec

## P2
Illuminator/P2 feed claims may cite dual-KEEP only under this pupil-gated eval.
