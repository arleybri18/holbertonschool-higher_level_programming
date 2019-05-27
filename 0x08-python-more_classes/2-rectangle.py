#!/usr/bin/python3
class Rectangle:
    """Class with a instance private attributes, with optional value 0
        validate type and value > to 0, send a message Error using raised
        and define a method to asign values
    """
    def __init__(self, width=0, height=0):
        """Method init
        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle

        """
        self.width = width
        self.height = height

    def area(self):
        """Method that return the area of the rectangle
        Args:
            Takes a self parameters
        Return:
            area of the rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """Method that return the perimeter of the rectangle
        Args:
            Takes a self parameters
        Return:
            perimeter of the rectangle
        """
        if self.__width == 0 or self.__height == 0:
            perimeter = 0
        else:
            perimeter = (2 * (self.__width + self.__height))
        return perimeter

    @property
    def width(self):
        """Getter method for width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method for width
        """
        if type(value) is not int:
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = value

    @property
    def height(self):
        """Getter method for height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method for height
        """
        if type(value) is not int:
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = value
