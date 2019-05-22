#!/usr/bin/python3
class Square:
    """Class with a instance private attribute, with optional value 0
        validate type and value > to 0, send a message Error using raised
        and define a method to calculate area of square
    """
    def __str__(self):
        text = ""
        if self.__size is 0:
            return text
        else:
            if self.__position[1] is not 0:
                for idx in range(position[1]):
                    text = text + "\n"
            for i in range(self.__size):

                print("{}".format(" " * self.__position[0]), end="")
                print("{}".format("#" * self.__size))

    def __init__(self, size=0, position=(0, 0)):
        """init method
        Args:
        size (int): Size of the square object
        position (int,int): position for print the square
        """
        self.size = size
        self.position = position

    def area(self):
        """Method to calculate area
        Returns:
            Return self.__size**2
        """
        return self.__size**2

    def my_print(self):
        """Method to print the square
        Returns:
            nothing, print the square
        """
        if self.__size is 0:
            print()
        else:
            if self.__position[1] is not 0:
                print("\n" * self.__position[1], end="")
            for i in range(self.__size):
                print("{}".format(" " * self.__position[0]), end="")
                print("{}".format("#" * self.__size))

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

    @property
    def position(self):
        """Method to get the position
        Args:
            position value
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Method to set position
        Args:
            value: value to set a position
        """
        if (type(value) is not tuple or len(value) is not 2 or type(value[0])
                is not int or type(value[1]) is not int or value[0] < 0 or
                value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value
