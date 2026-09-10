# P10 / FEL-10 — IF ownership shim

**Thesis:** Own the intermediate-focus (IF) contract even without owning the linac.
**Sandbox:** `shim.py` only.
**Cards:** coherence-if-v1, fel-source-v1, imaging-optics-v1, fel-scanner-twin-v1.
**Metric:** `if_compat_score` (+ pupil_fill_error ≤ 0.10, photons_kept ≥ 0.55).
**KEEP:** pupil_err≤0.10 AND photons_kept≥0.55 AND if_compat≥0.72 on holdout; dual-gate required.
**Must not touch:** eval.py, fixtures, HOLDOUT.sha256, assumptions/*.
**Notes:** Synthetic toys only. No vs-LPP KEEP without lpp-source-v2. Shim must not be a conditioner.py paste.
