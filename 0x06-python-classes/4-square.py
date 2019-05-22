#!/usr/bin/python3
class Square:
    """Class with a instance private attribute, with optional value 0
        validate type and value > to 0, send a message Error using raised
        and define a method to calculate area of square
    """
    def __init__(self, size=0):
        """init method
        Args:
        size (int): Size of the square object
        """
        self.__size = size

    def area(self):
        """Method to calculate area
        Args:
            Return self.__size**2
        """
        return self.__size**2

    @property
    def size(self):
        """Method to get the size
        Args:
            size (int): Size of the square object
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Method to set the size
        Args:
            size (int): Size of the square object
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
