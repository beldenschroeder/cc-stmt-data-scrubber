"""Tests for category_mappings module."""

import pytest

from cc_stmt_data_scrubber.category_mappings import (
    FAMILY_CATEGORY_MAPPINGS,
    PERSONAL_CATEGORY_MAPPINGS,
    get_category_mappings,
)


class TestCategoryMappingsData:
    """Tests for category mapping data structures."""

    def test_family_mappings_exist(self):
        """Test that family category mappings are defined."""
        assert len(FAMILY_CATEGORY_MAPPINGS) > 0
        assert "Amazon Prime" in FAMILY_CATEGORY_MAPPINGS

    def test_personal_mappings_exist(self):
        """Test that personal category mappings are defined."""
        assert len(PERSONAL_CATEGORY_MAPPINGS) > 0
        assert "Starbucks" in PERSONAL_CATEGORY_MAPPINGS

    def test_family_category_format(self):
        """Test that family categories have correct format."""
        assert FAMILY_CATEGORY_MAPPINGS["Amazon Prime"] == "Family - Subscriptions"
        assert FAMILY_CATEGORY_MAPPINGS["Costco"] == "Family - Groceries"

    def test_personal_category_format(self):
        """Test that personal categories have correct format."""
        assert PERSONAL_CATEGORY_MAPPINGS["Starbucks"] == "Meals"
        assert PERSONAL_CATEGORY_MAPPINGS["Audible"] == "Subscriptions"


class TestGetCategoryMappings:
    """Tests for get_category_mappings function."""

    def test_family_mappings(self):
        """Test getting family category mappings."""
        mappings = get_category_mappings("family")
        assert mappings == FAMILY_CATEGORY_MAPPINGS
        assert "Amazon Prime" in mappings

    def test_personal_mappings(self):
        """Test getting personal category mappings."""
        mappings = get_category_mappings("personal")
        assert mappings == PERSONAL_CATEGORY_MAPPINGS
        assert "Starbucks" in mappings

    def test_family_excludes_personal(self):
        """Test that family mappings don't include personal-only items."""
        mappings = get_category_mappings("family")
        assert "Starbucks" not in mappings

    def test_personal_excludes_family(self):
        """Test that personal mappings don't include family-only items."""
        mappings = get_category_mappings("personal")
        assert "Amazon Prime" not in mappings

    def test_invalid_card_type(self):
        """Test that invalid card type raises ValueError."""
        with pytest.raises(ValueError, match="Unknown card type: invalid"):
            get_category_mappings("invalid")

    def test_returns_reference(self):
        """Test that function returns reference to original dict."""
        mappings = get_category_mappings("family")
        assert mappings is FAMILY_CATEGORY_MAPPINGS
