#!/usr/bin/python3
"""Convert CSV to JSON using DictReader -> data.json."""

import csv
import json


def convert_csv_to_json(csv_filename):
    """Read csv_filename and write JSON list of dicts to data.json.

    Return True on success, False on error (e.g., file not found).
    """
    try:
        with open(csv_filename, "r", encoding="utf-8") as f:
            rows = list(csv.DictReader(f))
        with open("data.json", "w", encoding="utf-8") as out:
            json.dump(rows, out)
        return True
    except Exception:
        return False
