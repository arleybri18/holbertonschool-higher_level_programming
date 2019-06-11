#!/usr/bin/python3
'''class rectangle inherits from Base'''
from models.base import Base


class Rectangle(Base):
    '''class Rectangle inherits from Base'''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''defines the initilization of the class'''
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        '''this method get the width'''
        return self.__width

    @width.setter
    def width(self, value):
        '''this method set the width'''
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif (value <= 0):
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        '''this method get the height'''
        return self.__height

    @height.setter
    def height(self, value):
        '''this method set the height'''
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif (value <= 0):
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        '''this method get the x'''
        return self.__x

    @x.setter
    def x(self, value):
        '''this method set the x'''
        if type(value) != int:
            raise TypeError("x must be an integer")
        elif (value < 0):
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        '''this method get the y'''
        return self.__y

    @y.setter
    def y(self, value):
        '''this method set the y'''
        if type(value) != int:
            raise TypeError("y must be an integer")
        elif (value < 0):
            raise ValueError("y must be >= 0")
        else:
            self.__y = value
