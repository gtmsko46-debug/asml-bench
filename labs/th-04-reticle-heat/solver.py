"""Baseline reduced-order reticle-heating → overlay model. Harness may edit this file only."""
import math

# Intentionally weak SEED: constant + tiny duty term (missing proper thermal coupling)
THERMAL_COEF = 0.05  # nm per duty-cycle unit; should be learned upward


def predict_overlay(lot: dict) -> list[float]:
    """Return predicted overlay residual vector (nm, synthetic) for die grid samples."""
    duty = float(lot["duty_cycle"])
    exposure = float(lot.get("exposure_s", 1.0))
    refl = float(lot.get("reticle_reflectivity", 0.9))
    absorbed = duty * exposure * (1.0 - refl)
    base = THERMAL_COEF * absorbed
    n = int(lot.get("n_dies", 16))
    # simple radial-ish pattern
    out = []
    for i in range(n):
        r = (i + 1) / n
        out.append(base * (0.7 + 0.3 * r))
    return out
