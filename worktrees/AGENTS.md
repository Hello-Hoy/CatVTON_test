# Worktree Agent Rules

These instructions apply to all worktrees under `worktrees/`.

## Shared Contract

Every specialist worktree maintains these files:

- `brief.md`: task from orchestrator
- `output.md`: final analysis for the current cycle
- `handoff.md`: concise summary for downstream consumers
- `status.json`: machine-readable state
- `evidence/`: supporting artifacts, notes, links, or exported data

## Decision Rules

- Worktrees may recommend a direction but may not finalize the business item.
- `orchestrator` is the only worktree allowed to mark a candidate as selected.
- If a claim lacks evidence, say so explicitly instead of filling the gap with assumptions.
- Prefer the CatVTON repository facts over generic AI fashion claims.

## CatVTON Grounding

When making product or technical claims, ground them in:

- `RESULTS_AND_HANDOFF.md`
- `README.md`
- actual checkpoint layout under `outputs/`

Do not imply production-grade robustness if the repo only demonstrates qualitative validation.

## Evidence Standard

Use the following confidence levels in `output.md` when relevant:

- `high`: directly supported by repo artifacts or verified external data
- `medium`: likely, but based on partial evidence
- `low`: directional hypothesis that still needs validation
