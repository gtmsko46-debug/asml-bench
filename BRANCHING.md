# Branching Policy

## Experiment branches

```
exp/<thesis>-<ticket>
```

Examples:

- `exp/th-04-HT-1042`
- `exp/fel-02-COH-77`

## Rules

1. **Never edit main fixtures** (`fixture/train.json`, `holdout.json`, `cheat_trap.json`, hashes) on `main`.
2. Solvers and notebooks may diverge on `exp/*`; merge to `main` only via Foreman-reviewed PR.
3. Do not rewrite history of seeded `results.tsv` SEED rows.
4. Thesis id in branch name must match `labs/<thesis>/` directory slug prefix where applicable.
5. Ticket id must exist in harness ticket log / backlog reference.

## Forbidden on main

- Quietly changing holdout labels
- Zeroing thermal terms to pass TH-04
- Photon-dropping cheats as default FEL-02 solver
- `if platform == "NXE":` special-case forks in promoted solvers
