# Business Worktrees

This workspace adds a business-planning layer on top of the CatVTON training repo.

The source of truth for the CatVTON asset remains the project root:

- `README.md`
- `RESULTS_AND_HANDOFF.md`
- `outputs/full-resume/dresscode-16k-512/attention`

The source of truth for business execution lives under `worktrees/`.

## Structure

- `orchestrator`: routes tasks, validates evidence, assembles the final draft
- `brainstorm-pmf`: generates ideas, ICPs, and problem-solution hypotheses
- `market-research`: sizes the market and validates demand signals
- `competitor-intel`: analyzes substitutes, pricing, and positioning
- `pricing-revenue`: designs monetization, pricing, and value metrics
- `financial-model`: projects revenue, costs, burn, and runway
- `technical-story`: translates CatVTON assets into technical differentiation
- `templates`: reusable file templates

## Working Model

1. Start in `orchestrator/brief.md`.
2. Each worktree produces `output.md`, `handoff.md`, and `status.json`.
3. Only `orchestrator` can promote an idea from shortlist to selected business item.
4. Claims used in the final business plan should cite evidence gathered by a specialist worktree.

## Usage Notes

- The role rules live in `worktrees/AGENTS.md` and each worktree's own `AGENTS.md`.
- The role-to-skill mapping lives in `worktrees/SKILL_MATRIX.md`.
- The file contract lives in `worktrees/WORKTREE_CONTRACT.md`.
