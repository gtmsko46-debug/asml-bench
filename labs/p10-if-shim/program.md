# program.md — FEL-10 IF ownership

## Bindings

- **thesis:** `fel-10-if-ownership`
- **assumption_cards:** `coherence-if-v1`, `fel-source-v1`, `imaging-optics-v1`, `fel-scanner-twin-v1` (cite only; IF Spec contract)
- **provider:** stamp per ticket — `grok` (xai/grok-4.6) / `mock-mistral` (xai/grok-4.20-0309-non-reasoning)
- **sandbox:** `shim.py`
- **metric:** `if_compat_score` (multi-axis — see `tickets/IF_SPEC_FEL10_CONTRACT.md`)
- **budget:** stamp on ticket (multi-hour FUNDED behind P1)
- **ticket_id:** stamp on ticket (Experimentalist)
- **contract:** `tickets/IF_SPEC_FEL10_CONTRACT.md`

## Hypothesis (one sentence)

Stamp exactly one hypothesis on the Harness Ticket; copy it here for the run.
Default SEED: `SEED: IF shim reports all five IF Spec axes (pupil/etendue, power, pol, pulse, pointing) under coherence/IF cards without discarding photons.`

## Mandatory axes (IF Spec)

| Axis | SEED | Research KEEP AND |
|------|------|-------------------|
| Pupil/etendue (`pupil_fill_error`) | report | ≤ 0.10 |
| Power (`photons_kept`, `if_loss_db`) | report; no discard | photons_kept ≥ 0.55 |
| Polarization (`pol_contrast_proxy`) | non-null report | deferred |
| Pulse (`pulse_envelope_proxy`) | non-null report | deferred |
| Pointing (`pointing_err_proxy`) | non-null report | deferred |

Missing axis field → VOID. Soft `if_compat_score` ranks only — never KEEP alone.

## Guards

- `if_spec_fel10_contract_bound`
- `if_spec_pupil_err_max=0.10`
- `if_axes_report_pupil_power_pol_pulse_pointing`
- `no_photon_discard_cheat`
- `no_rewrite_if_spec` / `no_mutate_coherence-if-v1`
- `frozen_eval_untouched` / `holdout_hash_match`
- `no_pol_pulse_pointing_KEEP_claim`
- `no_lpp-source-v2_on_scaffold_seed`
- `no_upstairs_without_warden_tco`
- Critic: multi-axis `if_compat_score` before SEED (locked via CoS 2026-09-10)

## Must not touch

- `eval.py`
- `fixture/holdout*`
- `fixture/cheat_trap.json`
- `fixture/HOLDOUT.sha256`
- assumption cards under `assumptions/`

## Cheat-trap / RESET notes

Photon discard → VOID. Missing axis → VOID. Holdout hash must match after RESET.

## Dual-lane note

Same frozen `eval.py` + holdout for both lanes. Single-provider demos blocked. Champion copy: second-engine / mistral-lane — never trash Mistral or tin-LPP.

## Status

- **FUNDED** behind P1 · **IF Spec contract seated** · **Critic multi-axis falsifiers locked**
- **Gate left:** Warden honesty + Experimentalist real HT ids · then Foreman
- Thin `if-ownership-v1` deferred until after SEED (IF Spec non-decision)

## Warden

ACCEPT vs-LPP on `lpp-source-v2` only. Honesty bars on claim draft; scaffold SEED unbound to LPP.
