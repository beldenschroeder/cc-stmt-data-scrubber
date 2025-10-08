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
cc-scrubber
```

Alternatively, you can run it as a Python module:

```bash
python -m cc_stmt_data_scrubber.main
```

Run tests:

```bash
pytest
```

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
