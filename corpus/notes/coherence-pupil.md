# Coherence, pupil fill, and partial coherence (lab starter)

**Access / write date**: 2026-09-09  
**Primary labs**: `labs/fel-02-coherence/`, stubs touching pupil / polarization (`p4-polarization`, `p7-wavelength`)

## Vocabulary (Mack-style, cite-only book)

Optical lithography imaging depends on **partial coherence** parameterized by source shape in the pupil:

- **σ (sigma)**: ratio of illuminator NA to projection NA — conventional disk fill.
- **Annular / dipole / quadrupole**: off-axis illumination shapes that trade DOF vs resolution / contrast.
- **Pupil fill fraction**: how much of the projection pupil is illuminated; lab card `coherence-if-v1` uses a synthetic `pupil_fill_target`.
- **Speckle / spatial coherence**: FEL sources can be more temporally/spatially coherent than LPP → need an illumination filler / conditioner (FEL-02) to hit litho-friendly σ without destroying photon budget.

Mack *Fundamental Principles of Optical Lithography* (Wiley) is the cite-only textbook for this vocabulary (`papers/corpus.bib`) — **do not** dump paywalled chapters.

## Assumption cards

| Card | Parameters of interest |
|------|------------------------|
| `coherence-if-v1` | `pupil_fill_target`, `if_loss_db`, `spatial_sigma` |
| `fel-source-v1` | `temporal_coherence_length_um`, `baseline_speckle_contrast`, `photon_budget_nom` |
| `imaging-optics-v1` | `na_grid`, `pol_contrast_coeff`, `wavelength_pair_nm` |

## Open software helpers (local)

- `datasets/lithosim/` (BSD-3, VLSIDA) — Hopkins SOCS / conventional·annular·dipole·quad sources, Zernike pupil, aerial image. Ideal for synthetic intensity maps in conditioner evals.
- `datasets/OpenLithoHub/` (Apache-2.0 code) — differentiable Hopkins/SOCS forward pointers; check `DATA-LICENSES.md` before any binary data.

## Runnable lab

`labs/fel-02-coherence/`: conditioner shim that should move toward `pupil_fill_target` / reduce synthetic speckle vs baseline while respecting IF loss. Cite `coherence-if-v1` + `fel-source-v1` in any results note.

## Suggested citation

> Coherence IF proxies from `coherence-if-v1` (synthetic). Aerial-image helper: VLSIDA/lithosim @ pinned commit (see `datasets/lithosim/CLONE_NOTE.md`). Textbook vocabulary: Mack 2007 (cite-only).
