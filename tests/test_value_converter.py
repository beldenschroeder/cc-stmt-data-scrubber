"""Tests for value_converter module."""

import pytest

from cc_stmt_data_scrubber.value_converter import (
    convert_amount_value,
    convert_desc_value,
    convert_value_with_regex,
    map_desc_to_category,
)


class TestConvertValueWithRegex:
    """Tests for convert_value_with_regex function."""

    def test_match_found(self):
        """Test conversion when regex matches."""
        result = convert_value_with_regex(r"\bAMAZON\b", "AMAZON PRIME", "Amazon")
        assert result == "Amazon"

    def test_no_match(self):
        """Test no conversion when regex doesn't match."""
        result = convert_value_with_regex(r"\bAMAZON\b", "COSTCO", "Amazon")
        assert result == "COSTCO"

    def test_case_insensitive(self):
        """Test that matching is case insensitive."""
        result = convert_value_with_regex(r"\bstarbucks\b", "STARBUCKS", "Starbucks")
        assert result == "Starbucks"

    def test_word_boundary(self):
        """Test word boundary matching."""
        result = convert_value_with_regex(r"\bNETFLIX\b", "NETFLIX.COM", "Netflix")
        assert result == "Netflix"


class TestConvertDescValue:
    """Tests for convert_desc_value function."""

    def test_family_conversion(self):
        """Test family card type conversion."""
        result = convert_desc_value("family", "AMAZON PRIME")
        assert result == "Amazon Prime"

    def test_personal_conversion(self):
        """Test personal card type conversion."""
        result = convert_desc_value("personal", "STARBUCKS")
        assert result == "Starbucks"

    def test_common_conversion_family(self):
        """Test common conversion for family card."""
        result = convert_desc_value("family", "BARNES &amp; NOBLE")
        assert result == "Barnes & Noble"

    def test_common_conversion_personal(self):
        """Test common conversion for personal card."""
        result = convert_desc_value("personal", "BARNES &amp; NOBLE")
        assert result == "Barnes & Noble"

    def test_no_conversion(self):
        """Test when no conversion pattern matches."""
        result = convert_desc_value("family", "UNKNOWN MERCHANT")
        assert result == "UNKNOWN MERCHANT"

    def test_invalid_card_type(self):
        """Test with invalid card type raises ValueError."""
        with pytest.raises(ValueError, match="Unknown card type: invalid"):
            convert_desc_value("invalid", "STARBUCKS")


class TestMapDescToCategory:
    """Tests for map_desc_to_category function."""

    def test_family_category_mapping(self):
        """Test category mapping for family card."""
        result = map_desc_to_category("family", "Amazon Prime")
        assert result == "Family - Subscriptions"

    def test_personal_category_mapping(self):
        """Test category mapping for personal card."""
        result = map_desc_to_category("personal", "Starbucks")
        assert result == "Meals"

    def test_empty_category(self):
        """Test mapping that returns empty category."""
        result = map_desc_to_category("family", "Amazon")
        assert result == ""

    def test_unknown_description(self):
        """Test unknown description returns empty string."""
        result = map_desc_to_category("family", "Unknown Merchant")
        assert result == ""

    def test_invalid_card_type(self):
        """Test invalid card type raises ValueError."""
        with pytest.raises(ValueError, match="Unknown card type: invalid"):
            map_desc_to_category("invalid", "Starbucks")


class TestConvertAmountValue:
    """Tests for convert_amount_value function."""

    def test_positive_to_negative(self):
        """Test converting positive amount to negative."""
        result = convert_amount_value("100.50")
        assert result == -100.50

    def test_negative_to_positive(self):
        """Test converting negative amount to positive."""
        result = convert_amount_value("-50.25")
        assert result == 50.25

    def test_zero(self):
        """Test converting zero."""
        result = convert_amount_value("0")
        assert result == 0.0

    def test_integer_string(self):
        """Test converting integer string."""
        result = convert_amount_value("100")
        assert result == -100.0

    def test_float_conversion(self):
        """Test that result is a float."""
        result = convert_amount_value("10")
        assert isinstance(result, float)
