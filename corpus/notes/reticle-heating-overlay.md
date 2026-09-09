# Reticle heating → overlay (lab starter)

**Access / write date**: 2026-09-09  
**Primary lab**: `labs/th-04-reticle-heat/`

## Physics sketch (toy-level)

Absorbed EUV / DUV power in the reticle stack raises local temperature → thermal expansion of the substrate / absorber stack → in-plane pattern placement error that shows up as **overlay** on the wafer after reduction optics. Lab toys collapse this to:

1. absorbed fraction × load → ΔT  
2. ΔT × CTE (ppm/K) → expansion (ppm)  
3. expansion × scale → overlay-nm for RMSE metrics  

This is **not** a mask-shop or ASML scanner thermal model.

## Assumption card

`assumptions/overlay-thermal-v1.yaml`:

| Parameter | Toy intent |
|-----------|------------|
| `reticle_absorb_frac` | Absorber / stack absorption under load |
| `thermal_expansion_ppm_k` | Low-expansion substrate CTE order-of-magnitude (open materials data) |
| `delta_t_k_nom` | Synthetic ΔT under exposure load |
| `overlay_scale_nm_per_ppm` | Map expansion → overlay-nm for eval RMSE |

Guards in the card / lab: thermal term must be non-zero; no `platform==NXE` special-case forks (`commonality-v1` spirit).

## Related cards / labs

- `imaging-optics-v1` — NA / wavelength context when thermal overlay sits beside imaging toys.
- `commonality-v1` — forbid single-NA forks to win eval.
- Cite-only: Levinson *Principles of Lithography* (SPIE) for overlay / imaging fundamentals — `papers/corpus.bib`.

## How to write a TH-04 results blurb

> Overlay RMSE uses `overlay-thermal-v1` (synthetic, open-proxy). Solver must keep a non-zero thermal contribution; no platform-specific NXE forks. Textbook context: Levinson (cite-only).

## What not to do

- Do not ingest proprietary reticle metrology or scanner logs.
- Do not claim ppm/K or absorb fractions are EXE/NXE production values.
