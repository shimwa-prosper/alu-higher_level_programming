#!/usr/bin/python3
"""Module that defines the append_write function."""


def append_write(filename="", text=""):
    """Append a string to a UTF8 text file and return the characters added."""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
