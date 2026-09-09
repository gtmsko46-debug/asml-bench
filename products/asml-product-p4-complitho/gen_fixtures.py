#!/usr/bin/env python3
"""Generate synthetic P4/P7 fixtures. Toy numbers only — not ASML confidential."""
from __future__ import annotations

import hashlib
import json
import math
import random
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]  # asml-bench
MIRRORS = [ROOT]
LITH = Path("/workspace/litho-lab")
if LITH.is_dir():
    MIRRORS.append(LITH)


def roundf(x: float, n: int = 6) -> float:
    return round(float(x), n)


# --- P4 ground truth (synthetic) ---
def p4_truth(na, pitch_nm, pol_degree, pol_angle_deg, dose, defocus, blur):
    contrast = (
        0.4
        + 0.35 * pol_degree * abs(math.sin(2.0 * math.radians(pol_angle_deg)))
        + 0.15 * (na / 0.55)
    )
    pw_area = contrast * dose / (1.0 + 0.5 * blur + 0.3 * abs(defocus)) * (pitch_nm / 40.0)
    epe_nm = 2.5 / max(contrast, 0.1) + 0.8 * abs(defocus) + 0.2 * blur
    return roundf(pw_area), roundf(epe_nm)


def gen_p4_rows(seed: int, n: int, prefix: str):
    rng = random.Random(seed)
    nas = [0.33, 0.45, 0.55, 0.65, 0.75]
    rows = []
    for i in range(n):
        na = rng.choice(nas)
        pitch_nm = roundf(rng.uniform(28.0, 64.0), 3)
        pol_degree = roundf(rng.uniform(0.0, 1.0), 4)
        pol_angle_deg = roundf(rng.uniform(0.0, 90.0), 2)
        dose = roundf(rng.uniform(0.6, 1.4), 4)
        defocus = roundf(rng.uniform(-1.2, 1.2), 4)
        blur = roundf(rng.uniform(0.05, 0.55), 4)
        pw, epe = p4_truth(na, pitch_nm, pol_degree, pol_angle_deg, dose, defocus, blur)
        rows.append(
            {
                "id": f"{prefix}-{seed}-{i:04d}",
                "na": na,
                "pitch_nm": pitch_nm,
                "pol_degree": pol_degree,
                "pol_angle_deg": pol_angle_deg,
                "dose": dose,
                "defocus": defocus,
                "blur": blur,
                "pw_area": pw,
                "epe_nm": epe,
            }
        )
    return rows


def gen_p4_cheat():
    rows = []
    # Polarization sensitivity: same geometry, pol 0 vs 1
    base = dict(na=0.55, pitch_nm=40.0, pol_angle_deg=45.0, dose=1.0, defocus=0.0, blur=0.2)
    for i, pol in enumerate([0.0, 0.25, 0.5, 0.75, 1.0]):
        pw, epe = p4_truth(pol_degree=pol, **base)
        rows.append({"id": f"p4-cheat-pol-{i}", **base, "pol_degree": pol, "pw_area": pw, "epe_nm": epe})
    # Multi-NA matched case — punishes single-NA hardcode
    for i, na in enumerate([0.33, 0.45, 0.55, 0.65, 0.75]):
        kw = dict(na=na, pitch_nm=36.0, pol_degree=0.9, pol_angle_deg=45.0, dose=1.1, defocus=0.2, blur=0.15)
        pw, epe = p4_truth(**kw)
        rows.append({"id": f"p4-cheat-na-{i}", **kw, "pw_area": pw, "epe_nm": epe})
    return rows


# --- P7 ground truth (synthetic; 6.x not free) ---
def p7_truth(wavelength_nm, na, multilayer_R, resist_blur_nm, dose, k1_proxy):
    if wavelength_nm >= 13.0:
        optics_penalty = 1.0
    else:
        optics_penalty = 0.55 + 0.45 * multilayer_R
    resist_penalty = 1.0 + 0.08 * resist_blur_nm * (13.5 / wavelength_nm)
    pw_area = (dose * k1_proxy * na * optics_penalty) / resist_penalty
    return roundf(pw_area)


