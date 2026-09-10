"""Baseline coherence conditioner. Harness may edit this file only."""

DIFFUSER_STRENGTH = 0.05
PHOTON_KEEP = 1.0


def condition(field: dict) -> dict:
    """Return conditioned field moments for IF."""
    coherence = float(field["coherence"])
    bandwidth = float(field.get("bandwidth", 0.001))
    # field coherence+bandwidth for speckle
    speckle = max(0.02, coherence * 0.08 * (1.0 + bandwidth / 0.001))
    pupil_err = abs(float(field.get("pupil_fill_error", 0.2)) - 0.72) * 0.2
    out_coh = coherence * (1.0 - 0.5 * DIFFUSER_STRENGTH)
    return {
        "speckle": speckle,
        "pupil_fill_error": pupil_err,
        "photons_kept": PHOTON_KEEP * float(field.get("photons", 1.0)),
    }
