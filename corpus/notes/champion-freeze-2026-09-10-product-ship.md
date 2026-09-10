# Champion freeze — product ship snapshot (2026-09-10)

**Order:** FREEZE new hills. Docs / READMEs / research writeups only. No new harness tickets.

## What shipped (product)

| Product | Repo | Baseline | Notes |
|---------|------|----------|-------|
| P1 Twin | `asml-product-p1-twin` | `reference_twin` = **HT-1026** (dual HT-1027; soft IF-only disclosed) | PR #4 |
| P2 Coherence | `asml-product-p2-coherence` | `reference_conditioner` = **HT-1023** (dual HT-1034; soft `*120` + `1−pfe` disclosed) | PR #3 |
| P3 Scheduler | `asml-product-p3-scheduler` | M1 `schedule_facility` SEED | Lab `labs/p3-scheduler` SEED eval |
| P4/P7 Comp-litho | `asml-product-p4-complitho` | M1 `process_window` / `wavelength_window` SEED | M2 drafts offline |
| P5 Stochastics | `asml-product-p5-stochastics` | M1 `stochastic_risk` SEED | Lab `labs/p5-stochastics` |
| P6 Thermal | `asml-product-p6-thermal` | M1 `thermal_overlay` (TH-04 inherit SEED) | Spec #49 holdout decision open |
| P8 Controls | `asml-product-p8-controls` | M1 `recover_from_glitch` SEED | Lab `labs/p8-controls` |
| P9 TCO | `asml-product-p9-tco` | M1 `compare_tco` SEED (may lose) | Lab `labs/p9-tco` |
| P10 IF shim | `asml-product-p10-if-shim` | M1 `shim_if` SEED | Live research lab `labs/p10-if-shim` (FEL-10) |

## Research dual-KEEPs that fed products

- P1: HT-1015∧HT-1025 then deepen **HT-1026∧HT-1027**
- P2: FEL-02 pupil path → product dual **HT-1023∧HT-1034** (after VOID chain 1024→1030→1031)
- FEL-10: hills frozen mid-climb for champion docs pass

## Factory rule (unchanged)

Spec → Build → Review → Ship via **Issues + PRs only** (no Projects). Solvers still Foreman→Operator when hills resume. Eval Integrity freezes HOLDOUT; Critic/Repro/Diplomat before product `reference_*` sync.
