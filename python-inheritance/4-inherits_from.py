#!/usr/bin/python3
"""
This module defines a function to check subclass inheritance.
"""


def inherits_from(obj, a_class):
    """Check if an object is an instance of a class inherited from a_class.

    Args:
        obj: The object to check.
        a_class: The class to match against.

    Returns:
        True if obj's class is a subclass of a_class (and not a_class itself),
        otherwise False.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
