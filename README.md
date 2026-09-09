# ASML Litho-Lab Data Plane

Local research-factory corpus for **asml-bench** (https://github.com/gtmsko46-debug/asml-bench).

This tree holds synthetic labs, assumption cards, schemas, and curated bibliography pointers.
**No real wafer data. No ASML confidential numbers.** All numeric parameters are literature- or open-proxy-cited toys for multi-agent experimentation.

## Quick start

```bash
# Live demo labs
python labs/th-04-reticle-heat/eval.py
python labs/fel-02-coherence/eval.py

# Regenerate leaderboard from results.tsv rows
python scripts/gen_leaderboard.py

# Verify holdout integrity
python scripts/hash_holdout.py
```

## Layout

| Path | Role |
|------|------|
| `assumptions/` | Versioned assumption cards (YAML) with citations + flags |
| `schemas/` | JSON Schema for tickets, results, theses, cards |
| `labs/` | Per-thesis sandboxes; live demos under `th-04-*` and `fel-02-*` |
| `corpus/` | Bibliography index + dataset license pointers (no pirated PDFs) |
| `field/` | Synthetic field signatures |
| `products/` | Product backlog |
| `dashboards/` | Generated leaderboard |
| `scripts/` | Holdout hashing + leaderboard generation |
| `LAB_RULES.md` | Foreman choke point, dual-provider, no eval edits |
| `DUAL_PROVIDER.md` | Diplomat router + demo contract (grok / mock-mistral) |
| `PROGRAM_TEMPLATE.md` | program.md brief template for lab runs |
| `BRANCHING.md` | `exp/<thesis>-<ticket>` branch policy |
| `HARNESS_TICKET.md` | Ticket contract for lasercode |
| `ASSUMPTIONS.md` | How assumption cards are authored and frozen |

## Live labs

- **TH-04 reticle heat** — holdout RMSE (synthetic-nm); thermal term must be non-zero; no `platform==NXE` forks.
- **FEL-02 coherence** — speckle contrast, pupil-fill RMSE, photons_kept; cheat = discard photons.

## Safety

Synthetic fixtures only. Holdouts are hashed (`fixture/HOLDOUT.sha256`). Eval is frozen; solvers may not edit eval or fixtures on `main`.
