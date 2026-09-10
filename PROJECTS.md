# GitHub Projects — Litho Lab Factory

## Status (2026-09-10)

Attempted to create Project (v2) **"Litho Lab Factory"** under `gtmsko46-debug` via GraphQL `createProjectV2`.

**Blocked:** token scopes are only `gist`, `read:org`, `repo`. Projects API requires `project` + `read:project` (INSUFFICIENT_SCOPES / effectively 403).

## Refresh command (run as gtmsko46-debug)

```bash
gh auth refresh -s read:project,project
```

Then recreate / link the board:

```bash
# After refresh — create project and add asml-bench
OWNER_ID=$(gh api user --jq .node_id)
gh api graphql -f query='
mutation($ownerId:ID!, $title:String!) {
  createProjectV2(input:{ownerId:$ownerId, title:$title}) {
    projectV2 { id title url number }
  }
}' -f ownerId="$OWNER_ID" -f title='Litho Lab Factory'
```

Desired status columns: **Backlog → Spec → Build → Review → Ship → Done**. Link repo `gtmsko46-debug/asml-bench` (and optionally `asml-product-p1-twin`, `asml-research-fel`).

## Fallback board (active now)

Milestones on `asml-bench` mirror the columns:

| Milestone | Role |
|-----------|------|
| Backlog | Unscheduled / waiting |
| Spec | Spec stage |
| Build | Build stage |
| Review | Dual-provider review |
| Ship | Ship queue |
| Done | Closed / shipped |

Filter issues by milestone + labels (`stage:*`, `track:*`, `provider:*`, `dual-gate`).

Do not wake bots from this doc. Foreman owns hills.
