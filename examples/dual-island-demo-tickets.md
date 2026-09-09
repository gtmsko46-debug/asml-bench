# Example dual-island tickets (same frozen eval)

Use as a paired demo seed. Two tickets, identical thesis/sandbox/eval bindings, different providers.

## Island A — mock-mistral (weak / scaffold island)

```json
{
  "ticket_id": "HT-DEMO-MISTRAL",
  "thesis": "th-04-reticle-heat",
  "hypothesis": "A linear thermal residual term reduces holdout RMSE without NXE forks.",
  "provider": "mock-mistral",
  "assumption_cards": ["overlay-thermal-v1"],
  "lab_path": "labs/th-04-reticle-heat",
  "sandbox": "solver.py",
  "metric": "holdout_rmse",
  "budget": "3 ratchets / 20m",
  "must_not_touch": ["eval.py", "fixture/holdout*", "fixture/cheat_trap.json", "fixture/HOLDOUT.sha256", "assumptions/"],
  "decision": "SEED",
  "guards": ["thermal_term_nonzero", "no_nxe_platform_fork"],
  "created_at": "2026-09-09T00:00:00Z",
  "notes": "Demo island A. Pair with HT-DEMO-GROK. Do not present alone."
}
```

## Island B — grok (science / long-loop island)

```json
{
  "ticket_id": "HT-DEMO-GROK",
  "thesis": "th-04-reticle-heat",
  "hypothesis": "A linear thermal residual term reduces holdout RMSE without NXE forks.",
  "provider": "grok",
  "assumption_cards": ["overlay-thermal-v1"],
  "lab_path": "labs/th-04-reticle-heat",
  "sandbox": "solver.py",
  "metric": "holdout_rmse",
  "budget": "6 ratchets / 40m",
  "must_not_touch": ["eval.py", "fixture/holdout*", "fixture/cheat_trap.json", "fixture/HOLDOUT.sha256", "assumptions/"],
  "decision": "SEED",
  "guards": ["thermal_term_nonzero", "no_nxe_platform_fork"],
  "created_at": "2026-09-09T00:00:00Z",
  "notes": "Demo island B. Pair with HT-DEMO-MISTRAL. Same frozen eval."
}
```
