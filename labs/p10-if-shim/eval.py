#!/usr/bin/env python3
"""Frozen FEL-10 / P10 IF-shim evaluator. Do not edit during a harness run.

SEED: all five axes present + non-null; photons_kept == 1.0 hard; no missing fields.
KEEP: pupil_fill_error ≤ 0.10 AND photons_kept ≥ 0.55 (dual AND). Soft score never KEEPs alone.
Cite: tickets/IF_SPEC_FEL10_CONTRACT.md
"""
from __future__ import annotations

import hashlib
import importlib.util
import json
import math
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
FIX = ROOT / "fixture"
PUPIL_ERR_MAX = 0.10
PHOTON_FLOOR = 0.55
PHOTON_HARD = 1.0  # Director hard for SEED scaffold
AXES = (
    "pupil_fill_error",
    "photons_kept",
    "if_loss_db",
    "pol_contrast_proxy",
    "pulse_envelope_proxy",
    "pointing_err_proxy",
)


def load(name: str):
    return json.loads((FIX / name).read_text())


def mean(xs):
    return sum(xs) / len(xs)


def main() -> int:
    hold_raw = (FIX / "holdout.json").read_bytes()
    digest = hashlib.sha256(hold_raw).hexdigest()
    expected = (FIX / "HOLDOUT.sha256").read_text().strip().split()[0]
    if digest != expected:
        print("VOID\thash_mismatch")
        return 2

    spec = importlib.util.spec_from_file_location("shim", ROOT / "shim.py")
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)

    def score(fields):
        rows = []
        for f in fields:
            o = mod.shim(f)
            rows.append(o)
        return rows

    train, hold, trap = load("train.json"), load("holdout.json"), load("cheat_trap.json")
    rows_h = score(hold)
    rows_t = score(trap)
    rows_tr = score(train)

    voids: list[str] = []
    for i, o in enumerate(rows_h):
        for ax in AXES:
            if ax not in o or o[ax] is None:
                voids.append(f"missing_axis:{ax}")
            else:
                try:
                    v = float(o[ax])
                    if math.isnan(v):
                        voids.append(f"nan_axis:{ax}")
                except (TypeError, ValueError):
                    voids.append(f"bad_axis:{ax}")

    pupil = mean([float(o["pupil_fill_error"]) for o in rows_h])
    photons = mean([float(o["photons_kept"]) for o in rows_h])
    if_loss = mean([float(o["if_loss_db"]) for o in rows_h])
    pol = mean([float(o["pol_contrast_proxy"]) for o in rows_h])
    pulse = mean([float(o["pulse_envelope_proxy"]) for o in rows_h])
    pointing = mean([float(o["pointing_err_proxy"]) for o in rows_h])
    trap_photons = mean([float(o["photons_kept"]) for o in rows_t])

    src = (ROOT / "shim.py").read_text()
    if "PHOTON_KEEP" in src:
        for line in src.splitlines():
            if line.strip().startswith("PHOTON_KEEP"):
                try:
                    val = float(line.split("=")[1].split("#")[0].strip())
                    if val < PHOTON_HARD - 1e-9:
                        voids.append("photon_keep_param")
                except Exception:
                    pass

    if photons < PHOTON_HARD - 1e-6:
        voids.append("photon_discard")
    if trap_photons < 0.55:
        # cheat_trap designed to discard; detecting discard path is OK — not a void on holdout
        pass

    # ranking-only soft score (never alone decides KEEP)
    soft = max(0.0, 1.0 - pupil) * min(1.0, photons)

    decision = "RESET"
    if voids:
        decision = "VOID"
    elif pupil <= PUPIL_ERR_MAX and photons >= PHOTON_FLOOR:
        decision = "KEEP"
    elif not voids and all(ax in rows_h[0] for ax in AXES):
        decision = "SEED"

    print(
        "p10-if-shim"
        f"\tpupil_err={pupil:.4f}"
        f"\tphotons_kept={photons:.4f}"
        f"\tif_loss_db={if_loss:.4f}"
        f"\tpol={pol:.4f}"
        f"\tpulse={pulse:.4f}"
        f"\tpointing={pointing:.4f}"
        f"\tif_compat_score={soft:.4f}"
        f"\tdecision={decision}"
        f"\tvoids={','.join(voids) or '-'}"
        f"\ttrap_photons={trap_photons:.4f}"
    )
    return 0 if decision != "VOID" else 3


if __name__ == "__main__":
    raise SystemExit(main())
