"""Тесты для модуля generate_diff (не CLI)."""

from __future__ import annotations

from pathlib import Path

import pytest

from gendiff.scripts.generate_diff import generate_diff


def test_generate_diff_stylish_json(tmp_path: Path):
    file1 = tmp_path / "a.json"
    file2 = tmp_path / "b.json"
    file1.write_text('{"k1": 1, "k2": true}', encoding="utf-8")
    file2.write_text('{"k1": 2, "k3": null}', encoding="utf-8")

    out = generate_diff(str(file1), str(file2), formatter="stylish")
    assert out == """{
  - k1: 1
  + k1: 2
  - k2: true
  + k3: null
}"""


def test_generate_diff_stylish_yaml(tmp_path: Path):
    file1 = tmp_path / "a.yml"
    file2 = tmp_path / "b.yml"
    file1.write_text("k1: 1\nk2: true\n", encoding="utf-8")
    file2.write_text("k1: 2\nk3: null\n", encoding="utf-8")

    out = generate_diff(str(file1), str(file2), formatter="stylish")
    assert out == """{
  - k1: 1
  + k1: 2
  - k2: true
  + k3: null
}"""


def test_generate_diff_unsupported_formatter(tmp_path: Path):
    file1 = tmp_path / "a.json"
    file2 = tmp_path / "b.json"
    file1.write_text('{"a": 1}', encoding="utf-8")
    file2.write_text('{"a": 2}', encoding="utf-8")

    with pytest.raises(ValueError):
        generate_diff(str(file1), str(file2), formatter="unknown")

