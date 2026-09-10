# FEL-10 → FEL-03 handoff (one-pager)

**Date:** 2026-09-10  
**From:** PI FEL-10 IF Ownership  
**To:** PI FEL-03 Beam Split  
**Authority:** FEL Program Director (FREEZE lifted; FEL-03 funded)  
**Status:** docs handoff only — FEL-10 dual-KEEP banked; promote/ship separate

## What FEL-10 banked

| Island | Ticket | Provider | pupil_err | photons |
|--------|--------|----------|-----------|---------|
| Grok | HT-1028 | grok-4.6 | 0.0895 | 1.0 |
| Second-engine | HT-1033 | mock-mistral / grok-4.20 stand-in | 0.0950 | 1.0 |

- **Diplomat DUAL-KEEP STAMPED** under HOLDOUT `d0dc1f8a…` (EI PR #68)
- Gates: Critic formal PASS + Repro PASS + Diplomat (both)
- Lab: `labs/p10-if-shim` · sandbox `shim.py` only
- Contract: `tickets/IF_SPEC_FEL10_CONTRACT.md` (five-axis report; KEEP = pupil≤0.10 ∧ photons==1.0)
- Card boundary: consume `coherence-if-v1` **read-only** (FEL-02 owns conditioner metrics)
- **Not claimed:** vs-LPP / `lpp-source-v2` — later falsifier ticket
- Board: `labs/p10-if-shim/BOARD-dual-KEEP-1028-1033.md`
- Lessons: `asml-research-fel` notes/`fel-10-dual-keep-2026-09-10.md` (PR #2); asml-bench #85

## Soft disclosure (must travel)

**HT-1033 soft no-gain** — Critic accepted; disclose on board/tickets/product notes. Does **not** reopen dual-KEEP. Do not hide in FEL-03 briefs.

## Honesty path that kept (steal the ban list, not the shim)

1. Reconstruct fill from **field features** (coherence / bandwidth / power) — never from `pupil_fill_error` input
2. Explicit correct toward 0.72: `fill += FILL_GAIN * (0.72 - fill)` (or Critic-accepted centering)
3. `pupil_err = |fill - 0.72|` **unscaled**
4. Field-derived pol / pulse / pointing (no constants)
5. `photons_kept == 1.0` hard

### Standing VOID patterns (do not revive)

| Ticket | Kill |
|--------|------|
| HT-1029 | Hardcode `pupil_err=0` |
| HT-1032 | `pupil_in−k` / `PUPIL_CORRECT` write-down family (changing *k* still VOID) |

Also banned lab-wide: `abs(delta)*k`, forced `fill=0.72`, conditioner paste / metric clone across HT IDs.

## What FEL-03 should inherit

- Dual-gate discipline (identical frozen eval + HOLDOUT pin before Diplomat)
- Critic falsifiers **before** first Foreman stamp
- Soft notes travel with KEEP
- Spine order: FEL-02 → FEL-10 → **you**
- No upstairs without Warden + TCO; never “Cymer lost”

## What FEL-03 should **not** steal

- Do **not** paste `p10-if-shim/shim.py` into a beam-split lab
- Do **not** mutate `coherence-if-v1` or IF Spec for split ratios
- Do **not** bind `lpp-source-v2` unless your claim is vs-LPP
- IF ownership commercial claim stays FEL-10 / P10 product path (PM offline PR)

## Open FEL-10 tails (not your blockers)

- P10 productize: offline PR `reference_shim ← HT-1028` (dual 1033); soft no-gain in SPEC/README; no auto-promote
- Vs-LPP compatibility falsifier: later ticket under Warden bars
- Emulator / compatibility matrix: still FEL-10 backlog after product sync

## One-line for your claim draft

> FEL-10 proved dual-KEEP IF shim honesty under frozen pupil/photon gates without linac ownership; FEL-03 may assume that IF contract holds as a **consumer** while owning split / multi-tool photon allocation — new falsifiers required; do not reopen 1029/1032 write-down theater.

## Bench paths

- Research mirror: `asml-research-fel/notes/fel-10-to-fel-03-handoff-2026-09-10.md`
- Lessons: `corpus/learnings/fel-10-dual-keep-lessons-2026-09-10.md`
- Pointer: `corpus/notes/fel-10-dual-keep-pointer.md`
- Board: `labs/p10-if-shim/BOARD-dual-KEEP-1028-1033.md`

Landed by Scribe `2026-09-10T11:06:16Z`.
