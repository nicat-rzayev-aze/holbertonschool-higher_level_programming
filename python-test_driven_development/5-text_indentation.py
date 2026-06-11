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

    formatted_text = text.replace('.', '.\n\n')
    formatted_text = formatted_text.replace('?', '?\n\n')
    formatted_text = formatted_text.replace(':', ':\n\n')

    lines = formatted_text.split('\n\n')
    
    for i, line in enumerate(lines):
        cleaned_line = line.strip(" ")
        if i < len(lines) - 1:
            print(cleaned_line)
            print()
        else:
            print(cleaned_line, end="")
