# Harness Ticket Contract (lasercode)

Tickets drive Foreman-gated work. Schema: `schemas/harness_ticket.schema.json`.
Provider routing: `DUAL_PROVIDER.md` (Diplomat owns it).

## Required fields

| Field | Type | Notes |
|-------|------|-------|
| `ticket_id` | string | e.g. `HT-1042` |
| `thesis` | string | e.g. `th-04-reticle-heat` |
| `hypothesis` | string | One-sentence claim under test |
| `provider` | enum | `grok` \| `mock-mistral` only (see Diplomat router) |
| `assumption_cards` | string[] | Card ids e.g. `overlay-thermal-v1` |
| `lab_path` | string | Relative path under `labs/` |
| `sandbox` | string | Single editable file under the lab (e.g. `solver.py`) |
| `metric` | string | Primary metric name |
| `budget` | string | Max ratchets / minutes |
| `must_not_touch` | string[] | Always includes `eval.py`, `fixture/holdout*`, assumption cards |
| `decision` | enum | `SEED` \| `RUN` \| `PROMOTE` \| `REJECT` \| `RESET` |
| `guards` | string[] | Invariants eval must enforce |
| `created_at` | string | ISO-8601 |

## Optional

- `notes`, `branch`, `baseline_solver`, `cheat_trap_expected`

## Provider routing (Diplomat)

| Provider | Route |
|----------|-------|
| `mock-mistral` | General software, docs, boilerplate, scaffolding, weak science island |
| `grok` | Science-heavy solvers, long tool loops, twins, controls, thesis code |

Reject tickets with unknown provider, two hypotheses, eval edits, or missing `sandbox`.

## Lifecycle

1. Agent opens ticket → Foreman validates schema + Diplomat provider enum
2. Experiment branch `exp/<thesis>-<ticket>`
3. Confirm lab `program.md` points at one backlog/thesis row, one assumption card, and this ticket's provider
4. Run sandbox only; frozen `eval.py` scores holdout
5. Append row to `labs/<lab>/results.tsv` (and aggregate via `scripts/gen_leaderboard.py`)
6. Dual-provider review for `PROMOTE` or `RESET` — same frozen eval on both islands for demos

## Demo gate

Single-provider demos are blocked. Show identical holdout/`eval.py` under both `mock-mistral` and `grok`. Do not trash Mistral in champion language.

## RESET

RESET is only valid when cheat-trap fires (documented in each `program.md`). After RESET, holdout hash must still match `HOLDOUT.sha256`; if not, Foreman aborts.
