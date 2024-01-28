#!/usr/bin/python3

import sys

if __name__ == "__main__":
    r = 0
    for i in range(1, len(sys.argv)):
        r = r + int(sys.argv[i])
    print(r)
