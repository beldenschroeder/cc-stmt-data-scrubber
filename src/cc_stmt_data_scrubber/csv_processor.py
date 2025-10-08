"""CSV file processing for credit card statement data scrubbing."""

import csv

from .csv_config import get_column_config
from .value_converter import convert_desc_value, map_desc_to_category, convert_amount_value


def process_row(card_type, row, config):
    """Process a single CSV row by applying conversions.
    
    Args:
        card_type: The credit card type ('family' or 'personal').
        row: List of column values for the row.
        config: ColumnConfig object with column indices.
        
    Returns:
        Modified row with conversions applied.
    """
    try:
        for column_index, column_value in enumerate(row):
            if column_index == config.description_column:
                row[column_index] = convert_desc_value(card_type, column_value)
            elif column_index == config.category_column:
                row[column_index] = map_desc_to_category(
                    card_type, row[config.description_column]
                )
            elif config.amount_column is not None and column_index == config.amount_column:
                row[column_index] = convert_amount_value(column_value)
    except (IndexError, ValueError):
        # Handle cases where the column is missing or the value can't be converted
        pass
    
    return row


def process_csv_file(card_type, input_filename, output_filename):
    """Process a CSV file by applying conversions to specific columns.
    
    Args:
        card_type: The credit card type ('family' or 'personal').
        input_filename: Path to the input CSV file.
        output_filename: Path to the output CSV file.
    """
    config = get_column_config(card_type)
    
    with open(input_filename, "r", encoding="utf-8") as infile, open(
        output_filename, "w", newline="", encoding="utf-8"
    ) as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)
        
        for row in reader:
            processed_row = process_row(card_type, row, config)
            writer.writerow(processed_row)
