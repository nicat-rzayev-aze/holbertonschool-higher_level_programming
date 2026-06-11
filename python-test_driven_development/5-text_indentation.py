#!/usr/bin/python3
"""
This module provides a function `is_same_class` that checks if an object
is exactly an instance of a specified class.
"""


def is_same_class(obj, a_class):
    """
    Checks if an object is exactly an instance of a specified class.

    Args:
        obj: The object to check.
        a_class: The class to match against.

    Returns:
        True if obj is exactly an instance of a_class, otherwise False.
    """
    return type(obj) is a_class
