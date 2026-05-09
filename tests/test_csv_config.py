"""Tests for csv_config module."""

import pytest
from cc_stmt_data_scrubber.csv_config import (
    CARD_TYPE_CONFIGS,
    OUTPUT_HEADER,
    ColumnConfig,
    get_column_config,
)


class TestColumnConfig:
    """Tests for ColumnConfig dataclass."""

    def test_column_config_creation(self):
        """Test creating a ColumnConfig instance."""
        config = ColumnConfig(
            clearing_date_column=1,
            merchant_column=3,
            amount_column=6,
        )
        assert config.clearing_date_column == 1
        assert config.merchant_column == 3
        assert config.amount_column == 6


class TestOutputHeader:
    """Tests for OUTPUT_HEADER."""

    def test_output_header_columns(self):
        """Test that output header has the correct columns."""
        assert OUTPUT_HEADER == [
            "Date",
            "Description",
            "Account",
            "Statement Ending",
            "Month Ending",
            "Item Total",
            "Debit",
            "Credit",
        ]


class TestCardTypeConfigs:
    """Tests for CARD_TYPE_CONFIGS data."""

    def test_family_config_exists(self):
        """Test that family configuration exists."""
        assert "family" in CARD_TYPE_CONFIGS
        config = CARD_TYPE_CONFIGS["family"]
        assert isinstance(config, ColumnConfig)

    def test_personal_config_exists(self):
        """Test that personal configuration exists."""
        assert "personal" in CARD_TYPE_CONFIGS
        config = CARD_TYPE_CONFIGS["personal"]
        assert isinstance(config, ColumnConfig)

    def test_family_config_values(self):
        """Test family (JPMorgan Chase) configuration values."""
        config = CARD_TYPE_CONFIGS["family"]
        assert config.clearing_date_column == 1
        assert config.merchant_column == 2
        assert config.amount_column == 5

    def test_personal_config_values(self):
        """Test personal (Apple Card) configuration values."""
        config = CARD_TYPE_CONFIGS["personal"]
        assert config.clearing_date_column == 1
        assert config.merchant_column == 3
        assert config.amount_column == 6


class TestGetColumnConfig:
    """Tests for get_column_config function."""

    def test_get_family_config(self):
        """Test getting family (JPMorgan Chase) column configuration."""
        config = get_column_config("family")
        assert config.clearing_date_column == 1
        assert config.merchant_column == 2
        assert config.amount_column == 5

    def test_get_personal_config(self):
        """Test getting personal (Apple Card) column configuration."""
        config = get_column_config("personal")
        assert config.clearing_date_column == 1
        assert config.merchant_column == 3
        assert config.amount_column == 6

    def test_invalid_card_type_raises_error(self):
        """Test that invalid card type raises ValueError."""
        with pytest.raises(ValueError) as exc_info:
            get_column_config("invalid")
        assert "Unknown card type: invalid" in str(exc_info.value)
        assert "Must be 'family' or 'personal'" in str(exc_info.value)

    def test_returns_same_instance(self):
        """Test that function returns the same config instance."""
        config1 = get_column_config("family")
        config2 = get_column_config("family")
        assert config1 is config2
