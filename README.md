# Credit Card Statement Data Scrubber

## Overview

This Python tool allows one to import a CSV file for a credit card statement and the tool will
scrub the data and format it in a way for importing into Excel document to used for budgeting
and finance.

## Setup

1. Clone the repository
2. Ensure you have [Poetry installed](https://python-poetry.org/docs/#installation)
3. Install dependencies and create virtual environment: `poetry install`
4. (Optional) For development, setup pre-commit hooks: `poetry run pre-commit install`

### Build the Project

To build the executable binary:

```bash
poetry build
```

This creates distribution files in the `dist/` directory.

## Usage

Run the application using Poetry:

```bash
poetry run cc-scrubber <cc_type> <input_file> <output_file>
```

Or activate Poetry's shell environment first:

```bash
poetry shell
cc-scrubber <cc_type> <input_file> <output_file>
```

Where:

- `cc_type`: Credit card type - either `family` or `personal`
- `input_file`: Path to the input CSV file
- `output_file`: Path to the output CSV file

Example (Mac):

```bash
poetry run cc-scrubber personal "/Users/[user]/Downloads/personal-cc-statement-2025-12-05.csv" "/Users/[user]/Desktop/personal-cc-statement-output.csv"
```

Example (Windows):

```bash
poetry run cc-scrubber personal "C:\Users\[user]\Downloads\personal-cc-statement-2025-12-05.csv" "C:\Users\[user]\Desktop\personal-cc-statement-output.csv"
```

Alternatively, you can run it as a Python module:

```bash
poetry run python -m cc_stmt_data_scrubber.main <cc_type> <input_file> <output_file>
```

## Testing

The project includes comprehensive unit tests using pytest.

### Run All Tests

```bash
poetry run pytest tests/ -v
```

### Run Specific Test File

```bash
poetry run pytest tests/test_value_converter.py -v
```

### Run Specific Test Class

```bash
poetry run pytest tests/test_csv_processor.py::TestProcessRow -v
```

### Run with Short Traceback

```bash
poetry run pytest tests/ -v --tb=short
```

### Test Coverage

The test suite includes 67 tests covering:

- Value conversion functions
- Description and category mappings
- CSV configuration
- CSV file processing
- Command-line argument parsing
- Error handling and edge cases

## Development

### Pre-commit Hooks

This project uses `pre-commit` to automatically format and lint code before each commit.

**Install pre-commit (if not already installed):**

Since `pre-commit` is a dev dependency, it's installed with Poetry:

```bash
poetry install
```

**Setup pre-commit hooks:**

Once installed, activate the hooks in your repository:

```bash
poetry run pre-commit install
```

**What it does:**

- Automatically runs `black` to format code
- Runs `flake8` to check code style
- Runs `isort` to sort imports
- Checks for trailing whitespace, large files, merge conflicts, etc.

**Manual run (optional):**

```bash
# Run on all files
poetry run pre-commit run --all-files

# Run on staged files only
poetry run pre-commit run
```

**Skip hooks (when needed):**

```bash
# Skip all hooks for emergency commits
git commit --no-verify -m "Emergency fix"
```

### Manual Formatting and Linting

If you prefer to run tools manually:

**Format code:**

```bash
poetry run black src/ tests/
```

**Sort imports:**

```bash
poetry run isort src/ tests/
```

**Lint code:**

```bash
poetry run flake8 src/ tests/
```
