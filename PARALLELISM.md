# Parallel lasercode (no DB lock bottleneck)

## Rule
Always run fleet work through `lasercode-session` with a **unique** `LASERCODE_SESSION_ID`.

That gives each run its own `XDG_DATA_HOME` / SQLite under:
`/home/box/.local/share/lasercode-sessions/<id>/`

Do **not** pile concurrent plain `lasercode` onto the default `~/.local/share/opencode` DB.

## Reading another bot’s session
No auto-export. If you need another run’s chat/DB, read it from disk:

```bash
lasercode-sessions list
lasercode-sessions show <id>
# or directly:
ls /home/box/.local/share/lasercode-sessions/<id>/share/opencode/
```

Open that session’s DB / files read-only. Do not write into another session’s home.

## Example
```bash
export LASERCODE_SESSION_ID="ticket-123-operator"
lasercode-session run --dir labs/th-04-reticle-heat --auto --format json \
  -m xai/grok-4.6 --variant high "..."
```
