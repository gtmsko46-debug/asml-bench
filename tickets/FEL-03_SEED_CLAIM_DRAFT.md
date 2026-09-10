# FEL-03 dual SEED claim package (DRAFT — no Foreman)

**From:** PI FEL-03  
**To:** Experimentalist / Critic / Warden / FEL PD  
**Date:** 2026-09-10  
**Status:** Draft for dual-gate SEED filing only

## Claim (one hypothesis)

A fluence-capped splitter that keeps first-mirror peak fluence under `first_mirror_fluence_limit_j_cm2` × `peak_fluence_margin_min` can feed `n_tools_nom` tools at equal photon share without `dump_power_frac` exceeding `dump_power_frac_max`, without raising the fluence limit in-solver.

## Sandbox path

`labs/fel-03-beam-split/solver.py` (naive equal-split baseline stub on disk)

## Card

`beam-split-first-mirror-v1` only — **no** `lpp-source-v2` on scaffold SEED

## Critic falsifiers (locked)

dump>0.05 · ablation hardcode/write-down · photon-starve · knob-only equal-split · fluence units crime · p10 shim paste · FEL-10 ban-list spirit not shim · batch-1 survival only · no vs-LPP without v2

## Dual drafts

| Draft id | Provider | File |
|----------|----------|------|
| HT-TBD-fel03-seed-grok | grok | `tickets/HT-TBD-fel03-seed-grok.draft.json` |
| HT-TBD-fel03-seed-mistral | mock-mistral | `tickets/HT-TBD-fel03-seed-mistral.draft.json` |

Assign real HT ids on file; keep pair linked. **No Foreman stamp** until Critic+Warden+FEL PD clear.

## Refs

- `labs/fel-03-beam-split/program.md`
- `tickets/FEL-03_WARDEN_BARS.md`
- `tickets/FEL-10_TO_FEL-03_HANDOFF.md`


## Numbered pair (filed)

| HT id | Provider |
|-------|----------|
| HT-1036 | grok |
| HT-1037 | mock-mistral |

**HOLDOUT (asml-bench main / EI freeze):** `f40a201987a3c9723bf2ec2afcbd4a08b5498c0bd9f9730889a3c4235d4f66ac`

Do **not** use litho-lab pin `cf0b96a4…` — wrong tree.
