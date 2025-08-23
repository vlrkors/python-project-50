from gendiff.scripts.generate_diff import generate_diff

TESTS_DIR = "gendiff/tests/test_data"


def test_generate_diff_yaml():
    file1 = f"{TESTS_DIR}/file1.yml"
    file2 = f"{TESTS_DIR}/file2.yml"
    expected = """{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}"""
    result = generate_diff(file1, file2)
    assert result == expected
