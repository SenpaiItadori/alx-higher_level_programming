#!/usr/bin/python3

"""Defines a funtion that write an object top a txt file."""
import json


def save_to_json_file(my_obj, filename):
    """Write an object to a txt file using json representation.
    Args:
        my_obj (any): The object to be written  to a txt file
        filename (str): The file to be written to
    """

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
