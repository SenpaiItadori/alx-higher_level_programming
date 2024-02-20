#!/usr/bin/python3

"""Defines a function that appends to a file."""


def append_write(filename="", text=""):
    """Return the number of chars added to a file.
    Args:
        filename (str): The name of the file to be append to.
        text (str): The text to be appended to the file.
    """

    with open(filename, "a", encoding="utf-8") as f:
        num_of_chars = f.write(text)
    return (num_of_chars)
