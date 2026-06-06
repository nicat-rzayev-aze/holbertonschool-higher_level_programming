#!/usr/bin/python3
"""Converts an object to a JSON string."""
import json


def to_json_string(my_obj):
    """Returns the JSON representation of an object (string)."""
    return json.dumps(my_obj)
