"""Bootstrap checklist helpers for local and mobile access."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Requirement:
    name: str
    required: bool = True


COMMON_REQUIREMENTS = (
    Requirement("Python 3.11+"),
    Requirement("pip"),
    Requirement("Git"),
    Requirement("Google Chrome on the host machine"),
    Requirement("Google AI Studio API key"),
    Requirement("Stable internet connection"),
)

LAPTOP_REQUIREMENTS = (
    Requirement("Laptop with Chrome tabs available for the Mariner session"),
    Requirement("Ability to keep the browser window and host machine awake during runs"),
)

ANDROID_REQUIREMENTS = (
    Requirement("Android phone with Chrome installed"),
    Requirement("Phone and host machine on the same network or a secure tunnel to the host"),
)

OPTIONAL_REQUIREMENTS = (
    Requirement("Dedicated VPS or always-on machine for long running sessions", required=False),
    Requirement("Password manager for storing the API key", required=False),
)


def build_setup_checklist(has_api_key: bool = False) -> dict[str, list[str]]:
    """Return a grouped setup checklist for bootstrapping the project."""
    common = [item.name for item in COMMON_REQUIREMENTS if has_api_key or "API key" not in item.name]
    if not has_api_key:
        common.append("Get a Google AI Studio API key before first run")

    return {
        "common": common,
        "laptop": [item.name for item in LAPTOP_REQUIREMENTS],
        "android": [item.name for item in ANDROID_REQUIREMENTS],
        "optional": [item.name for item in OPTIONAL_REQUIREMENTS],
    }


def render_checklist(has_api_key: bool = False) -> str:
    """Render the grouped setup checklist as readable text."""
    checklist = build_setup_checklist(has_api_key=has_api_key)
    ordered_sections = ("common", "laptop", "android", "optional")
    titles = {
        "common": "Common requirements",
        "laptop": "Laptop / Chrome tabs",
        "android": "Android phone access",
        "optional": "Optional but recommended",
    }

    lines: list[str] = []
    for section in ordered_sections:
        lines.append(f"{titles[section]}:")
        lines.extend(f"- {item}" for item in checklist[section])
        lines.append("")

    return "\n".join(lines).strip()


if __name__ == "__main__":
    print(render_checklist())
