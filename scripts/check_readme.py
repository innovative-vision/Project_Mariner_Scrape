"""Lightweight README validation for this repository."""

from __future__ import annotations

from pathlib import Path


REQUIRED_PHRASES = (
    "# Project Mariner Scrape",
    "## Current repos",
    "## Before you begin",
    "## Android phone access",
    "## Laptop Chrome tabs",
    "## What else you'll need",
    "## Validation",
)


def validate_readme(path: Path) -> list[str]:
    """Return missing required phrases for the README."""
    content = path.read_text(encoding="utf-8")
    return [phrase for phrase in REQUIRED_PHRASES if phrase not in content]


def main() -> int:
    readme_path = Path(__file__).resolve().parent.parent / "README.md"
    missing = validate_readme(readme_path)

    if missing:
        for phrase in missing:
            print(f"Missing README content: {phrase}")
        return 1

    print("README validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
