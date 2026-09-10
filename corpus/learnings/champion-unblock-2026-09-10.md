# Champion unblock — lab learnings

**Recorded by Scribe** `2026-09-10T08:56:31Z`  
**Source:** Chief of Staff (champion unblock)

## 1. HT-1020 Critic VOID
- **Decision:** RESET
- **Reason:** metric reuse / preds byte-equal to HT-1015 (code-only / comment-sha fork)
- **Dual:** none — no dual, no promote
- **Replaced by:** HT-1025

## 2. HT-1025 successor (#44)
- **Role:** r3 dual partner for HT-1015 KEEP
- **Guard:** pred-diff vs HT-1015 (max abs diff > 1e-3); no metric paste / comment-only fork
- **Session:** `ticket-HT-1016-p1-deepen-mistral-r3`
- **Ops note:** CLOSED KEEP @exit0 (mid-climb death FALSE ALARM — re-kick retracted; Critic PASS; dual pending Repro+Diplomat)
- **Board at record time:** CLOSED KEEP holdout=0.2467 trap=0.3356; Critic PASS; dual pending Repro+Diplomat vs HT-1015

## 3. FEL-02 dual-KEEP + P2
- **Dual-KEEP:** HT-1011 ∧ HT-1022 stamped (`FEL-02-coherence-dual-001`); post-freeze Repro PASS
- **Eval:** `EVAL_PUPIL_FREEZE` main@84520ee PR#40
- **P2 productize:** Lab Director **OPEN** — queued **behind P1 bay P0** (research source feed remains dual-001 → Illuminator+Experimentalist when bay clears)

## Standing rules reinforced
- `no_metric_reuse_across_ticket_ids` — trap PASS does not save a remapped triad
- Pred-diff guard required on mistral deepen retickets vs KEEP sibling
- P2 productize does not jump P1 bay P0
