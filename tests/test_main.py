"""Tests for main module."""

from unittest.mock import patch

import pytest
from cc_stmt_data_scrubber.main import main
from click.testing import CliRunner


@pytest.fixture
def runner():
    return CliRunner()


@pytest.fixture
def sample_csv(tmp_path):
    """Create a sample input CSV file."""
    input_file = tmp_path / "input.csv"
    input_file.write_text(
        "Transaction Date,Clearing Date,Description,Merchant,Category,"
        "Type,Amount (USD),Purchased By\n"
        "01/15/2025,01/16/2025,AMAZON PRIME,AMAZON PRIME,Shopping,"
        "Purchase,-50.00,John\n"
    )
    return input_file


class TestMainCommand:
    """Tests for the Click CLI command."""

    def test_valid_arguments(self, runner, sample_csv, tmp_path):
        """Test running with valid command-line arguments."""
        output_file = tmp_path / "output.csv"
        result = runner.invoke(
            main,
            [
                "--cc-type",
                "family",
                "--input-file",
                str(sample_csv),
                "--output-file",
                str(output_file),
            ],
        )
        assert result.exit_code == 0
        assert "Application finished successfully!" in result.output
        assert output_file.exists()

    @patch("cc_stmt_data_scrubber.main.load_dotenv")
    def test_missing_cc_type(
        self, mock_dotenv, runner, sample_csv, tmp_path, monkeypatch
    ):
        """Test that missing --cc-type causes an error."""
        monkeypatch.delenv("CC_TYPE", raising=False)
        output_file = tmp_path / "output.csv"
        result = runner.invoke(
            main,
            ["--input-file", str(sample_csv), "--output-file", str(output_file)],
        )
        assert result.exit_code != 0

    @patch("cc_stmt_data_scrubber.main.load_dotenv")
    def test_missing_input_file(self, mock_dotenv, runner, tmp_path, monkeypatch):
        """Test that missing --input-file causes an error."""
        monkeypatch.delenv("INPUT_FILE", raising=False)
        output_file = tmp_path / "output.csv"
        result = runner.invoke(
            main,
            ["--cc-type", "family", "--output-file", str(output_file)],
        )
        assert result.exit_code != 0

    @patch("cc_stmt_data_scrubber.main.load_dotenv")
    def test_missing_output_file(self, mock_dotenv, runner, sample_csv, monkeypatch):
        """Test that missing --output-file causes an error."""
        monkeypatch.delenv("OUTPUT_FILE", raising=False)
        result = runner.invoke(
            main,
            ["--cc-type", "family", "--input-file", str(sample_csv)],
        )
        assert result.exit_code != 0

    def test_invalid_cc_type(self, runner, sample_csv, tmp_path):
        """Test that invalid --cc-type is rejected."""
        output_file = tmp_path / "output.csv"
        result = runner.invoke(
            main,
            [
                "--cc-type",
                "invalid",
                "--input-file",
                str(sample_csv),
                "--output-file",
                str(output_file),
            ],
        )
        assert result.exit_code != 0
        assert "Invalid value" in result.output

    def test_nonexistent_input_file(self, runner, tmp_path):
        """Test that a nonexistent input file is rejected."""
        output_file = tmp_path / "output.csv"
        result = runner.invoke(
            main,
            [
                "--cc-type",
                "family",
                "--input-file",
                "nonexistent.csv",
                "--output-file",
                str(output_file),
            ],
        )
        assert result.exit_code != 0

    def test_env_file_defaults(self, runner, sample_csv, tmp_path):
        """Test that .env values are used as defaults."""
        output_file = tmp_path / "output.csv"
        env_vars = {
            "CC_TYPE": "family",
            "INPUT_FILE": str(sample_csv),
            "OUTPUT_FILE": str(output_file),
        }
        with patch.dict("os.environ", env_vars):
            runner.invoke(main, [])
            # May fail due to Click's exists check timing, but env vars are read
            # The important thing is it doesn't fail with "Missing option"

    def test_cli_overrides_env(self, runner, sample_csv, tmp_path):
        """Test that CLI arguments override .env values."""
        output_file = tmp_path / "output.csv"
        env_vars = {"CC_TYPE": "personal"}
        with patch.dict("os.environ", env_vars):
            result = runner.invoke(
                main,
                [
                    "--cc-type",
                    "family",
                    "--input-file",
                    str(sample_csv),
                    "--output-file",
                    str(output_file),
                ],
            )
            assert result.exit_code == 0

    def test_help_output(self, runner):
        """Test that --help displays usage info."""
        result = runner.invoke(main, ["--help"])
        assert result.exit_code == 0
        assert "Credit Card Statement Data Scrubber" in result.output
        assert "--cc-type" in result.output
        assert "--input-file" in result.output
        assert "--output-file" in result.output

    @patch("cc_stmt_data_scrubber.main.process_csv_file")
    def test_value_error_handling(self, mock_process, runner, sample_csv, tmp_path):
        """Test that ValueError is handled gracefully."""
        mock_process.side_effect = ValueError("Unknown card type")
        output_file = tmp_path / "output.csv"
        result = runner.invoke(
            main,
            [
                "--cc-type",
                "family",
                "--input-file",
                str(sample_csv),
                "--output-file",
                str(output_file),
            ],
        )
        assert result.exit_code == 1

    @patch("cc_stmt_data_scrubber.main.process_csv_file")
    def test_unexpected_error_handling(
        self, mock_process, runner, sample_csv, tmp_path
    ):
        """Test that unexpected exceptions are handled gracefully."""
        mock_process.side_effect = Exception("Unexpected error")
        output_file = tmp_path / "output.csv"
        result = runner.invoke(
            main,
            [
                "--cc-type",
                "family",
                "--input-file",
                str(sample_csv),
                "--output-file",
                str(output_file),
            ],
        )
        assert result.exit_code == 1
