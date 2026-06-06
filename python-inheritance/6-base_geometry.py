#!/usr/bin/python3
"""
This module defines a class BaseGeometry with an area method.
"""


class BaseGeometry:
    """A class representing base geometry."""

    def area(self):
        """Raise an Exception indicating that area is not implemented."""
        raise Exception("area() is not implemented")
