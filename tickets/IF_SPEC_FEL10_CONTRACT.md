# IF Spec contract — FEL-10 / P10 IF shim (2026-09-10)

**Owner:** IF Spec Owner  
**Lab:** `labs/p10-if-shim` · sandbox `shim.py` · metric `if_compat_score`  
**Tickets:** HT-1028 (grok) ∧ HT-1029 (mock-mistral) SEED dual-gate

## Sacred IF axes

| Axis | Field | SEED | Research KEEP AND |
|------|-------|------|-------------------|
| Pupil / etendue | `pupil_fill_error` | report | **≤ 0.10** |
| Power | `photons_kept`, `if_loss_db` | report; **no discard** | photons_kept **≥ 0.55** (SEED ticket hard `==1.0`) |
| Polarization | `pol_contrast_proxy` | non-null report | deferred (not waived) |
| Pulse | `pulse_envelope_proxy` | non-null report | deferred |
| Pointing | `pointing_err_proxy` | non-null report | deferred |

Missing / null / NaN axis → **VOID**. Soft `if_compat_score` ranks only — **never KEEP alone**.

## Frozen eval gates (`labs/p10-if-shim/eval.py`)

- **VOID:** missing axes; `PHOTON_KEEP < 1.0`; holdout mean `photons_kept < 1.0`
- **KEEP:** `pupil_fill_error ≤ 0.10` **AND** `photons_kept ≥ 0.55`
- **SEED:** all axes present, no voids, not yet KEEP
- Cheat trap: low-photon inputs (discard paths must not KEEP)

## HOLDOUT

Frozen digest: `d0dc1f8a7b8cc97ddd00122fb4156252c7642a09a7f0ae5102b939747c6cc5be`

## Cards (SEED)

`coherence-if-v1`, `fel-source-v1`, `imaging-optics-v1`, `fel-scanner-twin-v1` — read-only. No `lpp-source-v2` on scaffold SEED.

## Ticket guards

`if_spec_fel10_contract_bound` · `if_spec_pupil_err_max=0.10` · `if_axes_report_pupil_power_pol_pulse_pointing` · `no_photon_discard_cheat` · `photons_kept_eq_1.0`
