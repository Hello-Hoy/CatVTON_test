# Skill Matrix

This file maps each worktree to the recommended local skills and external skill candidates.

## Already Available Locally

- `catvton-train-reconstruction`
- `apify-market-research`
- `apify-competitor-intelligence`
- `pricing-strategy`
- `startup-financial-modeling`
- `doc`
- `pdf`
- `slides`
- `spreadsheet`

## Worktree Mapping

### `orchestrator`

- Primary: repo-local `AGENTS.md` contract
- Optional support: `doc`, `pdf`, `slides`
- Reason: synthesis and final document assembly are custom to this repo

### `brainstorm-pmf`

- Primary local behavior: repo-local `AGENTS.md`
- External candidates from `phuryn/pm-skills`:
  - `pm-product-discovery/skills/brainstorm-ideas-new`
  - `pm-go-to-market/skills/ideal-customer-profile`
  - `pm-product-strategy/skills/startup-canvas`
  - `pm-product-strategy/skills/value-proposition`

### `market-research`

- Primary: `apify-market-research`
- External candidates from `phuryn/pm-skills`:
  - `pm-market-research/skills/market-sizing`
  - `pm-market-research/skills/market-segments`
  - `pm-market-research/skills/user-personas`

### `competitor-intel`

- Primary: `apify-competitor-intelligence`
- External candidates from `phuryn/pm-skills`:
  - `pm-market-research/skills/competitor-analysis`
  - `pm-go-to-market/skills/competitive-battlecard`
  - `pm-product-strategy/skills/porters-five-forces`

### `pricing-revenue`

- Primary: `pricing-strategy`
- External candidates from `phuryn/pm-skills`:
  - `pm-product-strategy/skills/business-model`
  - `pm-product-strategy/skills/monetization-strategy`
  - `pm-product-strategy/skills/pricing-strategy`

### `financial-model`

- Primary: `startup-financial-modeling`
- Secondary: `spreadsheet`
- External candidates from `phuryn/pm-skills`:
  - `pm-data-analytics/skills/cohort-analysis`

### `technical-story`

- Primary: `catvton-train-reconstruction`
- Secondary: repo artifacts only

## Documentation Skills

Useful optional installs from `anthropics/skills`:

- `skills/doc-coauthoring`
- `skills/pptx`
- `skills/pdf`

These are not required immediately because similar local capabilities already exist.

## Install Commands

The helper below installs skills into `~/.codex/skills`. Restart Codex after using it.

Example from `phuryn/pm-skills`:

```bash
python3 /Users/hyohee/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py \
  --repo phuryn/pm-skills \
  --path \
  pm-product-discovery/skills/brainstorm-ideas-new \
  pm-go-to-market/skills/ideal-customer-profile \
  pm-market-research/skills/market-sizing
```

Example from `anthropics/skills`:

```bash
python3 /Users/hyohee/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py \
  --repo anthropics/skills \
  --path skills/doc-coauthoring
```
