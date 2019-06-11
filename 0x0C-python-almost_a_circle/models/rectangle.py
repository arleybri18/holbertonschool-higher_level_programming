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

    def area(self):
        '''this method Return the area of the rectangle'''
        return self.__height * self.__width

    def display(self):
        '''Print the rectangle with # character
        move depends of x or y'''
        if self.__y > 0:
            print('\n'*self.__y, end="")
        for i in range(self.__height):
            print("{}{}".format(" "*self.__x, "#"*self.__width))

    def __str__(self):
        '''Generate a string object
        Return: a string with the information of the object'''
        return "[{}] ({}) {}/{} - {}/{}".format(
            self.__class__.__name__, self.id, self.__x,
            self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        '''method update
       Args:
            *args (list):
                1st argument should be the id attribute
                2nd argument should be the width attribute
                3rd argument should be the height attribute
                4th argument should be the x attribute
                5th argument should be the y attribute
            **kwargs can be thought of as a double pointer
            to a dictionary: key/value
                skipped if *args exists and is not empty
        Return: Nothing, update the argument sended'''
        if (len(args) > 0):
            for idx in range(len(args)):
                if idx == 0:
                    self.id = args[idx]
                elif idx == 1:
                    self.width = args[idx]
                elif idx == 2:
                    self.height = args[idx]
                elif idx == 3:
                    self.x = args[idx]
                elif idx == 4:
                    self.y = args[idx]
        else:
            for key in kwargs:
                if key == "id":
                    self.id = kwargs[key]
                elif key == "width":
                    self.width = kwargs[key]
                elif key == "height":
                    self.height = kwargs[key]
                elif key == "x":
                    self.x = kwargs[key]
                elif key == "y":
                    self.y = kwargs[key]

    def to_dictionary(self):
        '''this method return a dictionary'''
        new_dict = {}
        new_dict["x"] = self.__dict__["_Rectangle__x"]
        new_dict["y"] = self.__dict__["_Rectangle__y"]
        new_dict["width"] = self.__dict__["_Rectangle__width"]
        new_dict["height"] = self.__dict__["_Rectangle__height"]
        new_dict["id"] = self.__dict__["id"]
        return new_dict
