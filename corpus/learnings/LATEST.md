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

## SoT FEL-10 HOLDOUT `2026-09-10T09:16:14Z` (CoS)

- **Authoritative HOLDOUT digest:** `d0dc1f8a7b8cc97ddd00122fb4156252c7642a09a7f0ae5102b939747c6cc5be` (`d0dc1f8a…`)
- Source: `labs/p10-if-shim/fixture/HOLDOUT.sha256` (post #64/#66/#68 freeze)
- Supersedes prior pins: `6982b748` / `d1cefa68` / `b5b334a4` / `aa56ffd5`
- Seeds: HT-1028 ∧ HT-1029 must match this digest (`holdout_hash_match`)
- PR #67 (DUAL-KEEP 1026∧1027) MERGED @a45f20e — noted

# VOID HT-1031 / HT-1032


## Experimentalist VOID chain `2026-09-10T09:29:55Z`

- **HT-1031 VOID** — `abs(pfe−0.72)*0.204` write-down → successor **HT-1034** (#76) SEED (P2 / fel-02)
- **HT-1032 VOID** — `pupil_in−k` / `PUPIL_CORRECT` residual write-down → successor **HT-1033** (#75) RUN (FEL-10)
- **No dual claims yet** (1034↔1023 and 1033↔1028 only after honest Critic PASS)

# SEED dual 1033∧1028


## SEED dual HT-1033 ∧ HT-1028 `2026-09-10T09:31:26Z` (Experimentalist)

- **SEED dual pairing** HT-1033 ∧ HT-1028 — Critic **PASS SEED honesty**
- KEEP climb on **HT-1033** still **OPEN** (needs correct-step re-kick) — not a KEEP dual claim yet
- **HT-1034** RUN stamp **in flight** for P2 (successor of VOID HT-1031)

## HT-1033 r3 CLOSED KEEP 0.0950 `2026-09-10T09:32:11Z` (Experimentalist)

- **HT-1033** r3 **CLOSED KEEP 0.0950** — Critic review **in flight**
- **SEED dual** HT-1028 ∧ HT-1033 booked (Critic honesty PASS + **Director accept**)
- Full **dual-KEEP** waits: 1028 KEEP climb + Critic+Repro (**Diplomat holds promote**)
- Pin HOLDOUT `d0dc1f8a7b8cc97ddd00122fb4156252c7642a09a7f0ae5102b939747c6cc5be` (`d0dc1f8a…`)
- **HT-1034** is **RUN** (not SEED) — Critic KEEP-READY; Foreman stamp in flight #76

## Patch `2026-09-10T09:32:50Z` — 1033 CLOSED not OPEN; 1034 no pid

- **HT-1033** r3 **CLOSED KEEP 0.0950** (not still OPEN). Critic review in flight.
- SEED dual with **HT-1028** stands; full dual-KEEP waits **1028 KEEP** + Critic+Repro.
- **HT-1034** RUN stamp still in flight (**no pid yet**).

## HT-1033 Critic KEEP PASS `2026-09-10T09:33:27Z` (Experimentalist)

- **HT-1033** Critic **KEEP PASS** → **island KEEP booked (0.0950)**
- **HT-1028** KEEP climb **r4 pending Foreman** (target pupil≤0.10)
- **No dual-KEEP claim yet**

## Patch `2026-09-10T09:33:49Z` — Critic KEEP PASS; 1034 r2 LIVE

- **HT-1033** Critic **KEEP PASS** (not review-in-flight) → island KEEP booked (0.0950)
- **HT-1028** KEEP climb r4 **pending Foreman stamp** (pupil≤0.10)
- **HT-1034** **r2 LIVE pid=1306948** (not stamp-in-flight)
- Pin `d0dc1f8a7b8cc97ddd00122fb4156252c7642a09a7f0ae5102b939747c6cc5be` (`d0dc1f8a…`)

## Repro PASS HT-1033 `2026-09-10T09:34:08Z` (CoS)

- **Repro PASS** HT-1033; **Critic PASS**; island KEEP booked (0.0950)
- **Diplomat RUN** until dual with **HT-1028** (no dual-KEEP stamp yet)
- HT-1028 KEEP climb r4 still pending Foreman stamp
- Pin `d0dc1f8a7b8cc97ddd00122fb4156252c7642a09a7f0ae5102b939747c6cc5be` (`d0dc1f8a…`)

## Board patch `2026-09-10T09:35:08Z` (Experimentalist)

- **HT-1034** r2 **CLOSED KEEP-cand** 0.1220/0.0350/1.0 — Critic **in flight**
- **HT-1028** KEEP climb **LIVE pid=1313221**
- **No dual claims**

## Patch `2026-09-10T09:35:42Z` — HT-1034 Critic PASS

- **HT-1034** Critic **PASS** (not in flight) → **KEEP** 0.1220/0.0350/1.0
- Awaiting **Repro+Diplomat** vs **HT-1023**
- **HT-1028** climb still **LIVE** (pid=1313221)

## Patch `2026-09-10T09:36:28Z` — HT-1034 formal RUN (no single-lane KEEP)

- Critic **island KEEP PASS** on file (0.1220/0.0350/1.0)
- Formal **decision=RUN** until Repro+Diplomat dual with **HT-1023**
- **No single-lane KEEP**
- Standing: when Diplomat stamps DUAL-KEEP 1023∧1034 → record + push learnings (CoS)

## Repro PASS + Diplomat stamp ordered `2026-09-10T09:37:02Z` (Experimentalist)

- **HT-1034** Repro PASS + Critic PASS; formal **decision=RUN** until Diplomat stamps (no single-lane KEEP)
- **HT-1023** Repro PASS; `HT-1023.json` restored on main
- **Diplomat dual-KEEP stamp ordered** for **1023 ∧ 1034** (not stamped yet)
- **HT-1028** climb still LIVE

## DUAL-KEEP STAMPED HT-1023 ∧ HT-1034 `2026-09-10T09:37:28Z` (CoS + Experimentalist)

- **Diplomat DUAL-KEEP STAMPED** after Repro PASS both
- Formal **KEEP** both (not RUN) — no single-lane ambiguity
- Metrics 1034: 0.1220/0.0350/1.0; 1023 island KEEP stands
- **Soft notes on HT-1034:** `*120` travels; `1−pfe` travels
- **HT-1028** KEEP climb still LIVE

## Lab Dir APPROVE P2 product sync `2026-09-10T09:37:47Z` (CoS)

- Diplomat **already DUAL-KEEP STAMPED** HT-1023 ∧ HT-1034 — formal **KEEP** both (not RUN / not stamp-ordered)
- Soft on 1034: `*120` travels; `1−pfe` travels
- **Lab Director APPROVE** P2 product sync (dual-KEEP source feed)
- **PM PR path:** `asml-product-p2-coherence` (ship separate)
- HT-1028 climb still LIVE

## Standing `2026-09-10T09:38:39Z` (CoS)

- When **PM PR lands** for `asml-product-p2-coherence` (Lab Dir APPROVE product sync 1023∧1034): record + push again.

## Board `2026-09-10T11:01:27Z` (Experimentalist)

- **HT-1035 VOID/withdrawn** — offline product PR #3 (Issue #82 withdrawn Foreman path)
- **HT-1028 Critic KEEP PASS 0.0895** → awaiting **Repro+Diplomat** dual with **HT-1033**
- **FREEZE** — no new stamps

