"""IF shim sandbox (FEL-10 / P10). Harness may edit this file only."""

PUPIL_CORRECT = 0.02
PHOTON_KEEP = 1.0
IF_LOSS_DB = 0.8
POL_CONTRAST_PROXY = 0.35
PULSE_ENVELOPE_PROXY = 12.0
POINTING_ERR_PROXY = 0.30


def shim(field: dict) -> dict:
    pupil_in = float(field.get("pupil_fill_error", 0.22))
    photons_in = float(field.get("photons", 1.0))
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
