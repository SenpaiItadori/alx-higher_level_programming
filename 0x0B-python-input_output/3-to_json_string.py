#!/usr/bin/python3

"""Defines a fuhnction that formats an object to the JSON representation."""
import json


def to_json_string(my_obj):
    """Return the JSON rep of an object string.
    Args:
        my_obj (any): The object to be parsed to JSON
    """
    return (json.dumps(my_obj))
