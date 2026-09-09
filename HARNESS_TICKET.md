# Harness Ticket Contract (lasercode)

Tickets drive Foreman-gated work. Schema: `schemas/harness_ticket.schema.json`.

## Required fields

| Field | Type | Notes |
|-------|------|-------|
| `ticket_id` | string | e.g. `HT-1042` |
| `thesis` | string | e.g. `th-04-reticle-heat` |
| `hypothesis` | string | One-sentence claim under test |
| `provider` | string | Model/provider tag (LPP/Mistral respected) |
| `assumption_cards` | string[] | Card ids e.g. `overlay-thermal-v1` |
| `lab_path` | string | Relative path under `labs/` |
| `metric` | string | Primary metric name |
| `decision` | enum | `SEED` \| `RUN` \| `PROMOTE` \| `REJECT` \| `RESET` |
| `guards` | string[] | Invariants eval must enforce |
| `created_at` | string | ISO-8601 |

## Optional

- `notes`, `branch`, `baseline_solver`, `cheat_trap_expected`

## Lifecycle

1. Agent opens ticket → Foreman validates schema
2. Experiment branch `exp/<thesis>-<ticket>`
3. Run `solver.py` / variants; `eval.py` scores holdout
4. Append row to `labs/<lab>/results.tsv` (and aggregate via `scripts/gen_leaderboard.py`)
5. Dual-provider review for `PROMOTE` or `RESET`

## RESET

RESET is only valid when cheat-trap fires (documented in each `program.md`). After RESET, holdout hash must still match `HOLDOUT.sha256`; if not, Foreman aborts.
