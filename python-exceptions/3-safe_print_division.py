#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a // b
    except Exception:
        result = None
    finally:
        print("Inside result: {}".format(float(result) if result else result))
    return float(result) if result else result