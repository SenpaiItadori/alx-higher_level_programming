#!/usr/bin/python3

def uniq_add(my_list=[]):
    total = 0
    new = my_list.copy()
    for i in set(new):
        total = total + i
    return (total)
