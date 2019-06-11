#!/usr/bin/python3
import json
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

    @staticmethod
    def to_json_string(list_dictionaries):
        '''method to_json_string
        Args:
            list_dictionaries (dict):
                convert to json string'''
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        '''method save_to_file
        Args:
            cls -- class
            list_objs : List of objects
            Return: Write a file'''
        new_list = []
        if list_objs is not None:
            for li_obj in list_objs:
                new_list.append(li_obj.to_dictionary())
        with open(type(list_objs[0]).__name__ + '.json', 'w', encoding ="utf-8") as file:
            file.write(cls.to_json_string(new_list))
