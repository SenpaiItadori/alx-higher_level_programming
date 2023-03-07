#!/usr/bin/python3
for i in range(10):
    if i == 9:
        print("89")
    for j in range(i + 1, 10):
        if not i == 8:
            print("{}{}, ".format(int(i), int(j)), end="")
