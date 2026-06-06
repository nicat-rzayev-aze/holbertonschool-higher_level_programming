#!/usr/bin/python3
"""
This module provides a function `say_name` that prints a formatted name.
"""


def say_name(first_name, last_name=""):
    """
    Prints "My name is <first name> <last name>".

    Args:
        first_name: A string representing the first name.
        last_name: A string representing the last name (defaults to "").

    Raises:
        TypeError: If either first_name or last_name is not a string.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
