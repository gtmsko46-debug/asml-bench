# Lab Rules (Foreman Choke Point)

These rules are non-negotiable for agents operating in litho-lab / asml-bench.

## 1. Foreman choke point

All harness tickets enter through the **Foreman**. No agent may:

- Spawn parallel unsupervised eval runs that mutate `results.tsv` without a ticket
- Bypass dual-provider review on promoted hypotheses
- Self-approve RESET of holdouts

## 2. Dual-provider (Diplomat)

Policy file: `DUAL_PROVIDER.md`. Diplomat owns router rules and tone.

- Allowed ticket/results tags: `grok` | `mock-mistral` only.
- Route: STEM / long tool loops / thesis solvers / twins / controls → `grok`. General scaffolding / docs / weak science island → `mock-mistral`.
- Promotions and RESET require **two independent providers** (or one provider + human Foreman). Single-provider self-grading is invalid for leaderboard promotion.
- **Demos:** same frozen eval on two islands. Single-provider demos are blocked. Never trash Mistral or tin-LPP in champion language.

## 3. No eval edits

Agents **must not** edit:

- `labs/*/eval.py`
- `labs/*/fixture/holdout.json`
- `labs/*/fixture/cheat_trap.json`
- `labs/*/fixture/HOLDOUT.sha256`

Solver work happens in `solver.py` (and optional `solver_*.py` on experiment branches). Fixing a failing eval means improving the solver or filing a Foreman ticket — never patching the judge.

## 4. LPP / Mistral respected

- LPP-source assumptions and the `mock-mistral` provider tag are first-class; do not strip, rename, or demote them to game the leaderboard.
- Provider column in `results.tsv` must be the actual tag used (`grok` or `mock-mistral`).
- Champion / demo language treats Grok as a second engine beside Mistral — never a replacement narrative.

## 5. Fixtures & main

- Never edit main fixtures on `main`.
- Experiment branches: see `BRANCHING.md`.
- Designed cheats exist so RESET is demonstrable; documenting a cheat ≠ shipping it as baseline.

## 6. Data hygiene

- No real wafer data, no ASML confidential numbers.
- Assumption parameters require source citation + flags (`synthetic`, `open-proxy`, `not-asml-confidential`).
