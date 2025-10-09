"""Category mappings for credit card transactions.

This module contains mappings from merchant descriptions to expense categories
for both family and personal credit card types.
"""

FAMILY_CATEGORY_MAPPINGS = {
    "1Password": "Family - Subscriptions",
    "11th Hour Coffee": "Family - Meals",
    "76": "Family - Vehicle Fuel",
    "Ace Hardware": "Family - Home Improvement",
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
    "Captain + Stoker": "Family - Meals",
    "ChargePoint": "Family - Vehicle Fuel",
    "Chevron": "Family - Vehicle Fuel",
    "Coffeebar": "Family - Meals",
    "Costco": "Family - Groceries",
    "Coupa Café": "Family - Meals",
    "Credit card payment": "N/A",
    "Crystal Springs Produce": "Family - Groceries",
    "Disney+ Premium": "Family - Subscriptions",
    "Doppio Zero": "Family - Meals",
    "FasTrak": "Family - Tolls",
    "Flatbread Queen": "Family - Meals",
    "Footsteps@Cipriani": "Family - Child Schooling",
    "Gas & electricity (PG&E)": "Family - Housing",
    "General Motors": "Family - Car Expenses",
    "Giftly": "Family - Gifts",
    "Google Fi": "Family - Mobile Wireless",
    "Granlibakken": "Family - Travel",
    "Groovy Goose": "Family - Meals",
    "H&R Block tax software": "Family - Other Losses",
    "Hal's Office": "Family - Meals",
    "Highwire Coffee Roasters": "Family - Meals",
    "HMB Coffee": "Family - Meals",
    "Impark": "Family - Parking",
    "Impasto": "Family - Meals",
    "Instacart": "Family - Groceries",
    "Internet (Sonic)": "Family - Housing",
    "Kindle Services": "Family - Other Losses",
    "La Bicyclette": "Family - Meals",
    "La Burgueria": "Family - Meals",
    "La Lucha": "Family - Meals",
    "Lost Coffee": "Family - Meals",
    "Lucile Packard Children's Hospital": "Family - Health",
    "Lunardi's": "Family - Groceries",
    "Lyft": "Family - Travel",
    "Made out of Dough": "Family - Groceries",
    "Mademoiselle Colette": "Family - Meals",
    "Menchie's Frozen Yogurt": "Family - Meals",
    "Microsoft 365 Home": "Family - Subscriptions",
    "Mollie Stone's": "Family - Groceries",
    "Neighbor's Corner": "Family - Meals",
    "Netflix": "Family - Subscriptions",
    "Oral-B": "Family - Groceries",
    "Pizzaria Luba": "Family - Meals",
    "Putnam Chevrolet": "Family - Car Expenses",
    "Rally Gymnastics": "Family - Child Extracurricular",
    "Rebyl Coffee & Foods": "Family - Meals",
    "Redwood City Nissan": "Family - Car Expenses",
    "Ritual Coffee": "Family - Meals",
    "Royo Bread": "Family - Groceries",
    "Safeway": "Family - Groceries",
    "Santa Cruz City Parking": "Family - Parking",
    "SchoolForce": "Family - Child Schooling",
    "Shell": "Family - Vehicle Fuel",
    "Spectra Coffee": "Family - Meals",
    "SPRO Coffee Lab": "Family - Meals",
    "Stanford Health Care": "Family - Health",
    "Talons": "Family - Meals",
    "Temple Coffee": "Family - Meals",
    "The Home Depot": "Family - Home Improvement",
    "The Reading Bug": "Family - Child Other",
    "Ticino": "Family - Meals",
    "Trader Joe's": "Family - Groceries",
    "TuTu School": "Family - Child Extracurricular",
    "Water (Mid-Peninsula Water District)": "Family - Housing",
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
    "Patagonia": "Clothes",
    "Pink Owl Coffee": "Meals",
    "Starbucks": "Meals",
    "Strava Summit": "Subscriptions",
    "Tacx": "Subscriptions",
    "The New York Times": "Subscriptions",
    "WIRED Magazine": "Subscriptions",
}


def get_category_mappings(cc_type):
    """Get category mappings for the given cc_type.
    
    Args:
        cc_type: The credit card type ('family' or 'personal').
        
    Returns:
        Dictionary mapping descriptions to categories.
    """
    if cc_type == "family":
        return FAMILY_CATEGORY_MAPPINGS
    elif cc_type == "personal":
        return PERSONAL_CATEGORY_MAPPINGS
    else:
        return {}
