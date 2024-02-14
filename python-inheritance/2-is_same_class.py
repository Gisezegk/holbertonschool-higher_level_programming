#!/usr/bin/python3
"""module 2-is_same_class.py"""

def is_same_class(obj, a_class):
    """ object is exactly"""
    if obj is None:
        return False

    if not type(obj) is a_class:
        return False
    return True
