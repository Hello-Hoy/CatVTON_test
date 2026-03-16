#!/usr/bin/env python3

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
WORKTREES = ROOT / "worktrees"
EXPECTED = {
    "orchestrator",
    "brainstorm-pmf",
    "market-research",
    "competitor-intel",
    "pricing-revenue",
    "financial-model",
    "technical-story",
}
REQUIRED_FILES = {"AGENTS.md", "README.md", "brief.md", "output.md", "handoff.md", "status.json"}
REQUIRED_STATUS_KEYS = {
    "worktree",
    "state",
    "candidate_id",
    "updated_at",
    "owner",
    "candidate_stage",
    "upstream_inputs",
    "deliverables",
    "blocked_by",
}


def validate_worktree(path: Path) -> list[str]:
    errors: list[str] = []
    missing = [name for name in REQUIRED_FILES if not (path / name).exists()]
    if missing:
        errors.append(f"{path.name}: missing files: {', '.join(sorted(missing))}")
        return errors

    evidence_dir = path / "evidence"
    if not evidence_dir.exists():
        errors.append(f"{path.name}: missing evidence/ directory")

    try:
        status = json.loads((path / "status.json").read_text())
    except json.JSONDecodeError as exc:
        errors.append(f"{path.name}: invalid status.json: {exc}")
        return errors

    missing_keys = REQUIRED_STATUS_KEYS - status.keys()
    if missing_keys:
        errors.append(f"{path.name}: status.json missing keys: {', '.join(sorted(missing_keys))}")

    if status.get("worktree") != path.name:
        errors.append(f"{path.name}: status.json worktree should be '{path.name}'")

    if status.get("state") not in {"todo", "doing", "done", "blocked"}:
        errors.append(f"{path.name}: invalid state '{status.get('state')}'")

    return errors


def main() -> int:
    errors: list[str] = []
    missing_dirs = [name for name in sorted(EXPECTED) if not (WORKTREES / name).is_dir()]
    if missing_dirs:
        errors.append(f"missing worktree directories: {', '.join(missing_dirs)}")

    for name in sorted(EXPECTED):
        path = WORKTREES / name
        if path.is_dir():
            errors.extend(validate_worktree(path))

    if errors:
        print("Business worktree validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Business worktree validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
