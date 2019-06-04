#!/usr/bin/python3
class BaseGeometry:
    '''Class BaseGeometry'''
    def area(self):
        '''Method area
        arg self: object
        return an exception'''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''Method integer_validator
        arg self: object
        arg name (string): name of the geometric figure
        arg value (int): value
        return: Exceptions if the types not are supported'''
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
        else:
            return value
