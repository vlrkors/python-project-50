from pathlib import Path

from gendiff import generate_diff

FIXTURES_PATH = Path(__file__).with_name("test_data")


def test_generate_diff():
    """Сравнение плоских JSON-файлов в формате stylish."""
    file1_path = FIXTURES_PATH / "file1.json"
    file2_path = FIXTURES_PATH / "file2.json"

    expected_result = """{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}"""

    actual_result = generate_diff(str(file1_path), str(file2_path))

    assert actual_result == expected_result
