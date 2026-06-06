"""Tests for csv_processor module."""

import csv
import tempfile
from pathlib import Path

import pytest
from cc_stmt_data_scrubber.csv_config import ColumnConfig
from cc_stmt_data_scrubber.csv_processor import (
    process_csv_file,
    process_row,
    process_rows,
)

# Input format: Transaction Date, Clearing Date, Description, Merchant,
#               Category, Type, Amount (USD), Purchased By
INPUT_HEADER = [
    "Transaction Date",
    "Clearing Date",
    "Description",
    "Merchant",
    "Category",
    "Type",
    "Amount (USD)",
    "Purchased By",
]

FAMILY_CONFIG = ColumnConfig(
    clearing_date_column=1,
    merchant_column=3,
    amount_column=6,
    purchases_are_negative=True,
)

PERSONAL_CONFIG = ColumnConfig(
    clearing_date_column=1,
    merchant_column=3,
    amount_column=6,
    purchases_are_negative=False,
)


class TestProcessRow:
    """Tests for process_row function."""

    def test_process_family_row_purchase(self):
        """Test processing a family card row with a negative amount (purchase)."""
        row = [
            "01/15/2025",
            "01/16/2025",
            "AMAZON PRIME",
            "AMAZON PRIME",
            "Shopping",
            "Purchase",
            "-100.50",
            "John",
        ]

        result = process_row("family", row, FAMILY_CONFIG)

        assert result[0] == "01/16/2025"  # Date (from Clearing Date)
        assert result[1] == "Amazon Prime"  # Description (converted Merchant)
        assert result[2] == "Family - Subscriptions"  # Account
        assert result[3] == ""  # Statement Ending
        assert result[4] == ""  # Month Ending
        assert result[5] == ""  # Item Total
        assert result[6] == ""  # Debit (empty for purchase)
        assert result[7] == "100.50"  # Credit (purchase increases liability)

    def test_process_family_row_refund(self):
        """Test processing a family card row with a positive amount (refund/debit)."""
        row = [
            "01/15/2025",
            "01/16/2025",
            "REFUND",
            "Refund",
            "Refund",
            "Return",
            "50.00",
            "John",
        ]

        result = process_row("family", row, FAMILY_CONFIG)

        assert result[0] == "01/16/2025"  # Date
        assert result[2] == ""  # Account (no mapping for Refund)
        assert result[6] == "50.00"  # Debit (refund reduces liability)
        assert result[7] == ""  # Credit (empty for refund)

    def test_process_personal_row(self):
        """Test processing a personal card row."""
        row = [
            "01/15/2025",
            "01/16/2025",
            "STARBUCKS #1234",
            "STARBUCKS",
            "Food",
            "Purchase",
            "5.75",  # Apple Card exports purchases as positive
            "Jane",
        ]

        result = process_row("personal", row, PERSONAL_CONFIG)

        assert result[0] == "01/16/2025"
        assert result[1] == "Starbucks"
        assert result[2] == "Meals"  # Account
        assert result[6] == ""  # Debit (empty for purchase)
        assert result[7] == "5.75"  # Credit (purchase increases liability)

    def test_process_row_zero_amount_is_credit(self):
        """Test that zero amount goes to credit column."""
        row = [
            "01/15/2025",
            "01/16/2025",
            "ADJUSTMENT",
            "Adjustment",
            "",
            "Adjustment",
            "0.00",
            "John",
        ]

        result = process_row("family", row, FAMILY_CONFIG)

        assert result[2] == ""  # Account (no mapping for Adjustment)
        assert result[6] == ""  # Debit empty
        assert result[7] == "0.00"  # Credit

    def test_process_row_no_match(self):
        """Test processing row with no conversion match."""
        row = [
            "01/15/2025",
            "01/16/2025",
            "UNKNOWN",
            "UNKNOWN MERCHANT",
            "",
            "Purchase",
            "-10.00",
            "John",
        ]

        result = process_row("family", row, FAMILY_CONFIG)

        assert result[1] == "UNKNOWN MERCHANT"  # No conversion match

    def test_process_row_handles_index_error(self):
        """Test that process_row handles IndexError gracefully."""
        config = ColumnConfig(
            clearing_date_column=1,
            merchant_column=10,
            amount_column=12,
        )
        row = ["01/15/2025", "01/16/2025", "Merchant"]

        result = process_row("family", row, config)
        assert result == row

    def test_process_row_handles_value_error(self):
        """Test that process_row handles ValueError gracefully."""
        row = [
            "01/15/2025",
            "01/16/2025",
            "AMAZON",
            "Amazon",
            "",
            "Purchase",
            "invalid_amount",
            "John",
        ]

        result = process_row("family", row, FAMILY_CONFIG)
        assert result == row

    def test_output_has_eight_columns(self):
        """Test that output row has exactly 8 columns."""
        row = [
            "01/15/2025",
            "01/16/2025",
            "COSTCO",
            "COSTCO",
            "Groceries",
            "Purchase",
            "-75.50",
            "John",
        ]

        result = process_row("family", row, FAMILY_CONFIG)
        assert len(result) == 8


