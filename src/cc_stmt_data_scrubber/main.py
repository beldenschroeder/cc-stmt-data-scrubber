"""Main application entry point."""

import os
from dotenv import load_dotenv
from cc_stmt_data_scrubber.utils import greet, add_numbers
import csv
import sys
from cc_stmt_data_scrubber.value_converter import convert_desc_value
from cc_stmt_data_scrubber.value_converter import map_desc_to_category
from cc_stmt_data_scrubber.value_converter import convert_amount_value

# Load environment variables from .env file
load_dotenv()


def convert_csv_values(card_type, input_filename, output_filename):
    """
    Converts values in a specific column of a CSV file.

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
        desc_column = -1
        category_column = -1
        amount_column = -1

        if card_type == "family":
            desc_column = 2
            category_column = 3
            amount_column = 5
        elif card_type == "personal":
            desc_column = 3
            category_column = 4

        for row in reader:
            try:
                for column_index, column_value in enumerate(row):
                    if column_index == desc_column:
                        row[column_index] = convert_desc_value(card_type, column_value)
                    elif column_index == category_column:
                        row[column_index] = map_desc_to_category(
                            card_type, row[desc_column]
                        )
                    elif column_index == amount_column:
                        row[column_index] = convert_amount_value(column_value)
            except (IndexError, ValueError):
                # Handle cases where the column is missing or the value can't be converted
                pass
            writer.writerow(row)


def main():
    """Run the main application."""
    print("=" * 50)
    print("Welcome to My Project!")
    print("=" * 50)

    # Example: Using utility functions
    greet("World")
    result = add_numbers(10, 32)
    print(f"10 + 32 = {result}")

    # Example: Using environment variables
    debug_mode = os.getenv("DEBUG", "False")
    print(f"\nDebug mode: {debug_mode}")

    # Example: Making an API call (if API_KEY is set)
    api_key = os.getenv("API_KEY")
    if api_key and api_key != "your_api_key_here":
        print(f"API Key loaded: {api_key[:8]}...")
    else:
        print("No API key configured (see .env.example)")

    # Beginning of data scrubbing
    if len(sys.argv) == 4:
        cc_type = sys.argv[1]
        input_file = sys.argv[2]
        output_file = sys.argv[3]
        # Convert the second column (index 1) to integers
        # convert_csv_values(input_file, output_file, 1, int)

        # Convert the third column (index 2) to floats
        # convert_csv_values(input_file, output_file, 2, float)

        # Convert negative numbers to positive and vice versa
        # convert_csv_values(input_file, output_file, 5, lambda x: -float(x))
        convert_csv_values(cc_type, input_file, output_file)
    else:
        print("Usage: python main.py <cc_type> <input_file> <output_file>")
        sys.exit(1)

    print("\nApplication finished successfully!")


if __name__ == "__main__":
    main()
