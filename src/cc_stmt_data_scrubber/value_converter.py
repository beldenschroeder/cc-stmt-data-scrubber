"""Module converting values in a CSV file to a correct value."""

import re
from typing import Dict

from .conversion_mappings import get_desc_conversions
from .category_mappings import get_category_mappings


def convert_value_with_regex(regex: str, value: str, new_value: str) -> str:
    """
    Converts a value to its proper value.

    Args:
      regex: The regex used to convert the value if there is a match.
      value: The value to convert.
      new_value: The value to convert to.

    Returns:
      The value converted to its proper value if there is a match with the
      regex, otherwise return the original value.
    """
    result_value = value

    if re.search(regex, value, re.I):
        result_value = new_value

    return result_value


def convert_desc_value(cc_type: str, description: str) -> str:
    """
    Converts a description value to its proper value.

    Args:
      cc_type: The credit card type.
      description: The description value to convert.

    Returns:
      The description value converted to its proper value.
    """
    conversions = get_desc_conversions(cc_type)
    
    for clean_desc, regex_pattern in conversions.items():
        converted_value = convert_value_with_regex(regex_pattern, description, clean_desc)
        if converted_value != description:
            return converted_value
    
    return description


def map_desc_to_category(cc_type: str, description: str) -> str:
    """
    Maps a description value to a category value.

    Args:
      cc_type: The credit card type.
      description: The description value to map to a category.

    Returns:
      The category value mapped from the description value.
    """
    category_mappings = get_category_mappings(cc_type)
    return category_mappings.get(description, "")


def convert_amount_value(amount: str) -> float:
    """
    Converts an amount value to its proper value.

    Args:
      amount: The amount value to convert.

    Returns:
      The amount value converted to its proper value.
    """
    return -float(amount)
