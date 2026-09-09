# program.md — TH-04 reticle heat

## Bindings

- **thesis:** `th-04-reticle-heat`
- **assumption_card:** `overlay-thermal-v1`
- **provider:** stamp per ticket — `grok` for solver/thesis work; `mock-mistral` for docs/scaffold/weak-island baseline
- **sandbox:** `solver.py`
- **metric:** holdout RMSE (synthetic-nm); thermal term must be non-zero
- **budget:** stamp on ticket
- **ticket_id:** stamp on ticket

## Hypothesis (one sentence)

Stamp exactly one hypothesis on the Harness Ticket; copy it here for the run.

## Guards

- Thermal contribution to overlay residual is non-zero on holdout
- No `platform==NXE` special-case forks
- Do not edit eval or fixtures

## Must not touch

- `eval.py`
- `fixture/holdout*`
- `fixture/cheat_trap.json`
- `fixture/HOLDOUT.sha256`
- `assumptions/overlay-thermal-v1.yaml`

## Cheat-trap / RESET notes

Cheat-trap documents designed failures (see `fixture/cheat_trap.json`). RESET only when trap fires as designed; holdout hash must still match `HOLDOUT.sha256`.

## Dual-island note

Same frozen `eval.py` + holdout for both `mock-mistral` and `grok` tickets. Single-provider demos blocked. Do not trash Mistral in writeups.
