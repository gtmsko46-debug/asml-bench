"""IF shim sandbox (FEL-10 / P10). Harness may edit this file only."""

PHOTON_KEEP = 1.0
PUPIL_FILL_TARGET = 0.72
IF_LOSS_DB = 0.8
POL_CONTRAST_COEFF = 0.35
TEMPORAL_COHERENCE_UM = 12.0
IF_COUPLING = 0.55
PUPIL_UNIFORMITY_GAIN = 0.12
ILLUMINATOR_ACCEPTANCE_BASE = 0.70
SPATIAL_SIGMA = 0.15


def shim(field: dict) -> dict:
    pupil_in = float(field.get("pupil_fill_error", 0.22))
    photons_in = float(field.get("photons", 1.0))
    bandwidth = float(field.get("bandwidth", 0.02))
    pol_degree = float(field.get("pol_degree", 0.5))
    pulse_structure = float(field.get("pulse_structure", 1.0))
    pointing_jitter = float(field.get("pointing_jitter", 0.05))

    etendue_assist = PUPIL_UNIFORMITY_GAIN * IF_COUPLING
    etendue_assist *= max(0.0, 1.0 - SPATIAL_SIGMA * bandwidth / 0.05)
    etendue_assist = max(0.0, min(0.07, etendue_assist))
    fill = (PUPIL_FILL_TARGET - pupil_in) + etendue_assist
    pupil_err = abs(fill - PUPIL_FILL_TARGET)

    photons_kept = PHOTON_KEEP * photons_in
    if_loss_db = IF_LOSS_DB + 0.25 * pupil_err
    pol_contrast_proxy = POL_CONTRAST_COEFF * pol_degree
    pulse_envelope_proxy = TEMPORAL_COHERENCE_UM * max(0.0, pulse_structure)
    pointing_err_proxy = (1.0 - ILLUMINATOR_ACCEPTANCE_BASE) + pointing_jitter

    return {
        "pupil_fill_error": float(pupil_err),
        "photons_kept": float(photons_kept),
        "if_loss_db": float(if_loss_db),
        "pol_contrast_proxy": float(pol_contrast_proxy),
        "pulse_envelope_proxy": float(pulse_envelope_proxy),
        "pointing_err_proxy": float(pointing_err_proxy),
    }
