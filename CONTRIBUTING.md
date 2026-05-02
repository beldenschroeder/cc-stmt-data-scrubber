# Contributing

## Setup

1. Ensure you have [uv installed](https://docs.astral.sh/uv/getting-started/installation/)
2. Clone the repository
3. Install dependencies (including dev tools): `uv sync --extra dev`
4. Setup pre-commit hooks: `uv run pre-commit install`

## Testing

Run all tests:

```bash
uv run pytest tests/ -v
```

Run a specific test file:

```bash
uv run pytest tests/test_value_converter.py -v
```

## Linting and Formatting

Run manually:

```bash
uv run ruff check --fix src/ tests/
uv run ruff format src/ tests/
```

Or use pre-commit hooks, which run automatically on each commit:

```bash
uv run pre-commit install
```
