#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    """Print a dict sorted by key: 'key: value' per line."""
    for k in sorted(a_dictionary.keys()):
        print("{}: {}".format(k, a_dictionary[k]))
