#!/usr/bin/env python3
"""Frozen TH-04 evaluator. Do not edit during a harness run."""
from __future__ import annotations
import json, math, hashlib, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
FIX = ROOT / "fixture"

def load(name):
    return json.loads((FIX / name).read_text())

def rmse(pred, truth):
    if len(pred) != len(truth):
        return 1e9
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(pred, truth)) / len(truth))

def check_guards(solver_src: str, train_rmse: float, hold_rmse: float) -> list[str]:
    voids = []
    if "platform" in solver_src and "NXE" in solver_src:
        voids.append("commonality: NXE special-case")
    # thermal term ~0
    if "THERMAL_COEF" in solver_src:
        for line in solver_src.splitlines():
            if "THERMAL_COEF" in line and "=" in line and not line.strip().startswith("#"):
                try:
                    val = float(line.split("=")[1].split("#")[0].strip())
                    if abs(val) < 1e-6:
                        voids.append("physics: thermal coefficient ~0")
                except Exception:
                    pass
    if "mlp" in solver_src.lower() or "sklearn" in solver_src.lower() or "torch" in solver_src.lower():
        # cheat trap: if train much better than holdout
        if train_rmse + 0.15 < hold_rmse:
            voids.append("cheat-trap: unconstrained fit overfit")
    return voids

def main():
    # verify holdout hash
    hold_raw = (FIX / "holdout.json").read_bytes()
    digest = hashlib.sha256(hold_raw).hexdigest()
    expected = (FIX / "HOLDOUT.sha256").read_text().strip().split()[0]
    if digest != expected:
        print(f"VOID hash_mismatch got={digest} expected={expected}")
        sys.exit(2)

    import importlib.util
    spec = importlib.util.spec_from_file_location("solver", ROOT / "solver.py")
    solver = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solver)

    train = load("train.json")
    hold = load("holdout.json")
    trap = load("cheat_trap.json")

    def score(lots):
        errs = []
        for lot in lots:
            pred = solver.predict_overlay(lot)
            errs.append(rmse(pred, lot["overlay_nm"]))
        return sum(errs) / len(errs)

    train_rmse = score(train)
    hold_rmse = score(hold)
    trap_rmse = score(trap)
    src = (ROOT / "solver.py").read_text()
    voids = check_guards(src, train_rmse, hold_rmse)

    decision = "RESET"
    if voids:
        decision = "VOID"
    elif hold_rmse < 1.6:  # weak bar for KEEP candidate on synthetic
        decision = "KEEP"
    elif hold_rmse <= train_rmse * 1.5:
        decision = "SEED" if hold_rmse > 1.7 else "RESET"

    print(f"th-04\ttrain_rmse={train_rmse:.4f}\tholdout_rmse={hold_rmse:.4f}\ttrap_rmse={trap_rmse:.4f}\tdecision={decision}\tvoids={','.join(voids) or '-'}")
    # append results
    tsv = ROOT / "results.tsv"
    if not tsv.exists():
        tsv.write_text("thesis\trun\thypothesis\tprovider\tmetric\tdecision\tcard\n")
    # caller/Foreman appends; we just report
    return 0 if decision != "VOID" else 3

if __name__ == "__main__":
    raise SystemExit(main())
