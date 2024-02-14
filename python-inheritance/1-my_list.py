#!/usr/bin/python3
"""Module 1-mylist"""

class MyList(list):
    """class that inherits from list"""
    
    def print_sorted(self):
        if hasattr(self, '__str__'):
            print(sorted(self))
            return(sorted(self))
