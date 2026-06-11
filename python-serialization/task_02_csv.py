#!/usr/bin/env python3
"""Module for converting CSV data to JSON format."""
import csv
import json

def convert_csv_to_json(csv_filename):
    try:
        with open(csv_filename, newline='', encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file)
            data = [row for row in reader]

        with open("data.json", "w", encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=2)

        return True

    except FileNotFoundError:
        return False

csv_file = "data.csv"
convert_csv_to_json(csv_file)
print(f"Data from {csv_file} has been converted to data.json")
