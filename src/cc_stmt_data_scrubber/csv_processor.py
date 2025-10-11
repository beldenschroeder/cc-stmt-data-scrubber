"""CSV file processing for credit card statement data scrubbing."""

import csv
from typing import Iterable, List

from .csv_config import get_column_config
from .value_converter import (
    convert_amount_value,
    convert_desc_value,
    map_desc_to_category,
)


def process_row(card_type: str, row: List[str], config) -> List[str]:
    """Process a single CSV row by applying conversions.

    Args:
        card_type: The credit card type ('family' or 'personal').
        row: Column values for the row.
        config: Column configuration with indices.

    Returns:
        New list with conversions applied.
    """
    # Create a copy to avoid mutating the input
    processed_row = list(row)

    try:
        # Process description column
        if len(processed_row) > config.description_column:
            processed_row[config.description_column] = convert_desc_value(
                card_type, processed_row[config.description_column]
            )

        # Process category column
        if len(processed_row) > config.category_column:
            processed_row[config.category_column] = map_desc_to_category(
                card_type, processed_row[config.description_column]
            )

        # Process amount column (if configured)
        if (
            config.amount_column is not None
            and len(processed_row) > config.amount_column
        ):
            processed_row[config.amount_column] = convert_amount_value(
                processed_row[config.amount_column]
            )
    except (IndexError, ValueError):
        # Handle cases where the column is missing or the value can't be converted
        pass

    return processed_row


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

        # Delegate processing logic to process_rows()
        processed_rows = process_rows(card_type, reader)
        writer.writerows(processed_rows)
