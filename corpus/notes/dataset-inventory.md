# Dataset / software inventory (local corpus)

**Access date**: 2026-09-09  
**Policy**: license check before any dataset binary; URL+license note if unclear; never pirate.

## Local clones under `corpus/datasets/`

| Path | Upstream | License | Pinned commit | Binary data mirrored? | Lab use |
|------|----------|---------|---------------|----------------------|---------|
| `datasets/LithoBench/` | [shelljane/lithobench](https://github.com/shelljane/lithobench) | **MIT** (`LICENSE`) | `9c74e82218e377eaf6d02d113fc1ce6e36c92aa6` (2023-06-07) | **No** — Google Drive `lithodata` left as URL in `CLONE_NOTE.md` (verify Drive terms before redistribution) | P1 twin / ML OPC baselines |
| `datasets/lithosim/` | [VLSIDA/lithosim](https://github.com/VLSIDA/lithosim) | **BSD-3** | `b3868e025716ba1c236f892345d57709f0cebacd` (2026-03-19) | N/A (code + examples only; small) | Aerial image / SOCS for FEL-02, P4 |
| `datasets/OpenLithoHub/` | [OpenLithoHub/OpenLithoHub](https://github.com/OpenLithoHub/OpenLithoHub) | **Apache-2.0** (code) | `281447493190f7602c47495908c868d6981beeaa` | **No** — adapters only; see upstream `DATA-LICENSES.md` | Discovery / DatasetAdapter |

Each clone has `CLONE_NOTE.md` with pin + access date.

## Not mirrored (pointers only)

| Resource | Why skipped | Where noted |
|----------|-------------|-------------|
| LithoBench Drive tiles (~120k) | Large binary; redistribution terms need explicit verify beyond code MIT | `datasets/LithoBench/CLONE_NOTE.md`, `datasets/README.md` |
| LithoBench pre-trained model Drive dump | Same | upstream README |
| SPIE / Wiley book chapters (Bakshi, Levinson, Mack) | Paywalled — cite-only | `papers/corpus.bib`, `INDEX.md` |
| Proprietary fab / ASML internal pattern data | Forbidden | lab rules |

## Paper PDFs (OA) under `corpus/papers/`

See `papers/ABSTRACTS.md` and `papers/corpus.bib`. Counts at seed time: **9 PDFs** (8 arXiv + 1 NeurIPS OA) + bib + abstracts note.

## Recommendation for P1 twin work

1. Use LithoBench **code** APIs locally.  
2. If tiles are needed, download Drive archive yourself, record license/hash/access date in a new note, and keep binaries out of git if redistribution is unclear (`.gitignore` large archives).  
3. Prefer `lithosim` for lightweight aerial-image toys that must run in CI without Drive.
