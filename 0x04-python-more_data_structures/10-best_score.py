#!/usr/bin/python3

def best_score(a_dictionary):
    val = 0

    if a_dictionary == None:
        return (None)

    for key in a_dictionary:
        if val < a_dictionary[key]:
            val = a_dictionary[key]
    for key in a_dictionary:
        if val == a_dictionary[key]:
            return (key)
