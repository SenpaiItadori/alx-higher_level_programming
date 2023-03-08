#!/usr/bin/python3
def remove_char_at(str, n):
    if n >= 0:
        copy = str[0:n] + str[n + 1:]
    elif n < 0:
        copy = str[:]
    return copy
