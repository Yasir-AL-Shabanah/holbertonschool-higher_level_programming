#!/usr/bin/python3
import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Read CSV file and convert rows to a list of dictionaries,
    then write JSON output to data.json.
    Return True on success, False on failure.
    """
    try:
        with open(csv_filename, "r", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            rows = [row for row in reader]

        with open("data.json", "w", encoding="utf-8") as out:
            json.dump(rows, out)

        return True
    except Exception:
        return False
