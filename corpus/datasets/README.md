# Dataset Pointers (licenses)

Do **not** vend proprietary fab data. Clone or download only under the licenses below.  
**Inventory detail**: [`../notes/dataset-inventory.md`](../notes/dataset-inventory.md).  
**Access date for local clones**: 2026-09-09.

## LithoBench (local code clone)

- **What**: Pattern / lithography ML benchmark (NeurIPS 2023 Datasets & Benchmarks).
- **Local**: [`LithoBench/`](LithoBench/) — MIT LICENSE verified; pin in `LithoBench/CLONE_NOTE.md`
  (`9c74e82218e377eaf6d02d113fc1ce6e36c92aa6`).
- **Upstream**: https://github.com/shelljane/lithobench
- **Binary tiles**: **Not mirrored.** Upstream Google Drive:
  https://drive.google.com/file/d/1MzYiRRxi8Eu2L6WHCfZ1DtRnjVNOl4vu/view  
  Verify Drive/redistribution terms + cite Yang et al. NeurIPS 2023 before bulk copy.
- **Use in lab**: P1 twin feature shapes; never claim ASML production equivalence.

## lithosim / aerial-image helper (local)

- **What**: VLSIDA Python lithography simulator (Hopkins SOCS, sources, Zernike pupil, resist lump).
- **Local**: [`lithosim/`](lithosim/) — BSD-3 LICENSE; pin `b3868e025716ba1c236f892345d57709f0cebacd`.
- **Upstream**: https://github.com/VLSIDA/lithosim
- **Use in lab**: Synthetic intensity maps for coherence / pupil toys (FEL-02, P4).

## OpenLithoHub (local code clone)

- **What**: Community aggregation + DatasetAdapter layer (Apache-2.0 code).
- **Local**: [`OpenLithoHub/`](OpenLithoHub/) — pin `281447493190f7602c47495908c868d6981beeaa`.
- **Upstream**: https://github.com/OpenLithoHub/OpenLithoHub
- **License**: Framework Apache-2.0; **per-dataset** terms in upstream `DATA-LICENSES.md` —
  adapters do not relicense LithoBench Drive tiles or other third-party dumps.
- **Use in lab**: Discovery only; promote individual datasets into assumption citations when frozen.

## Local policy

If a dataset cannot be redistributed, keep **URL + hash of license text + access date** in
`corpus/notes/` (or `CLONE_NOTE.md`) instead of binary blobs.
