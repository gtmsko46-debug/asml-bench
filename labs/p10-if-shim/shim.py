"""IF shim sandbox (FEL-10 / P10). Harness may edit this file only."""
PHOTON_KEEP = 1.0
FILL_GAIN = 0.40
PUPIL_FILL_TARGET = 0.72


def shim(field: dict) -> dict:
    """Reconstruct fill from coherence/bandwidth/power; correct toward 0.72."""
    coherence = float(field.get("coherence", 0.5))
    bandwidth = float(field.get("bandwidth", 0.02))
    power_frac = float(field.get("power_frac", 0.7))
    pol = float(field.get("pol_degree", field.get("pol_contrast_proxy", 0.5)))
    pulse = float(field.get("pulse_structure", field.get("pulse_envelope_proxy", 0.5)))
    pointing = float(field.get("pointing_jitter", field.get("pointing_err_proxy", 0.05)))

    fill = 0.45 + 0.25 * coherence - 1.5 * bandwidth + 0.1 * power_frac
    fill = fill + FILL_GAIN * (PUPIL_FILL_TARGET - fill)
    fill = max(0.0, min(1.0, fill))
    pupil_err = abs(fill - PUPIL_FILL_TARGET)

    return {
        "pupil_fill_error": float(pupil_err),
        "photons_kept": float(PHOTON_KEEP * float(field.get("photons", 1.0))),
        "if_loss_db": float(1.0 + (1.0 - power_frac)),
        "pol_contrast_proxy": float(0.3 * pol),
        "pulse_envelope_proxy": float(0.4 * pulse + 8.0),
        "pointing_err_proxy": float(pointing * 1.1),
        "if_compat_score": float(max(0.0, 1.0 - pupil_err) * 0.4 + 0.6),
    }
