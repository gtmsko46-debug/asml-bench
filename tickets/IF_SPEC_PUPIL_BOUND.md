# IF Spec stamp — FEL-02 / P2 pupil bound (2026-09-10)

**Owner:** IF Spec Owner  
**Applies to:** `labs/fel-02-coherence` KEEP decisions; illuminator/P2 feed claims  
**Assumption card:** `coherence-if-v1` (`pupil_fill_target=0.72`)

## Decision

**No waive.** Pupil fill is first-class IF contract (see `program.md` metrics). A KEEP that only gates speckle + photons is illegal at IF.

## Bound (stamp this on harness tickets / eval contract)

| Gate | Metric | KEEP threshold | Notes |
|------|--------|----------------|-------|
| Speckle (existing) | holdout mean `speckle` | `< 0.15` | unchanged |
| Photons (existing) | holdout mean `photons_kept` | `≥ 0.55` | unchanged; discard → VOID |
| **Pupil (NEW)** | holdout mean `pupil_fill_error` | **`≤ 0.10`** | RMSE-style error vs fill target |

**Ticket guard string:** `if_spec_pupil_err_max=0.10`  
(replaces pending `if_spec_pupil_bound_pending`)

## Rationale

- SEED baseline (HT-1002): `pupil_err=0.2250`. KEEP must beat baseline, not ignore it.
- Card target is fill fraction `pupil_fill_target=0.72`; the harness metric is `pupil_fill_error` (mean absolute error). Gate the error metric, cite the fill target as the conditioner goal.
- `0.10` is ~2.25× better than SEED and still synthetic/open-proxy — not a production EXE claim.

## Eval wiring

Frozen `eval.py` currently decides KEEP on `s_h < 0.15 and ph_h >= PHOTON_FLOOR` only. **Eval Integrity** must AND `p_h <= 0.10` into KEEP (new eval version / stamp; do not mid-run edit on live islands). Until wired, dual-gate tickets carry the guard and **must not claim P2/illuminator feed** off a pupil-blind KEEP.

## Explicit non-decisions

- Not waiving in `thesis.md`.
- Not changing `pupil_fill_target=0.72` on the assumption card.
- Not a product KEEP — still research until P2/P10 product contract exists.
