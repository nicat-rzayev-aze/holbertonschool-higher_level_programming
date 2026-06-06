#!/usr/bin/python3
"""A function for reading documents"""


def read_file(filename=""):
    """So we can read files"""
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
