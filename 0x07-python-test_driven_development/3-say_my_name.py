#!/usr/bin/python3
"""Module for say_my_name
"""


def say_my_name(first_name, last_name=""):
    """Function that print the full name.

    Args:
        first_name (string): is a first name of the user.
        last_name (string): is a last name of the user.

    Returns:
        Nothing
        Print the full name, or Error message if the data
        entry not are strings.
    """
    if isinstance(first_name, str) is False:
        raise TypeError("first_name must be a string")
    if isinstance(last_name, str) is False:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
