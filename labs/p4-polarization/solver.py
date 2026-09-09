#!/usr/bin/env python3
"""Baseline P4 solver — weak synthetic model. Harness may edit this file only."""
from __future__ import annotations

import math


def solve(row: dict) -> dict:
    """Predict pw_area and epe_nm from polarization-aware imaging inputs."""
    na = float(row["na"])
    pitch_nm = float(row["pitch_nm"])
    pol_degree = float(row["pol_degree"])
    pol_angle_deg = float(row["pol_angle_deg"])
    dose = float(row["dose"])
    defocus = float(row["defocus"])
    blur = float(row["blur"])

    # Honest-ish baseline (same formula family as fixture truth; slight coefficient miss so not perfect)
    contrast = (
        0.38
        + 0.33 * pol_degree * abs(math.sin(2.0 * math.radians(pol_angle_deg)))
        + 0.14 * (na / 0.55)
    )
    pw_area = contrast * dose / (1.0 + 0.55 * blur + 0.28 * abs(defocus)) * (pitch_nm / 40.0)
    epe_nm = 2.6 / max(contrast, 0.1) + 0.75 * abs(defocus) + 0.22 * blur
    return {"pw_area": pw_area, "epe_nm": epe_nm}
