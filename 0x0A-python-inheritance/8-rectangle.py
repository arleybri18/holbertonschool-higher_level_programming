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