def p7_relative(row_pw, matched_135_pw):
    return roundf(row_pw / max(matched_135_pw, 1e-9), 6)


def gen_p7_rows(seed: int, n: int, prefix: str):
    rng = random.Random(seed)
    rows = []
    for i in range(n):
        wavelength_nm = 13.5 if rng.random() < 0.5 else 6.7
        na = roundf(rng.choice([0.33, 0.45, 0.55, 0.65]), 2)
        multilayer_R = roundf(rng.uniform(0.35, 0.95), 4)
        resist_blur_nm = roundf(rng.uniform(1.0, 6.0), 3)
        dose = roundf(rng.uniform(0.7, 1.3), 4)
        k1_proxy = roundf(rng.uniform(0.35, 0.7), 4)
        pw = p7_truth(wavelength_nm, na, multilayer_R, resist_blur_nm, dose, k1_proxy)
        pw135 = p7_truth(13.5, na, multilayer_R, resist_blur_nm, dose, k1_proxy)
        rows.append(
            {
                "id": f"{prefix}-{seed}-{i:04d}",
                "wavelength_nm": wavelength_nm,
                "na": na,
                "multilayer_R": multilayer_R,
                "resist_blur_nm": resist_blur_nm,
                "dose": dose,
                "k1_proxy": k1_proxy,
                "pw_area": pw,
                "relative_to_135": p7_relative(pw, pw135),
            }
        )
    return rows


def gen_p7_cheat():
    rows = []
    # Matched 13.5 vs 6.7 with poor multilayer — 6.7 should lose if honest
    for i, R in enumerate([0.4, 0.55, 0.7, 0.85]):
        for wl in (13.5, 6.7):
            kw = dict(
                wavelength_nm=wl,
                na=0.55,
                multilayer_R=R,
                resist_blur_nm=3.0,
                dose=1.0,
                k1_proxy=0.5,
            )
            pw = p7_truth(**kw)
            pw135 = p7_truth(13.5, kw["na"], kw["multilayer_R"], kw["resist_blur_nm"], kw["dose"], kw["k1_proxy"])
            rows.append(
                {
                    "id": f"p7-cheat-ml-{i}-{'135' if wl >= 13 else '67'}",
                    **kw,
                    "pw_area": pw,
                    "relative_to_135": p7_relative(pw, pw135),
                }
            )
    # Resist blur hurts 6.x harder
    for i, blur in enumerate([1.0, 2.5, 4.0, 5.5]):
        kw = dict(wavelength_nm=6.7, na=0.55, multilayer_R=0.8, resist_blur_nm=blur, dose=1.0, k1_proxy=0.5)
        pw = p7_truth(**kw)
        pw135 = p7_truth(13.5, kw["na"], kw["multilayer_R"], kw["resist_blur_nm"], kw["dose"], kw["k1_proxy"])
        rows.append(
            {
                "id": f"p7-cheat-resist-{i}",
                **kw,
                "pw_area": pw,
                "relative_to_135": p7_relative(pw, pw135),
            }
        )
    return rows


def write_json(path: Path, obj):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=2) + "\n")


def write_holdout_hash(holdout_path: Path):
    data = holdout_path.read_bytes()
    h = hashlib.sha256(data).hexdigest()
    (holdout_path.parent / "HOLDOUT.sha256").write_text(f"{h}  holdout.json\n")
    return h


P4_EVAL = r'''#!/usr/bin/env python3
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
'''

P4_SOLVER = r'''#!/usr/bin/env python3
"""Baseline P4 solver — weak synthetic model. Harness may edit this file only."""
from __future__ import annotations

import math


def solve(row: dict) -> dict:
    """Predict pw_area and epe_nm from polarization-aware imaging inputs."""
    na = float(row["na"])
    pitch_nm = float(row["pitch_nm"])
    pol_degree = float(row["pol_degree"])
    pol_angle_deg = float(row["pol_angle_deg"])
    dose = float(row["dose"])
    defocus = float(row["defocus"])
    blur = float(row["blur"])

    # Honest-ish baseline (same formula family as fixture truth; slight coefficient miss so not perfect)
    contrast = (
        0.38
        + 0.33 * pol_degree * abs(math.sin(2.0 * math.radians(pol_angle_deg)))
        + 0.14 * (na / 0.55)
    )
    pw_area = contrast * dose / (1.0 + 0.55 * blur + 0.28 * abs(defocus)) * (pitch_nm / 40.0)
    epe_nm = 2.6 / max(contrast, 0.1) + 0.75 * abs(defocus) + 0.22 * blur
    return {"pw_area": pw_area, "epe_nm": epe_nm}
'''

