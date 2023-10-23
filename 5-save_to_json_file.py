#!/usr/bin/python3
"""objet to a text file"""
import json


def save_to_json_file(my_obj, filename):
    with open(filename, 'w') as f:
        dct = json.dump(my_obj, f)

    return dct
