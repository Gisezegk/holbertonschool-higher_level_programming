#!/usr/bin/python3
"""base module """
import json


class Base():
    """clase base"""

    __nb_objects = 0

    def __init__(self, id=None):
        """inizialice"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ dictionaries to json """
        if not list_dictionaries:
            return "[]"

        json_data = json.dumps(list_dictionaries)
        return json_data

    @classmethod
    def save_to_file(cls, list_objs):
        """ saves json string representation to file """
        if not list_objs:
            my_list = []
        else:
            my_list = [obj.to_dictionary() for obj in list_objs]
        with open(f"{cls.__name__}.json", mode="w", encoding="utf-8") as f:
            f.write(cls.to_json_string(my_list))

    @staticmethod
    def from_json_string(json_string):
        """ returns representation """
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ returns the instance """
        if cls.__name__ == "Rectangle":
            ir = cls(1, 1)
        else:
            ir = cls(1)
        ir.update(**dictionary)
        return ir