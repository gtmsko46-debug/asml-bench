# How to cite assumption cards

**Access / write date**: 2026-09-09  
**Schema**: `schemas/assumption_card.schema.json`  
**Index of cards**: `ASSUMPTIONS.md` + files under `assumptions/*.yaml`

## Rules

1. **Cite by card id + version**, not by paraphrasing numbers without provenance.  
   Example: `coherence-if-v1@1.0.0`.
2. Every numeric claim in a lab `results.tsv` / note that comes from a card should name the **parameter** (`spatial_sigma`, `ce_percent`, …).
3. Respect card `flags`: `synthetic`, `open-proxy`, `not-asml-confidential`, `needs-review`. Never upgrade confidence in prose beyond the YAML.
4. When a note depends on OA literature *and* a card, cite **both** (card for the number; paper for the physics story).
5. Do not copy ASML confidential or customer process numbers into cards. Public investor-deck order-of-magnitude chatter is already marked synthetic in `lpp-source-v1` / `tco-v1`.

## Current cards (keep; do not delete)

| id | Title | Typical labs |
|----|-------|--------------|
| `lpp-source-v1` | LPP EUV source proxies | source / TCO narratives |
| `fel-source-v1` | FEL / alternate-source coherence | FEL-02 |
| `coherence-if-v1` | Illumination-filler / coherence IF | FEL-02, P10 |
| `overlay-thermal-v1` | Reticle / overlay thermal | TH-04 |
| `stochastics-resist-v1` | Resist stochastics / LCDU | p5-stochastics |
| `imaging-optics-v1` | NA / pupil / wavelength | P4, P7 |
| `beam-split-first-mirror-v1` | Multi-kW split + first mirror | FEL-03 |
| `commonality-v1` | Platform commonality | P4 BugBot gate |
| `tco-v1` | TCO toy model | p9-tco |

## Markdown citation snippets

Inline:

```markdown
Pupil fill target from [`coherence-if-v1`](../../assumptions/coherence-if-v1.yaml)
(`pupil_fill_target=0.72`, synthetic).
```

Results footer:

```markdown
## Assumptions
- coherence-if-v1@1.0.0
- fel-source-v1@1.0.0
## Literature
- Schneidmiller et al., arXiv:1108.5986 (local `corpus/papers/1108.5986.pdf`)
```

## Changing numbers

Edit the YAML card (bump `version` if semantics change), re-run the lab eval, and note the version in the commit message. Do **not** hard-code shadowed copies of card values inside solvers without a comment pointing at the card id.
