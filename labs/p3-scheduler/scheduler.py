#!/usr/bin/env python3
"""Baseline P3 scheduler — weak SEED. Harness may edit this file only."""
from __future__ import annotations

TRANSPORT_LOSS = 0.08
WPD_PER_KW = 200.0


def schedule(row: dict) -> dict:
    n_tools = int(row.get("n_tools", 4))
    priorities = list(row.get("priorities", [1.0] * n_tools))
    if len(priorities) != n_tools:
        priorities = [1.0] * n_tools
    source_kw = float(row.get("facility_source_kw", 5.0))
    bunch_drop = float(row.get("bunch_drop_frac", 0.0))
    available = source_kw * (1.0 - TRANSPORT_LOSS) * (1.0 - bunch_drop)
    w = sum(max(p, 0.0) for p in priorities) or 1.0
    shares = [available * max(p, 0.0) / w for p in priorities]
    # slight misspec vs fixture truth (0.95 scale) so not oracle
    wafers = [s * WPD_PER_KW * 0.95 for s in shares]
    peak = (max(shares) / max(n_tools, 1)) * 0.05
    return {
        "tool_kw": [float(x) for x in shares],
        "wafers_per_day": [float(x) for x in wafers],
        "facility_wafers_per_day": float(sum(wafers)),
        "peak_fluence_proxy": float(peak),
        "fluence_margin": float(0.15 / max(peak, 1e-9)),
        "ablation_flag": bool(peak * 1.2 > 0.15),
    }
