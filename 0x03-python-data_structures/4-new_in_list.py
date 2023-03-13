#!/usr/bin/python3
#4-new_in_list.py

def new_in_list(my_list, idx, element):
    x = my_list.copy()
    if idx < 0 or idx > len(my_list):
        return x
    else:
        x[idx] = element
        return x
