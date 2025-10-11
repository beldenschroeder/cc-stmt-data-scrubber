"""Main application entry point."""

import sys
from typing import Tuple

from cc_stmt_data_scrubber.csv_processor import process_csv_file


def parse_arguments() -> Tuple[str, str, str]:
    """Parse and validate command-line arguments.
    
    Returns:
        Tuple of (card_type, input_file, output_file).
        
    Raises:
        SystemExit: If arguments are invalid.
    """
    if len(sys.argv) != 4:
        print("Usage: cc-scrubber <cc_type> <input_file> <output_file>")
        print("  cc_type: 'family' or 'personal'")
        sys.exit(1)
    
    return sys.argv[1], sys.argv[2], sys.argv[3]


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
