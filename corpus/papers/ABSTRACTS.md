# Paper abstracts / why-mirrored (OA only)

Access date for local files: **2026-09-09**. Full texts live as PDFs beside this note; this file is a researcher-facing digest + lab hook. BibTeX: `corpus.bib`.

## FEL / EUV source (OA)

### `1108.5986.pdf` — Schneidmiller et al. (2011)
FLASH-like superconducting L-band FEL scaled to 13.5 / 6.8 nm with up to ~2.6 kW average power class. Classic open argument that accelerator FELs can meet next-gen lithography source power. **Lab hook**: `fel-source-v1`, `lpp-source-v1` contrast; FEL-02 / FEL-03 facility toys.

### `2501.14541.pdf` — He et al. (2025)
Regenerative-amplifier FEL (RAFEL) + energy-recovery linac proposal ~2 kW EUV at reduced electron energy via harmonic lasing. Positions accelerator sources vs LPP for ≤3 nm HVM power. **Lab hook**: LPP-vs-FEL notes; `beam-split-first-mirror-v1` multi-kW facility narrative.

### `2104.06075.pdf` — Molodozhentsev & Kruchinin (2021)
Compact LWFA-driven EUV FEL design constraints; few-fs pulses, brilliance estimates. **Lab hook**: alternate-source coherence / temporal structure for FEL-02.

## Computational lithography / ILT (OA)

### `lithobench-neurips2023.pdf` — Yang et al. NeurIPS 2023
Dataset+framework paper for ML lithography simulation and mask optimization (>120k tiles). **Lab hook**: P1 twin; local clone `datasets/LithoBench/` (code MIT; Drive tiles not mirrored).

### `1912.07254.pdf` — Yang et al. (ASP-DAC 2020 preprint)
Heterogeneous OPC: learn which engine (MB-OPC vs ILT) wins per clip. Early deep-learning mask-optimization framing on ICCAD-13-scale patterns. **Lab hook**: P4 complitho / inverse-litho surveys.

### `2405.03574.pdf` — Yang & Ren (ICML 2024)
ILILT: implicit-layer learning to emit optimized masks with few steps, grounded by lithography-conditioned intermediates. **Lab hook**: ML-ILT baselines without fab data.

## EUV stochastics / resist (OA)

### `2405.11717.pdf` — Shintake (2024)
Low-NA two-mirror projector efficiency proposal; clearly restates EUV photon-shot / stochastic LER limits (≈14× fewer ionization events vs ArF at equal absorbed energy). **Lab hook**: `stochastics-resist-v1` photon budget intuition.

### `2411.10177.pdf` — Gentile et al. (2024 arXiv; SPIE talk lineage)
PEPICO dissociative photoionization of resist-model monomers at 13.5 nm. Molecular view of EUV-driven solubility switch vs unwanted fragments. **Lab hook**: resist chemistry under `stochastics-resist-v1`; cite arXiv, not paywalled SPIE PDF.

### `1710.08733.pdf` — Fallica et al. (2017)
ZEP520A / mr-PosEBR at EBL vs EUV-IL; dose-to-size, 25 nm HP, LER comparison including shot-noise discussion. **Lab hook**: LCDU / LER proxies.

## Cite-only (no local PDF)
Bakshi *EUV Sources for Lithography* (SPIE), Levinson *Principles of Lithography* (SPIE), Mack *Fundamental Principles of Optical Lithography* (Wiley) — see `corpus.bib`. Naulleau-group Optics Express / JM3 EUV stochastics corpus: search doi.org / opg.optica.org for OA copies; do not pirate paywalled SPIE.
