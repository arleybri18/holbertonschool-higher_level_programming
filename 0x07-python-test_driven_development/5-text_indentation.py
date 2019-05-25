#!/usr/bin/python3
"""Module for text_indentation
"""


def text_indentation(text):
    """Function that print the square with the # symbol.

    Args:
        size (int, float > 0): is a size of the square.

    Returns:
        Nothing
        Print the square of the size given, or Error
        message if the data entry not are int.
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    text = text.replace(". ", ".\n\n")
    text = text.replace("? ", "?\n\n")
    text = text.replace(": ", ":\n\n")
    print(text)
