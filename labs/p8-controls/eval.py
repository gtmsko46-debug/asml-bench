#!/usr/bin/env python3
"""Frozen P8 controls evaluator. Do not edit during a harness run."""
from __future__ import annotations
import hashlib, json, math, sys
from pathlib import Path
import importlib.util

ROOT = Path(__file__).resolve().parent
FIX = ROOT / "fixture"

def load(name):
    return json.loads((FIX / name).read_text())

def main() -> int:
    hold_raw = (FIX / "holdout.json").read_bytes()
    digest = hashlib.sha256(hold_raw).hexdigest()
    expected = (FIX / "HOLDOUT.sha256").read_text().strip().split()[0]
    if digest != expected:
        print("VOID\thash_mismatch")
        return 2
    spec = importlib.util.spec_from_file_location("controller", ROOT / "controller.py")
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    def rmse(rows):
        errs = []
        for r in rows:
            pred = float(mod.recover(r)["t_recover_ms"])
            errs.append((pred - float(r["truth_t_recover_ms"])) ** 2)
        return math.sqrt(sum(errs) / len(errs))
    tr, ho, tp = rmse(load("train.json")), rmse(load("holdout.json")), rmse(load("cheat_trap.json"))
    voids = []
    if "truth_t_recover" in (ROOT / "controller.py").read_text():
        voids.append("oracle_peek")
    decision = "VOID" if voids else ("KEEP" if ho < 5 else ("SEED" if ho < 25 else "RESET"))
    print(f"p8\ttrain_rmse={tr:.4f}\tholdout_rmse={ho:.4f}\ttrap_rmse={tp:.4f}\tdecision={decision}\tvoids={','.join(voids) or '-'}")
    tsv = ROOT / "results.tsv"
    if not tsv.exists():
        tsv.write_text("ticket\ttrain_rmse\tholdout_rmse\ttrap_rmse\tdecision\n")
    with tsv.open("a") as f:
        f.write(f"local\t{tr:.4f}\t{ho:.4f}\t{tp:.4f}\t{decision}\n")
    return 0 if decision != "VOID" else 2

if __name__ == "__main__":
    raise SystemExit(main())
