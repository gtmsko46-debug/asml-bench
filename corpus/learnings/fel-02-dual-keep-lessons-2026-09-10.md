# FEL-02 dual-KEEP lessons (2026-09-10)

**Audience:** champion / FEL research spine / P2 Illuminator feed  
**Card:** `coherence-if-v1` only (live-demo spine — **not** vs-LPP)  
**Stamp:** HT-1011 ∧ HT-1022 `DUAL_KEEP_STAMPED` (Critic + Repro + Diplomat)  
**Eval:** pupil freeze `main@84520ee` PR #40 — KEEP ANDs `pupil_err ≤ 0.10` with `speckle < 0.15` and `photons ≥ 0.55`  
**Ticket docket:** `photons_kept == 1.0` where Critic stamped (stricter than eval floor)

## Metrics

| Ticket | Provider | Speckle | Pupil | Photons |
|--------|----------|---------|-------|---------|
| HT-1011 | grok | 0.0413 | 0.0096 | 1.0 |
| HT-1022 | mock-mistral | 0.1017 | 0.0475 | 1.0 |

## What won

1. **Pupil-first structure:** reconstruct fill → correct toward `pupil_fill_target=0.72` → emit `pupil_err = |fill − 0.72|`.
2. **Real field inputs for speckle:** use `field["coherence"]` and `bandwidth` — do not invent coherence from pupil error.
3. **Dual-gate discipline:** identical frozen eval; single-lane KEEP rejected until Diplomat stamps both.
4. **Independence:** conditioner sha and metric triad must not clone a sibling KEEP (HT-1012 died here).

## Critic VOID / RESET history (do not revive)

| Ticket | Kill |
|--------|------|
| HT-1012 | Metric + byte clone of HT-1009; diffuser-coupled pupil shrink |
| HT-1017 | Bar-tuned write-down `abs(err−0.72)*k` + invented coherence |
| HT-1019 | Soft `abs(delta)*k` residual; target ≠ 0.72; ignored field coherence |

## Standing falsifiers for conditioner tickets

- No `abs(err−target)*scale` or residual-only write-down without correcting fill state
- No invented coherence from pupil_err
- No metric reuse across ticket IDs
- No conditioner byte-clone of a KEEP sibling
- No P2/product KEEP language until Illuminator P2 eval/sandbox/champion job (feed tickets OK citing gated research dual-KEEP)

## Hand-offs

- **P2 productize:** Lab Director APPROVED; Illuminator + Experimentalist; feed HT-1023/1024 (queued behind P1 bay P0)
- **FEL-10:** commercial IF ownership on `p10-if-shim`; consumes `coherence-if-v1` read-only; Critic+Warden+IF Spec before Foreman
- **Bay:** do not starve P1 Operator lane

## Soft deepen (parked)

HT-1022 still uses crude `fill = 1 − pfe` and `speckle = coherence * bandwidth * 100` — Critic soft notes, not reopen of dual-KEEP. Product path may deepen; research may deepen only on explicit ask.
