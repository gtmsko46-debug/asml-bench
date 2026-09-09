# Dataset Pointers (licenses)

Do **not** vend proprietary fab data. Clone or download only under the licenses below.

## LithoBench

- **What**: Pattern / lithography ML benchmark (ICCAD-era open benchmark lineage).
- **Pointer**: Search GitHub / paperswithcode for `LithoBench`.
- **License**: Check upstream LICENSE (typically research / academic — verify before redistribution).
- **Use in lab**: P1 twin feature shapes; never claim ASML production equivalence.

## LithoSim

- **What**: Open / academic lithography simulation helpers (aerial image, simple resist).
- **Pointer**: Search `LithoSim` lithography GitHub; prefer projects with explicit LICENSE.
- **License**: Project-specific (MIT/BSD/Apache common) — pin commit + LICENSE file in notes.
- **Use in lab**: Synthetic intensity maps for coherence / pupil toys.

## OpenLithoHub

- **What**: Community aggregation of open lithography resources.
- **Pointer**: Track hub README for dataset cards + SPDX license tags.
- **License**: Per-dataset; reject anything without clear terms.
- **Use in lab**: Discovery only; promote individual datasets into assumption citations when frozen.

## Local policy

If a dataset cannot be redistributed, keep **URL + hash of license text + access date** in `corpus/notes/` instead of binary blobs.
