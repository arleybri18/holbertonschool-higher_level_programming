#!/usr/bin/python3
class Square:
    """Class with a instance private attribute, with optional value 0
        validate type and value > to 0, send a message Error using raised
    """
    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
