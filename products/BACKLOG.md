# Product backlog P1–P10 (Product Manager)

Updated: 2026-09-10 (Diplomat **DUAL-KEEP HT-1015∧HT-1025**; Lab Director APPROVE #17).  
**Factory:** Spec → Build → Review → Ship. [`FACTORY.md`](FACTORY.md) · Epic [#45](https://github.com/gtmsko46-debug/asml-bench/issues/45).  
Bots orchestrate; **all product code** via lasercode (Foreman→Operator). Commit+push every change to `asml-product-p*`.

## Live bay

| Rank | ID | Status | Action |
|------|----|--------|--------|
| **P0** | **P1 Twin** | Diplomat **DUAL-KEEP** HT-1015∧HT-1025; Repro PASS; Lab Director **APPROVE** [#17](https://github.com/gtmsko46-debug/asml-bench/issues/17) | Twin PI ships `reference_twin` from **HT-1015** (0.1489) + 1025 dual docs; deepen [#55](https://github.com/gtmsko46-debug/asml-bench/issues/55) HT-1026/1027 |
| 1 | **P2 Coherence** | M1 package merged; HT-1023/1024 **bay LIVE** (CoS keep-bay-hot) | Foreman→Operator; do not re-queue behind P1 dual |
| 2+ | P3–P10 | Spec Issues [#46](https://github.com/gtmsko46-debug/asml-bench/issues/46)–[#52](https://github.com/gtmsko46-debug/asml-bench/issues/52) | Real Spec→Build (starved list LIFTED) |

## Maturity

| ID | Product | Repo | Spec | Build | Review | Ship | Verdict |
|----|---------|------|------|-------|--------|------|---------|
| P1 | Twin | `asml-product-p1-twin` | yes | M1 + DUAL-KEEP | Critic+Repro+Diplomat | **#17 APPROVE** | **ship-queue** |
| P2 | Coherence | `asml-product-p2-coherence` | yes M1 | HT-1023/1024 live | — | — | **build / bay hot** |
| P3 | Scheduler | `asml-product-p3-scheduler` | [#46](https://github.com/gtmsko46-debug/asml-bench/issues/46) | — | — | — | **spec** |
| P4/P7 | Comp-litho | `asml-product-p4-complitho` | [#47](https://github.com/gtmsko46-debug/asml-bench/issues/47) | — | — | — | **spec** |
| P5 | Stochastics | `asml-product-p5-stochastics` | [#48](https://github.com/gtmsko46-debug/asml-bench/issues/48) | — | — | — | **spec** |
| P6 | Thermal | `asml-product-p6-thermal` | [#49](https://github.com/gtmsko46-debug/asml-bench/issues/49) | — | — | — | **spec** |
| P8 | Controls | `asml-product-p8-controls` | [#50](https://github.com/gtmsko46-debug/asml-bench/issues/50) | — | — | — | **spec** |
| P9 | TCO | `asml-product-p9-tco` | [#51](https://github.com/gtmsko46-debug/asml-bench/issues/51) | — | — | — | **spec** |
| P10 | IF shim | `asml-product-p10-if-shim` | [#52](https://github.com/gtmsko46-debug/asml-bench/issues/52) | — | — | — | **spec** |

## PM next
1. Land Twin PI `reference_twin` PR → close #17 when merged.
2. Stamp deepen HT-1026/1027 (#55) without starving P2 Operator.
3. Drive Spec Issues #46–#52 → real SPEC.md on each `asml-product-p*`.
