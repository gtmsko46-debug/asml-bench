#!/usr/bin/env python3
"""Baseline P7 solver — weak synthetic model. Harness may edit this file only."""
from __future__ import annotations


def solve(row: dict) -> dict:
    """Predict process-window proxies at 13.5 or 6.x nm. 6.7 is not free."""
    wavelength_nm = float(row["wavelength_nm"])
    na = float(row["na"])
    multilayer_R = float(row["multilayer_R"])
    resist_blur_nm = float(row["resist_blur_nm"])
    dose = float(row["dose"])
    k1_proxy = float(row["k1_proxy"])

    # Slightly misspecified vs fixture truth
    if wavelength_nm >= 13.0:
        optics_penalty = 1.0
    else:
        optics_penalty = 0.52 + 0.48 * multilayer_R
    resist_penalty = 1.0 + 0.085 * resist_blur_nm * (13.5 / wavelength_nm)
    pw_area = (dose * k1_proxy * na * optics_penalty) / resist_penalty

    # Matched 13.5 reference with same other inputs
    pw135 = (dose * k1_proxy * na * 1.0) / (1.0 + 0.085 * resist_blur_nm * (13.5 / 13.5))
    relative_to_135 = pw_area / max(pw135, 1e-9)
    return {"pw_area": pw_area, "relative_to_135": relative_to_135}
