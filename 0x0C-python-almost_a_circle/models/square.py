#!/usr/bin/python3
'''this class inherits from rectangle'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''inherits from Rectangle'''
    def __init__(self, size, x=0, y=0, id=None):
        '''method init use method of the super class'''
        super().__init__(size, size, x, y, id)

    def __str__(self):
        '''overwrite method str'''
        return "[{}] ({}) {}/{} - {}".format(
            self.__class__.__name__, self.id, self.x,
            self.y, self.width)

    @property
    def size(self):
        '''this method set the size'''
        return self.width

    @size.setter
    def size(self, value):
        '''this method the size'''
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        '''update arguments of the square'''
        args_sq = []
        for idx in range(len(args)):
            if idx == 0:
                args_sq.append(args[idx])
            elif idx == 1:
                args_sq.append(args[idx])
                args_sq.append(args[idx])
            elif idx == 2:
                args_sq.append(args[idx])
            elif idx == 3:
                args_sq.append(args[idx])

        if len(kwargs) != 0:
            kwargs_cp = kwargs.copy()
            for key in kwargs_cp:
                if key == "size":
                    kwargs["width"] = kwargs[key]
                    kwargs["height"] = kwargs[key]

        super().update(*args_sq, **kwargs)

    def to_dictionary(self):
        '''this method return a dictionary'''
        new_dict = {}
        new_dict["x"] = self.__dict__["_Rectangle__x"]
        new_dict["y"] = self.__dict__["_Rectangle__y"]
        new_dict["size"] = self.__dict__["_Rectangle__width"]
        new_dict["id"] = self.__dict__["id"]
        return new_dict
