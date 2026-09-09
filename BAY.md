# Coding bay (v1 — no redundancy)

```
Experimentalist files Issue ticket
        ↓
Harness Foreman  — validate, stamp, assign LASERCODE_SESSION_ID
        ↓
Lasercode Operator — ONE pair of hands
        ├── provider=grok        → xai/grok-4.6 [--variant high]
        └── provider=mock-mistral → mistral stub (same binary, XAI key)
        ↓
Eval Runner → results.tsv → Repro → kill-the-claim
```

**Retired:** Customer-Harness Operator (delete from sidebar). Dual-provider is a ticket field, not a second bot.

**Parallelism:** always `/workspace/tools/bin/lasercode-session` with unique `LASERCODE_SESSION_ID` (isolates SQLite via XDG_DATA_HOME). Never pile plain `lasercode` onto the shared default DB.
