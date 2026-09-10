# program.md — FEL-10 IF ownership

## Bindings

- **thesis:** `fel-10-if-ownership`
- **assumption_cards:** `coherence-if-v1`, `fel-source-v1`, `imaging-optics-v1`, `fel-scanner-twin-v1`
- **sandbox:** `shim.py`
- **metric:** `if_compat_score` (soft rank only — see `tickets/IF_SPEC_FEL10_CONTRACT.md`)
- **contract:** `tickets/IF_SPEC_FEL10_CONTRACT.md`

## Must not touch

- `eval.py`
- `fixture/holdout*`
- `fixture/cheat_trap.json`
- `fixture/HOLDOUT.sha256`
- `assumptions/*`
