#!/bin/usr/python3
'''import class Rectangle'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''Class Square inherits from Rectangle'''
    def __init__(self, size, x=0, y=0, id=None):
        '''method __init__ use method of the super class'''
        super().__init__(size, size, x, y, id)

    def __str__(self):
        '''overwrite method __str__'''
        return "[{}] ({}) {}/{} - {}".format(
            self.__class__.__name__, self.id, self.x,
            self.y, self.width)
    @property
    def size(self):
        '''getter for size'''
        return self.width

    @size.setter
    def size(self, value):
        '''setter for size'''
        self.width = value
        self.height = value

