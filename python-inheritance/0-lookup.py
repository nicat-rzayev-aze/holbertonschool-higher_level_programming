#!/usr/bin/python3
"""
This module provides a utility function to inspect objects.
"""


def lookup(obj):
    """Return the list of available attributes and methods of an object."""
    return dir(obj)
