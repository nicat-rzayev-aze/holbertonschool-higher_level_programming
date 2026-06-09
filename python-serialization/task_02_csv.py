#!/usr/bin/env python3
"""Module for converting CSV data to JSON format."""
import csv
import json


def read_csv_and_convert_to_json(csv_filename, json_filename):
    """Reads a CSV file and converts its content to a JSON file"""
    try:
        with open(csv_filename, "r", encoding="utf-8") as csv_f:
            csv_reader = csv.DictReader(csv_f)
            data = [row for row in csv_reader]

        with open(json_filename, "w", encoding="utf-8") as json_f:
            json.dump(data, json_f)

        return True
    except Exception:
        return False
