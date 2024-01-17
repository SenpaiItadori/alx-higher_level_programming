#!/usr/bin/python3

def remove_char_at(str, n):
    if (n >= 0):
        copy = str[:n]
        copy = copy + str[n+1:]
        return (copy)
    return (str)
