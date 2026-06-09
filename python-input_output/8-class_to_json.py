#!/usr/bin/python3
"""Converts a class instance to a dictionary for JSON serialization."""


def class_to_json(obj):
    """Returns the dictionary description of an object"""
    return obj.__dict__
