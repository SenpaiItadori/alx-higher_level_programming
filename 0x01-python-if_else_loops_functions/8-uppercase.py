#!/usr/bin/python3
def uppercase(str):
    b = len(str)
    i = 0
    while i < b:
        a = ord(str[i])
        if a < 123 and a > 96:
            a -= 32
        print("{}".format(chr(a)), end="")
        i += 1
    print("")
    return 
