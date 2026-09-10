# Product factory schedule (Champion 2026-09-10)

**Rule:** Spec → Build → Review → Ship. Bots orchestrate; all product *code* via lasercode (Foreman→Operator). Every change lands on `asml-product-p*` via commit+push.

## Priority

| Order | Product | Backlog | Now |
|-------|---------|---------|-----|
| P0 | P1 Twin | #4 | HT-1015 KEEP_PENDING_DUAL; HT-1025 independent mock in flight; #17 blocked on Critic+Repro |
| 1 | P2 Coherence | #3 | M1 docs merged; HT-1023/1024 bay-queued; package code waits bay |
| 2 | P4/P7 Comp-litho | #6 | Labs ready; open dual-gate product tickets when bay free |
| 3 | P10 IF shim | #11 | Spec→eval scaffold |
| 4 | P9 TCO | #10 | Spec→eval scaffold |
| 5 | P6 Thermal | #8 | Decide inherit TH-04 vs new holdout |
| 6 | P3 Scheduler | #5 | Waits FEL-03 research feed; still schedule Spec Issues |
| 7 | P5 Stochastics | #7 | Spec now (was starved); bay later |
| 8 | P8 Controls | #9 | Spec now (was starved); bay later |

## Stage checklist (every product)

1. **Spec** — champion job, sandbox path, frozen eval bind, assumption card, dual-gate plan (Issue)
2. **Build** — package + harness tickets via Foreman (no hand-edits)
3. **Review** — Critic + Eval Integrity + Repro; dual-gate KEEP
4. **Ship** — ship-queue → merge `asml-product-p*` → maintain

## Bay

P1 HT-1025 owns Operator until honest dual + Critic/Repro. Do not pull bay for P2–P10 ratchets until CoS frees capacity.
