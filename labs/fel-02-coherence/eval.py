#!/usr/bin/env python3
"""Frozen FEL-02 evaluator. Do not edit during a harness run."""
from __future__ import annotations
import json, hashlib, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
FIX = ROOT / "fixture"
PHOTON_FLOOR = 0.55

def load(name):
    return json.loads((FIX / name).read_text())

def main():
    hold_raw = (FIX / "holdout.json").read_bytes()
    digest = hashlib.sha256(hold_raw).hexdigest()
    expected = (FIX / "HOLDOUT.sha256").read_text().strip().split()[0]
    if digest != expected:
        print(f"VOID hash_mismatch")
        sys.exit(2)

    import importlib.util
    spec = importlib.util.spec_from_file_location("conditioner", ROOT / "conditioner.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)

    def score(fields):
        speckles, pupils, photons = [], [], []
        for f in fields:
            o = mod.condition(f)
            speckles.append(o["speckle"])
            pupils.append(o["pupil_fill_error"])
            photons.append(o["photons_kept"])
        return sum(speckles)/len(speckles), sum(pupils)/len(pupils), sum(photons)/len(photons)

    train = load("train.json")
    hold = load("holdout.json")
    trap = load("cheat_trap.json")
    s_tr, p_tr, ph_tr = score(train)
    s_h, p_h, ph_h = score(hold)
    s_c, p_c, ph_c = score(trap)

    src = (ROOT / "conditioner.py").read_text()
    voids = []
    if ph_h < PHOTON_FLOOR:
        voids.append("photon_budget")
    if "PHOTON_KEEP" in src:
        for line in src.splitlines():
            if line.strip().startswith("PHOTON_KEEP"):
                try:
                    val = float(line.split("=")[1].split("#")[0].strip())
                    if val < PHOTON_FLOOR:
                        voids.append("photon_keep_param")
                except Exception:
                    pass

    decision = "RESET"
    if voids:
        decision = "VOID"
    elif s_h < 0.15 and ph_h >= PHOTON_FLOOR:
        decision = "KEEP"
    elif s_h < 0.45:
        decision = "SEED"

    print(f"fel-02\tspeckle={s_h:.4f}\tpupil_err={p_h:.4f}\tphotons_kept={ph_h:.4f}\tdecision={decision}\tvoids={','.join(voids) or '-'}\ttrap_speckle={s_c:.4f}")
    return 0 if decision != "VOID" else 3

if __name__ == "__main__":
    raise SystemExit(main())
