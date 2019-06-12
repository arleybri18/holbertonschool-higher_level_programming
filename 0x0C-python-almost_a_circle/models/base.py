#!/usr/bin/python3
'''Class Base'''
import json
import os.path
import csv


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
            self.id = self.__nb_objects

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
        if list_objs:
            for li_obj in list_objs:
                new_list.append(li_obj.to_dictionary())
        with open(cls.__name__ + '.json', 'w') as file:
            file.write(cls.to_json_string(new_list))

    @staticmethod
    def from_json_string(json_string):
        '''return the new list with the json string'''
        new_list = []
        if json_string is None or len(json_string) == 0:
            return new_list
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        '''create instances of the class'''
        if cls.__name__ == "Rectangle":
            base_obj = cls(5, 5)
        elif cls.__name__ == "Square":
            base_obj = cls(5)
        base_obj.update(**dictionary)
        return base_obj

    @classmethod
    def load_from_file(cls):
        new_list = []
        name_file = cls.__name__ + ".json"
        if os.path.exists(name_file):
            with open(name_file, "r") as file:
                string = file.read()
                output = cls.from_json_string(string)
                for item in output:
                    new_list.append(cls.create(**item))
        return new_list

    @classmethod
    def save_to_file_csv(cls, list_objs):
        '''save in csv file'''
        name_file = cls.__name__ + ".csv"
        new_list = []
        if list_objs:
            for li_obj in list_objs:
                new_list.append(li_obj.to_dictionary())
        with open(name_file, 'w') as file:
            keys = new_list[0].keys()
            writer = csv.DictWriter(file, keys)
            writer.writeheader()
            writer.writerows(new_list)

    @classmethod
    def load_from_file_csv(cls):
        '''load from file csv'''
        new_list = []
        new_dict = {}
        name_file = cls.__name__ + ".csv"
        if os.path.exists(name_file):
            with open(name_file, mode='r') as csv_file:
                csv_reader = csv.DictReader(csv_file)
                for row in csv_reader:
                    for key, value in row.items():
                        new_dict[key] = int(value)
                    new_list.append(cls.create(**new_dict))
        return new_list
