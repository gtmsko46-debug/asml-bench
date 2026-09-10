"""Baseline IF shim. Harness may edit this file only. Synthetic; not ASML fab data."""

# Intentionally weak SEED
FILL_GAIN = 0.02
PHOTON_KEEP = 1.0


def shim(row: dict) -> dict:
    coherence = float(row.get("coherence", 0.5))
    bandwidth = float(row.get("bandwidth", 0.02))
    power_frac = float(row.get("power_frac", 0.7))
    pol = float(row.get("pol_degree", 0.5))
    pulse = float(row.get("pulse_structure", 0.5))
    pointing = float(row.get("pointing_jitter", 0.05))

    fill = 0.48 + 0.22 * coherence - 2.2 * bandwidth
    fill = fill + FILL_GAIN * (0.72 - fill)
    fill = max(0.0, min(1.0, fill))
    pupil_fill_error = abs(fill - 0.72)

    photons_kept = PHOTON_KEEP * max(0.0, min(1.0, 0.75 * power_frac + 0.1 * coherence))
    if_loss_db = 1.5 + pupil_fill_error
    pol_contrast_proxy = 0.2 * pol
    pulse_envelope_proxy = 0.3 * pulse
    pointing_err_proxy = pointing * 1.2
    if_compat_score = max(0.0, 1.0 - pupil_fill_error) * 0.25 + photons_kept * 0.75

    return {
        "pupil_fill_error": float(pupil_fill_error),
        "photons_kept": float(photons_kept),
        "if_loss_db": float(if_loss_db),
        "pol_contrast_proxy": float(pol_contrast_proxy),
        "pulse_envelope_proxy": float(pulse_envelope_proxy),
        "pointing_err_proxy": float(pointing_err_proxy),
        "if_compat_score": float(if_compat_score),
        "etendue_proxy": "pupil_fill_error",
    }
