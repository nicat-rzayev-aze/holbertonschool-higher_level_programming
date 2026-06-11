#!/usr/bin/python3
"""Its function for printing a square with the character #"""


def print_square(size):
    """It will print a square."""
    if not isinstance(size, int) or isinstance(size, bool):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size)
