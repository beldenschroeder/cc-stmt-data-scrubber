"""Description conversion mappings for credit card transactions.

This module contains regex patterns used to normalize merchant names
from credit card statements into clean, consistent descriptions.
"""

from typing import Dict

# Common conversions shared by both personal and family
COMMON_DESC_CONVERSIONS = {
    "Barnes & Noble": r"\bBARNES &amp; NOBLE\b",
    "Kindle Services": r"\bKindle Svcs\b",
    "Lunardi's": r"\bLUNARDI'S\b",
    "Noe Café": r"NOE CAFE\b",
    "Starbucks": r"\bSTARBUCKS\b",
}

FAMILY_DESC_CONVERSIONS = {
    "11th Hour Coffee": r"\b11TH HOUR COFFEE\b",
    "1Password": r"\b1PASSWORD\b",
    "76": r"\b76\b",
    "Ace Hardware": r"\bACE HARDWARE\b",
    "Achadinha Cheese Comp.": r"\bACHADINHA CHEESE COMP\b",
    "Airbnb": r"\bAIRBNB\b",
    "AllTrails.com": r"\bALLTRAILS\b",
    "Alliance Gas": r"\bALLIANCE GAS\b",
    "Alta Bakery and Café": r"\bALTA BAKERY\b",
    "Alto Pharmacy": r"\bALTO PHARMACY\b",
    "Amazon": r"\bAMAZON\b(?!.*PRIME\b)|\bAMZN\b",
    "Amazon Prime": r"\bAMAZON PRIME\b",
    "Andytown Coffee Roasters": r"\bANDYTOWN COFFEE\b",
    "Annie's Hot Dogs": r"\bANNIE'S HOT DOGS\b",
    "B40 Café": r"\bB40 CAFE\b",
    "Barista Underground": r"\bBARISTA UNDERGROU\b",
    "Baskin-Robbins": r"\bBASKIN\b",
    "Bedi Farms": r"\bBEDI FARMS\b",
    "Ben Tre": r"\bBEN TRE\b",
    "Berkeley Bowl": r"\bBERKELEY BOWL\b",
    "Bi-Rite Market": r"\bBI-RITE MARKET\b",
    "Bloomsgiving": r"BLOOMSGIVING\b",
    "Blue Bottle Coffee": r"\bBLUE BOTTLE\b",
    "Bookworks": r"\bBOOKWORKS\b",
    "Broadway Babies and Kids": r"\bBroadwayBabiesandKids\b",
    "Budget Rent-a-Car": r"\bBUDGET RENT A CAR\b",
    "CA Academy of Sciences": r"\bCA ACAD. OF SCIENCES\b",
    "California Bakeshop": r"\bCALIFORNIA BAKESHOP\b",
    "Captain + Stoker": r"\bCAPTAIN + STOKER\b",
    "ChargePoint": r"\bCHARGEPOINT\b",
    "Chevron": r"\bCHEVRON\b",
    "Coffeebar": r"\bCOFFEEBAR\b",
    "Costco": r"\bCOSTCO\b",
    "Cotogna and Quince": r"\bCOTOGNA AND QUINCE\b",
    "Coupa Café": r"\bCOUPA CAFE\b",
    "Credit card payment": r"\bPayment Thank You - Web\b",
    "Crystal Springs Produce": r"\bCRYSTAL SPRINGS PRODUCE\b",
    "Diddams Party & Toy Store": r"\bDIDDAMS PARTY\b",
    "Disney+ Premium": r"\bDisney Plus\b",
    "Doppio Zero": r"\bDOPPIO ZERO\b",
    "Downtown Local": r"DOWNTOWN LOCAL\b",
    "Equator Coffees": r"\bEQUATOR COFFEES\b",
    "Flatbread Queen": r"\bFLATBREAD QUEEN\b",
    "Footsteps@Cipriani": r"\bFOOTSTEPS\b",
    "Gallardo's Organic Farm": r"\bGALLARDOS ORGANIC FAR\b",
    "Gas & electricity (PG&E)": r"\bPG&amp;E\b",
    "General Motors": r"\bGENERAL MOTORS\b",
    "Giftly": r"\bGIFTLY.COM\b",
    "Google Fi": r"\bGOOGLE \*FI\b",
    "Granlibakken": r"\bGRANLIBAKKEN\b",
    "Greek Table": r"\bGREEK TABLE\b",
    "Groovy Goose": r"\bGROOVY GOOSE\b",
    "FasTrak": r"\bFASTRAK\b",
    "H&R Block tax software": r"\bH&amp;R BLOCK SOFTWARE\b",
    "Hidden Star Orchards": r"\bHIDDEN STAR ORCHARDS\b",
    "Hal's Office": r"\bHAL'S OFFICE\b",
    "Highwire Coffee Roasters": r"\bHIGHWIRE COFFEE ROAST\b",
    "HMB Coffee": r"\bHMB COFFEE\b",
    "Impark": r"\bIMPARK\b",
    "Impasto": r"\bIMPASTO\b",
    "Instacart": r"\bINSTACART\b",
    "Internet (Sonic)": r"\bSONIC\b",
    "J&M Ibarra Farms": r"\bJ&amp;M IBARRA FARM\b",
    "La Bicyclette": r"\bLA BICYCLETTE\b",
    "La Boulangerie": r"\bLA BOULANGERIE\b",
    "La Lucha": r"\bLA LUCHA\b",
    "LAZ Parking": r"\bLAZ PARKING\b",
    "Lost Coffee": r"\bLOST COFFEE\b",
    "Lucile Packard Children's Hospital": r"\bLUCILE PACKARD CHILDRENS\b",
    "Lyft": r"\bLYFT\b",
    "Made out of Dough": r"\bMADE OUT OF DOUGH\b",
    "Mademoiselle Colette": r"\bMADEMOISELLE COLETTE\b",
    "Menchie's Frozen Yogurt": r"\bMENCHIES\b",
    "Menlo Swim & Sport": r"\bTEAM SHEEPER INC\b",
    "Microsoft 365 Home": r"\bMicrosoft 365\b",
    "MisterSoftee": r"MISTERSOFTEENORCAL\b",
    "Mollie Stone's": r"\bMOLLIE STONES\b",
    "Neighbor's Corner": r"\bNEIGHBOR'S CORNER\b",
    "Netflix": r"\bNETFLIX.COM\b",
    "Oral-B": r"\bORAL B\b",
    "Pérez Farms": r"PEREZ FARMS\b",
    "Pizzaria Luba": r"\bPIZZERIA LUBA\b",
    "Putnam Chevrolet": r"\bPUTNAM CHEVROLET\b",
    "Rally Gymnastics": r"\bRally Gymnastics\b",
    "Rebyl Coffee & Foods": r"\bREBYL\b",
    "Redwood City Nissan": r"\bREDWOOD CITY INFINITI\b",
    "REI": r"\bREI.COM\b",
    "RHJ Organic": r"RHJ ORGANIC\b",
    "Ritual Coffee": r"\bRITUAL COFFEE\b",
    "Rojas Family Farms": r"ROJAS FAMILY FARMS\b",
    "Royo Bread": r"\bROYO BREAD\b",
    "RJ Produce": r"\bRJ PRODUCE\b",
    "Rodriguez Bros. Ranch": r"\bRODRIGUEZ BROS.RANCH\b",
    "Russian School of Math": r"\bRSM - Peninsula\b",
    "Safeway": r"\bSAFEWAY\b",
    "Santa Cruz City Parking": r"\bSANTA CRUZ CITY PARKING\b",
    "SchoolForce": r"\bSCHOOLFORCE\b",
    "Shell": r"\bSHELL\b",
    "SodaStream": r"\bSODASTREAM\b",
    "Spectra Coffee": r"\bSPECTRA COFFEE\b",
    "SPRO Coffee Lab": r"\bSPRO\b",
    "Stanford Health Care": r"\bSTANFORD HEALTH CARE\b",
    "Talons": r"\bTALONS\b",
    "Temple Coffee": r"\bTEMPLE COFFEE\b",
    "The Epicurean Trader": r"\bTHE EPICUREAN TRADER\b",
    "The Frenchy Gourmet": r"\bTHE FRENCHY GOURMET\b",
    "Thai Tamarind": r"\bTHAI TAMARIND\b",
    "The Home Depot": r"\bHOME DEPOT\b",
    "The Reading Bug": r"\bTHE READING BUG\b",
    "Ticino": r"\bTICINO\b",
    "Trader Joe's": r"\bTRADER JOE S\b",
    "TuTu School": r"\bTUTU SCHOOL\b",
    "Luna's Farm": r"\bLUNAS FARMS\b",
    "Vina Enoteca": r"\bVINA ENOTECA\b",
    "Viva la Tarte": r"\bVIVE LA TARTE\b",
    "Waste (Recology)": r"\bRECOLOGY\b",
    "Water (Mid-Peninsula Water District)": r"\bMID-PENINSULA WATER\b",
    "Webb Ranch": r"\bWEBB RANCH\b",
    "YouTube Premium": r"\bYouTubePremium\b",
    "Whole Foods": r"\bWHOLE FOODS|WHOLEFDS\b",
    "ZombieRunner Coffee": r"\bZOMBIERUNNER\b",
}

