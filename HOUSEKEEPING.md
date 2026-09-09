# Housekeeping

Bots may install tools and work freely — but **leave no bloat**.

## Auto-cleanable (script)
```bash
lab-housekeep           # remove smoke/tmp/debug sessions + __pycache__
lab-housekeep --dry-run
```
Session homes: `/home/box/.local/share/lasercode-sessions/<id>/`

## Cannot auto-delete (sidebar)
Grok agents and channels cannot be deleted by bots. Rules:
- Do not create throwaway bots/channels
- If unavoidable, name `TEMP: …` and ask the user to Delete when done
- Delete `RETIRED Customer-Harness` if it still exists

See skill: lab housekeeping.
