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


def test_read_file_returns_exact_content(tmp_path: Path):
    """read_file возвращает содержимое без изменений (UTF-8)."""
    content = "строка с юникодом ✓ and ascii"
    path = tmp_path / "text.txt"
    path.write_text(content, encoding="utf-8")
    assert p.read_file(str(path)) == content


def test_get_file_format_from_complex_name():
    """Формат определяется по последнему суффиксу после точки."""
    assert p.get_file_format("backup.data.config.json") == "json"


def test_parse_data_from_file_uppercase_json_extension(tmp_path: Path):
    """Парсинг JSON работает при верхнем регистре расширения."""
    path = tmp_path / "DATA.JSON"
    path.write_text('{"a": 1, "b": true}', encoding="utf-8")
    assert p.parse_data_from_file(str(path)) == {"a": 1, "b": True}


def test_parse_data_from_file_uppercase_yaml_extension(tmp_path: Path):
    """Парсинг YAML работает при верхнем регистре расширения."""
    try:
        import yaml  # noqa: F401
    except ModuleNotFoundError:
        pytest.skip("PyYAML не установлен")

    path = tmp_path / "DATA.YML"
    path.write_text("a: 1\nb: false\n", encoding="utf-8")
    assert p.parse_data_from_file(str(path)) == {"a": 1, "b": False}


def test_parse_data_json_fallback_to_yaml_for_unquoted_keys():
    """Для формата 'json' допускаем YAML-парсинг при нестрогом JSON."""
    data = "{a: 1, b: true}"
    assert p.parse_data(data, "json") == {"a": 1, "b": True}
