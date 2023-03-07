#!/usr/bin/python3
for i in range(100):
    if (not i == 99):
        print("{:02d}, ".format(int(i)), end="")
    else:
        print("{}".format(int(i)), end="\n")
