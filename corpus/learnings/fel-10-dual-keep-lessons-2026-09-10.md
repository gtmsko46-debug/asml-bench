# FEL-10 dual-KEEP lessons (2026-09-10)

**Audience:** champion / FEL research spine / P10 IF shim / FEL-03 hand-off  
**Thesis:** `fel-10-if-ownership` — commercial IF ownership **without linac**  
**Lab:** `labs/p10-if-shim`  
**Stamp:** HT-1028 ∧ HT-1033 `DUAL_KEEP_STAMPED` (Critic + Repro + Diplomat)  
**Pin:** HOLDOUT `d0dc1f8a7b8cc97ddd00122fb4156252c7642a09a7f0ae5102b939747c6cc5be` (`d0dc1f8a…`) — EI PR **#68**  
**Board:** `labs/p10-if-shim/BOARD-dual-KEEP-1028-1033.md`  
**Not in scope for this dual:** vs-LPP / `lpp-source-v2` (do not bind on this dual)

## Metrics

| Ticket | Provider tag | Runtime | pupil_err | photons_kept |
|--------|--------------|---------|-----------|--------------|
| HT-1028 | `grok` | `xai/grok-4.6` | 0.0895 | 1.0 |
| HT-1033 | `mock-mistral` | `xai/grok-4.20` stand-in | 0.0950 | 1.0 |

Gates cleared: Critic formal PASS (both), Repro PASS (both), Diplomat dual-KEEP stamp. Formal **KEEP** both.

Champion language: **second-engine / mistral-lane** (ticket tag stays `mock-mistral`). Dual-gate models: **grok-4.6 vs grok-4.20 stand-in**.

## What won

1. **IF Spec contract discipline:** pupil_fill_error KEEP ≤ 0.10; `photons_kept == 1.0` hard on docket; holdout hash match to SoT `d0dc1f8a…`.
2. **Dual-gate on identical frozen eval:** Grok-lane + second-engine lane; single-lane KEEP rejected until Diplomat stamps both.
3. **Honest structure over residual knobs:** reconstruct / correct fill → `pupil_err = |fill − 0.72|`; no hardcode-0; no `pupil_in−k` / `PUPIL_CORRECT` write-downs.
4. **Card hygiene:** commercial IF ownership without linac on `p10-if-shim`; consumes coherence IF read-only; **no** `lpp-source-v2` on this dual.

## Soft travels (disclose — do not VOID)

- **HT-1033:** no-gain path travels with the dual stamp. Disclose on board / tickets / champion notes; not a reopen of dual-KEEP. Promote/ship separate.

## Critic VOID / RESET history (do not revive)

| Ticket | Kill |
|--------|------|
| HT-1029 | Hardcode `pupil_err=0` (structure cheat) → VOID; successor climb via HT-1032 → HT-1033 |
| HT-1032 | `pupil_in−k` / `PUPIL_CORRECT` residual write-downs → VOID; successor **HT-1033** |

## Standing bans (FEL-10 / lab-wide)

- **`pupil_in−k` family** (including `PUPIL_CORRECT` offsets) — residual write-down, not reconstruct/correct
- **Constant / hardcode `pupil_err`** (esp. `pupil_err=0`)
- **Write-down `abs(delta)*k`** / `p_err*scale` gatesitting (carried from FEL-02 critic lessons)

## Spine & hand-offs

- **Spine:** FEL-02 done → **FEL-10 dual-KEEP done** → **FEL-03 next** when Lab Director funds **and** climb freeze lifts
- **FREEZE closeout** on this dual; promote/ship annotated separately
- No upstairs brief without Warden + TCO; never claim Cymer lost

## Board (verbatim)

```
# FEL-10 Dual KEEP — HT-1028 ∧ HT-1033

- **stamped:** 2026-09-10
- **pin:** HOLDOUT d0dc1f8a… (EI PR #68)
- **metrics:** HT-1028 pupil=0.0895 photons=1.0; HT-1033 pupil=0.0950 photons=1.0
- **gates:** Critic+Repro+Diplomat
- **soft travels:** no-gain path on HT-1033 (disclose)
- **not:** vs-LPP / lpp-source-v2; no upstairs; promote/ship separate
- **spine next:** FEL-03 after Lab Dir fund + climb freeze lifts
```

## Cross-links

- Stamp digest: `corpus/learnings/dual-keep-1028-1033-2026-09-10.md`
- Research pack: `asml-research-fel/notes/fel-10-dual-keep-2026-09-10.md`
- Prior spine: `corpus/learnings/fel-02-dual-keep-lessons-2026-09-10.md`
