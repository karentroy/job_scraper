# filters.py

from config import NORTHEAST_STATES, ENTRY_LEVEL_TERMS, ROLE_QUERIES

def is_northeast(location):

    if not location:
        return False

    loc = location.upper()

    return any(state in loc for state in NORTHEAST_STATES)


def is_entry_level(text):

    text = (text or "").lower()

    return any(term in text for term in ENTRY_LEVEL_TERMS)


def is_relevant(text):

    text = (text or "").lower()

    keywords = [
        "biomedical",
        "medical",
        "regulatory",
        "FDA"
        "medical device",
        "clinical",
        "healthcare",
        "engineering",
        "pharma",
        "pharmaceutical"
    ]

    return any(k in text for k in keywords)