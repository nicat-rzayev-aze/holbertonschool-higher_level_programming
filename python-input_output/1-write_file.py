#!/usr/bin/python3
"""For Reading and printing a text file."""


def read_file(filename=""):
    """Reads a text file and prints it to stdout."""
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
