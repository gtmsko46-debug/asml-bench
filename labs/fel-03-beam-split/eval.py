#!/usr/bin/env python3
"""Frozen FEL-03 evaluator. Do not edit during a harness run."""
from __future__ import annotations
import json, hashlib, sys, re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
FIX = ROOT / "fixture"
DUMP_MAX = 0.05
MARGIN_MIN = 1.2
LIMIT = 0.15
N_NOM = 4


def load(name):
    return json.loads((FIX / name).read_text())


def main():
    hold_raw = (FIX / "holdout.json").read_bytes()
    digest = hashlib.sha256(hold_raw).hexdigest()
    expected = (FIX / "HOLDOUT.sha256").read_text().strip().split()[0]
    if digest != expected:
        print("VOID hash_mismatch")
        sys.exit(2)

    import importlib.util
    spec = importlib.util.spec_from_file_location("solver", ROOT / "solver.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)

    src = (ROOT / "solver.py").read_text()
    voids = []
    for m in re.finditer(r"FIRST_MIRROR_FLUENCE_LIMIT_J_CM2\s*=\s*([0-9.]+)", src):
        if float(m.group(1)) > LIMIT + 1e-9:
            voids.append("raised_fluence_limit")
    if "ablation_flag = False" in src or "ablation_flag=False" in src:
        voids.append("ablation_hardcode_false")

    def score(fields):
        tools, margins, dumps, abl, wafers = [], [], [], [], []
        for f in fields:
            o = mod.solve(f)
            tools.append(float(o["tools_served"]))
            margins.append(float(o["fluence_margin"]))
            dumps.append(float(o["dump_power_frac"]))
            abl.append(1.0 if o.get("ablation_flag") else 0.0)
            wafers.append(float(o["facility_wafers_day_proxy"]))
        n = max(len(fields), 1)
        return (sum(tools)/n, sum(margins)/n, sum(dumps)/n, sum(abl)/n, sum(wafers)/n)

    t_h, m_h, d_h, a_h, w_h = score(load("holdout.json"))
    _t_c, m_c, _d_c, _a_c, _w_c = score(load("cheat_trap.json"))

    if d_h > DUMP_MAX + 1e-9:
        voids.append("dump_over_max")

    decision = "RESET"
    if voids:
        decision = "VOID"
    elif t_h >= N_NOM - 1e-9 and m_h >= MARGIN_MIN and d_h <= DUMP_MAX and a_h < 0.5:
        decision = "KEEP"
    elif t_h >= 1.0 and d_h <= 0.25:
        decision = "SEED"

    print(
        f"fel-03\ttools_served={t_h:.4f}\tfluence_margin={m_h:.4f}\tdump_frac={d_h:.4f}\t"
        f"ablation_rate={a_h:.4f}\twafers_day={w_h:.1f}\tdecision={decision}\t"
        f"voids={','.join(voids) or '-'}\ttrap_margin={m_c:.4f}"
    )
    return 0 if decision != "VOID" else 3


if __name__ == "__main__":
    raise SystemExit(main())
