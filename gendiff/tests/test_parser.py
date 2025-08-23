"""Тесты для модуля parser."""

from __future__ import annotations

from pathlib import Path

import pytest

from gendiff.scripts import parser as p


def test_get_file_format():
    assert p.get_file_format("config.json") == "json"
    assert p.get_file_format("config.yaml") == "yaml"
    assert p.get_file_format("config.yml") == "yml"


def test_read_file_not_found(tmp_path: Path):
    missing = tmp_path / "missing.json"
    with pytest.raises(FileNotFoundError):
        p.read_file(str(missing))


def test_parse_data_json(tmp_path: Path):
    content = "{a: 1, b: true}"
    path = tmp_path / "data.json"
    path.write_text(content, encoding="utf-8")
    data = p.parse_data_from_file(str(path))
    assert data == {"a": 1, "b": True}


def test_parse_data_yaml(tmp_path: Path):
    try:
        import yaml  # noqa: F401
    except ModuleNotFoundError:
        pytest.skip("PyYAML не установлен")

    content = "a: 1\nb: true\n"
    path = tmp_path / "data.yml"
    path.write_text(content, encoding="utf-8")
    data = p.parse_data_from_file(str(path))
    assert data == {"a": 1, "b": True}


def test_parse_data_unsupported():
    with pytest.raises(ValueError):
        p.parse_data("a=b", "ini")
