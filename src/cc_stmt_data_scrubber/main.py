"""Main application entry point."""

import sys

import click
from dotenv import load_dotenv

from cc_stmt_data_scrubber.csv_processor import process_csv_file


class EnvDefaultCommand(click.Command):
    """A Click command that loads .env before resolving defaults."""

    def invoke(self, ctx: click.Context) -> None:
        load_dotenv()
        super().invoke(ctx)


@click.command(cls=EnvDefaultCommand)
@click.option(
    "--cc-type",
    type=click.Choice(["family", "personal"], case_sensitive=False),
    envvar="CC_TYPE",
    help="Credit card type (can be set in .env as CC_TYPE).",
    required=True,
)
@click.option(
    "--input-file",
    type=click.Path(exists=True),
    envvar="INPUT_FILE",
    help="Path to the input CSV file (can be set in .env as INPUT_FILE).",
    required=True,
)
@click.option(
    "--output-file",
    type=click.Path(),
    envvar="OUTPUT_FILE",
    help="Path to the output CSV file (can be set in .env as OUTPUT_FILE).",
    required=True,
)
def main(cc_type: str, input_file: str, output_file: str) -> None:
    """Credit Card Statement Data Scrubber.

    Scrubs credit card statement CSV data and formats it for Excel import.
    Options can also be provided via a .env file.
    """
    try:
        process_csv_file(cc_type, input_file, output_file)
        click.echo("\nApplication finished successfully!")
    except ValueError as e:
        click.echo(f"Error: {e}", err=True)
        sys.exit(1)
    except FileNotFoundError as e:
        click.echo(f"Error: File not found - {e}", err=True)
        sys.exit(1)
    except Exception as e:
        click.echo(f"Unexpected error: {e}", err=True)
        sys.exit(1)


if __name__ == "__main__":
    main()
