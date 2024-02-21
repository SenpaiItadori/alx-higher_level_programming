#!/usr/bin/python3

"""Defines a class Student."""


class Student:
    """Represent a Student."""

    def __init__(self, first_name, last_name, age):
        """Initialize  a Student.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student
            age (int): The age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Get a dictionary representation ofthe Student.
        Args:
            attrs (list): The attribute to represent
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return ({k: getattr(self, k) for k in attrs if hasattr(self, k)})
        return (self.__dict__)

    def reload_from_json(self, json):
        """Replace all attributes o the Student.
        Args:
            json (dict): The key/value pairs to replace attributes
        """
        for i, j in json.items():
            setattr(self, i, j)