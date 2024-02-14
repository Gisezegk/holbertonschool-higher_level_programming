#!/usr/bin/python3
"""module 4-inherits_from.py"""

def inherits_from(obj, a_class):
    """more comments"""
    if type(obj) == a_class:
        return False
    if issubclass(type(obj), a_class):
        return True
    return False
