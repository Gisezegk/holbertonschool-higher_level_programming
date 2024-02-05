#!/usr/bin/python3
"""Function that prints My name is <first name> <last name>"""


def say_my_name(first_name, last_name=""):
    """Function that prints My name is <first name> <last name>"""

    error1 = "first_name must be a string"
    error2 = "last_name must be a string"

    if not isinstance(first_name, str):
        raise TypeError(error1)
    elif not isinstance(last_name, str):
        raise TypeError(error2)
    print("My name is {} {}".format(first_name, last_name))
