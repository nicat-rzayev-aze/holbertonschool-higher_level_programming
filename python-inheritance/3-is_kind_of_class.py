#!/usr/bin/python3
"""
This module defines a function to check object instances and inheritance.
"""


def is_kind_of_class(obj, a_class):
    """Check if an object is an instance of, or inherited from, a class.

    Args:
        obj: The object to check.
        a_class: The class to match against.

    Returns:
        True if obj is an instance or inherited instance, otherwise False.
    """
    return isinstance(obj, a_class)
