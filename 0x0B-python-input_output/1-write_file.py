#!/usr/bin/python3

"""Defines a function that writes to a file."""


def write_file(filename="", text=""):
    """Return the number of chars written to a file.
    Args:
        filename (str): The name of the fiile to be written to
        text (str): The text to be written to the file
    """

    with open(filename, "w", encoding="utf-8") as f:
        num_of_chars = f.write(text)
    return (num_of_chars)
