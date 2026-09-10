"""Baseline coherence conditioner. Harness may edit this file only."""

def condition(field: dict) -> dict:
    """Return conditioned field moments for IF."""
    pfe = float(field.get("pupil_fill_error", 0.25))
    fill = 1.0 - pfe
    fill = fill + 0.3 * (0.72 - fill)
    fill = max(0.0, min(1.0, fill))
    pupil_err = abs(fill - 0.72)
    coherence = float(field.get("coherence", 0.8))
    bandwidth = float(field.get("bandwidth", 0.001))
    speckle = coherence * bandwidth * 120.0
    photons = float(field.get("photons", 1.0))
    return {
        "speckle": speckle,
        "pupil_fill_error": pupil_err,
        "photons_kept": 1.0 * photons,
    }
