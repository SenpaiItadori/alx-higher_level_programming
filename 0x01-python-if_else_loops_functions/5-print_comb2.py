#!/usr/bin/python3
for i in range(100):
    print("{:02d}".format(int(i)),end="")
    if (not i == 99):
        print(", ", end="")
