#!/usr/bin/python3
"""Deserialize a Python object from a binary pickle file."""

import pickle


def load_from_pickle_file(filename):
    """Load and return a Python object from a pickle file."""
    with open(filename, "rb") as f:
        return pickle.load(f)


if __name__ == "__main__":
    pass
