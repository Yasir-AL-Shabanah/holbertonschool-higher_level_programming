#!/usr/bin/python3
"""Serialize a Python object to a binary file using pickle."""

import pickle


def save_to_pickle_file(my_obj, filename):
    """Write a pickled representation of my_obj to filename."""
    with open(filename, "wb") as f:
        pickle.dump(my_obj, f)


if __name__ == "__main__":
    pass
