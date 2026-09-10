# P1 twin fixture harden — HT-1018 (2026-09-10)

**Owner:** Eval Integrity  
**Ticket:** HT-1018 / Issue #33  
**Trigger:** HT-1013 oracle recovery of v1 `gen_fixtures.truth()` (train/holdout/trap ≈ 0).

## Contract (Twin PI revise)
- **Sandbox:** `labs/p1-twin/gen_fixtures_harden.py` (editable regenerator)
- **Frozen:** `eval.py`, `twin.py`, `assumptions/fel-scanner-twin-v1.yaml`
- **Import-only:** `products/asml-product-p1-twin/gen_fixtures.py` (v1 reference for oracle contrast)
- Regen **together:** train + holdout + cheat_trap + HOLDOUT.sha256

## Landed
- Critic: `eval.py` VOIDs if `holdout_nrmse < 1e-6` alone (`saturated: generative recovery`), independent of trap
- `fixture_gen=v2-ht1018-harden-2026-09-10`
- **HOLDOUT.sha256:** `2c398448a78b496b871794ad27d644d7a14b174426b538f1af7807f75bcc603c`
- Nonlinear / saturation / cross terms + label jitter + OOD holdout + `p1-cheat-v1oracle` trap rows

## Acceptance (frozen eval KEEP bar `<0.55`)
| Twin | holdout_nrmse | decision |
|------|---------------|----------|
| HT-1013 oracle clone | ≈1.12 | **RESET** (fails KEEP) |
| HT-1014-class structural | ≈1.03 | **SEED** (scoreable) |
| Baseline weak twin | ≈1.27 | **SEED** |

## Next
Experimentalist stamps DEEP HT-1015/1016 against this HOLDOUT only. Dual-gate required. Do not copy harden `truth_v2`. Metric-bar changes (if any) → Critic + Director — not this ticket.
