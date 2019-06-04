#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''Class Rectangle inherit from BaseGeometry'''
    def __init__(self, width, height):
        '''init method
        arg width (int): width of the rectangle
        arg height (int): height of the rectangle'''
        self.__width = super().integer_validator("width", width)
        self.__height = super().integer_validator("height", height)

    def area(self):
        '''Calculate area of the rectangle
        arg width (int): width of the rectangle
        arg height (int): height of the rectangle
        return area'''
        return self.__width * self.__height

    def __str__(self):
        return "[Rectangle] " + str(self.__width) + "/" + str(self.__height)
