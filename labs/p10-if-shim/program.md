# program.md — FEL-10 IF shim — HT-1028 KEEP climb

## Bindings
- **ticket_id:** HT-1028
- **provider:** grok → xai/grok-4.6 [--variant high]
- **sandbox:** shim.py only
- **HOLDOUT pin:** d0dc1f8a7b8cc97ddd00122fb4156252c7642a09a7f0ae5102b939747c6cc5be
- **dual_gate_pair:** HT-1033 (Critic formal KEEP PASS)
- **session:** ticket-HT-1028-fel10-shim-grok-keep-r4

## Hypothesis
Reconstruct fill from coherence/bandwidth/power ONLY (never field pupil_fill_error). Correct toward 0.72 with named fill += gain*(0.72-fill). Emit pupil_err=|fill-0.72| unscaled. Field-derived pol/pulse/pointing. photons_kept=1.0 HARD.

## BANS
- pupil_in / field['pupil_fill_error'] as fill source
- pupil_in − k / PUPIL_CORRECT
- abs(delta)*k write-down
- hardcode pupil_err=0
- forced fill=0.72 constant

## Target
pupil_err ≤ 0.10 on holdout with photons=1.0 → KEEP candidate for dual with HT-1033.
You MUST edit shim.py before exit (add correct-toward-0.72 gain step and tune). Unchanged SEED = FAIL.
