#!/usr/bin/env python3
"""Baseline P8 glitch recovery — weak SEED. Harness may edit this file only."""
from __future__ import annotations


def recover(row: dict) -> dict:
    n_tools = int(row.get("n_tools", 4))
    severity = float(row.get("glitch_severity", 0.3))
    duration_ms = float(row.get("glitch_duration_ms", 50.0))
    overlay_open = float(row.get("overlay_open_nm", 2.0))
    # slight miss vs truth (1.05)
    t_recover_ms = duration_ms * (1.0 + 1.5 * severity) * (0.5 + 0.5 * n_tools / 4.0) * 1.05
    wafers_lost = (t_recover_ms / 60000.0) * float(row.get("wafers_per_min", 2.0)) * n_tools
    residual = overlay_open * severity * 0.4
    return {
        "t_recover_ms": float(t_recover_ms),
        "wafers_lost_proxy": float(wafers_lost),
        "residual_overlay_nm": float(residual),
        "recovery_ok": bool(residual < 1.0 and t_recover_ms < 500.0),
        "tools_affected": n_tools,
    }
