#!/usr/bin/python3
"""base module"""
import json


class Base:
    """Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of a list of dictionaries."""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file."""
        if list_objs is None:
            list_objs = []
        file_name = cls.__name__ + ".json"
        with open(file_name, "w") as file:
            obj_list = [obj.to_dictionary() for obj in list_objs]
            file.write(cls.to_json_string(obj_list))

    @staticmethod
    def from_json_string(json_string):
        """Returns a list from a JSON string representation."""
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Creates an instance with attributes set based on the given dictionary."""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)  # Create a dummy Rectangle instance
        elif cls.__name__ == "Square":
            dummy = cls(1)  # Create a dummy Square instance
        else:
            return None
        # Update the dummy instance using the dictionary (kwargs)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances based on a JSON file."""
        file_name = cls.__name__ + ".json"
        try:
            with open(file_name, "r") as file:
                data = file.read()
                if not data:
                    return []
                json_list = cls.from_json_string(data)
                return [cls.create(**item) for item in json_list]
        except FileNotFoundError:
            return []
