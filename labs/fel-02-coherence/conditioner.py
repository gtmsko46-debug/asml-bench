"""Baseline coherence conditioner. Harness may edit this file only."""

# Field coherence+bandwidth targeting literal pupil_fill_target=0.72; pupil_err=|fill-0.72|
PHOTON_KEEP = 1.0


def condition(field: dict) -> dict:
    """Return conditioned field moments for IF."""
    coherence = float(field["coherence"])
    bandwidth = float(field.get("bandwidth", 0.001))
    fill = 0.72 + (coherence - 0.8) * 0.15 + (bandwidth - 0.001) * 80.0
    pupil_err = abs(fill - 0.72)
    speckle = max(0.02, (1.0 - coherence) * 0.9)
    return {
        "speckle": speckle,
        "pupil_fill_error": pupil_err,
        "photons_kept": PHOTON_KEEP * float(field.get("photons", 1.0)),
    }
