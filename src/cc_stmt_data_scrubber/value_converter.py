"""Module converting values in a CSV file to a correct value."""

import re
from typing import Dict

from .conversion_mappings import get_desc_conversions
from .category_mappings import get_category_mappings


def convert_value_with_regex(regex: str, value: str, new_value: str) -> str:
    """Convert a value to its proper value using regex matching.

    Args:
        regex: The regex pattern used to match the value.
        value: The value to convert.
        new_value: The value to convert to if regex matches.

    Returns:
        The converted value if regex matches, otherwise the original value.
    """
    result_value = value

    if re.search(regex, value, re.I):
        result_value = new_value

    return result_value


def convert_desc_value(cc_type: str, description: str) -> str:
    """Convert a description value to its proper normalized form.

    Args:
        cc_type: The credit card type ('family' or 'personal').
        description: The raw description value to convert.

    Returns:
        The normalized description value.
    """
    conversions = get_desc_conversions(cc_type)
    
    for clean_desc, regex_pattern in conversions.items():
        converted_value = convert_value_with_regex(regex_pattern, description, clean_desc)
        if converted_value != description:
            return converted_value
    
    return description


def map_desc_to_category(cc_type: str, description: str) -> str:
    """Map a description value to its corresponding category.

    Args:
        cc_type: The credit card type ('family' or 'personal').
        description: The description value to map.

    Returns:
        The category value, or empty string if no mapping exists.
    """
    category_mappings = get_category_mappings(cc_type)
    return category_mappings.get(description, "")


def convert_amount_value(amount: str) -> float:
    """Convert an amount string to a negative float.

    Args:
        amount: The amount value as a string.

    Returns:
        The amount as a negative float value.
    """
    return -float(amount)
