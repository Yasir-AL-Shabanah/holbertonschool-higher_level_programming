#!/usr/bin/python3
def best_score(a_dictionary):
    """Return key with the highest integer value; None if dict is None/empty."""
    if not a_dictionary:
        return None
    return max(a_dictionary, key=a_dictionary.get)
