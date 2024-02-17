#!/usr/bin/python3
"""module 5-save_to_json_file"""
import json


def save_to_json_file(my_obj, filename):
    """file"""
    with open(filename, 'w') as f:
        n = json.dump(my_obj, f)

    return n
