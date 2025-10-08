"""CSV column configuration for different credit card types.

This module defines which columns contain specific data for each card type.
"""

from dataclasses import dataclass


@dataclass
class ColumnConfig:
    """Configuration for CSV column indices."""
    
    description_column: int
    category_column: int
    amount_column: int | None = None


# Column configurations for each card type
CARD_TYPE_CONFIGS = {
    "family": ColumnConfig(
        description_column=2,
        category_column=3,
        amount_column=5
    ),
    "personal": ColumnConfig(
        description_column=3,
        category_column=4,
        amount_column=None
    ),
}


def get_column_config(card_type):
    """Get column configuration for the given card type.
    
    Args:
        card_type: The credit card type ('family' or 'personal').
        
    Returns:
        ColumnConfig object with column indices.
        
    Raises:
        ValueError: If card_type is not recognized.
    """
    if card_type not in CARD_TYPE_CONFIGS:
        raise ValueError(f"Unknown card type: {card_type}. Must be 'family' or 'personal'.")
    
    return CARD_TYPE_CONFIGS[card_type]
