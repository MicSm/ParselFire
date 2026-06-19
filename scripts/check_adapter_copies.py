from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CANONICAL_PATH = Path("AGENTS.md")
COPY_ADAPTERS = [
    Path("CLAUDE.md"),
    Path(".github/copilot-instructions.md"),
    Path(".windsurf/rules/parselfire.md"),
    Path(".clinerules/parselfire.md"),
    Path(".agents/rules/parselfire.md"),
]
WRAPPED_COPY_ADAPTERS = [
    Path(".kiro/steering/parselfire.md"),
]
MANIFEST_ADAPTERS = [
    Path("gemini-extension.json"),
]


def read_text(rel_path: Path) -> str:
    path = ROOT / rel_path
    return path.read_text(encoding="utf-8").replace("\r\n", "\n").strip()


def strip_frontmatter(text: str) -> str:
    return re.sub(r"^---\n[\s\S]*?\n---\n*", "", text).strip()


def main() -> int:
    errors: list[str] = []

    try:
        canonical = read_text(CANONICAL_PATH)
    except FileNotFoundError:
        print(f"Missing canonical adapter source: {CANONICAL_PATH}")
        return 1

    for rel_path in COPY_ADAPTERS:
        try:
            actual = read_text(rel_path)
        except FileNotFoundError:
            errors.append(f"missing copy-based adapter: {rel_path}")
            continue
        if actual != canonical:
            errors.append(f"{rel_path} drifted from {CANONICAL_PATH}")

    for rel_path in WRAPPED_COPY_ADAPTERS:
        try:
            actual = strip_frontmatter(read_text(rel_path))
        except FileNotFoundError:
            errors.append(f"missing wrapped copy adapter: {rel_path}")
            continue
        if actual != canonical:
            errors.append(f"{rel_path} drifted from {CANONICAL_PATH}")

    try:
        version = read_text(Path("VERSION"))
    except FileNotFoundError:
        errors.append("missing VERSION")
        version = ""

    for rel_path in MANIFEST_ADAPTERS:
        try:
            manifest = json.loads(read_text(rel_path))
        except FileNotFoundError:
            errors.append(f"missing manifest-only adapter: {rel_path}")
            continue
        except json.JSONDecodeError as exc:
            errors.append(f"{rel_path} is not valid JSON: {exc}")
            continue

        if manifest.get("contextFileName") != CANONICAL_PATH.name:
            errors.append(f"{rel_path} must point at {CANONICAL_PATH.name}")
        if version and manifest.get("version") != version:
            errors.append(f"{rel_path} version must match VERSION ({version})")

    if errors:
        print("Adapter portability check failed:")
        for error in errors:
            print(f"  - {error}")
        return 1

    print(
        "OK: copy-based adapters match AGENTS.md, wrapped adapters normalize to "
        "AGENTS.md, and manifest-only adapters point at the canonical contract."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
