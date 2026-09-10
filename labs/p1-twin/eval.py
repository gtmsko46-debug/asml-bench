#!/usr/bin/env python3
"""Frozen P1 FEL↔scanner twin evaluator. Do not edit during a harness run."""
from __future__ import annotations

import hashlib
import importlib.util
import json
import math
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
FIX = ROOT / "fixture"
METRICS = (
    "if_power_w",
    "uniformity",
    "first_mirror_fluence",
    "illuminator_acceptance",
)


def load(name: str):
    data = json.loads((FIX / name).read_text())
    if isinstance(data, dict) and "rows" in data:
        return data["rows"]
    return data


def rmse(pred, truth):
    if len(pred) != len(truth) or not truth:
        return 1e9
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(pred, truth)) / len(truth))


def std(vals):
    if not vals:
        return 1.0
    m = sum(vals) / len(vals)
    return math.sqrt(sum((v - m) ** 2 for v in vals) / len(vals)) or 1.0


def score_rows(predict_fn, rows):
    """Return per-metric RMSE and combined normalized RMSE."""
    by_m = {m: [] for m in METRICS}
    for row in rows:
        pred = predict_fn(row)
        if not isinstance(pred, dict):
            return {m: 1e9 for m in METRICS}, 1e9
        for m in METRICS:
            if m not in pred:
                return {m: 1e9 for m in METRICS}, 1e9
            by_m[m].append((float(pred[m]), float(row[m])))
    rmses = {m: rmse([a for a, _ in pairs], [b for _, b in pairs]) for m, pairs in by_m.items()}
    norms = []
    for m, pairs in by_m.items():
        s = std([b for _, b in pairs])
        norms.append(rmses[m] / s)
    combined = sum(norms) / len(norms)
    return rmses, combined


def check_guards(twin_src: str, train_c: float, hold_c: float) -> list[str]:
    voids = []
    if "platform" in twin_src and "NXE" in twin_src:
        voids.append("commonality: NXE special-case")
    for term in ("IF_COUPLING", "MIRROR_LOAD"):
        if term in twin_src:
            for line in twin_src.splitlines():
                if term in line and "=" in line and not line.strip().startswith("#"):
                    try:
                        val = float(line.split("=")[1].split("#")[0].strip())
                        if abs(val) < 1e-6:
                            voids.append(f"physics: {term} ~0")
                    except Exception:
                        pass
    low = twin_src.lower()
    if "mlp" in low or "sklearn" in low or "torch" in low:
        if train_c + 0.15 < hold_c:
            voids.append("cheat-trap: unconstrained fit overfit")
    return voids


def main():
    hold_raw = (FIX / "holdout.json").read_bytes()
    digest = hashlib.sha256(hold_raw).hexdigest()
    expected = (FIX / "HOLDOUT.sha256").read_text().strip().split()[0]
    if digest != expected:
        print(f"VOID\thash_mismatch\tgot={digest}\texpected={expected}")
        sys.exit(2)

    spec = importlib.util.spec_from_file_location("twin", ROOT / "twin.py")
    twin = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(twin)

    train = load("train.json")
    hold = load("holdout.json")
    trap = load("cheat_trap.json")

    train_rmses, train_c = score_rows(twin.predict_twin, train)
    hold_rmses, hold_c = score_rows(twin.predict_twin, hold)
    trap_rmses, trap_c = score_rows(twin.predict_twin, trap)

    src = (ROOT / "twin.py").read_text()
    voids = check_guards(src, train_c, hold_c)
    # Critic: holdout saturation alone ⇒ generative recovery (independent of trap).
    if hold_c < 1e-6:
        voids.append("saturated: generative recovery")

    decision = "RESET"
    if voids:
        decision = "VOID"
    elif hold_c < 0.55:
        decision = "KEEP"
    elif hold_c <= train_c * 1.5 + 0.05:
        decision = "SEED" if hold_c > 0.35 else "RESET"

    # TSV-friendly one-liner
    print(
        f"p1-twin\ttrain_nrmse={train_c:.4f}\tholdout_nrmse={hold_c:.4f}\t"
        f"trap_nrmse={trap_c:.4f}\t"
        f"hold_if={hold_rmses['if_power_w']:.4f}\t"
        f"hold_unif={hold_rmses['uniformity']:.4f}\t"
        f"hold_flu={hold_rmses['first_mirror_fluence']:.4f}\t"
        f"hold_acc={hold_rmses['illuminator_acceptance']:.4f}\t"
        f"decision={decision}\tvoids={','.join(voids) or '-'}"
    )
    tsv = ROOT / "results.tsv"
    if not tsv.exists():
        tsv.write_text("thesis\trun\thypothesis\tprovider\tmetric\tdecision\tcard\n")
    return 0 if decision != "VOID" else 3


if __name__ == "__main__":
    raise SystemExit(main())
