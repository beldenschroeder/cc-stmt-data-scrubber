"""Main application entry point."""

import os
from dotenv import load_dotenv
from cc_stmt_data_scrubber.utils import greet, add_numbers

# Load environment variables from .env file
load_dotenv()


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

    print("\nApplication finished successfully!")


if __name__ == "__main__":
    main()
