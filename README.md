# Credit Card Statement Data Scrubber

## Overview

This Python tool allows one to import a CSV file for a credit card statement and the tool will
scrub the data and format it in a way for importing into Excel document to used for budgeting
and finance.

## Setup

1. Clone the repository
2. Create virtual environment: `python -m venv venv`
3. Activate virtual environment:
   - Linux/Mac: `source venv/bin/activate`
   - Windows: `venv\Scripts\activate`
4. Install the package in editable mode: `pip install -e .`
5. (Optional) For development, install with dev dependencies: `pip install -e ".[dev]"`
6. (Optional) For development, setup pre-commit hooks: `pre-commit install`

## Usage

Run the application:

```bash
cc-scrubber <cc_type> <input_file> <output_file>
```

Where:
- `cc_type`: Credit card type - either `family` or `personal`
- `input_file`: Path to the input CSV file
- `output_file`: Path to the output CSV file

Example (Mac):

```bash
cc-scrubber personal "/Users/[user]/Downloads/statement.csv" "/Users/[user]/Desktop/output.csv"
```

Example (Windows):

```bash
cc-scrubber personal "C:\Users\[user]\Downloads\statement.csv" "C:\Users\[user]\Desktop\output.csv"
```

Alternatively, you can run it as a Python module:

```bash
python -m cc_stmt_data_scrubber.main <cc_type> <input_file> <output_file>
```

## Testing

The project includes comprehensive unit tests using pytest.

### Run All Tests

```bash
pytest tests/ -v
```

### Run Specific Test File

```bash
pytest tests/test_value_converter.py -v
```

### Run Specific Test Class

```bash
pytest tests/test_csv_processor.py::TestProcessRow -v
```

### Run with Short Traceback

```bash
pytest tests/ -v --tb=short
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

### Install Development Dependencies

Install the package with dev dependencies (pytest, black, flake8, isort, pre-commit):

```bash
pip install -e ".[dev]"
```

### Pre-commit Hooks

This project uses `pre-commit` to automatically format and lint code before each commit.

**Setup pre-commit hooks:**

```bash
pre-commit install
```

**What it does:**
- Automatically runs `black` to format code
- Runs `flake8` to check code style
- Runs `isort` to sort imports
- Checks for trailing whitespace, large files, merge conflicts, etc.

**Manual run (optional):**

```bash
# Run on all files
pre-commit run --all-files

# Run on staged files only
pre-commit run
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
black src/ tests/
```

**Sort imports:**

```bash
isort src/ tests/
```

**Lint code:**

```bash
flake8 src/ tests/
```
