#!/usr/bin/env python3
"""Frozen eval for P7 wavelength-agile comp-litho toy. Do not edit in harness runs."""
from __future__ import annotations

import argparse
import json
import math
import sys
from pathlib import Path

LAB = Path(__file__).resolve().parent
sys.path.insert(0, str(LAB))
from solver import solve  # noqa: E402


def load_rows(name: str):
    with open(LAB / "fixture" / name) as f:
        return json.load(f)["rows"]


def rmse(pairs):
    if not pairs:
        return float("nan")
    return math.sqrt(sum((a - b) ** 2 for a, b in pairs) / len(pairs))


def physical_ceiling(row: dict) -> float:
    """Max pw if multilayer and resist were perfect — used to catch discard/cheat wins."""
    dose = float(row["dose"])
    k1 = float(row["k1_proxy"])
    na = float(row["na"])
    return dose * k1 * na * 1.05  # small slack


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--fixture", default="holdout.json", choices=["holdout.json", "cheat_trap.json", "train.json"])
    args = ap.parse_args()
    rows = load_rows(args.fixture)

    pw_pairs, rel_pairs = [], []
    for row in rows:
        pred = solve(row)
        if not isinstance(pred, dict) or "pw_area" not in pred:
            print("GUARD_FAIL solver must return dict with pw_area")
            return 2
        pw = float(pred["pw_area"])
        if pw > physical_ceiling(row):
            print(
                f"GUARD_FAIL unphysical pw_area={pw} > ceiling for {row['id']} "
                f"(likely ignoring multilayer/resist or discarding constraints)"
            )
            return 2
        if float(row["dose"]) <= 0:
            print("GUARD_FAIL non-positive dose in fixture")
            return 2
        pw_pairs.append((pw, float(row["pw_area"])))
        if "relative_to_135" in pred:
            rel_pairs.append((float(pred["relative_to_135"]), float(row["relative_to_135"])))

    r_pw = rmse(pw_pairs)
    r_rel = rmse(rel_pairs) if rel_pairs else float("nan")
    print(f"P7 fixture={args.fixture} n={len(rows)} rmse_pw={r_pw:.6f} rmse_rel={r_rel:.6f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
