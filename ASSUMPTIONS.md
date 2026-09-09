# Assumption Cards

Every numeric or structural claim used by a lab must live in an **assumption card** under `assumptions/`.

## Card requirements

1. **id** + **version** (semver-ish: `*-v1`)
2. **parameters** — each with `value`, `unit`, `source` (citation or open proxy), `confidence` (`low|med|high`), `flags`
3. **flags** must include at least one of:
   - `synthetic` — toy / non-production number
   - `open-proxy` — public literature or open dataset proxy
   - `not-asml-confidential` — explicit non-confidential marker
   - `needs-review` — pending SME check
4. **forbidden**: real fab metrology, customer wafers, ASML internal specs, NXE/EXE production numbers

## Lifecycle

- Cards are immutable once referenced by a seeded results row.
- Amendments → new version file (`*-v2.yaml`), never silent overwrite.
- Labs bind cards via `program.md` and results `card` column.

## Current cards

| File | Scope |
|------|-------|
| `lpp-source-v1.yaml` | LPP source brightness / CE proxies |
| `fel-source-v1.yaml` | FEL / free-electron source proxies |
| `coherence-if-v1.yaml` | Coherence / illumination-filler IF |
| `stochastics-resist-v1.yaml` | Resist stochastics proxies |
| `overlay-thermal-v1.yaml` | Overlay + reticle thermal |
| `tco-v1.yaml` | Cost-of-ownership toy model |
| `commonality-v1.yaml` | Platform commonality hypotheses |
| `imaging-optics-v1.yaml` | Imaging / NA / pupil proxies |
