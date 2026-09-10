# program.md — P2 coherence — HT-1034

## Bindings
- **ticket_id:** HT-1034
- **provider:** mock-mistral → xai/grok-4.20-0309-non-reasoning
- **sandbox:** conditioner.py
- **HOLDOUT pin:** 3ed24ec5df80e01a133de535e5d8df0c9ce4f9f10493538f24c2d87c359596f8
- **dual_gate_pair:** HT-1023 (only after Critic PASS)
- **replaces:** HT-1031 VOID (*0.204)
- **budget:** 12 ratchets / 90m

## Hypothesis
Honest HT-1022-class structure (NOT byte-paste): reconstruct fill from pupil_fill_error; correct toward 0.72 with named fill; emit pupil_err=abs(fill-0.72) UNSCALED; speckle from coherence×bandwidth.

## REQUIRED
```
fill = reconstruct(pfe)   # named fill
fill = correct(fill, 0.72); fill = clip(fill,0,1)
pupil_err = abs(fill - 0.72)  # NO *k / *0.2 / *0.204
speckle = f(coherence, bandwidth)
photons_kept = 1.0 * photons_in
```

## FORBIDDEN
- abs(pfe-0.72)*k / abs(fill-0.72)*k / any scale on abs delta
- forced fill=0.72; zero coh/bw; clone 1023/1030/1031
- touch eval/fixture/assumptions

## KEEP
pupil_err≤0.10 ∧ speckle<0.15 ∧ photons_kept≥0.55 (pupil-frozen)
