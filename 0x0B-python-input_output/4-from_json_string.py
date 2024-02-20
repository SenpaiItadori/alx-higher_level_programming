#!/usr/bin/python3

"""Defines a function that converts a json string to a py datat structure."""
import json


def from_json_string(my_str):
    """Return a python data structure from a json string.
    Args:
        my_str (str): the json string to be converted
    """
    return (json.loads(my_str))
