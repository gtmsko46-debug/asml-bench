# Litho Lab Go-Live — Champion Orders

**Account:** `gtmsko46-debug` only  
**Nervous system:** Issues + labels + milestones on [`asml-bench`](https://github.com/gtmsko46-debug/asml-bench)  
**Date:** 2026-09-10  

Projects (v2) board blocked on missing `project`/`read:project` scopes — see `PROJECTS.md` for `gh auth refresh -s read:project,project`.

## Champion orders (P0)

### 1. Product factory SDLC (P1 twin P0)

Stand up P1 FEL↔scanner digital twin as the first product-factory build.

| Island | Issue | Provider | Model |
|--------|-------|----------|-------|
| STEM scaffold | [#18](https://github.com/gtmsko46-debug/asml-bench/issues/18) Twin v0 scaffold | `grok` | xai/grok-4.6 (+high) |
| Docs/boilerplate | [#19](https://github.com/gtmsko46-debug/asml-bench/issues/19) Twin docs/boilerplate | `mock-mistral` | mistral/mistral-large-latest |

- Product repo: `asml-product-p1-twin`
- Labels: `track:product`, `product:p1-twin`, `dual-gate`, `stage:spec`
- Milestone: Spec → Build → Review → Ship → Done
- Related backlog placeholder: [#4](https://github.com/gtmsko46-debug/asml-bench/issues/4)

### 2. FEL dual-gate hill-climb (research KEEP gate)

Every research **KEEP** needs **both** islands: `provider=grok` **and** `provider=mock-mistral` on the same frozen `eval.py` + holdout. Single-provider demos are blocked. Do not trash Mistral in champion language.

| Thesis | Issue | Paired tickets |
|--------|-------|----------------|
| TH-04 reticle heat | [#20](https://github.com/gtmsko46-debug/asml-bench/issues/20) | HT-TH04-B1-GROK + HT-TH04-B1-MISTRAL |
| FEL-02 coherence | [#21](https://github.com/gtmsko46-debug/asml-bench/issues/21) | HT-FEL02-B1-GROK + HT-FEL02-B1-MISTRAL |

- Labels: `track:research`, `thesis:th-04` / `thesis:fel-02`, both providers, `dual-gate`, `stage:build`
- Milestone: Build
- Prior SEEDs: HT-1001 / HT-1002 (issues #1 / #2 closed)
- **Foreman owns long lasercode hills** — do not wake bots / TEMP agents from go-live setup

### 3. Factory Spec→ship checklist (PM)

| Issue | Purpose |
|-------|---------|
| [#22](https://github.com/gtmsko46-debug/asml-bench/issues/22) | Spec→Build→Review→Ship workflow for PM |

## Ticket contract

- Spec: `HARNESS_TICKET.md` + `schemas/harness_ticket.schema.json`
- Routing: `DUAL_PROVIDER.md` (Diplomat)
- Allowed providers only: `grok` \| `mock-mistral`

## Label vocabulary (factory)

`track:product`, `track:research`, `provider:grok`, `provider:mock-mistral`, `stage:spec`, `stage:build`, `stage:review`, `stage:ship`, `thesis:th-04`, `thesis:fel-02`, `product:p1-twin`, `dual-gate`, `blocked`, `KEEP`, `RESET`

## Guardrails

1. Dual gate: KEEP / PROMOTE needs both islands on identical holdout.
2. No long hills from this go-live pass — Foreman executes.
3. No bot wake / no TEMP agents.
4. Until Projects scopes refresh, use milestones + labels as the board (`PROJECTS.md`).
