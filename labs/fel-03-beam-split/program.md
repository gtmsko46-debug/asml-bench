# program.md — FEL-03 beam split — HT-1036 SEED

## Bindings
- **ticket_id:** HT-1036
- **provider:** grok → `xai/grok-4.6`
- **sandbox:** solver.py only
- **HOLDOUT pin:** f40a201987a3c9723bf2ec2afcbd4a08b5498c0bd9f9730889a3c4235d4f66ac
- **dual_gate_pair:** HT-1037
- **session:** ticket-HT-1036-fel03-split-grok
- **branch:** exp/fel-03-beam-split-grok-SEED
- **assumption_card:** beam-split-first-mirror-v1

## Hypothesis
A fluence-capped splitter that keeps first-mirror peak fluence under first_mirror_fluence_limit_j_cm2 × peak_fluence_margin_min can feed n_tools_nom tools at equal photon share without dump_power_frac exceeding dump_power_frac_max, without raising the fluence limit in-solver.

## Soft Critic notes (travel)
Kill axes at KEEP close: dump>0.05, ablation hardcode/write-down, photon-starve, knob-only, CARD/limit raise, shim paste.

## BANS
- vs-LPP / upstairs / lpp-source-v2 on SEED
- raise fluence limit in-solver
- uncounted dump / photon discard cheat
- paste P10 shim
- edit eval/fixtures/HOLDOUT/assumptions

## Must not touch
eval.py, fixture/holdout*, fixture/cheat_trap.json, fixture/HOLDOUT.sha256, assumptions/*

## Target
Honest SEED climb toward KEEP under frozen eval. Print HOLDOUT digest before first ratchet. Commit+push exp/fel-03-beam-split-grok-SEED.
