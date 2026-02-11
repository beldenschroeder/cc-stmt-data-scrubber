# Credit Card Statement Data Scrubber

## Overview

This Python tool allows one to import a CSV file for a credit card statement and the tool will
scrub the data and format it in a way for importing into Excel document to used for budgeting
and finance.

## Setup

1. Ensure you have [uv installed](https://docs.astral.sh/uv/getting-started/installation/)
2. Clone the repository
3. Install dependencies: `uv sync`
4. (Optional) Setup pre-commit hooks: `uv run pre-commit install`

## Usage

### Option 1: Command-Line Arguments

```bash
uv run cc-scrubber --cc-type personal --input-file input.csv --output-file output.csv
```

**Parameters:**
- `--cc-type`: Credit card type (`family` or `personal`)
- `--input-file`: Path to input CSV file
- `--output-file`: Path to output CSV file

### Option 2: Using .env File

Create a `.env` file (copy from `.env.example`):

```bash
CC_TYPE=personal
INPUT_FILE=/path/to/input.csv
OUTPUT_FILE=/path/to/output.csv
```

Then run without arguments:

```bash
uv run cc-scrubber
```

Command-line arguments override `.env` values.

## Testing

Run all tests:
```bash
uv run pytest tests/ -v
```

Run specific test file:
```bash
uv run pytest tests/test_value_converter.py -v
```

The test suite includes 67 tests covering value conversion, CSV processing, argument parsing, and error handling.

## Development

### Linting and Formatting

Run manually:
```bash
uv run ruff check --fix src/ tests/
uv run ruff format src/ tests/
```

Or use pre-commit hooks (auto-runs on commit):
```bash
uv run pre-commit install
```
