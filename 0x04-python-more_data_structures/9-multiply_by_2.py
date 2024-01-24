#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    A = a_dictionary.copy()
    for key in A:
        A[key] = A[key] * 2
    return A
