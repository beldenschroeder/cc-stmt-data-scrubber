"""Main application entry point."""

import argparse
import os
import sys
from typing import Tuple

from dotenv import load_dotenv

from cc_stmt_data_scrubber.csv_processor import process_csv_file


def parse_arguments() -> Tuple[str, str, str]:
    """Parse and validate command-line arguments.

    Supports both command-line arguments and .env file configuration.
    Command-line arguments take precedence over .env file values.

    Returns:
        Tuple of (card_type, input_file, output_file).

    Raises:
        SystemExit: If required arguments are missing or invalid.
    """
    # Load .env file if it exists
    load_dotenv()

    parser = argparse.ArgumentParser(
        description="Credit Card Statement Data Scrubber",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Using command-line arguments
  cc-scrubber --cc-type personal --input-file statement.csv --output-file output.csv

  # Using .env file (values can be overridden with command-line arguments)
  cc-scrubber
        """,
    )

    parser.add_argument(
        "--cc-type",
        dest="cc_type",
        help="Credit card type: 'family' or 'personal' (can be set in .env as CC_TYPE)",
        default=os.getenv("CC_TYPE"),
    )

    parser.add_argument(
        "--input-file",
        dest="input_file",
        help="Path to the input CSV file (can be set in .env as INPUT_FILE)",
        default=os.getenv("INPUT_FILE"),
    )

    parser.add_argument(
        "--output-file",
        dest="output_file",
        help="Path to the output CSV file (can be set in .env as OUTPUT_FILE)",
        default=os.getenv("OUTPUT_FILE"),
    )

    args = parser.parse_args()

    # Validate that all required arguments are provided
    missing_args: list[str] = []
    if not args.cc_type:
        missing_args.append("--cc-type (or CC_TYPE in .env)")
    if not args.input_file:
        missing_args.append("--input-file (or INPUT_FILE in .env)")
    if not args.output_file:
        missing_args.append("--output-file (or OUTPUT_FILE in .env)")

    if missing_args:
        parser.print_help()
        print(f"\nError: Missing required arguments: {', '.join(missing_args)}")
        sys.exit(1)

    return args.cc_type, args.input_file, args.output_file


def main() -> None:
    """Run the main application."""
    card_type, input_file, output_file = parse_arguments()

    try:
        process_csv_file(card_type, input_file, output_file)
        print("\nApplication finished successfully!")
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)
    except FileNotFoundError as e:
        print(f"Error: File not found - {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
