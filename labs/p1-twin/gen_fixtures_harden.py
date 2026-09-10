#!/usr/bin/env python3
"""HT-1018 fixture harden regenerator (Eval Integrity).

Writes train.json + holdout.json + cheat_trap.json + HOLDOUT.sha256 together.
Imports v1 gen_fixtures.truth only as oracle-trap contrast — does not edit that file.
eval.py / twin.py stay frozen.
"""
from __future__ import annotations

import hashlib
import importlib.util
import json
import math
import struct
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
LAB = Path(__file__).resolve().parent
FIX = LAB / "fixture"
FIXTURE_GEN = "v2-ht1018-harden-2026-09-10"

# Coupling targets (fel-scanner-twin-v1)
IF_COUPLING_TRUE = 0.55
MIRROR_LOAD_TRUE = 0.12


def _load_v1():
    path = ROOT / "products" / "asml-product-p1-twin" / "gen_fixtures.py"
    spec = importlib.util.spec_from_file_location("gen_fixtures_v1", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def roundf(x: float, n: int = 6) -> float:
    return round(float(x), n)


def _jitter(row_id: str, channel: str, scale: float) -> float:
    digest = hashlib.sha256(f"{row_id}:{channel}:{FIXTURE_GEN}".encode()).digest()
    u = struct.unpack(">I", digest[:4])[0] / 0xFFFFFFFF
    return (u - 0.5) * 2.0 * scale


def truth_v2(row_feats: dict, row_id: str) -> dict:
    """Hardened generative truth — nonlinear / saturation / cross + label jitter."""
    fel_power_kw = float(row_feats["fel_power_kw"])
    beam_split_ratio = float(row_feats["beam_split_ratio"])
    undulator_k = float(row_feats["undulator_k"])
    scanner_na = float(row_feats["scanner_na"])
    pupil_fill = float(row_feats["pupil_fill"])
    pulse_rep_hz = float(row_feats["pulse_rep_hz"])
    first_mirror_angle_deg = float(row_feats["first_mirror_angle_deg"])

    # Stronger departure from v1 linear skeleton (HT-1013 oracle class)
    undulator_eff = (
        0.40
        + 0.15 * undulator_k
        + 0.12 * (undulator_k - 1.2) ** 2
        + 0.04 * math.sin(1.7 * undulator_k)
    )
    if_power_lin = (
        fel_power_kw * 1000.0 * beam_split_ratio * undulator_eff * IF_COUPLING_TRUE
    )
    # Aggressive soft saturation — linear clone overshoots high-power holdout
    if_power_w = if_power_lin / (1.0 + if_power_lin / 12000.0)

    uniformity = (
        0.85
        + 0.12 * pupil_fill
        - 0.05 * abs(scanner_na - 0.55)
        + 0.03 * beam_split_ratio
        + 0.10 * pupil_fill * (scanner_na - 0.55)
        - 0.06 * (pupil_fill - 0.7) ** 2
    )
    uniformity = max(0.0, min(1.0, uniformity))

    angle_factor = (
        1.0
        + 0.02 * first_mirror_angle_deg
        + 0.0025 * first_mirror_angle_deg**2
    )
    first_mirror_fluence = (
        fel_power_kw
        * pulse_rep_hz
        * MIRROR_LOAD_TRUE
        * angle_factor
        / max(scanner_na, 0.2)
        * (1.0 + 0.22 * max(0.0, beam_split_ratio - 0.55) ** 2)
    )

    illuminator_acceptance = (
        pupil_fill
        * beam_split_ratio
        * (0.70 + 0.20 * scanner_na)
        * (0.92 + 0.06 * math.tanh(undulator_k - 1.0))
        * (1.0 - 0.12 * abs(pupil_fill - 0.72))
        * (1.0 + 0.08 * math.tanh(scanner_na - 0.55))
    )
    illuminator_acceptance = max(0.0, min(1.0, illuminator_acceptance))

    if_power_w *= 1.0 + _jitter(row_id, "if_power_w", 0.025)
    first_mirror_fluence *= 1.0 + _jitter(row_id, "first_mirror_fluence", 0.025)
    uniformity = max(0.0, min(1.0, uniformity + _jitter(row_id, "uniformity", 0.015)))
    illuminator_acceptance = max(
        0.0,
        min(1.0, illuminator_acceptance + _jitter(row_id, "illuminator_acceptance", 0.015)),
    )

    return {
        "if_power_w": roundf(if_power_w),
        "uniformity": roundf(uniformity),
        "first_mirror_fluence": roundf(first_mirror_fluence),
        "illuminator_acceptance": roundf(illuminator_acceptance),
    }


def sample_feats(rng, *, holdout: bool = False) -> dict:
    import random as _r

    assert isinstance(rng, _r.Random)
    if holdout:
        return {
            "fel_power_kw": roundf(rng.uniform(18.0, 55.0), 3),
            "beam_split_ratio": roundf(rng.uniform(0.25, 0.99), 4),
            "undulator_k": roundf(rng.uniform(0.8, 3.0), 4),
            "scanner_na": roundf(rng.choice([0.33, 0.45, 0.55, 0.65, 0.75, 0.85, 0.93]), 2),
            "pupil_fill": roundf(rng.uniform(0.45, 0.99), 4),
            "pulse_rep_hz": roundf(rng.uniform(100.0, 480.0), 2),
            "first_mirror_angle_deg": roundf(rng.uniform(5.0, 30.0), 2),
        }
    return {
        "fel_power_kw": roundf(rng.uniform(5.0, 40.0), 3),
        "beam_split_ratio": roundf(rng.uniform(0.15, 0.95), 4),
        "undulator_k": roundf(rng.uniform(0.5, 2.5), 4),
        "scanner_na": roundf(rng.choice([0.33, 0.45, 0.55, 0.65, 0.75]), 2),
        "pupil_fill": roundf(rng.uniform(0.35, 0.95), 4),
        "pulse_rep_hz": roundf(rng.uniform(50.0, 400.0), 2),
        "first_mirror_angle_deg": roundf(rng.uniform(2.0, 25.0), 2),
    }


def make_row(prefix: str, seed: int, i: int, feats: dict) -> dict:
    row_id = f"{prefix}-{seed}-{i:04d}"
    return {"id": row_id, **feats, **truth_v2(feats, row_id)}


def gen_rows(seed: int, n: int, prefix: str, *, holdout: bool) -> list[dict]:
    import random

    rng = random.Random(seed)
    return [make_row(prefix, seed, i, sample_feats(rng, holdout=holdout)) for i in range(n)]


def gen_cheat_trap(v1) -> list[dict]:
    rows: list[dict] = []

    base = dict(
        fel_power_kw=20.0,
        undulator_k=1.2,
        scanner_na=0.55,
        pupil_fill=0.72,
        pulse_rep_hz=200.0,
        first_mirror_angle_deg=10.0,
    )
    for i, split in enumerate([0.15, 0.30, 0.45, 0.60, 0.75, 0.90]):
        rows.append(make_row("p1-cheat-split", 0, i, {**base, "beam_split_ratio": split}))

    base2 = dict(
        beam_split_ratio=0.55,
        undulator_k=1.5,
        scanner_na=0.65,
        pupil_fill=0.80,
        pulse_rep_hz=150.0,
        first_mirror_angle_deg=8.0,
    )
    for i, pwr in enumerate([5.0, 12.0, 20.0, 28.0, 36.0]):
        rows.append(make_row("p1-cheat-power", 0, i, {**base2, "fel_power_kw": pwr}))

    for i, split in enumerate([0.2, 1.0]):
        feats = dict(
            fel_power_kw=15.0,
            beam_split_ratio=split,
            undulator_k=1.0,
            scanner_na=0.45,
            pupil_fill=0.60,
            pulse_rep_hz=100.0,
            first_mirror_angle_deg=12.0,
        )
        rows.append(make_row("p1-cheat-photon", 0, i, feats))

    # Extreme rows where v1 truth diverges hard from v2 (oracle trap)
    for i, (k, ang, split, pwr) in enumerate(
        [
            (2.8, 28.0, 0.95, 48.0),
            (2.6, 26.0, 0.92, 42.0),
            (0.55, 5.0, 0.22, 8.0),
            (2.9, 29.0, 0.98, 52.0),
            (2.4, 24.0, 0.88, 38.0),
            (3.0, 30.0, 0.99, 55.0),
        ]
    ):
        feats = dict(
            fel_power_kw=pwr,
            beam_split_ratio=split,
            undulator_k=k,
            scanner_na=0.85,
            pupil_fill=0.92,
            pulse_rep_hz=360.0,
            first_mirror_angle_deg=ang,
        )
        row = make_row("p1-cheat-v1oracle", 0, i, feats)
        # Annotate v1 prediction gap in meta-ish id only; labels stay v2
        _ = v1.truth(feats)
        rows.append(row)

    return rows


def write_json(path: Path, rows: list[dict], meta: dict):
    path.write_text(json.dumps({"meta": meta, "rows": rows}, indent=2) + "\n")


def main() -> int:
    v1 = _load_v1()
    FIX.mkdir(parents=True, exist_ok=True)

    train = gen_rows(seed=46, n=64, prefix="p1-train", holdout=False)
    hold = gen_rows(seed=3046, n=48, prefix="p1-hold", holdout=True)
    trap = gen_cheat_trap(v1)

    write_json(
        FIX / "train.json",
        train,
        {"synthetic": True, "seed": 46, "n": len(train), "fixture_gen": FIXTURE_GEN},
    )
    write_json(
        FIX / "holdout.json",
        hold,
        {
            "synthetic": True,
            "seed": 3046,
            "n": len(hold),
            "frozen": True,
            "fixture_gen": FIXTURE_GEN,
            "ood_vs_train": True,
            "ticket": "HT-1018",
        },
    )
    write_json(
        FIX / "cheat_trap.json",
        trap,
        {
            "synthetic": True,
            "purpose": "RESET — constant / discard-photon / v1-oracle clones",
            "fixture_gen": FIXTURE_GEN,
            "ticket": "HT-1018",
        },
    )

    digest = hashlib.sha256((FIX / "holdout.json").read_bytes()).hexdigest()
    (FIX / "HOLDOUT.sha256").write_text(f"{digest}  holdout.json\n")
    print(f"fixture_gen={FIXTURE_GEN}")
    print(f"HOLDOUT.sha256={digest}")
    print(f"train={len(train)} holdout={len(hold)} cheat_trap={len(trap)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
