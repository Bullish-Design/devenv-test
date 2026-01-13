# Agent Development Guidelines

This document contains guidelines for agentic coding agents working in this repository.

## Environment Setup

This project uses [devenv](https://devenv.sh) for environment management with Python 3.13 and uv package manager.

Activate the environment:
```bash
devenv shell
```

The devenv environment automatically sets up Python with uv for dependency management.

## Build, Lint, and Test Commands

### Building
```bash
devenv shell
python -m build
```

### Linting
```bash
devenv shell
python -m ruff check .
python -m ruff check --fix .
```

### Formatting
```bash
devenv shell
python -m ruff format .
```

### Type Checking
```bash
devenv shell
python -m mypy src/
```

### Running Tests
```bash
devenv shell
python -m pytest                    # Run all tests
python -m pytest tests/test_file.py # Run specific test file
python -m pytest -k test_name       # Run tests matching pattern
python -m pytest -v                 # Verbose output
python -m pytest -x                 # Stop on first failure
```

## Code Style Guidelines

### Imports
- Always start with `from __future__ import annotations` for modern type hints
- Import order: standard library → third-party → local imports
- Use absolute imports within the project (e.g., `from quote_cli.models import Quote`)
- Group related imports together
- No line breaks between import groups

### Formatting
- Use [Ruff](https://docs.astral.sh/ruff/) for formatting (configured in devenv)
- 4-space indentation
- Maximum line length: 88 characters
- Prefer double quotes over single quotes for strings

### Type Hints
- Use modern Python 3.9+ type hint syntax (e.g., `list[Quote]` not `List[Quote]`)
- All functions must include return type hints
- Use `None` explicitly for void returns (e.g., `def main() -> None:`)
- Use Pydantic models for data validation

### Naming Conventions
- Classes: PascalCase (e.g., `QuoteCollection`)
- Functions and methods: snake_case (e.g., `create_default_collection`)
- Constants: UPPER_SNAKE_CASE
- Private members: leading underscore (e.g., `_quotes`)
- Modules and packages: snake_case

### Code Organization
- Models go in `src/quote_cli/models.py`
- Business logic goes in `src/quote_cli/quotes.py`
- CLI interface goes in `src/quote_cli/cli.py`
- Package version in `src/quote_cli/__init__.py`

### Error Handling
- Use Pydantic Field validation for model constraints (e.g., `Field(..., min_length=1)`)
- Raise descriptive exceptions with clear messages
- Log errors appropriately when applicable

### Testing
- Use pytest as the test framework
- Test files should be named `test_*.py` or `*_test.py`
- Place tests in a `tests/` directory at the root
- Write descriptive test names that explain what is being tested

### Dependencies
- Add project dependencies to `dependencies` in pyproject.toml
- Use semantic versioning for dependencies
- Prefer well-maintained packages with recent activity
- Current key dependencies: pydantic (data models), typer (CLI framework)

### CLI Development
- Use typer for CLI applications
- Define CLI entry points in `[project.scripts]` section of pyproject.toml
- Use `typer.echo()` for output
- Include help text for commands and options

### Git Workflow
- Never commit dependencies (uv.lock is committed, but .devenv and .direnv are not)
- Never commit .env or .envrc files with secrets
- Run linting and type checking before committing
- Test changes before committing

## Project Structure

```
src/quote_cli/
├── __init__.py    # Package initialization, version
├── models.py      # Pydantic data models
├── quotes.py      # Business logic and quote collection
└── cli.py         # Typer CLI application
```

## Additional Notes

- This is a CLI application that displays random inspirational quotes
- Python 3.11+ is required
- The entry point is `quote_cli.cli:app` registered as the `quote` command
- Quotes are stored as Pydantic models with text and author fields
- QuoteCollection manages a collection of Quote objects
