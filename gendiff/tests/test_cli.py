"""Тесты для CLI (gendiff.scripts.cli)."""

from __future__ import annotations

import sys
from pathlib import Path

from gendiff.scripts.cli import main


def test_cli_main_stdout(tmp_path: Path, capsys):
    f1 = tmp_path / "f1.json"
    f2 = tmp_path / "f2.json"
    f1.write_text('{"a": 1, "b": 2}', encoding="utf-8")
    f2.write_text('{"a": 1, "c": 3}', encoding="utf-8")

    argv_backup = sys.argv[:]
    try:
        sys.argv = ["gendiff", str(f1), str(f2)]
        main()
    finally:
        sys.argv = argv_backup

    captured = capsys.readouterr()
    assert captured.out == """{
    a: 1
  - b: 2
  + c: 3
}
"""

