# Dual-Provider Diplomat Policy

Owner: Dual-Provider Diplomat. Do not improvise routing.

Goal: EB can say we added a second engine next to Mistral — not that we replaced it.

## Allowed provider tags (tickets + results.tsv)

| Tag | Use for |
|-----|---------|
| `mock-mistral` | General software, docs, boilerplate, scaffolding, intentionally weak science island |
| `grok` | Science-heavy solvers, long tool loops, twins, controls, thesis code |

No other provider tags on stamped tickets. Reject unknown values.

## Router rules

1. One hypothesis → one provider per ticket. Never two providers on one ticket.
2. Science / STEM / solver / twin / control / thesis code → `grok`.
3. Docs, README, harness glue, boilerplate, weak-island baselines → `mock-mistral`.
4. When unsure, prefer `mock-mistral` for non-science surface area and file a Foreman note — do not silently upgrade to `grok` to “win” the metric.
5. Diplomat policy wins over operator preference.

## Demo contract (non-negotiable)

- Every public or exec demo shows the **same frozen eval** on **two islands**: one `mock-mistral` run and one `grok` run against identical `eval.py` + holdout hash.
- **Single-provider demos are blocked.** No Mistral-only or Grok-only leaderboard slides.
- Tone: never trash Mistral, tin-LPP, or the weak island. Frame as second engine beside Mistral.
- Champion language: no fake nm/yield; metrics stay tied to synthetic fixtures and assumption cards.

## Promotion / RESET

- `PROMOTE` and `RESET` need dual-provider review (both islands, or one island + human Foreman).
- Single-provider self-grading is invalid for leaderboard promotion.

## Where this lives

- This file: lab-wide policy.
- `HARNESS_TICKET.md` + `schemas/harness_ticket.schema.json`: ticket contract.
- Each lab `program.md`: binds one thesis row, one assumption card, and the stamped provider for that run.