class TestProcessRows:
    """Tests for process_rows function (SRP-compliant data processing)."""

    def test_process_rows_in_memory(self):
        """Test processing rows without file I/O (demonstrates SRP benefit)."""
        # Chase (JPMorgan) format: Date, Post Date, Desc, Category, Type, Amount, Memo
        input_rows = [
            [
                "01/15/2025",
                "01/16/2025",
                "AMAZON PRIME",
                "Shopping",
                "Purchase",
                "-50.00",
                "",
            ],
            [
                "01/16/2025",
                "01/17/2025",
                "COSTCO",
                "Groceries",
                "Purchase",
                "-100.00",
                "",
            ],
        ]

        result = list(process_rows("family", input_rows))

        assert len(result) == 2
        assert result[0][0] == "01/16/2025"  # Post Date
        assert result[0][1] == "Amazon Prime"  # Converted merchant
        assert result[0][2] == "Family - Subscriptions"  # Account
        assert result[0][6] == ""  # Debit (empty for purchase)
        assert result[0][7] == "50.00"  # Credit (purchase increases liability)
        assert result[1][1] == "Costco"

    def test_process_rows_generator(self):
        """Test that process_rows returns a generator (memory efficient)."""
        input_rows = [
            [
                "01/15/2025",
                "01/16/2025",
                "STARBUCKS",
                "STARBUCKS",
                "Food",
                "Purchase",
                "-5.00",
                "Jane",
            ]
        ]

        result = process_rows("personal", input_rows)

        assert hasattr(result, "__iter__")
        assert hasattr(result, "__next__")

    def test_process_rows_empty(self):
        """Test processing empty row list."""
        result = list(process_rows("family", []))
        assert result == []


