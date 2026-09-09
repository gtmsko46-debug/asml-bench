# asml-product-p4-complitho

Comp-litho product umbrella for **P4** (polarization-aware) and **P7** (wavelength-agile 13.5 → 6.x).

Owner: Comp-Litho Product PI.

## Labs (asml-bench)

| Lab path | Product slice | Thesis feed |
|----------|---------------|-------------|
| `labs/p4-polarization/` | P4 | FEL-04 |
| `labs/p7-wavelength/` | P7 | FEL-07 |

## Shared rules

- Critics shared with TH-01 (inverse litho) and TH-03 (overlay commonality)
- Promotion needs BugBot + commonality — Applications-recognizable toys, not NA- or λ-special-case forks
- Harness tickets only via Foreman; dual-provider demos required
- Setup mode until harness provider keys are live — no lasercode runs from this PI

## Status

- [x] Lab `program.md` stubs
- [ ] Assumption card files on disk (`imaging-optics-v1`, `commonality-v1`, …)
- [ ] Frozen `eval.py` + holdout + cheat_trap per lab
- [ ] Baseline `solver.py` scaffolds
- [ ] Product GitHub/Origin repo (name reserved: `asml-product-p4-complitho`)
- [ ] Harness keys live
- [ ] First SEED tickets (paired mock-mistral + grok)
