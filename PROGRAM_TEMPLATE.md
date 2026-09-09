# program.md — lab brief (Diplomat-stamped)

Fill one brief per run. Lasercode attaches this file (`-f program.md`).

## Bindings

- **thesis:** `<id>` (e.g. `th-04-reticle-heat`)
- **assumption_card:** `<card-id>` (exactly one primary card)
- **provider:** `grok` | `mock-mistral` (Diplomat router; do not improvise)
- **sandbox:** single editable path (e.g. `solver.py`)
- **metric:** primary metric name
- **budget:** max ratchets / minutes
- **ticket_id:** `HT-…` when stamped

## Hypothesis (one sentence)

…

## Guards

- …

## Must not touch

- `eval.py`
- `fixture/holdout*`
- `fixture/cheat_trap.json`
- `fixture/HOLDOUT.sha256`
- assumption cards under `assumptions/`

## Cheat-trap / RESET notes

Document when RESET is valid. Holdout hash must still match after RESET.

## Dual-island note

Demos pair this brief's eval with the sibling provider ticket against the same frozen eval. Do not run or present a single-provider demo.
