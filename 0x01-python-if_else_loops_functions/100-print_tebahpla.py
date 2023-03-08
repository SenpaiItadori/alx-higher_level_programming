#!/usr/bin/python3
i = 122
while i > 96:
    k = i % 2
    if not k == 0:
        j = i - 32
        print("{}".format(chr(j)), end="")
    elif k == 0:
        j = i
        print("{}".format(chr(j)), end="")
    i -= 1
