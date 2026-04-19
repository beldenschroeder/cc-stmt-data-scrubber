"""CSV file processing for credit card statement data scrubbing."""

import csv
from typing import Iterable, List

from .csv_config import OUTPUT_HEADER, ColumnConfig, get_column_config
from .value_converter import convert_desc_value


def process_row(card_type: str, row: List[str], config: ColumnConfig) -> List[str]:
    """Process a single CSV row by applying conversions and restructuring output.

    Output columns: Date, Description, Amount, Statement Ending, Month Ending,
    Item Total, Debit, Credit

    Args:
        card_type: The credit card type ('family' or 'personal').
        row: Column values for the row.
        config: Column configuration with indices.

    Returns:
        New list with the restructured output columns.
    """
    try:
        clearing_date = row[config.clearing_date_column]
        merchant = row[config.merchant_column]
        amount_str = row[config.amount_column]

        # Apply description conversion to merchant value
        description = convert_desc_value(card_type, merchant)

        # Parse amount
        amount = float(amount_str)

        # Split into debit/credit based on sign
        debit = f"{amount:.2f}" if amount < 0 else ""
        credit = f"{amount:.2f}" if amount >= 0 else ""

        return [
            clearing_date,
            description,
            f"{amount:.2f}",
            "",
            "",
            "",
            debit,
            credit,
        ]
    except (IndexError, ValueError):
        return row


def process_rows(card_type: str, rows: Iterable[List[str]]) -> Iterable[List[str]]:
    """Process multiple CSV rows by applying conversions.

    This function focuses solely on data transformation logic,
    separated from I/O concerns (SRP compliance).

    Args:
        card_type: The credit card type ('family' or 'personal').
        rows: Iterable of rows, where each row is a list of column values.

    Yields:
        Processed rows with conversions applied.
    """
    config = get_column_config(card_type)

    for row in rows:
        yield process_row(card_type, row, config)


def process_csv_file(card_type: str, input_filename: str, output_filename: str) -> None:
    """Process a CSV file by applying conversions to specific columns.

    This function handles file I/O and delegates processing to process_rows().

    Args:
        card_type: The credit card type ('family' or 'personal').
        input_filename: Path to the input CSV file.
        output_filename: Path to the output CSV file.
    """
    with open(input_filename, "r", encoding="utf-8") as infile, open(
        output_filename, "w", newline="", encoding="utf-8"
    ) as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        # Skip input header
        next(reader, None)

        # Write output header
        writer.writerow(OUTPUT_HEADER)

        # Delegate processing logic to process_rows()
        processed_rows = process_rows(card_type, reader)
        writer.writerows(processed_rows)
