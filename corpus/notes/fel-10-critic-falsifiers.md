# Critic FEL-10 falsifiers

**Encoded by Scribe** `2026-09-10T08:58:19Z` from CoS request + `tickets/FEL-10_CLAIM_DRAFT.md` / `IF_SPEC_FEL10_CONTRACT.md`.

## Primary falsifier
Tin-LPP-class fixture on `lpp-source-v2` matches or beats FEL shim/compat score without FEL-specific IF ownership → **RESET**.

## Kill lines before SEED
- `lpp-source-v2` only on vs-LPP falsifier ticket (never scaffold SEED)
- No photon-discard / weaken-tin LPP win (Warden)
- IF Spec contract bound (pupil ≤0.10 KEEP; photons_kept ≥0.55 + if_loss_db; pol/pulse/pointing reported)
- No rewrite IF Spec / no mutate `coherence-if-v1`
- Frozen eval + holdout hash
- Dual-gate required; bay behind P1; no upstairs without Warden+TCO; not product KEEP

See also: `corpus/learnings/LATEST.md`, `corpus/notes/if-ownership-fel-10.md`.

## SoT HOLDOUT pin `2026-09-10T09:16:14Z`
- Authoritative: `d0dc1f8a7b8cc97ddd00122fb4156252c7642a09a7f0ae5102b939747c6cc5be`
- File: `labs/p10-if-shim/fixture/HOLDOUT.sha256`
