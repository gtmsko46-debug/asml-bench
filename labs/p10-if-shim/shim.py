"""IF shim sandbox (FEL-10 / P10). Harness may edit this file only."""

# Tunables (SEED baseline — honest, no photon discard)
PUPIL_CORRECT = 0.02          # weak pupil nudge toward target
PHOTON_KEEP = 1.0             # must stay 1.0 on SEED; discard → VOID
IF_LOSS_DB = 0.8              # cite coherence-if-v1
POL_CONTRAST_PROXY = 0.35     # cite imaging-optics-v1 pol_contrast_coeff
PULSE_ENVELOPE_PROXY = 12.0   # cite fel-source-v1 temporal_coherence_length_um
POINTING_ERR_PROXY = 0.30     # interim; twin illuminator_acceptance_base=0.70 → err proxy 1-0.70


def shim(field: dict) -> dict:
    """Map IF input field → five IF Spec axis reports + photons_kept."""
    pupil_in = float(field.get("pupil_fill_error", 0.22))
    photons_in = float(field.get("photons", 1.0))
    # weak correction only — SEED may still exceed 0.10 KEEP AND
    pupil_err = max(0.0, pupil_in - PUPIL_CORRECT)
    photons_kept = PHOTON_KEEP * photons_in
    return {
        "pupil_fill_error": pupil_err,
        "photons_kept": photons_kept,
        "if_loss_db": float(field.get("if_loss_db", IF_LOSS_DB)),
        "pol_contrast_proxy": float(field.get("pol_contrast_proxy", POL_CONTRAST_PROXY)),
        "pulse_envelope_proxy": float(field.get("pulse_envelope_proxy", PULSE_ENVELOPE_PROXY)),
        "pointing_err_proxy": float(field.get("pointing_err_proxy", POINTING_ERR_PROXY)),
    }
