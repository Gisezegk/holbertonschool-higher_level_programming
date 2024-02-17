#!/usr/bin/python3
"""module 7-add_item"""
import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
args = sys.argv[1:]

try:
    with open('add_item.json') as f:
        my_data = load_from_json_file('add_item.json')
except FileNotFoundError:
    my_data = []

my_data.extend(args)
save_to_json_file(my_data, 'add_item.json')
