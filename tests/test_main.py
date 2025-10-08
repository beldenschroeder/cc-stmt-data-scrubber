"""Tests for main module."""

import sys
import pytest
from unittest.mock import patch, MagicMock
from cc_stmt_data_scrubber.main import parse_arguments, main


class TestParseArguments:
    """Tests for parse_arguments function."""

    def test_valid_arguments(self):
        """Test parsing valid command-line arguments."""
        test_args = ["cc-scrubber", "family", "input.csv", "output.csv"]
        with patch.object(sys, 'argv', test_args):
            card_type, input_file, output_file = parse_arguments()
            assert card_type == "family"
            assert input_file == "input.csv"
            assert output_file == "output.csv"

    def test_missing_arguments(self):
        """Test that missing arguments causes exit."""
        test_args = ["cc-scrubber", "family"]
        with patch.object(sys, 'argv', test_args):
            with pytest.raises(SystemExit) as exc_info:
                parse_arguments()
            assert exc_info.value.code == 1

    def test_no_arguments(self):
        """Test that no arguments causes exit."""
        test_args = ["cc-scrubber"]
        with patch.object(sys, 'argv', test_args):
            with pytest.raises(SystemExit) as exc_info:
                parse_arguments()
            assert exc_info.value.code == 1

    def test_too_many_arguments(self):
        """Test that too many arguments causes exit."""
        test_args = ["cc-scrubber", "family", "input.csv", "output.csv", "extra"]
        with patch.object(sys, 'argv', test_args):
            with pytest.raises(SystemExit) as exc_info:
                parse_arguments()
            assert exc_info.value.code == 1


class TestMain:
    """Tests for main function."""

    @patch('cc_stmt_data_scrubber.main.process_csv_file')
    @patch('cc_stmt_data_scrubber.main.parse_arguments')
    def test_main_success(self, mock_parse, mock_process):
        """Test successful execution of main."""
        mock_parse.return_value = ("family", "input.csv", "output.csv")
        mock_process.return_value = None
        
        main()
        
        mock_parse.assert_called_once()
        mock_process.assert_called_once_with("family", "input.csv", "output.csv")

    @patch('cc_stmt_data_scrubber.main.process_csv_file')
    @patch('cc_stmt_data_scrubber.main.parse_arguments')
    def test_main_value_error(self, mock_parse, mock_process):
        """Test main handles ValueError."""
        mock_parse.return_value = ("invalid", "input.csv", "output.csv")
        mock_process.side_effect = ValueError("Unknown card type")
        
        with pytest.raises(SystemExit) as exc_info:
            main()
        assert exc_info.value.code == 1

    @patch('cc_stmt_data_scrubber.main.process_csv_file')
    @patch('cc_stmt_data_scrubber.main.parse_arguments')
    def test_main_file_not_found(self, mock_parse, mock_process):
        """Test main handles FileNotFoundError."""
        mock_parse.return_value = ("family", "missing.csv", "output.csv")
        mock_process.side_effect = FileNotFoundError("File not found")
        
        with pytest.raises(SystemExit) as exc_info:
            main()
        assert exc_info.value.code == 1

    @patch('cc_stmt_data_scrubber.main.process_csv_file')
    @patch('cc_stmt_data_scrubber.main.parse_arguments')
    def test_main_unexpected_error(self, mock_parse, mock_process):
        """Test main handles unexpected exceptions."""
        mock_parse.return_value = ("family", "input.csv", "output.csv")
        mock_process.side_effect = Exception("Unexpected error")
        
        with pytest.raises(SystemExit) as exc_info:
            main()
        assert exc_info.value.code == 1