P7_EVAL = r'''#!/usr/bin/env python3
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
'''

P7_SOLVER = r'''#!/usr/bin/env python3
"""Baseline P7 solver — weak synthetic model. Harness may edit this file only."""
from __future__ import annotations


def solve(row: dict) -> dict:
    """Predict process-window proxies at 13.5 or 6.x nm. 6.7 is not free."""
    wavelength_nm = float(row["wavelength_nm"])
    na = float(row["na"])
    multilayer_R = float(row["multilayer_R"])
    resist_blur_nm = float(row["resist_blur_nm"])
    dose = float(row["dose"])
    k1_proxy = float(row["k1_proxy"])

    # Slightly misspecified vs fixture truth
    if wavelength_nm >= 13.0:
        optics_penalty = 1.0
    else:
        optics_penalty = 0.52 + 0.48 * multilayer_R
    resist_penalty = 1.0 + 0.085 * resist_blur_nm * (13.5 / wavelength_nm)
    pw_area = (dose * k1_proxy * na * optics_penalty) / resist_penalty

    # Matched 13.5 reference with same other inputs
    pw135 = (dose * k1_proxy * na * 1.0) / (1.0 + 0.085 * resist_blur_nm * (13.5 / 13.5))
    relative_to_135 = pw_area / max(pw135, 1e-9)
    return {"pw_area": pw_area, "relative_to_135": relative_to_135}
'''


def write_lab(root: Path, name: str, train, holdout, cheat, eval_src: str, solver_src: str, program_src: Path | None):
    lab = root / "labs" / name
    fix = lab / "fixture"
    write_json(fix / "train.json", {"meta": {"synthetic": True, "seed": train[0]["id"].split("-")[1] if False else None, "frozen": False}, "rows": train})
    # fix meta properly
    seed_train = int(train[0]["id"].split("-")[1])
    seed_hold = int(holdout[0]["id"].split("-")[1])
    write_json(fix / "train.json", {"meta": {"synthetic": True, "seed": seed_train, "frozen": False}, "rows": train})
    write_json(fix / "holdout.json", {"meta": {"synthetic": True, "seed": seed_hold, "frozen": True}, "rows": holdout})
    write_json(fix / "cheat_trap.json", {"meta": {"synthetic": True, "purpose": "RESET demo"}, "rows": cheat})
    h = write_holdout_hash(fix / "holdout.json")
    (lab / "eval.py").write_text(eval_src)
    (lab / "solver.py").write_text(solver_src)
    if program_src and program_src.is_file():
        (lab / "program.md").write_text(program_src.read_text())
    return h