class TestProcessCsvFile:
    """Tests for process_csv_file function."""

    def test_process_family_csv(self):
        """Test processing a family (JPMorgan Chase) card CSV file."""
        # Chase (JPMorgan) format: Date, Post Date, Desc, Category, Type, Amount, Memo
        chase_header = [
            "Transaction Date",
            "Post Date",
            "Description",
            "Category",
            "Type",
            "Amount",
            "Memo",
        ]
        with tempfile.NamedTemporaryFile(
            mode="w", delete=False, suffix=".csv"
        ) as infile:
            writer = csv.writer(infile)
            writer.writerow(chase_header)
            writer.writerow(
                [
                    "01/15/2025",
                    "01/16/2025",
                    "AMAZON PRIME",
                    "Shopping",
                    "Purchase",
                    "-50.00",
                    "",
                ]
            )
            writer.writerow(
                [
                    "01/16/2025",
                    "01/17/2025",
                    "COSTCO",
                    "Groceries",
                    "Purchase",
                    "-100.00",
                    "",
                ]
            )
            input_path = infile.name

        with tempfile.NamedTemporaryFile(
            mode="w", delete=False, suffix=".csv"
        ) as outfile:
            output_path = outfile.name

        try:
            process_csv_file("family", input_path, output_path)

            with open(output_path, "r") as f:
                reader = csv.reader(f)
                rows = list(reader)

            # Header + 2 data rows
            assert len(rows) == 3
            # Verify output header
            assert rows[0] == [
                "Date",
                "Description",
                "Account",
                "Statement Ending",
                "Month Ending",
                "Item Total",
                "Debit",
                "Credit",
            ]
            # Verify first data row
            assert rows[1][0] == "01/16/2025"  # Date
            assert rows[1][1] == "Amazon Prime"  # Description
            assert rows[1][2] == "Family - Subscriptions"  # Account
            assert rows[1][3] == ""  # Statement Ending
            assert rows[1][4] == ""  # Month Ending
            assert rows[1][5] == ""  # Item Total
            assert rows[1][6] == ""  # Debit (empty for purchase)
            assert rows[1][7] == "50.00"  # Credit (purchase increases liability)
            # Verify second data row
            assert rows[2][1] == "Costco"
            assert rows[2][2] == "Family - Groceries"  # Account
        finally:
            Path(input_path).unlink()
            Path(output_path).unlink()

    def test_process_personal_csv(self):
        """Test processing a personal card CSV file."""
        with tempfile.NamedTemporaryFile(
            mode="w", delete=False, suffix=".csv"
        ) as infile:
            writer = csv.writer(infile)
            writer.writerow(INPUT_HEADER)
            writer.writerow(
                [
                    "01/15/2025",
                    "01/16/2025",
                    "STARBUCKS #1234",
                    "STARBUCKS",
                    "Food",
                    "Purchase",
                    "5.75",  # Apple Card exports purchases as positive
                    "Jane",
                ]
            )
            input_path = infile.name

        with tempfile.NamedTemporaryFile(
            mode="w", delete=False, suffix=".csv"
        ) as outfile:
            output_path = outfile.name

        try:
            process_csv_file("personal", input_path, output_path)

            with open(output_path, "r") as f:
                reader = csv.reader(f)
                rows = list(reader)

            assert len(rows) == 2
            assert rows[0][0] == "Date"  # Header
            assert rows[1][0] == "01/16/2025"
            assert rows[1][1] == "Starbucks"
            assert rows[1][6] == ""  # Debit (empty for purchase)
            assert rows[1][7] == "5.75"  # Credit (purchase increases liability)
        finally:
            Path(input_path).unlink()
            Path(output_path).unlink()

    def test_process_csv_credit_amount(self):
        """Test processing a family CSV with a positive amount (credit)."""
        # Chase (JPMorgan) format: Date, Post Date, Desc, Category, Type, Amount, Memo
        chase_header = [
            "Transaction Date",
            "Post Date",
            "Description",
            "Category",
            "Type",
            "Amount",
            "Memo",
        ]
        with tempfile.NamedTemporaryFile(
            mode="w", delete=False, suffix=".csv"
        ) as infile:
            writer = csv.writer(infile)
            writer.writerow(chase_header)
            writer.writerow(
                ["01/15/2025", "01/16/2025", "REFUND", "", "Return", "25.00", ""]
            )
            input_path = infile.name

        with tempfile.NamedTemporaryFile(
            mode="w", delete=False, suffix=".csv"
        ) as outfile:
            output_path = outfile.name

        try:
            process_csv_file("family", input_path, output_path)

            with open(output_path, "r") as f:
                reader = csv.reader(f)
                rows = list(reader)

            assert rows[1][6] == "25.00"  # Debit (refund reduces liability)
            assert rows[1][7] == ""  # Credit (empty for refund)
        finally:
            Path(input_path).unlink()
            Path(output_path).unlink()

    def test_process_csv_invalid_card_type(self):
        """Test that invalid card type raises ValueError."""
        with tempfile.NamedTemporaryFile(
            mode="w", delete=False, suffix=".csv"
        ) as infile:
            input_path = infile.name

        with tempfile.NamedTemporaryFile(
            mode="w", delete=False, suffix=".csv"
        ) as outfile:
            output_path = outfile.name

        try:
            with pytest.raises(ValueError):
                process_csv_file("invalid", input_path, output_path)
        finally:
            Path(input_path).unlink()
            Path(output_path).unlink()

    def test_process_csv_file_not_found(self):
        """Test that missing input file raises FileNotFoundError."""
        with pytest.raises(FileNotFoundError):
            process_csv_file("family", "nonexistent.csv", "output.csv")
