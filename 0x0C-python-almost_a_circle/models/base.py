#!/usr/bin/python3
class Base:
    '''This class will be the base of all other classes in this project.
    The goal of it is to manage id attribute in all your future classes
    and to avoid duplicating the same code (by extension, same bugs)'''
    __nb_objects = 0

    def __init__(self, id=None):
        '''__init__ method
        id (int) is an id of the object, assign if is sended or use the
        number of object in the class'''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
