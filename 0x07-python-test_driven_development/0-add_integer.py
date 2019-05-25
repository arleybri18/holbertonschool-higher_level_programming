#!/usr/bin/python3
"""Module for add_integer
"""


def add_integer(a, b=98):
    """Function to add two integers.

    Args:
        a (int, float): is a number.
        b (int, float): is number to add to a.

    Returns:
        int: The value of a add b. or Error message if
        a or b is not integer or float.
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    else:
        return int(a) + int(b)
