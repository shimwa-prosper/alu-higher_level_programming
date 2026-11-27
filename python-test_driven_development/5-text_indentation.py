#!/usr/bin/python3
"""Module that defines a function to indent text.

The function text_indentation prints a text with 2 new lines after
each of these characters: '.', '?' and ':'.
"""


def text_indentation(text):
    """Print a text with 2 new lines after each '.', '?' and ':'.

    Args:
        text (str): the text to print.

    Raises:
        TypeError: if text is not a string.
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    line = ""
    for char in text:
        line += char
        if char in ".?:":
            print(line.strip())
            print("")
            line = ""
    print(line.strip(), end="")
