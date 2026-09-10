#!/usr/bin/env python3
"""Baseline P9 TCO — weak SEED from tco-v1. Harness may edit this file only."""
from __future__ import annotations

CARD_TOOL_CAPITAL_MUSD = 150.0
CARD_CONSUMABLES = 5.0


def compare(row: dict) -> dict:
    wpd = float(row.get("wafers_per_day", 1000.0))
    years = float(row.get("horizon_years", 5.0))
    lpp_cap = float(row.get("lpp_capital_m_usd", CARD_TOOL_CAPITAL_MUSD))
    fel_cap = float(row.get("fel_capital_m_usd", CARD_TOOL_CAPITAL_MUSD * 1.15))
    lpp_cons = float(row.get("lpp_consumables_per_wafer_usd", CARD_CONSUMABLES))
    fel_cons = float(row.get("fel_consumables_per_wafer_usd", CARD_CONSUMABLES * 0.7))
    fel_collector = float(row.get("fel_collector_m_usd_per_year", 8.0))
    lpp_source = float(row.get("lpp_source_m_usd_per_year", 12.0))
    days = years * 365.0
    wafers = wpd * days
    lpp_tco = lpp_cap + wafers * lpp_cons / 1e6 + lpp_source * years
    fel_tco = fel_cap + wafers * fel_cons / 1e6 + fel_collector * years
    # tiny miss
    fel_tco *= 1.01
    delta = fel_tco - lpp_tco
    winner = "lpp" if delta > 0 else ("fel" if delta < 0 else "tie")
    return {
        "lpp_tco_m_usd": float(lpp_tco),
        "fel_tco_m_usd": float(fel_tco),
        "delta_fel_minus_lpp_m_usd": float(delta),
        "winner": winner,
        "wafers_modeled": float(wafers),
    }
