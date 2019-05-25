#!/usr/bin/python3
"""Module for print_square
"""


def print_square(size):
    """Function that print the square with the # symbol.

    Args:
        size (int, float > 0): is a size of the square.

    Returns:
        Nothing
        Print the square of the size given, or Error message
        if the data entry not are int.
    """
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    if type(size) is float:
        size = int(size)
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("{}".format("#"*size))
