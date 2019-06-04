#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''Class Square inherit from Rectangle'''
    def __init__(self, size):
        '''init method'''
        self.__size = super().integer_validator("size", size)
        super().__init__(self.__size, self.__size)

    def area(self):
        '''Calculate area of the rectangle
        arg width (int): width of the rectangle
        arg height (int): height of the rectangle
        return area'''
        return self.__size ** 2

    def __str__(self):
        return "[Square] " + str(self.__size) + "/" + str(self.__size)
