#!/usr/bin/python3
"""module 6-load_from_json_file"""
import json


def load_from_json_file(filename):
    """file"""
    with open(filename, 'r') as file:
        data = json.load(file)

    return data
