#!/usr/bin/env python3
"""Frozen P10 / FEL-10 IF shim evaluator. Do not edit during a harness run."""
from __future__ import annotations
import json, hashlib, math, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
FIX = ROOT / "fixture"
PHOTON_FLOOR = 0.55
PUPIL_MAX = 0.10

def load(name):
    return json.loads((FIX / name).read_text())

def rmse(pred, truth):
    if len(pred) != len(truth):
        return 1e9
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(pred, truth)) / max(1, len(truth)))

def main():
    hold_raw = (FIX / "holdout.json").read_bytes()
    digest = hashlib.sha256(hold_raw).hexdigest()
    expected = (FIX / "HOLDOUT.sha256").read_text().strip().split()[0]
    if digest != expected:
        print("VOID hash_mismatch")
        return 2

    import importlib.util
    spec = importlib.util.spec_from_file_location("shim", ROOT / "shim.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)

    def score(rows):
        pupils, photons, comps, truths = [], [], [], []
        for r in rows:
            o = mod.shim(r)
            for k in ("pupil_fill_error", "photons_kept", "if_compat_score",
                      "if_loss_db", "pol_contrast_proxy", "pulse_envelope_proxy", "pointing_err_proxy"):
                if k not in o:
                    raise KeyError(k)
            pupils.append(float(o["pupil_fill_error"]))
            photons.append(float(o["photons_kept"]))
            comps.append(float(o["if_compat_score"]))
            truths.append(float(r["if_compat_score"]))
        return (
            sum(pupils) / len(pupils),
            sum(photons) / len(photons),
            sum(comps) / len(comps),
            rmse(comps, truths),
        )

    tr = score(load("train.json"))
    h = score(load("holdout.json"))
    c = score(load("cheat_trap.json"))

    src = (ROOT / "shim.py").read_text()
    voids = []
    if h[1] < PHOTON_FLOOR:
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
    if "conditioner" in src.lower() and "def condition" in src:
        voids.append("shim_not_conditioner_paste")

    pupil_ok = h[0] <= PUPIL_MAX
    decision = "RESET"
    if voids:
        decision = "VOID"
    elif pupil_ok and h[1] >= PHOTON_FLOOR and h[2] >= 0.72:
        decision = "KEEP"
    elif h[2] >= 0.55 and h[1] >= PHOTON_FLOOR:
        decision = "SEED"

    print(
        f"p10-if-shim\tpupil_err={h[0]:.4f}\tphotons_kept={h[1]:.4f}\t"
        f"if_compat={h[2]:.4f}\tcompat_rmse={h[3]:.4f}\t"
        f"decision={decision}\tvoids={','.join(voids) or '-'}\t"
        f"trap_compat={c[2]:.4f}\ttrain_compat={tr[2]:.4f}"
    )
    return 0 if decision != "VOID" else 3

if __name__ == "__main__":
    raise SystemExit(main())
