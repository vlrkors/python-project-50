install:
	uv sync

install_project:
	uv pip install -e 

build: 
	uv build

gendiff:
	uv run gendiff

package-install:
	uv tool install dist/*.whl

package-uninstall:
	uv tool uninstall dist/*.whl

uninstall:
	uv tool uninstall .
	
lint: format
	uv run ruff check gendiff

format:
	uv run ruff format gendiff

record:
	asciinema rec gendiff.cast
	
	