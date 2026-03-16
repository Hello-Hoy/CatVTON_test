# Worktree Contract

## Required Files

### `brief.md`

Must include:

- business objective
- current candidate stage
- required deliverables
- evidence expectations
- known constraints

### `output.md`

Must include:

- executive summary
- recommendation
- evidence references
- open risks
- confidence level

### `handoff.md`

Must include:

- what changed
- what the next worktree should do
- unresolved questions

### `status.json`

Must include:

- `worktree`
- `state`
- `candidate_id`
- `updated_at`
- `owner`
- `upstream_inputs`
- `deliverables`
- `blocked_by`

## Lifecycle

Allowed `state` values:

- `todo`
- `doing`
- `done`
- `blocked`

Allowed candidate stages:

- `idea_pool`
- `shortlist`
- `validated_candidate`
- `selected_business_item`
- `business_plan_draft_ready`

## Promotion Rules

- `brainstorm-pmf` can move ideas into `shortlist`.
- `market-research`, `competitor-intel`, `pricing-revenue`, `financial-model`, and `technical-story` can recommend promotion to `validated_candidate`.
- `orchestrator` is responsible for final promotion into `selected_business_item` and `business_plan_draft_ready`.