def write_assumption_cards(root: Path):
    assumptions = root / "assumptions"
    assumptions.mkdir(parents=True, exist_ok=True)
    imaging = """id: imaging-optics-v1
version: "1.0.0"
title: Imaging / NA / pupil proxies (synthetic)
scope: P4/P7 computational lithography toys
flags:
  - synthetic
  - open-proxy
  - not-asml-confidential
  - needs-review
parameters:
  - name: na_grid
    value: [0.33, 0.45, 0.55, 0.65, 0.75]
    unit: "1"
    source: "synthetic demo grid — not NXE/EXE production NA"
    confidence: low
    flags: [synthetic, not-asml-confidential]
  - name: pol_contrast_coeff
    value: 0.35
    unit: "1"
    source: "toy coefficient for polarized vs unpolarized contrast proxy"
    confidence: low
    flags: [synthetic, not-asml-confidential]
  - name: wavelength_pair_nm
    value: [13.5, 6.7]
    unit: nm
    source: "public EUV / beyond-EUV conversation wavelengths; toy only"
    confidence: med
    flags: [open-proxy, not-asml-confidential]
notes: >
  Numbers are lab toys for multi-agent experimentation. Not ASML confidential.
"""
    commonality = """id: commonality-v1
version: "1.0.0"
title: Platform commonality hypotheses
scope: Shared software shape across NA / wavelength (TH-03 / BugBot gate)
flags:
  - synthetic
  - not-asml-confidential
  - needs-review
parameters:
  - name: forbid_single_na_fork
    value: true
    unit: "bool"
    source: "lab rule — Applications-recognizable common software; no one-NA special case to win eval"
    confidence: high
    flags: [synthetic, not-asml-confidential]
  - name: min_na_buckets_in_holdout
    value: 3
    unit: "count"
    source: "P4 eval guard"
    confidence: med
    flags: [synthetic, not-asml-confidential]
notes: >
  Promotion for asml-product-p4-complitho needs BugBot + commonality review.
"""
    (assumptions / "imaging-optics-v1.yaml").write_text(imaging)
    (assumptions / "commonality-v1.yaml").write_text(commonality)


def main():
    p4_train = gen_p4_rows(41, 40, "p4")
    p4_hold = gen_p4_rows(42, 40, "p4")
    p4_cheat = gen_p4_cheat()
    p7_train = gen_p7_rows(61, 40, "p7")
    p7_hold = gen_p7_rows(62, 40, "p7")
    p7_cheat = gen_p7_cheat()
    program_p4 = ROOT / "labs" / "p4-polarization" / "program.md"
    program_p7 = ROOT / "labs" / "p7-wavelength" / "program.md"
    hashes = {}
    for root in MIRRORS:
        write_assumption_cards(root)
        hashes[str(root / "p4")] = write_lab(root, "p4-polarization", p4_train, p4_hold, p4_cheat, P4_EVAL, P4_SOLVER, program_p4)
        hashes[str(root / "p7")] = write_lab(root, "p7-wavelength", p7_train, p7_hold, p7_cheat, P7_EVAL, P7_SOLVER, program_p7)
        prod = root / "products" / "asml-product-p4-complitho"
        prod.mkdir(parents=True, exist_ok=True)
        readme = prod / "README.md"
        readme.write_text(
            """# asml-product-p4-complitho

Comp-litho product umbrella for **P4** (polarization-aware) and **P7** (wavelength-agile 13.5 → 6.x).

Owner: Comp-Litho Product PI.

## Labs (asml-bench)

| Lab path | Product slice | Thesis feed |
|----------|---------------|-------------|
| `labs/p4-polarization/` | P4 | FEL-04 |
| `labs/p7-wavelength/` | P7 | FEL-07 |

## Shared rules

- Critics shared with TH-01 (inverse litho) and TH-03 (overlay commonality)
- Promotion needs BugBot + commonality — Applications-recognizable toys, not NA- or λ-special-case forks
- Harness tickets only via Foreman; dual-provider demos required
- Setup mode until harness provider keys are live — no lasercode runs from this PI

## Status

- [x] Lab `program.md` stubs
- [x] Assumption card files on disk (`imaging-optics-v1`, `commonality-v1`)
- [x] Frozen `eval.py` + holdout + cheat_trap per lab
- [x] Baseline `solver.py` scaffolds
- [ ] Product GitHub/Origin repo (name reserved: `asml-product-p4-complitho`)
- [ ] Harness keys live
- [ ] First SEED tickets (paired mock-mistral + grok)

## Local smoke

```bash
python labs/p4-polarization/eval.py
python labs/p7-wavelength/eval.py
```

Fixtures are synthetic only (`meta.synthetic`). Regenerator: `products/asml-product-p4-complitho/gen_fixtures.py`.
"""
        )
        # copy generator into litho-lab product folder too
        if root != ROOT:
            (prod / "gen_fixtures.py").write_text((ROOT / "products" / "asml-product-p4-complitho" / "gen_fixtures.py").read_text())
    print(json.dumps(hashes, indent=2))


if __name__ == "__main__":
    main()
