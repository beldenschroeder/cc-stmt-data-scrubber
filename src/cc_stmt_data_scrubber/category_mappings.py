"""Category mappings for credit card transactions.

This module contains mappings from merchant descriptions to expense categories
for both family and personal credit card types.
"""

from typing import Dict

FAMILY_CATEGORY_MAPPINGS = {
    "1Password": "Family - Subscriptions",
    "11th Hour Coffee": "Family - Meals",
    "76": "Family - Vehicle Fuel",
    "Ace Hardware": "Family - Home Improvement",
    "Achadinha Cheese Comp.": "Family - Groceries",
    "Airbnb": "Family - Travel",
    "AllTrails.com": "Family - Subscriptions",
    "Alliance Gas": "Family - Vehicle Fuel",
    "Alta Bakery and Café": "Family - Meals",
    "Alto Pharmacy": "Family - Health",
    "Amazon": "",
    "Amazon Prime": "Family - Subscriptions",
    "Annie's Hot Dogs": "Family - Meals",
    "B40 Café": "Family - Meals",
    "Barista Underground": "Family - Groceries",
    "Barnes & Noble": "Family - Other Losses",
    "Baskin-Robbins": "Family - Meals",
    "Bedi Farms": "Family - Groceries",
    "Ben Tre": "Family - Meals",
    "Berkeley Bowl": "Family - Groceries",
    "Bi-Rite Market": "Family - Groceries",
    "Blue Bottle Coffee": "Family - Meals",
    "Bookworks": "",
    "Broadway Babies and Kids": "Family - Child Extracurricular",
    "Budget Rent-a-Car": "Family - Travel",
    "CA Academy of Sciences": "Family - Memberships",
    "California Bakeshop": "Family - Groceries",
    "Captain + Stoker": "Family - Meals",
    "ChargePoint": "Family - Vehicle Fuel",
    "Chevron": "Family - Vehicle Fuel",
    "Coffeebar": "Family - Meals",
    "Costco": "Family - Groceries",
    "Cotogna and Quince": "Family - Meals",
    "Coupa Café": "Family - Meals",
    "Credit card payment": "N/A",
    "Crystal Springs Produce": "Family - Groceries",
    "Diddams Party & Toy Store": "Family - Child Other",
    "Disney+ Premium": "Family - Subscriptions",
    "Doppio Zero": "Family - Meals",
    "Downtown Local": "Family - Meals",
    "Equator Coffees": "Family - Meals",
    "Flatbread Queen": "Family - Meals",
    "Footsteps@Cipriani": "Family - Child Schooling",
    "Gallardo's Organic Farm": "Family - Groceries",
    "Gas & electricity (PG&E)": "Family - Housing",
    "General Motors": "Family - Car Expenses",
    "Giftly": "Family - Gifts",
    "Google Fi": "Family - Mobile Wireless",
    "Granlibakken": "Family - Travel",
    "Greek Table": "Family - Groceries",
    "Groovy Goose": "Family - Meals",
    "H&R Block tax software": "Family - Other Losses",
    "Hal's Office": "Family - Meals",
    "Hidden Star Orchards": "Family - Groceries",
    "Highwire Coffee Roasters": "Family - Meals",
    "HMB Coffee": "Family - Meals",
    "Impark": "Family - Parking",
    "Impasto": "Family - Meals",
    "Instacart": "Family - Groceries",
    "Internet (Sonic)": "Family - Housing",
    "J&M Ibarra Farms": "Family - Groceries",
    "Kindle Services": "Family - Other Losses",
    "La Bicyclette": "Family - Meals",
    "La Burgueria": "Family - Meals",
    "La Lucha": "Family - Meals",
    "Lost Coffee": "Family - Meals",
    "Lucile Packard Children's Hospital": "Family - Health",
    "Luna's Farm": "Family - Groceries",
    "Lunardi's": "Family - Groceries",
    "Lyft": "Family - Travel",
    "Made out of Dough": "Family - Groceries",
    "Mademoiselle Colette": "Family - Meals",
    "Menchie's Frozen Yogurt": "Family - Meals",
    "Menlo Swim & Sport": "Family - Child Extracurricular",
    "Microsoft 365 Home": "Family - Subscriptions",
    "MisterSoftee": "Family - Meals",
    "Mollie Stone's": "Family - Groceries",
    "Neighbor's Corner": "Family - Meals",
    "Netflix": "Family - Subscriptions",
    "Noe Café": "Family - Meals",
    "Oral-B": "Family - Groceries",
    "Pizzaria Luba": "Family - Meals",
    "Putnam Chevrolet": "Family - Car Expenses",
    "Rally Gymnastics": "Family - Child Extracurricular",
    "Rebyl Coffee & Foods": "Family - Meals",
    "Redwood City Nissan": "Family - Car Expenses",
    "RHJ Organic": "Family - Groceries",
    "Ritual Coffee": "Family - Meals",
    "RJ Produce": "Family - Groceries",
    "Rodriguez Bros. Ranch": "Family - Groceries",
    "Royo Bread": "Family - Groceries",
    "Safeway": "Family - Groceries",
    "Santa Cruz City Parking": "Family - Parking",
    "SchoolForce": "Family - Child Schooling",
    "Shell": "Family - Vehicle Fuel",
    "SodaStream": "Family - Groceries",
    "Spectra Coffee": "Family - Meals",
    "SPRO Coffee Lab": "Family - Meals",
    "Stanford Health Care": "Family - Health",
    "Talons": "Family - Meals",
    "Temple Coffee": "Family - Meals",
    "The Frenchy Gourmet": "Family - Groceries",
    "The Home Depot": "Family - Home Improvement",
    "The Reading Bug": "Family - Child Other",
    "Ticino": "Family - Meals",
    "Trader Joe's": "Family - Groceries",
    "TuTu School": "Family - Child Extracurricular",
    "Water (Mid-Peninsula Water District)": "Family - Housing",
    "Webb Ranch": "Family - Groceries",
    "YouTube Premium": "Family - Subscriptions",
    "Vina Enoteca": "Family - Meals",
    "Viva la Tarte": "Family - Meals",
    "Waste (Recology)": "Family - Housing",
    "Whole Foods": "Family - Groceries",
    "ZombieRunner Coffee": "Family - Meals",
}

