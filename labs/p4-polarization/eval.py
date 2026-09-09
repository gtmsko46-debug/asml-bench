#!/usr/bin/env python3
"""Frozen eval for P4 polarization-aware comp-litho toy. Do not edit in harness runs."""
from __future__ import annotations

import argparse
import ast
import json
import math
import sys
from collections import defaultdict
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


def solver_hardcodes_single_na(src: str) -> bool:
    """Light commonality guard: reject solvers that branch on one literal NA."""
    try:
        tree = ast.parse(src)
    except SyntaxError:
        return True
    for node in ast.walk(tree):
        if isinstance(node, ast.Compare):
            left = node.left
            if isinstance(left, ast.Name) and left.id == "na":
                for comp in node.comparators:
                    if isinstance(comp, ast.Constant) and isinstance(comp.value, (int, float)):
                        return True
            if isinstance(left, ast.Subscript):
                pass
            # row["na"] == 0.75 style
            if isinstance(left, ast.Subscript):
                sl = left.slice
                if isinstance(sl, ast.Constant) and sl.value == "na":
                    for comp in node.comparators:
                        if isinstance(comp, ast.Constant) and isinstance(comp.value, (int, float)):
                            return True
    return False


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--fixture", default="holdout.json", choices=["holdout.json", "cheat_trap.json", "train.json"])
    args = ap.parse_args()
    rows = load_rows(args.fixture)
    src = (LAB / "solver.py").read_text()
    if solver_hardcodes_single_na(src):
        print("GUARD_FAIL commonality: solver hardcodes a literal NA comparison")
        return 2

    pw_pairs, epe_pairs = [], []
    by_na = defaultdict(list)
    for row in rows:
        pred = solve(row)
        if not isinstance(pred, dict) or "pw_area" not in pred or "epe_nm" not in pred:
            print("GUARD_FAIL solver must return dict with pw_area and epe_nm")
            return 2
        pw_pairs.append((float(pred["pw_area"]), float(row["pw_area"])))
        epe_pairs.append((float(pred["epe_nm"]), float(row["epe_nm"])))
        by_na[row["na"]].append(1)

    if args.fixture == "holdout.json":
        for na, xs in by_na.items():
            if len(xs) < 5:
                print(f"GUARD_FAIL holdout NA bucket too small: na={na} n={len(xs)}")
                return 2
        if len(by_na) < 3:
            print("GUARD_FAIL holdout must cover >=3 NA values")
            return 2

    r_pw, r_epe = rmse(pw_pairs), rmse(epe_pairs)
    # crude normalization by target std
    def std(vals):
        m = sum(vals) / len(vals)
        return math.sqrt(sum((v - m) ** 2 for v in vals) / len(vals)) or 1.0

    pw_std = std([b for _, b in pw_pairs])
    epe_std = std([b for _, b in epe_pairs])
    combined = 0.5 * (r_pw / pw_std) + 0.5 * (r_epe / epe_std)
    print(
        f"P4 fixture={args.fixture} n={len(rows)} rmse_pw={r_pw:.6f} rmse_epe={r_epe:.6f} combined={combined:.6f}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
