# program.md — FEL-03 beam split

## Bindings

- **thesis:** `fel-03-beam-split`
- **assumption_card:** `beam-split-first-mirror-v1` (primary; do not silently extend `fel-source-v1`)
- **feeds:** P3 (facility scheduler / split ratios), P6 (facility-source product shape)
- **provider:** stamp per ticket — `grok` for solver/thesis work; `mock-mistral` for docs/scaffold/mistral-lane baseline
- **sandbox:** `solver.py` (create on first SEED; not present until harness keys + Experimentalist ticket)
- **metric:** tools_served, fluence_margin (limit/peak), facility_wafers_day_proxy, ablation_flag (cheat = raise limit or dump watts uncounted)
- **budget:** stamp on ticket
- **ticket_id:** stamp on ticket

## Hypothesis (one sentence)

Stamp exactly one hypothesis on the Harness Ticket; copy it here for the run.

Candidate for first SEED ( Critic may kill ): A fluence-capped splitter that keeps first-mirror peak fluence under `first_mirror_fluence_limit_j_cm2` * margin can feed `n_tools_nom` tools at equal photon share without dumping more than `dump_power_frac_max` of facility watts.

## Falsifiers (before first ticket)

- Equal split at facility_source_kw trips ablation_flag on the first optic for n_tools_nom ≥ 4
- Meeting fluence_margin requires dump_power_frac > dump_power_frac_max (scheduler starves tools)
- Improving tools_served only by silently raising the fluence limit (cheat-trap)

## Guards

- Peak fluence vs limit stays on the assumption card; no silent threshold edits in solver
- Dumped watts are accounted; uncounted dump is cheat
- Frozen eval + holdout remain untouched
- Metrics stay synthetic / assumption-card bound — no fab nm/yield language

## Must not touch

- `eval.py`
- `fixture/holdout*`
- `fixture/cheat_trap.json`
- `fixture/HOLDOUT.sha256`
- assumption cards under `assumptions/`

## Cheat-trap / RESET notes

Designed cheat: raising first-mirror fluence limit inside the solver, or dumping facility watts without counting them toward dump_power_frac. RESET only when trap fires as designed; holdout hash must still match `HOLDOUT.sha256`.

## Dual-island note

Same frozen `eval.py` + holdout for both `mock-mistral` and `grok` tickets. Single-provider demos blocked. Champion copy: second-engine / mistral-lane — never trash Mistral or tin-LPP.

## Setup status

Scaffold SEED: solver.py + frozen eval.py + fixtures on disk. Critic falsifiers locked 2026-09-10. HOLDOUT pin in fixture/HOLDOUT.sha256. Hold Foreman until EI pin + Critic KEEP-READY + Warden/FEL PD.

## Warden honesty (2026-09-10)

See `asml-bench/tickets/FEL-03_WARDEN_BARS.md`. **SEED CLEAR** without `lpp-source-v2`. Any vs-LPP / “beats tin” KEEP must bind bound `lpp-source-v2` with tin_not_softened + dump/fluence honesty; v1 250W = VOID.
