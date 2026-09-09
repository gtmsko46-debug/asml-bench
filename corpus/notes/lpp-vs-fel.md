# LPP vs FEL EUV sources (lab starter)

**Access / write date**: 2026-09-09  
**Audience**: researchers standing up litho-lab / asml-bench source pathways  
**Policy**: synthetic toys + OA literature only — never ASML internal CE / power specs.

## One-sentence contrast

**LPP (laser-produced plasma)** is today’s HVM path: Sn droplets + CO₂ drive laser → 13.5 nm in-band EUV with conversion-efficiency (CE) and debris/collector challenges. **FEL / accelerator** proposals aim for multi-kW, debris-free, potentially tunable sources but bring facility-scale RF, undulators, and beam-split / first-mirror fluence problems.

## Assumption cards to cite

| Card | Role |
|------|------|
| `assumptions/lpp-source-v1.yaml` | CE %, in-band power proxy, droplet rate toys |
| `assumptions/fel-source-v1.yaml` | Temporal coherence length, photon budget, speckle contrast |
| `assumptions/beam-split-first-mirror-v1.yaml` | Multi-kW facility split → N tools; first-mirror fluence margin |
| `assumptions/tco-v1.yaml` | Public-narrative capital / WPD toys when comparing source TCO stories |

## What the OA papers buy you

- **Schneidmiller et al. 2011** (`papers/1108.5986.pdf`): FLASH-tech FEL at 13.5/6.8 nm toward kW-class average power — historical “FEL can meet litho power” argument.
- **He et al. 2025** (`papers/2501.14541.pdf`): Compact RAFEL + ERL ~2 kW with lower e-beam energy via harmonic lasing — modern compact-facility narrative vs LPP power headroom at ≤3 nm.
- **Molodozhentsev & Kruchinin 2021** (`papers/2104.06075.pdf`): LWFA-driven compact EUV FEL constraints; ultra-short pulses → coherence / temporal structure differs from LPP plasma emission.

Cite-only context (no local chapters): Bakshi *EUV Sources for Lithography* (SPIE) for LPP physics vocabulary — see `papers/corpus.bib`.

## Lab wiring

- Source brightness / CE demos → parameters in `lpp-source-v1`.
- Coherence conditioner FEL-02 → `fel-source-v1` + `coherence-if-v1`.
- Facility split / first mirror FEL-03 → `beam-split-first-mirror-v1`.
- Do **not** assert EXE/NXE internal CE or collector lifetime from these toys.

## Suggested citation line in results notes

> Source proxies from `lpp-source-v1` / `fel-source-v1` (synthetic, open-proxy). Physics context: Schneidmiller et al. arXiv:1108.5986; He et al. arXiv:2501.14541.
