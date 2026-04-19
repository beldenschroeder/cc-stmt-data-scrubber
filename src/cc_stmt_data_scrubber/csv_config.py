"""CSV column configuration for different credit card types.

This module defines which columns contain specific data for each card type.
"""

from dataclasses import dataclass


@dataclass
class ColumnConfig:
    """Configuration for CSV column indices.

    Input columns: Transaction Date, Clearing Date, Description, Merchant,
    Category, Type, Amount (USD), Purchased By
    """

    clearing_date_column: int
    description_column: int
    merchant_column: int
    category_column: int
    amount_column: int


OUTPUT_HEADER = [
    "Date",
    "Description",
    "Amount",
    "Statement Ending",
    "Month Ending",
    "Item Total",
    "Debit",
    "Credit",
]


# Column configurations for each card type
CARD_TYPE_CONFIGS = {
    "family": ColumnConfig(
        clearing_date_column=1,
        description_column=2,
        merchant_column=3,
        category_column=4,
        amount_column=6,
    ),
    "personal": ColumnConfig(
        clearing_date_column=1,
        description_column=2,
        merchant_column=3,
        category_column=4,
        amount_column=6,
    ),
}


def get_column_config(card_type: str) -> ColumnConfig:
    """Get column configuration for the given card type.

    Args:
        card_type: The credit card type ('family' or 'personal').

    Returns:
        Column configuration with column indices.

    Raises:
        ValueError: If card_type is not recognized.
    """
    if card_type not in CARD_TYPE_CONFIGS:
        raise ValueError(
            f"Unknown card type: {card_type}. Must be 'family' or 'personal'."
        )

    return CARD_TYPE_CONFIGS[card_type]
