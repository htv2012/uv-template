.PHONY: all test run lint clean install

### Default target(s)
all: test run

### Clean up generated files
clean:
	uv clean
	rm -fr .ruff_cache .venv

### Install this tool locally
install:
	uv tool install --upgrade .

### Perform static analysis
lint:
	uv tool run ruff check --select I --fix .
	uv tool run ruff format .
	uv tool run ruff check . --fix

### Run the project
run: lint
	uv run xyz

### Run unit tests
test: lint
	uv run pytest --suppress-no-test-exit-code -vv

