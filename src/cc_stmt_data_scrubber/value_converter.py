"""Module converting values in a CSV file to a correct value."""

import re


def convert_value_with_regex(regex, value, new_value):
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


def convert_desc_value(cc_type, description):
    """
    Converts a description value to its proper value.

    Args:
      cc_type: The credit card type.
      description: The description value to convert.

    Returns:
      The description value converted to its proper value.
    """

    conversions_with_regex = {}

    if cc_type == "family":
        conversions_with_regex = {
            "11th Hour Coffee": r"\b11TH HOUR COFFEE\b",
            "1Password": r"\b1PASSWORD\b",
            "76": r"\b76\b",
            "Ace Hardware": r"\bACE HARDWARE\b",
            "Airbnb": r"\bAIRBNB\b",
            "AllTrails.com": r"\bALLTRAILS\b",
            "Alliance Gas": r"\bALLIANCE GAS\b",
            "Alta Bakery and Café": r"\bALTA BAKERY\b",
            "Alto Pharmacy": r"\bALTO PHARMACY\b",
            "Amazon": r"\bAMAZON\b(?!.*PRIME\b)|\bAMZN\b",
            "Amazon Prime": r"\bAMAZON PRIME\b",
            "Annie's Hot Dogs": r"\bANNIE'S HOT DOGS\b",
            "B40 Café": r"\bB40 CAFE\b",
            "Barista Underground": r"\bBARISTA UNDERGROU\b",
            "Barnes & Noble": r"\bBARNES &amp; NOBLE\b",
            "Baskin-Robbins": r"\bBASKIN\b",
            "Bedi Farms": r"\bBEDI FARMS\b",
            "Ben Tre": r"\bBEN TRE\b",
            "Berkeley Bowl": r"\bBERKELEY BOWL\b",
            "Bi-Rite Market": r"\bBI-RITE MARKET\b",
            "Blue Bottle Coffee": r"\bBLUE BOTTLE\b",
            "Bookworks": r"\bBOOKWORKS\b",
            "Broadway Babies and Kids": r"\bBroadwayBabiesandKids\b",
            "Budget Rent-a-Car": r"\bBUDGET RENT A CAR\b",
            "CA Academy of Sciences": r"\bCA ACAD. OF SCIENCES\b",
            "Captain + Stoker": r"\bCAPTAIN + STOKER\b",
            "ChargePoint": r"\bCHARGEPOINT\b",
            "Chevron": r"\bCHEVRON\b",
            "Coffeebar": r"\bCOFFEEBAR\b",
            "Costco": r"\bCOSTCO\b",
            "Coupa Café": r"\bCOUPA CAFE\b",
            "Credit card payment": r"\bPayment Thank You - Web\b",
            "Crystal Springs Produce": r"\bCRYSTAL SPRINGS PRODUCE\b",
            "Disney+ Premium": r"\bDisney Plus\b",
            "Doppio Zero": r"\bDOPPIO ZERO\b",
            "Flatbread Queen": r"\bFLATBREAD QUEEN\b",
            "Footsteps@Cipriani": r"\bFOOTSTEPS\b",
            "Gas & electricity (PG&E)": r"\bPG&amp;E\b",
            "General Motors": r"\bGENERAL MOTORS\b",
            "Giftly": r"\bGIFTLY.COM\b",
            "Google Fi": r"\bGOOGLE *FI\b",
            "Granlibakken": r"\bGRANLIBAKKEN\b",
            "Groovy Goose": r"\bGROOVY GOOSE\b",
            "FasTrak": r"\bFASTRAK\b",
            "H&R Block tax software": r"\bH&amp;R BLOCK SOFTWARE\b",
            "Hal's Office": r"\bHAL'S OFFICE\b",
            "Highwire Coffee Roasters": r"\bHIGHWIRE COFFEE ROAST\b",
            "HMB Coffee": r"\bHMB COFFEE\b",
            "Impark": r"\bIMPARK\b",
            "Impasto": r"\bIMPASTO\b",
            "Instacart": r"\bINSTACART\b",
            "Internet (Sonic)": r"\bSONIC\b",
            "Kindle Services": r"\bKindle Svcs\b",
            "La Bicyclette": r"\bLA BICYCLETTE\b",
            "La Boulangerie": r"\bLA BOULANGERIE\b",
            "La Lucha": r"\bLA LUCHA\b",
            "Lost Coffee": r"\bLOST COFFEE\b",
            "Lucile Packard Children's Hospital": r"\bLUCILE PACKARD CHILDRENS\b",
            "Lunardi's": r"\bLUNARDI'S\b",
            "Lyft": r"\bLYFT\b",
            "Made out of Dough": r"\bMADE OUT OF DOUGH\b",
            "Mademoiselle Colette": r"\bMADEMOISELLE COLETTE\b",
            "Menchie's Frozen Yogurt": r"\bMENCHIES\b",
            "Microsoft 365 Home": r"\bMicrosoft 365\b",
            "Mollie Stone's": r"\bMOLLIE STONES\b",
            "Neighbor's Corner": r"\bNEIGHBOR'S CORNER\b",
            "Netflix": r"\bNETFLIX.COM\b",
            "Oral-B": r"\bORAL B\b",
            "Pizzaria Luba": r"\bPIZZERIA LUBA\b",
            "Putnam Chevrolet": r"\bPUTNAM CHEVROLET\b",
            "Rally Gymnastics": r"\bRally Gymnastics\b",
            "Rebyl Coffee & Foods": r"\bREBYL\b",
            "Redwood City Nissan": r"\bREDWOOD CITY INFINITI\b",
            "Ritual Coffee": r"\bRITUAL COFFEE\b",
            "REI": r"\bREI.COM\b",
            "Royo Bread": r"\bROYO BREAD\b",
            "Safeway": r"\bSAFEWAY\b",
            "Santa Cruz City Parking": r"\bSANTA CRUZ CITY PARKING\b",
            "SchoolForce": r"\bSCHOOLFORCE\b",
            "Shell": r"\bSHELL\b",
            "Spectra Coffee": r"\bSPECTRA COFFEE\b",
            "SPRO Coffee Lab": r"\bSPRO\b",
            "Stanford Health Care": r"\bSTANFORD HEALTH CARE\b",
            "Talons": r"\bTALONS\b",
            "Temple Coffee": r"\bTEMPLE COFFEE\b",
            "The Home Depot": r"\bHOME DEPOT\b",
            "The Reading Bug": r"\bTHE READING BUG\b",
            "Ticino": r"\bTICINO\b",
            "Trader Joe's": r"\bTRADER JOE S\b",
            "TuTu School": r"\bTUTU SCHOOL\b",
            "Vina Enoteca": r"\bVINA ENOTECA\b",
            "Viva la Tarte": r"\bVIVE LA TARTE\b",
            "Waste (Recology)": r"\bRECOLOGY\b",
            "Water (Mid-Peninsula Water District)": r"\bMID-PENINSULA WATER\b",
            "YouTube Premium": r"\bYouTubePremium\b",
            "Whole Foods": r"\bWHOLE FOODS|WHOLEFDS\b",
            "ZombieRunner Coffee": r"\bZOMBIERUNNER\b"
        }

    elif cc_type == "personal":
        conversions_with_regex = {
            "Amazon Web Services": r"\bAMAZON WEB SERVICES\b",
            "Audible": r"\bAUDIBLE\b",
            "Barnes & Noble": r"\bBARNES &amp; NOBLE\b",
            "Calvin Klein": r"\bCalvin Klein\b",
            "Fjällräven": r"\bFJALLRAVEN\b",
            "Fooda": r"\bFOODA\b",
            "J.Crew": r"\bJ Crew\b",
            "KCSM membership": r"\bKcsm Jazz 91\b",
            "Kindle Services": r"\bKindle Svcs\b",
            "KQED membership": r"\bKQED\b",
            "L.L. Bean": r"\bLlbean\b",
            "Lunardi's": r"\bLUNARDI'S\b",
            "Patagonia": r"\bPATAGONIA\b",
            "Pink Owl Coffee": r"\bPINK OWL COFFEE\b",
            "Starbucks": r"\bSTARBUCKS\b",
            "Strava Summit": r"\bSTRAVA\b",
            "Tacx": r"\bGARMIN\b",
            "The Atlantic": r"\bThe Atlantic\b",
            "The New York Times": r"\bNYTIMES\b",
        }

    converted_result = description

    for conv_to, conv_tokens in conversions_with_regex.items():
        converted_value = convert_value_with_regex(conv_tokens, description, conv_to)
        if converted_value != description:
            converted_result = converted_value
            break
    return converted_result


def map_desc_to_category(cc_type, description):
    """
    Maps a description value to a category value.

    Args:
      cc_type: The credit card type.
      description: The description value to map to a category.

    Returns:
      The category value mapped from the description value.
    """

    desc_to_category_mapper = {}

    if cc_type == "family":
        desc_to_category_mapper = {
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
            "ZombieRunner Coffee": "Family - Meals"
        }
    elif cc_type == "personal":
        desc_to_category_mapper = {
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
        }
    category_result = ""

    for desc, category in desc_to_category_mapper.items():
        if desc == description:
            category_result = category
            break

    return category_result


def convert_amount_value(amount):
    """
    Converts an amount value to its proper value.

    Args:
      amount: The amount value to convert.

    Returns:
      The amount value converted to its proper value.
    """
    return -float(amount)
