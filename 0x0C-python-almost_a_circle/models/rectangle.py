#!/usr/bin/python3
"""Module base | Almost a circle
This module is part of repository for review everything about Python:
Import, Exceptions, Class, Private attribute, Getter/Setter, Class method,
Static method, Inheritance, Unittest, Read/Write file"""
from models.base import Base


class Rectangle(Base):
    """Rectangle - defines a rectangle.
    Attributes: width, height, x, y
    Method:__init__, [width, height, x, y] setter and getter.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """__init__ - method constructor.
        Args:
            width (int): width of rectangle.
            height (int): height of rectangle
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def to_dictionary(self):
        """to_dictionary - returns the dictionary representation of a Rectangle.
        Args: nothing
        return: the dictionary representation of a Rectangle.
        """
        dict_rep = {}
        for key in self.__dict__:
            if "_" in key[0]:
                if "_Rectangle__" in key:
                    dict_rep[key[12:]] = self.__dict__[key]
                else:
                    dict_rep[key[1:]] = self.__dict__[key]
            else:
                dict_rep[key] = self.__dict__[key]
        return dict_rep

    def update(self, *args, **kwargs):
        """update - Update the class Rectangle, that assigns an argument to
        each attribute:
        Args:
            *args (list):
                1st argument should be the id attribute
                2nd argument should be the width attribute
                3rd argument should be the height attribute
                4th argument should be the x attribute
                5th argument should be the y attribute
            **kwargs(dict):
                 key/value (keyworded arguments)
        """
        for i in range(len(args)):
            if i == 0:
                self.id = args[i]
            elif i == 1:
                self.width = args[i]
            elif i == 2:
                self.height = args[i]
            elif i == 3:
                self.x = args[i]
            elif i == 4:
                self.y = args[i]

        if len(args) == 0:
            for key in kwargs:
                if key == "id":
                    self.id = kwargs[key]
                if key == "width":
                    self.width = kwargs[key]
                if key == "height":
                    self.height = kwargs[key]
                if key == "x":
                    self.x = kwargs[key]
                if key == "y":
                    self.y = kwargs[key]

    def __str__(self):
        """__str__ - Create a new string object from the given object.
        Args: nothing
        return: empty string
        """
        return "[{}] ({}) {}/{} - {}/{}".format(self.__class__.__name__,
                                                self.id, self.x, self.y,
                                                self.width, self.height)

    def display(self):
        """display - prints in stdout the Rectangle instance with the
        character #
        Args: none
        return: nothing
        """
        print("\n" * self.y, end="")
        for i in range(self.__height):
            print(" " * self.x, end="")
            print(self.__width * '#')

    def area(self):
        """area - width * height.
        Args: nothing
        Return: area of rectangle.
        """
        return self.__width * self.__height

    @property
    def width(self):
        """width - get width.
        Args: nothing
        """
        return self.__width

    @property
    def height(self):
        """height - get height.
        Args: nothing
        """
        return self.__height

    @property
    def x(self):
        """height - get x.
        Args: nothing
        """
        return self.__x

    @property
    def y(self):
        """height - get y.
        Args: nothing
        """
        return self.__y

    @width.setter
    def width(self, value):
        """width - set width.
        Args:
        - value (int): set width of rectangle.
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        else:
            if value <= 0:
                raise ValueError("width must be > 0")
            self.__width = value

    @height.setter
    def height(self, value):
        """height - set height.
        Args:
        - value (int): set height of rectangle.
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        else:
            if value <= 0:
                raise ValueError("height must be > 0")
            self.__height = value

    @x.setter
    def x(self, value):
        """height - set x of rectangle.
        Args:
        - value (int): set x of rectangle.
        """
        if type(value) != int:
            raise TypeError("x must be an integer")
        else:
            if value < 0:
                raise ValueError("x must be >= 0")
            self.__x = value

    @y.setter
    def y(self, value):
        """height - set y of rectangle
        Args:
        - value (int): set y of rectangle.
        """
        if type(value) != int:
            raise TypeError("y must be an integer")
        else:
            if value < 0:
                raise ValueError("y must be >= 0")
            self.__y = value