PERSONAL_DESC_CONVERSIONS = {
    "Amazon Web Services": r"\bAMAZON WEB SERVICES\b",
    "Audible": r"\bAUDIBLE\b",
    "Calvin Klein": r"\bCalvin Klein\b",
    "Fjällräven": r"\bFJALLRAVEN\b",
    "Fooda": r"\bFOODA\b",
    "GitHub Copilot Pro": r"\bGITHUB, INC.\b",
    "Grammarly": r"\bGRAMMARLY",
    "J.Crew": r"\bJ Crew\b",
    "KCSM membership": r"\bKcsm Jazz 91\b",
    "KQED membership": r"\bKQED\b",
    "L.L. Bean": r"\bLlbean\b",
    "Patagonia": r"\bPATAGONIA\b",
    "Pink Owl Coffee": r"\bPINK OWL COFFEE\b",
    "Strava Summit": r"\bSTRAVA\b",
    "Tacx": r"\bGARMIN\b",
    "The Atlantic": r"\bThe Atlantic\b",
    "The New York Times": r"\bNYTIMES\b",
    "WIRED Magazine": r"\bWired - Digital\b",
}


# Registry for description conversions - open for extension, closed for modification
_DESC_CONVERSIONS_REGISTRY = {
    "family": FAMILY_DESC_CONVERSIONS,
    "personal": PERSONAL_DESC_CONVERSIONS,
}


def register_desc_conversions(cc_type: str, conversions: Dict[str, str]) -> None:
    """Register description conversions for a new card type.

    This allows extending the system with new card types without modifying
    existing code.

    Args:
        cc_type: The credit card type identifier.
        conversions: Mapping from clean descriptions to regex patterns.
    """
    _DESC_CONVERSIONS_REGISTRY[cc_type] = conversions


def get_desc_conversions(cc_type: str) -> Dict[str, str]:
    """Get description conversion mappings for the given card type.

    Args:
        cc_type: The credit card type ('family' or 'personal').

    Returns:
        Mapping from clean descriptions to regex patterns.

    Raises:
        ValueError: If cc_type is not registered.
    """
    if cc_type not in _DESC_CONVERSIONS_REGISTRY:
        raise ValueError(
            f"Unknown card type: {cc_type}. "
            f"Available types: {', '.join(_DESC_CONVERSIONS_REGISTRY.keys())}"
        )

    conversions = _DESC_CONVERSIONS_REGISTRY[cc_type].copy()
    # Merge common conversions
    conversions.update(COMMON_DESC_CONVERSIONS)
    return conversions
