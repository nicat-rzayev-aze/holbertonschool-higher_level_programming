#!/usr/bin/python3
"""Creates an objekt from a JSON file."""


def load_from_json_file(filename):
    """Creates an Object from a 'JSON file'."""
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
