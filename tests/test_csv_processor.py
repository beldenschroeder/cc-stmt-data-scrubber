"""Tests for csv_processor module."""

import csv
import tempfile
import pytest
from pathlib import Path
from cc_stmt_data_scrubber.csv_processor import process_row, process_csv_file
from cc_stmt_data_scrubber.csv_config import ColumnConfig


class TestProcessRow:
    """Tests for process_row function."""

    def test_process_family_row(self):
        """Test processing a family card row."""
        config = ColumnConfig(description_column=2, category_column=3, amount_column=5)
        row = ["Date", "Type", "AMAZON PRIME", "", "Merchant", "100.50"]
        
        result = process_row("family", row, config)
        
        assert result[2] == "Amazon Prime"
        assert result[3] == "Family - Subscriptions"
        assert result[5] == -100.50

    def test_process_personal_row(self):
        """Test processing a personal card row."""
        config = ColumnConfig(description_column=3, category_column=4, amount_column=None)
        row = ["Date", "Type", "Merchant", "STARBUCKS", ""]
        
        result = process_row("personal", row, config)
        
        assert result[3] == "Starbucks"
        assert result[4] == "Meals"

    def test_process_row_no_match(self):
        """Test processing row with no conversion match."""
        config = ColumnConfig(description_column=2, category_column=3, amount_column=None)
        row = ["Date", "Type", "UNKNOWN MERCHANT", ""]
        
        result = process_row("family", row, config)
        
        assert result[2] == "UNKNOWN MERCHANT"
        assert result[3] == ""

    def test_process_row_handles_index_error(self):
        """Test that process_row handles IndexError gracefully."""
        config = ColumnConfig(description_column=10, category_column=11, amount_column=None)
        row = ["Date", "Type", "Merchant"]
        
        # Should not raise an exception
        result = process_row("family", row, config)
        assert result == row

    def test_process_row_handles_value_error(self):
        """Test that process_row handles ValueError gracefully."""
        config = ColumnConfig(description_column=2, category_column=3, amount_column=5)
        row = ["Date", "Type", "AMAZON", "", "Merchant", "invalid_amount"]
        
        # Should not raise an exception
        result = process_row("family", row, config)
        assert result[2] == "Amazon"  # Description still converted


class TestProcessCsvFile:
    """Tests for process_csv_file function."""

    def test_process_family_csv(self):
        """Test processing a family card CSV file."""
        # Create temporary input file
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.csv') as infile:
            writer = csv.writer(infile)
            writer.writerow(["Date", "Type", "Description", "Category", "Merchant", "Amount"])
            writer.writerow(["2025-01-01", "Purchase", "AMAZON PRIME", "", "Amazon", "50.00"])
            writer.writerow(["2025-01-02", "Purchase", "COSTCO", "", "Costco", "100.00"])
            input_path = infile.name
        
        # Create temporary output file
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.csv') as outfile:
            output_path = outfile.name
        
        try:
            # Process the file
            process_csv_file("family", input_path, output_path)
            
            # Read and verify output
            with open(output_path, 'r') as f:
                reader = csv.reader(f)
                rows = list(reader)
            
            assert len(rows) == 3
            assert rows[1][2] == "Amazon Prime"
            assert rows[1][3] == "Family - Subscriptions"
            assert rows[1][5] == "-50.0"
            assert rows[2][2] == "Costco"
            assert rows[2][3] == "Family - Groceries"
        finally:
            # Clean up
            Path(input_path).unlink()
            Path(output_path).unlink()

    def test_process_personal_csv(self):
        """Test processing a personal card CSV file."""
        # Create temporary input file
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.csv') as infile:
            writer = csv.writer(infile)
            writer.writerow(["Date", "Type", "Merchant", "Description", "Category"])
            writer.writerow(["2025-01-01", "Purchase", "Starbucks", "STARBUCKS", ""])
            input_path = infile.name
        
        # Create temporary output file
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.csv') as outfile:
            output_path = outfile.name
        
        try:
            # Process the file
            process_csv_file("personal", input_path, output_path)
            
            # Read and verify output
            with open(output_path, 'r') as f:
                reader = csv.reader(f)
                rows = list(reader)
            
            assert len(rows) == 2
            assert rows[1][3] == "Starbucks"
            assert rows[1][4] == "Meals"
        finally:
            # Clean up
            Path(input_path).unlink()
            Path(output_path).unlink()

    def test_process_csv_invalid_card_type(self):
        """Test that invalid card type raises ValueError."""
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.csv') as infile:
            input_path = infile.name
        
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.csv') as outfile:
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
