# Credit Card Statement Data Scrubber

## Overview

This Python tool allows one to import a CSV file for a credit card statement and the tool will
scrub the data and format it in a way for importing into an Excel document to be used for budgeting
and finance.

Requires Python 3.14+.

## CSV Input Format

The input CSV must be a transaction export downloaded from [JPMorgan Chase](https://www.chase.com/) online banking. Chase provides this file when you select "Download account activity" from a credit card account and choose the CSV format.

The file must have the following columns in this order:

| Column           | Description                                      |
| ---------------- | ------------------------------------------------ |
| Transaction Date | Date the transaction was made                    |
| Clearing Date    | Date the transaction cleared                     |
| Description      | Raw transaction description from Chase           |
| Merchant         | Merchant name as identified by Chase             |
| Category         | Chase-assigned spending category                 |
| Type             | Transaction type (e.g. Purchase, Return)         |
| Amount (USD)     | Transaction amount; negative for debits          |
| Purchased By     | Cardholder name (relevant for family/joint cards)|

## CSV Output Format

The tool produces an output CSV with the following columns:

| Column           | Description                                                        |
| ---------------- | ------------------------------------------------------------------ |
| Date             | From the input "Clearing Date" column                              |
| Description      | From the input "Merchant" column, with name normalization applied  |
| Account          | Expense category derived from the merchant (e.g. "Meals")          |
| Statement Ending | Empty (for manual entry in Excel)                                  |
| Month Ending     | Empty (for manual entry in Excel)                                  |
| Item Total       | Empty (for manual entry in Excel)                                  |
| Debit            | The absolute amount if the transaction is a debit, otherwise empty |
| Credit           | The amount if the transaction is a credit, otherwise empty         |

## Setup

1. Ensure you have [uv installed](https://docs.astral.sh/uv/getting-started/installation/)
2. Clone the repository
3. Install dependencies: `uv sync`

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

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for development setup, testing, and linting instructions.
