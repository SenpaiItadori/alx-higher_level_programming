#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        a = number % -10
        a = a * -1
        print(f"{a}", end="")
        return a
    else:
        a = number % 10
        print(f"{a}", end="")
        return a
