#!/usr/bin/python3

import hidden_4


if __name__ == "__main__":
    sorted_names = sorted(name for name in dir(hidden_4)
                            if not name.startswith("__"))
    for name in sorted_names:
        print(name)
