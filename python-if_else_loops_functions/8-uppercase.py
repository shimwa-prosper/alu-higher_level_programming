#!/usr/bin/python3
def uppercase(str):
    """Print a string in uppercase, followed by a new line."""
    for c in str:
        if 97 <= ord(c) <= 122:
            c = chr(ord(c) - 32)
        print("{}".format(c), end="")
    print("")
