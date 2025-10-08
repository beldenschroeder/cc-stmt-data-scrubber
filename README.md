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
5. Copy `.env.example` to `.env` and configure

## Usage

Run the application:

```bash
cc-scrubber <cc_type> <input_file> <output_file>
```

Where:
- `cc_type`: Credit card type - either `family` or `personal`
- `input_file`: Path to the input CSV file
- `output_file`: Path to the output CSV file

Example:

```bash
cc-scrubber personal "~/Downloads/statement.csv" "~/Desktop/output.csv"
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

Install the package with dev dependencies (pytest, black, flake8):

```bash
pip install -e ".[dev]"
```

Format code:

```bash
black src/ tests/
```

Lint code:

```bash
flake8 src/ tests/
```
