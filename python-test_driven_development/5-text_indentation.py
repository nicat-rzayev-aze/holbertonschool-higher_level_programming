#!/usr/bin/python3
"""
This module provides a function `text_indentation` that prints text
with 2 new lines after each of these characters: '.', '?' and ':'.
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each '.', '?' and ':'.

    Args:
        text: The text to be formatted (must be a string).

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    skip_space = False
    for char in text:
        if skip_space and char == ' ':
            continue
        skip_space = False

        print(char, end="")

        if char in ['.', '?', ':']:
            print("\n")
            skip_space = True
