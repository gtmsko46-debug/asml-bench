# Product backlog P1–P10 (Product Manager)

Updated: 2026-09-10 (Champion: build **all** P1–P10 as real products).  
**Factory:** Spec → Build → Review → Ship. Schedule: [`FACTORY.md`](FACTORY.md) · Epic [#45](https://github.com/gtmsko46-debug/asml-bench/issues/45).  
Bots orchestrate; **all product code** via lasercode (Foreman→Operator). Commit+push every change to `asml-product-p*`.

## Live bay

| Rank | ID | Status | Action |
|------|----|--------|--------|
| **P0** | **P1 Twin** | HT-1015 KEEP_PENDING_DUAL @ HOLDOUT `2c398448…`; HT-1020 VOID (metric reuse); **HT-1025** independent mock Operator `-r3` | Wait Critic+Repro; no `#17` / `reference_twin` sync until honest dual |
| 1 | **P2 Coherence** | M1 docs merged (PR #1); HT-1023/1024 stamped ready | Bay-queued — package code when CoS frees Operator |
| 2+ | P3–P10 | Spec Issues open | Spec-only until bay capacity |

## Maturity

| ID | Product | Repo | Lab | Spec | Build | Review | Ship | Verdict |
|----|---------|------|-----|------|-------|--------|------|---------|
| P1 | Twin | `asml-product-p1-twin` | `labs/p1-twin/` | yes | M1 API + deepen | dual pending 1025 | blocked #17 | **KEEP climb** |
| P2 | Coherence | `asml-product-p2-coherence` | `labs/fel-02-coherence/` | yes M1 | package pending | — | — | **build / bay-queued** |
| P3 | Scheduler | `asml-product-p3-scheduler` | waits FEL-03 | [#46](https://github.com/gtmsko46-debug/asml-bench/issues/46) | — | — | — | **spec** |
| P4/P7 | Comp-litho | `asml-product-p4-complitho` | p4+p7 labs | [#47](https://github.com/gtmsko46-debug/asml-bench/issues/47) | — | — | — | **spec** |
| P5 | Stochastics | `asml-product-p5-stochastics` | scaffold | [#48](https://github.com/gtmsko46-debug/asml-bench/issues/48) | — | — | — | **spec** |
| P6 | Thermal | `asml-product-p6-thermal` | TH-04 inherit? | [#49](https://github.com/gtmsko46-debug/asml-bench/issues/49) | — | — | — | **spec** |
| P8 | Controls | `asml-product-p8-controls` | TBD | [#50](https://github.com/gtmsko46-debug/asml-bench/issues/50) | — | — | — | **spec** |
| P9 | TCO | `asml-product-p9-tco` | scaffold | [#51](https://github.com/gtmsko46-debug/asml-bench/issues/51) | — | — | — | **spec** |
| P10 | IF shim | `asml-product-p10-if-shim` | scaffold | [#52](https://github.com/gtmsko46-debug/asml-bench/issues/52) | — | — | — | **spec** |

Parents: [#3](https://github.com/gtmsko46-debug/asml-bench/issues/3)–[#11](https://github.com/gtmsko46-debug/asml-bench/issues/11).

## PM next
1. Close HT-1025 → Critic → Repro → only then `#17` / weight sync.
2. When CoS frees bay: P2 package + HT-1023/1024.
3. Drive Spec Issues #46–#52 (docs on product repos; no bay steal).
4. After Spec freeze: dual-gate Build tickets in Lab Director order (P4/P7 → P10 → P9 → P6; P3 after FEL-03; P5/P8 last).
