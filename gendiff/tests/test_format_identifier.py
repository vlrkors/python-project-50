"""Тесты для диспетчера форматтеров format_identifier."""

from gendiff.formatters.format_identifier import format_identifier
from gendiff.formatters.plain import format_diff_plain
from gendiff.formatters.stylish import format_stylish
from gendiff.formatters.json_formatter import format_diff_json
from gendiff.scripts.find_diff import build_diff


def _sample_diff():
    d1 = {"a": 1, "b": {"x": 1}}
    d2 = {"a": 2, "b": {"x": 1, "y": 2}}
    return build_diff(d1, d2)


def test_format_identifier_stylish():
    diff = _sample_diff()
    assert format_identifier(diff, "stylish") == format_stylish(diff)


def test_format_identifier_plain():
    diff = _sample_diff()
    assert format_identifier(diff, "plain") == format_diff_plain(diff)


def test_format_identifier_json():
    diff = _sample_diff()
    assert format_identifier(diff, "json") == format_diff_json(diff)


def test_format_identifier_unknown():
    diff = _sample_diff()
    with pytest.raises(ValueError):
        format_identifier(diff, "unknown")

