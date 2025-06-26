install:
	uv sync

build: 
	uv build

gendiff:
	uv run gendiff

package-install:
	uv tool install dist/*.whl

package-uninstall:
	uv tool uninstall dist/*.whl

install:
	uv tool install .

uninstall:
	uv tool uninstall .
	
lint:
	uv run ruff check hexlet_code

record:
	asciinema rec gendiff.cast
	
	