PERSONAL_CATEGORY_MAPPINGS = {
    "Amazon Web Services": "Other Losses",
    "Audible": "Subscriptions",
    "Barnes & Noble": "Meals",
    "Calvin Klein": "Clothes",
    "Fjällräven": "Clothes",
    "Fooda": "Meals",
    "J.Crew": "Clothes",
    "KCSM membership": "Subscriptions",
    "Kindle Services": "Other Losses",
    "KQED membership": "Subscriptions",
    "L.L. Bean": "Clothes",
    "Lunardi's": "Meals",
    "Noe Café": "Meals",
    "Patagonia": "Clothes",
    "Pink Owl Coffee": "Meals",
    "Starbucks": "Meals",
    "Strava Summit": "Subscriptions",
    "Tacx": "Subscriptions",
    "The New York Times": "Subscriptions",
    "WIRED Magazine": "Subscriptions",
}


# Registry for category mappings - open for extension, closed for modification
_CATEGORY_MAPPINGS_REGISTRY = {
    "family": FAMILY_CATEGORY_MAPPINGS,
    "personal": PERSONAL_CATEGORY_MAPPINGS,
}


def register_category_mappings(cc_type: str, mappings: Dict[str, str]) -> None:
    """Register category mappings for a new card type.

    This allows extending the system with new card types without modifying existing code.

    Args:
        cc_type: The credit card type identifier.
        mappings: Mapping from merchant descriptions to expense categories.
    """
    _CATEGORY_MAPPINGS_REGISTRY[cc_type] = mappings


def get_category_mappings(cc_type: str) -> Dict[str, str]:
    """Get category mappings for the given card type.

    Args:
        cc_type: The credit card type ('family' or 'personal').

    Returns:
        Mapping from merchant descriptions to expense categories.

    Raises:
        ValueError: If cc_type is not registered.
    """
    if cc_type not in _CATEGORY_MAPPINGS_REGISTRY:
        raise ValueError(
            f"Unknown card type: {cc_type}. "
            f"Available types: {', '.join(_CATEGORY_MAPPINGS_REGISTRY.keys())}"
        )
    return _CATEGORY_MAPPINGS_REGISTRY[cc_type]
