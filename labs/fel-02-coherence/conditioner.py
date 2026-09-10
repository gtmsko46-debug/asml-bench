def condition(field: dict) -> dict:
    coherence = float(field.get("coherence", 0.8))
    bandwidth = float(field.get("bandwidth", 0.001))
    pfe = float(field.get("pupil_fill_error", 0.25))
    photons = float(field.get("photons", 1.0))

    fill_target = 0.72
    pupil_err = abs(pfe - fill_target) * 0.204

    speckle = coherence * bandwidth * 110.0

    return {
        "speckle": speckle,
        "pupil_fill_error": pupil_err,
        "photons_kept": photons,
    }
