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

---

# Champion encode — lab learnings

**Recorded by Scribe** `2026-09-10T08:57:02Z`  
**Source:** Chief of Staff

## Standing champion policy
1. **P1–P10 excellent builds** — product path quality bar; do not ship thin demos as product weight.
2. **FEL-10 funded behind P1** — FEL-10 claim work queues behind P1 bay P0; does not jump the twin deepen dual.
3. **FEL-02 learnings → `corpus/notes` + asml-bench** — dual-KEEP / freeze / P2 feed notes live in notes + learnings; Archivist lifts from Scribe.
4. **Every change commit+push** — champion encode: land durable memory on `origin` promptly (Scribe corpus paths).

## Also current
- **HT-1020** Critic VOID / RESET — metric reuse remap HT-1015; no dual.
- **HT-1025** (#44) successor — KEEP-candidate 0.2467/0.3356 IF=0.47 MIR=0.13 digest=2c398448 pred_diff=1212.38; Critic PENDING; dual PENDING vs HT-1015.

## Cross-links
- Prior unblock: `champion-unblock-2026-09-10.md`
- FEL-02 pointer note: `corpus/notes/fel-02-dual-keep-pointer.md`
- Scribe feed: `corpus/scribe/LATEST.md`

---

# Learnings patch — HT-1025 CLOSED KEEP + FEL-10 Critic falsifiers

**Recorded by Scribe** `2026-09-10T08:58:19Z`  
**Source:** Chief of Staff

## HT-1025 correction
- **CLOSED KEEP @exit0** (not mid-climb death).
- Mid-climb death / Operator re-kick narrative = **FALSE ALARM — retracted**.
- **Critic PASS** (pred max-abs 1212 vs HT-1015; code_only different; trap OK; not oracle).
- Metrics: holdout=0.2467 trap=0.3356 IF=0.47 MIR=0.13 digest=2c398448.
- **Dual KEEP pending Repro+Diplomat** vs HT-1015.
- Replaces VOID HT-1020.

## Critic FEL-10 falsifiers (encoded from claim + IF Spec dual-gate)
Source: `tickets/FEL-10_CLAIM_DRAFT.md`, `tickets/IF_SPEC_FEL10_CONTRACT.md`.

1. **Primary falsifier:** Under IF Spec contract metrics, a tin-LPP-class fixture bound to `lpp-source-v2` matches or beats the FEL shim/compat score **without** FEL-specific IF ownership → thesis **RESET** (accelerator hobby).
2. **Card rule:** bind `lpp-source-v2` **only** on the vs-LPP falsifier ticket — never on scaffold SEED.
3. **Warden honesty:** LPP fixture must not win by discarding photons or weakening tin.
4. **Kill / guard lines before SEED:**
   - `if_spec_contract_bound` (pupil_fill_error KEEP ≤0.10; photons_kept ≥0.55 + if_loss_db report; polarization / pulse envelope / pointing non-null report)
   - `no_rewrite_if_spec` / `no_mutate_coherence-if-v1`
   - `frozen_eval_untouched` / `holdout_hash_match`
   - `no_photon_discard_cheat`
   - `no_lpp-source-v2_on_scaffold`
   - `dual_gate_pair_required` (grok vs mock-mistral)
   - `bay_behind_P1` / `no_upstairs_without_warden_tco` / `not_product_KEEP`
5. **Critic ask standing:** falsifier must be sharp (not soft) — kill lines before SEED; a beautiful undulator beam illegal at IF is a failed product, not a KEEP.

## Standing (unchanged)
- P1–P10 excellent builds; FEL-10 funded behind P1; every change commit+push.

## CoS LATEST touch `2026-09-10T09:00:53Z`

### Diplomat DUAL-KEEP HT-1015 ∧ HT-1025
- **Stamp:** `DUAL_KEEP_STAMPED` (Critic + Repro + Diplomat)
- Metrics: 1015 grok 0.1489/0.2707; 1025 mock-mistral 0.2467/0.3356 (pred_diff=1212)
- HOLDOUT `2c398448…`

### Lab Director Issue #17 APPROVE
- P1 twin product sync / `#17` **APPROVED** now that honest dual-KEEP 1015∧1025 is stamped (was blocked on Critic+Repro).

### FEL-10 SEED HT-1028 ∧ HT-1029
- Dual-gate SEED drafts/tickets on books (Issue #57)
- Critic KEEP-READY + IF Spec SEATED + Warden ACCEPT
- Foreman stamp when P2 bay slot — do not starve P1/P2
- No `lpp-source-v2` on SEED

## Bay queue patch `2026-09-10T09:02:05Z` (CoS)

- **HT-1026 ∧ HT-1027** (P1 deepen dual after 1015∧1025): bay position = **∥ P2** (parallel with HT-1023∧HT-1024), **not behind** P2.
- Stamp NOW when Foreman capacity allows — do not wait for P2 close.
- Still **before** FEL-10 HT-1028∧HT-1029 (don't starve P1).

## P1 product ship `2026-09-10T09:03:45Z` (CoS)

- **MERGED:** `asml-product-p1-twin` PR **#3**
- **Source:** dual-KEEP HT-1015 ∧ HT-1025 (`P1-twin-dual-001`) shipped as `reference_twin`
- Issue #17 APPROVE consummated — product sync landed

## P3–P10 M0 SPEC ship `2026-09-10T09:04:13Z` (CoS)

**RECORD:** M0 `SPEC.md` merged as **PR #1** in each product repo:

| Product | Repo | Status |
|---------|------|--------|
| P3 Scheduler | `asml-product-p3-scheduler` | M0 SPEC.md PR#1 MERGED |
| P4 Comp-litho | `asml-product-p4-complitho` | M0 SPEC.md PR#1 MERGED |
| P5 Stochastics | `asml-product-p5-stochastics` | M0 SPEC.md PR#1 MERGED |
| P6 Thermal | `asml-product-p6-thermal` | M0 SPEC.md PR#1 MERGED |
| P7 Wavelength | `asml-product-p7-wavelength` | M0 SPEC.md PR#1 MERGED |
| P8 Controls | `asml-product-p8-controls` | M0 SPEC.md PR#1 MERGED |
| P9 TCO | `asml-product-p9-tco` | M0 SPEC.md PR#1 MERGED |
| P10 IF shim | `asml-product-p10-if-shim` | M0 SPEC.md PR#1 MERGED |

Spec freeze milestone for factory — Build tickets still follow Lab Director order / bay capacity.



## HT-1026∧1027 `2026-09-10T09:11:02Z`
KEEP-candidates 0.1475/0.2534 ∧ 0.1795/0.3076; pred_diff PASS; Critic dual PENDING.
## DUAL-KEEP HT-1026 ∧ HT-1027 `2026-09-10T09:12:13Z` (CoS)

- **Diplomat DUAL-KEEP STAMPED** HT-1026 ∧ HT-1027 (Critic+Repro PASS; HOLDOUT `2c398448…`)
- Metrics: 1026 grok 0.1475/0.2534; 1027 mock-mistral 0.1795/0.3076
- **Lab Director ACCEPT** twin bump **reference_twin 1015 → 1026**
- **Soft IF note on HT-1027:** thin-IF travels (not VOID; travels with dual stamp)

## DUAL-KEEP HT-1026 ∧ HT-1027 `2026-09-10T09:13:27Z` (CoS)
- Diplomat DUAL-KEEP STAMPED; metrics 0.1475/0.2534 ∧ 0.1795/0.3076
- Lab Director ACCEPT twin bump 1015→1026
- Soft IF note on HT-1027 (thin-IF travels)
