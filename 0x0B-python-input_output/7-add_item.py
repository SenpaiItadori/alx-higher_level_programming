#!/usr/bin/python3

"""Defines a script that adds all arguments to a list and saves it to file."""


import sys
import json


if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file

    try:
        new = load_from_json_file("add_item.json")
    except FileNotFoundError:
        new = []
    for i in range(1, len(sys.argv)):
        new.append(str(sys.argv[i]))
    save_to_json_file(new, "add_item.json")
