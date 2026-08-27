"""Fail when a fixture/example root lacks its required synthetic-data marker."""

from __future__ import annotations

from pathlib import Path


DATA_ROOTS = (Path("fixtures"), Path("examples"), Path("tests/fixtures"))
MARKER_NAME = "SYNTHETIC_DATA.md"
REQUIRED_TEXT = "synthetic"


def main() -> int:
    failures: list[str] = []

    for root in DATA_ROOTS:
        if not root.exists():
            continue

        marker = root / MARKER_NAME
        if not marker.is_file():
            failures.append(f"{root}: add {MARKER_NAME} before committing data")
            continue

        if REQUIRED_TEXT not in marker.read_text(encoding="utf-8").lower():
            failures.append(f"{marker}: state that all data is synthetic")

    if failures:
        print("Synthetic-data policy check failed:")
        print("\n".join(failures))
        return 1

    print("Synthetic-data policy check passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

