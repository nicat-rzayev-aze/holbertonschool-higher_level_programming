#!/usr/bin/python3
"""
This module defines a class MyList that inherits from the built-in list.
"""


class MyList(list):
    """A custom list class that extends the built-in list functionality."""

    def print_sorted(self):
        """Print the list elements sorted in ascending order without modifying the original list."""
        print(sorted(self))
