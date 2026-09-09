"""Baseline coherence conditioner. Harness may edit this file only."""

# Identity diffuser: barely helps speckle; keeps all photons
DIFFUSER_STRENGTH = 0.05  # 0..1
PHOTON_KEEP = 1.0         # must stay high; throwing away photons is a VOID


def condition(field: dict) -> dict:
    """Return conditioned field moments for IF."""
    coherence = float(field["coherence"])
    # weak conditioning
    out_coh = coherence * (1.0 - 0.5 * DIFFUSER_STRENGTH)
    speckle = max(0.02, out_coh * 0.5)
    pupil_err = abs(float(field.get("pupil_fill_error", 0.2)) - 0.1 * DIFFUSER_STRENGTH)
    return {
        "speckle": speckle,
        "pupil_fill_error": pupil_err,
        "photons_kept": PHOTON_KEEP * float(field.get("photons", 1.0)),
    }
