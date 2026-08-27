from __future__ import annotations

import subprocess
import sys
from pathlib import Path


def test_fixture_and_example_roots_have_synthetic_data_markers() -> None:
    repository_root = Path(__file__).parents[1]
    result = subprocess.run(
        [sys.executable, "scripts/check_synthetic_data.py"],
        cwd=repository_root,
        capture_output=True,
        text=True,
        check=False,
    )

    assert result.returncode == 0, result.stdout + result.stderr
