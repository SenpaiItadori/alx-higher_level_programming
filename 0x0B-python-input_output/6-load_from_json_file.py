#!/usr/bin/python3

"""Defines a funtion that convertes a string from txt file to an object."""
import json


def load_from_json_file(filename):
    """Read an object from a txt file using json representation.
    Args:
        filename (str): The file to br read from
    """

    with open(filename, encoding="utf-8") as f:
        f.seek(0)
        return (json.load(f))
