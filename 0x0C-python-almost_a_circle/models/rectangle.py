#!/usr/bin/python3
'''import class Base'''
from models.base import Base


class Rectangle(Base):
    '''class Rectangle inherits from Base'''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''__init__ method for Rectangle
        width (int) widht of the Rectangle
        height (int) height of the Rectangle
        x (int)
        y (int)
        id (int) asiigned in the super class'''
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        '''getter for width'''
        return self.__width

    @width.setter
    def width(self, value):
        '''setter for width'''
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif (value <= 0):
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        '''getter for height'''
        return self.__height

    @height.setter
    def height(self, value):
        '''setter for height'''
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif (value <= 0):
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        '''getter for x'''
        return self.__x

    @x.setter
    def x(self, value):
        '''setter for x'''
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif (value < 0):
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        '''getter for y'''
        return self.__y

    @y.setter
    def y(self, value):
        '''setter for y'''
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif (value < 0):
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        '''method area
        Return the area of the rectangle'''
        return self.__height * self.__width

    def display(self):
        '''method display
        Print the rectangle with # character, move depends of x or y'''
        if self.__y > 0:
            print('\n'*self.__y, end="")
        for i in range(self.__height):
            print("{}{}".format(" "*self.__x, "#"*self.__width))

    def __str__(self):
        '''method __str__ , generate a string object
        Return: a string with the information of the object'''
        return "[{}] ({}) <{}>/<{}> - <{}>/<{}>".format(
            self.__class__.__name__, self.id, self.__x,
            self.__y, self.__width, self.__height)
