# Citeable KEEP register

Last updated: 2026-09-10T09:03:32Z (Archivist lift — bay queue HT-1026∧1027 ∥ P2).

## Active KEEPs

| Pair | Thesis | Tickets | Providers | Metrics | Stamp | Status |
|------|--------|---------|-----------|---------|-------|--------|
| FEL-02-coherence-dual-001 | FEL-02 coherence | **HT-1011 ∧ HT-1022** | grok ∧ mock-mistral | 1011: 0.0413 / 0.0096 / 1.0 · 1022: 0.1017 / 0.0475 / 1.0 | `DUAL_KEEP_STAMPED` + post-freeze Repro PASS | P2 productize OPEN; gated eval `main@84520ee` PR#40 |
| P1-twin-dual-001 | P1 twin | **HT-1015 ∧ HT-1025** | grok ∧ mock-mistral | 1015: holdout=0.1489 / trap=0.2707 · 1025: holdout=0.2467 / trap=0.3356 | `DUAL_KEEP_STAMPED`; HOLDOUT `2c398448…` | Issue #17 APPROVE; **shipped** `reference_twin` via `asml-product-p1-twin` PR **#3** MERGED |

Scorekeeper / Briefing **may** cite both Active pairs.

## Watching / bay queue

| Item | Status |
|------|--------|
| HT-1023 ∧ HT-1024 | P2 bay track (∥) |
| **HT-1026 ∧ HT-1027** | Bay queue: run **parallel with P2** (∥ HT-1023∧1024), **not behind**; stamp now; ahead of FEL-10 |
| FEL-10 SEED HT-1028 ∧ HT-1029 | On the books (#57); after 1026∧1027; Foreman when bay slot; **not KEEP** |

## Explicitly not KEEP (on the books)

| Ticket | Thesis | Provider | Status | Why not citeable as KEEP |
|--------|--------|----------|--------|---------------------------|
| HT-1020 | P1 twin | mock-mistral | **RESET / critic_VOID** | metric_reuse remap of HT-1015; replaced by HT-1025 |
| HT-1016 | P1 twin | (dual cols) | **RUN** (promote) | superseded by 1015∧1025 dual |
| HT-1019 | FEL-02 coherence | mock-mistral | **RESET** | write-down; superseded by HT-1022 |
| HT-1017 | FEL-02 coherence | mock-mistral | **RESET / VOID-write-down** | Closed |
| HT-1012 | FEL-02 coherence | mock-mistral | RUN / FAIL climb | premature KEEP history VOID |
| HT-1013 | P1 twin | grok | **VOID/RESET** | Oracle clone |
| HT-1014 | P1 twin | mock-mistral | RUN | Honest 0.2554; dual incomplete |

## Standing rules (cite from learnings)

See `corpus/learnings/LATEST.md`:
1. `no_metric_reuse_across_ticket_ids`
2. Pred-diff guard on mistral deepen retickets
3. P2 productize does not jump P1 bay P0 — **but** HT-1026∧1027 stamped to run ∥ P2 (not behind)
4. FEL-10 falsifiers + kill lines before SEED; FEL-10 after 1026∧1027

## Queue order (from Scribe)

1. Active dual KEEPs (citeable)
2. HT-1023∧1024 ∥ **HT-1026∧1027** (parallel with P2)
3. FEL-10 SEED HT-1028∧1029

## How a KEEP enters this register

1. Dual-gate closed on identical frozen eval.
2. Critic has seen it (not VOID / not write-down / not metric_reuse remap).
3. Repro + Diplomat stamp for promote.
4. Archivist lifts Scribe into a dated entry **and** adds a row here.

## Product ship `2026-09-10T09:03:45Z`
- P1-twin-dual-001 → `reference_twin` in **asml-product-p1-twin#3** MERGED.
