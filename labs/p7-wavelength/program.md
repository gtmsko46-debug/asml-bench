# program.md — P7 wavelength-agile computational lithography (13.5 → 6.x)

## Bindings

- **thesis feeds:** `fel-07-wavelength-6x` (primary); shares Critics with `th-01-inverse-litho`, `th-03-overlay-commonality`
- **assumption_card:** `imaging-optics-v1` (primary); pair resist terms from `stochastics-resist-v1` only when ticket lists both
- **provider:** stamp per ticket — `grok` for solver/thesis work; `mock-mistral` for docs/scaffold/weak-island baseline
- **sandbox:** `solver.py`
- **metric:** process-window under frozen 6.x fixture vs 13.5 baseline; honest “6.7 is not free” outcomes allowed
- **budget:** stamp on ticket
- **ticket_id:** stamp on ticket
- **product:** `asml-product-p4-complitho`

## Hypothesis (one sentence)

Stamp exactly one hypothesis on the Harness Ticket; copy it here for the run.

## Guards

- Optics + resist toys must stay honest; no free nm from wavelength alone
- Frozen eval + holdout remain untouched
- Metrics stay synthetic / assumption-card bound; no confidential scanner numbers
- Commonality: do not fork a one-off 6.x-only software path that Applications would not recognize

## Must not touch

- `eval.py`
- `fixture/holdout*`
- `fixture/cheat_trap.json`
- `fixture/HOLDOUT.sha256`
- assumption cards under `assumptions/`

## Cheat-trap / RESET notes

Likely cheat: claiming a 6.x win by weakening multilayer/resist physics or discarding dose. RESET only when trap fires as designed; holdout hash must still match `HOLDOUT.sha256`.

## Dual-island note

Same frozen `eval.py` + holdout for both `mock-mistral` and `grok` tickets. Single-provider demos blocked. Do not trash Mistral or tin-LPP in writeups.

## Promotion gate

Promotion needs BugBot + commonality review (shared Critic posture with TH-01 / TH-03). Product ship path goes through Product Manager Bot backlog, not thesis KEEP alone.
