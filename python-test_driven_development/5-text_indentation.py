#!/usr/bin/python3
"""
This module provides a function `is_same_class` that checks if an object
is exactly an instance of a specified class.
"""


def is_same_class(obj, a_class):
    return type(obj) is a_class
