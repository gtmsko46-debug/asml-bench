# Product backlog P1–P10 (Product Manager)

Updated: 2026-09-10 (Diplomat **DUAL-KEEP HT-1015∧HT-1025**; Lab Director APPROVE #17).  
**Factory:** Spec → Build → Review → Ship. [`FACTORY.md`](FACTORY.md) · Epic [#45](https://github.com/gtmsko46-debug/asml-bench/issues/45).  
Bots orchestrate; **all product code** via lasercode (Foreman→Operator). Commit+push every change to `asml-product-p*`.

## Live bay

| Rank | ID | Status | Action |
|------|----|--------|--------|
| **P0** | **P1 Twin** | Diplomat **DUAL-KEEP** HT-1026∧HT-1027; `reference_twin` = **HT-1026** (0.1475) via product PR #4 | Soft IF-only on 1027 documented; next deepen/M2 as funded |
| 1 | **P2 Coherence** | Diplomat **DUAL-KEEP** HT-1023∧HT-1034; Lab Dir+PM APPROVE product sync | Foreman→Operator → `reference_conditioner` PR; soft *120+1−pfe explicit | No Operator steal; Critic→Foreman on 1031 | Honest mistral successor HT-1030; no Operator steal for offline M1s |
| 2+ | P3–P10 | Spec Issues [#46](https://github.com/gtmsko46-debug/asml-bench/issues/46)–[#52](https://github.com/gtmsko46-debug/asml-bench/issues/52) | Real Spec→Build (starved list LIFTED) |

## Maturity

| ID | Product | Repo | Spec | Build | Review | Ship | Verdict |
|----|---------|------|------|-------|--------|------|---------|
| P1 | Twin | `asml-product-p1-twin` | yes | M1 + deepen | DUAL-KEEP 1026∧1027 | **PR #4 baseline 1026** | **shipped + deepen** |
| P2 | Coherence | `asml-product-p2-coherence` | yes M1 | HT-1023/1024 live | — | — | **build / bay hot** |
| P3 | Scheduler | `asml-product-p3-scheduler` | M0 SPEC [#46](https://github.com/gtmsko46-debug/asml-bench/issues/46) | — | — | — | **spec** |
| P4/P7 | Comp-litho | `asml-product-p4-complitho` | M0+M1 [#47](https://github.com/gtmsko46-debug/asml-bench/issues/47) | — | — | — | **spec** |
| P5 | Stochastics | `asml-product-p5-stochastics` | M0 SPEC [#48](https://github.com/gtmsko46-debug/asml-bench/issues/48) | — | — | — | **spec** |
| P6 | Thermal | `asml-product-p6-thermal` | M0+M1 [#49](https://github.com/gtmsko46-debug/asml-bench/issues/49) | — | — | — | **spec** |
| P8 | Controls | `asml-product-p8-controls` | M0 SPEC [#50](https://github.com/gtmsko46-debug/asml-bench/issues/50) | — | — | — | **spec** |
| P9 | TCO | `asml-product-p9-tco` | M0+M1 [#51](https://github.com/gtmsko46-debug/asml-bench/issues/51) | — | — | — | **spec** |
| P10 | IF shim | `asml-product-p10-if-shim` | M0+M1 [#52](https://github.com/gtmsko46-debug/asml-bench/issues/52) | — | — | — | **spec** |

## PM next
1. ~~#17 ship~~ done (PR #3). Stamp deepen HT-1026/1027 (#55) parallel with P2 (CoS).
2. P2 HT-1023/1024 Operator → Critic/Repro when KEEP.
3. ~~P4/P7 + P10 + P9 + P6 M1 packages~~ landed offline. Next: P3/P5/P8 M1; dual-gate tickets when bay frees; P6 Spec #49 holdout decision.
3. Next Build after Spec: P4/P7 M1 package (funded order), then P10 → P9 → P6; P3 waits FEL-03 physics; P5/P8 after.

<!-- scribe-bay-queue-2026-09-10 -->
Scribe: **HT-1026∧HT-1027 ∥ P2** (not behind). Before FEL-10 1028∧1029.
Scribe `2026-09-10T09:02:05Z`: **HT-1026∧HT-1027 ∥ P2** (not behind). Before FEL-10 1028∧1029.

<!-- scribe-p3-p10-m0 -->
Scribe: P3–P10 M0 SPEC.md PR#1 MERGED `2026-09-10T09:04:13Z`.
