# Product backlog P1–P10 (Product Manager)

Last map: 2026-09-09. Gate: a thesis KEEP is **not** a product. Product needs frozen eval + sandbox + ticket path + champion-facing job.

Repos: `gtmsko46-debug/asml-product-*`. Shared tickets: `asml-bench`. No hill-climbs until lasercode has provider credentials (currently **0**).

## Maturity matrix

| ID | Product | Repo | Bench lab | Frozen eval | Sandbox | Ticket path | Champion job | Verdict |
|----|---------|------|-----------|-------------|---------|-------------|--------------|---------|
| P1 | FEL↔scanner digital twin | `asml-product-p1-twin` | `labs/p1-twin/` empty | no | no | none | twin IF power/uncertainty | **scaffold** |
| P2 | Coherence / etendue conditioner | `asml-product-p2-coherence` | feeds `fel-02-coherence` | yes (live) | `conditioner.py` | [#3](https://github.com/gtmsko46-debug/asml-bench/issues/3) + [#2](https://github.com/gtmsko46-debug/asml-bench/issues/2) | illuminator-near module | **closest** — research SEED, product still thin |
| P3 | Beam-split facility scheduler | `asml-product-p3-scheduler` | none | no | no | none | wafers/day under dropouts | **scaffold** |
| P4 | Polarization-aware comp-litho | `asml-product-p4-complitho` | `labs/p4-polarization/` | yes | `solver.py` | none yet | Applications-recognizable toys | **lab ready**, no SEED ticket |
| P5 | Stochastic / resist dose | `asml-product-p5-stochastics` | `labs/p5-stochastics/` empty | no | no | none | dose vs pulse structure | **scaffold** |
| P6 | Optic survival / thermal | `asml-product-p6-thermal` | none (TH-04 is research) | research yes | research `solver.py` | [#1](https://github.com/gtmsko46-debug/asml-bench/issues/1) research | thermal control product | **research ahead of product** |
| P7 | Wavelength-agile (6.x) | *same repo as P4* | `labs/p7-wavelength/` | yes | `solver.py` | none yet | λ-agile without special-case forks | **lab ready**, no SEED ticket |
| P8 | Source-interface controls | `asml-product-p8-controls` | none | no | no | none | glitch recovery / IF control | **scaffold** |
| P9 | LPP vs FEL TCO | `asml-product-p9-tco` | `labs/p9-tco/` empty | no | no | none | decision product, may lose | **scaffold** |
| P10 | IF compatibility shim | `asml-product-p10-if-shim` | `labs/p10-if-shim/` empty | no | no | none | own IF even without linac | **scaffold** |

## Live bench (not product yet)

| Lab | Eval smoke | Decision | Notes |
|-----|------------|----------|-------|
| `th-04-reticle-heat` | holdout_rmse≈0.07 | KEEP | Primary demo island — still research until P6 product contract |
| `fel-02-coherence` | photons_kept=1.0 | SEED | Feeds P2; pull demos back to `conditioner.py` + RESET when they become FEL seminars |

## Blockers

1. **Lasercode credentials = 0** (`lasercode providers list`). Foreman choke stays closed for hill-climbs.
2. Product repos are README/LAB stubs only — no package layout, no champion demo path.
3. Empty product lab dirs (P1/P5/P9/P10) have no `eval.py` / holdout / sandbox.
4. Do **not** parallel-wake ~60 persona bots until keys exist.

## PM next moves (ordered)

1. Wire Grok (+ mock-mistral) into lasercode — unblocks Foreman.
2. Promote P4/P7: open paired SEED tickets (grok + mock-mistral); keep demos on `solver.py`.
3. Productize P2 off FEL-02: champion job + product sandbox contract in `asml-product-p2-coherence`.
4. Decide whether P6 inherits TH-04 frozen eval or needs a separate product holdout.
5. Stub frozen evals for P1/P3/P5/P8/P9/P10 before any island fan-out.
