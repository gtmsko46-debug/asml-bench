# Corpus Index (curated bibliography)

Pointers and *why* — **not** pirated PDFs. Prefer DOI / publisher / arXiv / open datasets.  
**Seed access date**: 2026-09-09.

## Local layout

| Path | Contents |
|------|----------|
| `corpus/notes/` | Markdown notes we write (5 starter notes) |
| `corpus/papers/` | OA PDFs + `corpus.bib` + `ABSTRACTS.md` |
| `corpus/datasets/` | Licensed clones + `README.md` + per-clone `CLONE_NOTE.md` |

## Lab-log (Archivist)

| Path | Contents |
|------|----------|
| [`lab-log/`](lab-log/) | Single continuous lab-log: Scribe lifts + citeable KEEP register |
| [`lab-log/LATEST.md`](lab-log/LATEST.md) | Current digest |
| [`lab-log/keeps/REGISTER.md`](lab-log/keeps/REGISTER.md) | Only KEEPs Scorekeeper/Briefing may cite |
| [`learnings/`](learnings/) | Scribe-encoded CoS/Critic/PI durable learnings |
| [`learnings/LATEST.md`](learnings/LATEST.md) | Current champion/lab learnings digest |

## Starter notes (local)

| Note | Path | Ties to |
|------|------|---------|
| LPP vs FEL sources | [`notes/lpp-vs-fel.md`](notes/lpp-vs-fel.md) | `lpp-source-v1`, `fel-source-v1`, `beam-split-first-mirror-v1` |
| Coherence / pupil | [`notes/coherence-pupil.md`](notes/coherence-pupil.md) | `coherence-if-v1`, FEL-02, `datasets/lithosim/` |
| Reticle heat → overlay | [`notes/reticle-heating-overlay.md`](notes/reticle-heating-overlay.md) | `overlay-thermal-v1`, TH-04 |
| Cite assumption cards | [`notes/how-to-cite-assumptions.md`](notes/how-to-cite-assumptions.md) | all `assumptions/*.yaml` |
| Dataset inventory | [`notes/dataset-inventory.md`](notes/dataset-inventory.md) | license status table |

## Datasets / open software (local clones)

| Ref | Local path | Upstream | License | Access date | Why |
|-----|------------|----------|---------|-------------|-----|
| LithoBench | [`datasets/LithoBench/`](datasets/LithoBench/) | https://github.com/shelljane/lithobench | MIT | 2026-09-09 | ML lithography benchmark framework; pin `9c74e822…`; Drive tiles **not** mirrored — see `CLONE_NOTE.md` |
| lithosim | [`datasets/lithosim/`](datasets/lithosim/) | https://github.com/VLSIDA/lithosim | BSD-3 | 2026-09-09 | Hopkins SOCS aerial-image helper; pin `b3868e02…` |
| OpenLithoHub | [`datasets/OpenLithoHub/`](datasets/OpenLithoHub/) | https://github.com/OpenLithoHub/OpenLithoHub | Apache-2.0 (code) | 2026-09-09 | Adapters + DATA-LICENSES; pin `28144749…` |

Paper: Yang et al., LithoBench, NeurIPS 2023 — local OA PDF [`papers/lithobench-neurips2023.pdf`](papers/lithobench-neurips2023.pdf)  
URL: https://proceedings.neurips.cc/paper_files/paper/2023/file/604b9fa9e1c16284e6517d923cf9ff20-Paper-Datasets_and_Benchmarks.pdf

## Open-access papers (local PDFs)

BibTeX: [`papers/corpus.bib`](papers/corpus.bib) · Digests: [`papers/ABSTRACTS.md`](papers/ABSTRACTS.md)

| File | Key | DOI / arXiv | Why for litho-lab |
|------|-----|-------------|-------------------|
| `papers/1108.5986.pdf` | Schneidmiller et al. 2011 | https://arxiv.org/abs/1108.5986 | kW-class FLASH FEL for NGL |
| `papers/2501.14541.pdf` | He et al. 2025 | https://arxiv.org/abs/2501.14541 | Compact RAFEL/ERL EUV ~2 kW vs LPP |
| `papers/2104.06075.pdf` | Molodozhentsev 2021 | https://arxiv.org/abs/2104.06075 · doi:10.3390/instruments6010004 | LWFA EUV FEL design constraints |
| `papers/1912.07254.pdf` | Yang et al. ASP-DAC'20 | https://arxiv.org/abs/1912.07254 | ML mask optimization / heterogeneous OPC |
| `papers/2405.03574.pdf` | Yang & Ren ICML'24 | https://arxiv.org/abs/2405.03574 | ILILT implicit inverse lithography |
| `papers/2405.11717.pdf` | Shintake 2024 | https://arxiv.org/abs/2405.11717 | EUV efficiency + stochastic/photon-noise discussion |
| `papers/2411.10177.pdf` | Gentile et al. 2024 | https://arxiv.org/abs/2411.10177 · doi:10.1117/12.2657702 | EUV resist dissociative photoionization (cite arXiv) |
| `papers/1710.08733.pdf` | Fallica et al. 2017 | https://arxiv.org/abs/1710.08733 · doi:10.1116/1.5003476 | EUV vs EBL resist LER / shot noise |
| `papers/lithobench-neurips2023.pdf` | Yang et al. NeurIPS'23 | NeurIPS proceedings URL above | LithoBench dataset paper |

## Cite-only (no local chapter PDFs)

| Ref | Link | Why |
|-----|------|-----|
| Bakshi — EUV Source Technology | SPIE Press / books.spie.org | LPP physics for `lpp-source-v1` |
| Levinson — Principles of Lithography | SPIE Press | Imaging / overlay for TH-04 |
| Mack — Fundamental Principles of Optical Lithography | Wiley | Coherence, pupil, σ for FEL-02 |
| Naulleau et al. EUV stochastics | doi.org / Optics Express search "EUV stochastic" | Prefer OA publisher copies; do not pirate JM3/SPIE |
| ASML public annual reports / Investor Day | https://www.asml.com/investors | Public TCO / throughput narratives only |
| SEMI standards (public abstracts) | https://www.semi.org | Overlay / metrology vocabulary |

## Usage rules

1. Store notes under `corpus/notes/` (markdown summaries you write).
2. `corpus/papers/` is for **open-access** PDFs or bibtex only — no paywalled dumps.
3. Always record license before copying any dataset into `corpus/datasets/`.
4. Cite assumption cards by `id@version` — see `notes/how-to-cite-assumptions.md`.
