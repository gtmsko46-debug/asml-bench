# program.md — P4 polarization-aware computational lithography

## Bindings

- **thesis feeds:** `fel-04-polarization` (primary); shares Critics with `th-01-inverse-litho`, `th-03-overlay-commonality`
- **assumption_card:** `imaging-optics-v1` (primary); bind `commonality-v1` when testing NA-agnostic software shape
- **provider:** stamp per ticket — `grok` for solver/thesis work; `mock-mistral` for docs/scaffold/weak-island baseline
- **sandbox:** `solver.py`
- **metric:** process-window area proxy + EPE proxy vs unpolarized LPP baseline fixture
- **budget:** stamp on ticket
- **ticket_id:** stamp on ticket
- **product:** `asml-product-p4-complitho`

## Hypothesis (one sentence)

Stamp exactly one hypothesis on the Harness Ticket; copy it here for the run.

## Guards

- Do not special-case a single NA to win the metric (commonality / BugBot gate)
- Frozen eval + holdout remain untouched
- Metrics stay synthetic / assumption-card bound; no confidential scanner numbers
- Polarization treated as first-class imaging input, not a post-hoc scale factor

## Must not touch

- `eval.py`
- `fixture/holdout*`
- `fixture/cheat_trap.json`
- `fixture/HOLDOUT.sha256`
- assumption cards under `assumptions/`

## Cheat-trap / RESET notes

Likely cheat: NA-specific hardcode or ignoring polarization Jones terms while claiming a polarized win. RESET only when trap fires as designed; holdout hash must still match `HOLDOUT.sha256`.

## Dual-island note

Same frozen `eval.py` + holdout for both `mock-mistral` and `grok` tickets. Single-provider demos blocked. Do not trash Mistral or tin-LPP in writeups.

## Promotion gate

Promotion needs BugBot + commonality review (shared Critic posture with TH-01 / TH-03). Product ship path goes through Product Manager Bot backlog, not thesis KEEP alone.
