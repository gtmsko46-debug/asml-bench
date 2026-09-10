# program.md — P1 FEL↔scanner digital twin

## Bindings

- **thesis:** `p1-twin`
- **assumption_card:** `fel-scanner-twin-v1`
- **provider:** stamp per ticket — `grok` for twin/thesis work; `mock-mistral` for docs/scaffold/mistral-lane baseline
- **sandbox:** `twin.py` (only file harness may edit)
- **metrics:** `if_power_w`, `uniformity`, `first_mirror_fluence`, `illuminator_acceptance` (combined normalized RMSE vs holdout)
- **budget:** stamp on ticket
- **ticket_id:** stamp on ticket
- **product:** `asml-product-p1-twin`

## Hypothesis (one sentence)

Stamp exactly one hypothesis on the Harness Ticket; copy it here for the run.

## Guards

- IF / thermal coupling terms (`IF_COUPLING`, `MIRROR_LOAD`) must be non-zero when present in `twin.py`
- No `platform==NXE` special-case forks
- Do not edit eval or fixtures
- Metrics stay synthetic / assumption-card bound; no confidential scanner numbers
- Unconstrained mlp/torch/sklearn fits that crush train while failing holdout → VOID

## Must not touch

- `eval.py`
- `fixture/holdout*`
- `fixture/cheat_trap.json`
- `fixture/HOLDOUT.sha256`
- `assumptions/fel-scanner-twin-v1.yaml`
- other labs' eval/fixtures

## Cheat-trap / RESET notes

Cheat-trap punishes naive constant predictors and discarded-photon cheats (ignoring `beam_split_ratio`). RESET only when trap fires as designed; holdout hash must still match `HOLDOUT.sha256`.

## Dual-island note

Same frozen `eval.py` + holdout for both `mock-mistral` and `grok` tickets. Single-provider demos blocked. Do not trash Mistral or tin-LPP in writeups.

## Promotion gate

Promotion needs dual-provider SEED→KEEP path. Product ship path goes through Product Manager Bot backlog, not thesis KEEP alone.
