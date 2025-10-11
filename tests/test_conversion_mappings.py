"""Tests for conversion_mappings module."""

import pytest

from cc_stmt_data_scrubber.conversion_mappings import (
    COMMON_DESC_CONVERSIONS,
    FAMILY_DESC_CONVERSIONS,
    PERSONAL_DESC_CONVERSIONS,
    get_desc_conversions,
)


class TestConversionMappingsData:
    """Tests for conversion mapping data structures."""

    def test_common_conversions_exist(self):
        """Test that common conversions are defined."""
        assert len(COMMON_DESC_CONVERSIONS) > 0
        assert "Barnes & Noble" in COMMON_DESC_CONVERSIONS

    def test_family_conversions_exist(self):
        """Test that family conversions are defined."""
        assert len(FAMILY_DESC_CONVERSIONS) > 0
        assert "Amazon Prime" in FAMILY_DESC_CONVERSIONS

    def test_personal_conversions_exist(self):
        """Test that personal conversions are defined."""
        assert len(PERSONAL_DESC_CONVERSIONS) > 0
        assert "Starbucks" in PERSONAL_DESC_CONVERSIONS

    def test_conversions_are_regex_patterns(self):
        """Test that conversion values are regex patterns."""
        assert COMMON_DESC_CONVERSIONS["Barnes & Noble"] == r"\bBARNES &amp; NOBLE\b"
        assert FAMILY_DESC_CONVERSIONS["Amazon Prime"] == r"\bAMAZON PRIME\b"


class TestGetDescConversions:
    """Tests for get_desc_conversions function."""

    def test_family_includes_common(self):
        """Test that family conversions include common conversions."""
        conversions = get_desc_conversions("family")
        assert "Barnes & Noble" in conversions
        assert "Amazon Prime" in conversions

    def test_personal_includes_common(self):
        """Test that personal conversions include common conversions."""
        conversions = get_desc_conversions("personal")
        assert "Barnes & Noble" in conversions
        assert "Starbucks" in conversions

    def test_family_excludes_personal(self):
        """Test that family conversions don't include personal-only items."""
        conversions = get_desc_conversions("family")
        assert "Starbucks" not in conversions

    def test_personal_excludes_family(self):
        """Test that personal conversions don't include family-only items."""
        conversions = get_desc_conversions("personal")
        assert "Amazon Prime" not in conversions

    def test_invalid_card_type(self):
        """Test that invalid card type raises ValueError."""
        with pytest.raises(ValueError, match="Unknown card type: invalid"):
            get_desc_conversions("invalid")

    def test_returns_copy(self):
        """Test that function returns a copy, not the original dict."""
        conversions1 = get_desc_conversions("family")
        conversions2 = get_desc_conversions("family")
        conversions1["TEST"] = "test"
        assert "TEST" not in conversions2
