"""Tests for csv_config module."""

import pytest
from cc_stmt_data_scrubber.csv_config import (
    ColumnConfig,
    CARD_TYPE_CONFIGS,
    get_column_config,
)


class TestColumnConfig:
    """Tests for ColumnConfig dataclass."""

    def test_column_config_creation(self):
        """Test creating a ColumnConfig instance."""
        config = ColumnConfig(
            description_column=2,
            category_column=3,
            amount_column=5
        )
        assert config.description_column == 2
        assert config.category_column == 3
        assert config.amount_column == 5

    def test_column_config_optional_amount(self):
        """Test ColumnConfig with optional amount column."""
        config = ColumnConfig(
            description_column=3,
            category_column=4
        )
        assert config.description_column == 3
        assert config.category_column == 4
        assert config.amount_column is None


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
        """Test family configuration values."""
        config = CARD_TYPE_CONFIGS["family"]
        assert config.description_column == 2
        assert config.category_column == 3
        assert config.amount_column == 5

    def test_personal_config_values(self):
        """Test personal configuration values."""
        config = CARD_TYPE_CONFIGS["personal"]
        assert config.description_column == 3
        assert config.category_column == 4
        assert config.amount_column is None


class TestGetColumnConfig:
    """Tests for get_column_config function."""

    def test_get_family_config(self):
        """Test getting family column configuration."""
        config = get_column_config("family")
        assert config.description_column == 2
        assert config.category_column == 3
        assert config.amount_column == 5

    def test_get_personal_config(self):
        """Test getting personal column configuration."""
        config = get_column_config("personal")
        assert config.description_column == 3
        assert config.category_column == 4
        assert config.amount_column is None

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
