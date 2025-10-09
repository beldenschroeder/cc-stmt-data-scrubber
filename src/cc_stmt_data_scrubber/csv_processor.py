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
        if config.amount_column is not None and len(processed_row) > config.amount_column:
            processed_row[config.amount_column] = convert_amount_value(
                processed_row[config.amount_column]
            )
    except (IndexError, ValueError):
        # Handle cases where the column is missing or the value can't be converted
        pass
    
    return processed_row


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
