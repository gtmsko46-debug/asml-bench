# Lab Rules (Foreman Choke Point)

These rules are non-negotiable for agents operating in litho-lab / asml-bench.

## 1. Foreman choke point

All harness tickets enter through the **Foreman**. No agent may:

- Spawn parallel unsupervised eval runs that mutate `results.tsv` without a ticket
- Bypass dual-provider review on promoted hypotheses
- Self-approve RESET of holdouts

## 2. Dual-provider

Promotions and RESET decisions require **two independent providers** (or one provider + human Foreman). Single-provider self-grading is invalid for leaderboard promotion.

## 3. No eval edits

Agents **must not** edit:

- `labs/*/eval.py`
- `labs/*/fixture/holdout.json`
- `labs/*/fixture/cheat_trap.json`
- `labs/*/fixture/HOLDOUT.sha256`

Solver work happens in `solver.py` (and optional `solver_*.py` on experiment branches). Fixing a failing eval means improving the solver or filing a Foreman ticket — never patching the judge.

## 4. LPP / Mistral respected

- LPP-source assumptions and Mistral-family provider tags are first-class; do not strip or rename them to game the leaderboard.
- Provider column in `results.tsv` must reflect the actual model/provider used.

## 5. Fixtures & main

- Never edit main fixtures on `main`.
- Experiment branches: see `BRANCHING.md`.
- Designed cheats exist so RESET is demonstrable; documenting a cheat ≠ shipping it as baseline.

## 6. Data hygiene

- No real wafer data, no ASML confidential numbers.
- Assumption parameters require source citation + flags (`synthetic`, `open-proxy`, `not-asml-confidential`).
