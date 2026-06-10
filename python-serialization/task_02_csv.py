#!/usr/bin/env python3
"""Module for converting CSV data to JSON format."""
import csv
import json


def convert_csv_to_json(csv_file):
    """Converts csv content to a JSON file"""
try:

        with open(csv_file, mode='r', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)

            data = list(csv_reader)

        with open('data.json', mode='w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4, ensure_ascii=False)

        print(f"Data has been successfully converted from {csv_file} to data.json.")
        return True

    except FileNotFoundError:
        print(f"Error: File '{csv_file}' not found.")
        raise
    except Exception as e:
        print(f"Unexpected error: {e}")
        raise
