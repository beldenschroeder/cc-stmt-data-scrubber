"""CSV column configuration for different credit card types.

This module defines which columns contain specific data for each card type.

Family card (JPMorgan Chase) columns:
    Transaction Date, Post Date, Description, Category, Type, Amount, Memo

Personal card (Apple Card) columns:
    Transaction Date, Clearing Date, Description, Merchant,
    Category, Type, Amount (USD), Purchased By
"""

from dataclasses import dataclass


@dataclass
class ColumnConfig:
    """Configuration for CSV column indices."""

    clearing_date_column: int
    merchant_column: int
    amount_column: int


OUTPUT_HEADER = [
    "Date",
    "Description",
    "Account",
    "Statement Ending",
    "Month Ending",
    "Item Total",
    "Debit",
    "Credit",
]


# Column configurations for each card type
CARD_TYPE_CONFIGS = {
    # JPMorgan Chase: Transaction Date(0), Post Date(1), Description(2),
    #                 Category(3), Type(4), Amount(5), Memo(6)
    "family": ColumnConfig(
        clearing_date_column=1,
        merchant_column=2,
        amount_column=5,
    ),
    # Apple Card: Transaction Date(0), Clearing Date(1), Description(2),
    #             Merchant(3), Category(4), Type(5), Amount (USD)(6), Purchased By(7)
    "personal": ColumnConfig(
        clearing_date_column=1,
        merchant_column=3,
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
