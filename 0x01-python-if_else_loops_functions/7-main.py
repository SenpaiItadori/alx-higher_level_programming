#!/usr/bin/env python3
islower = __import__('7-islower').islower

print("3 is {}".format("lower" if islower("3") else "upper"))
print("a is {}".format("lower" if islower("a") else "upper"))
print("A is {}".format("lower" if islower("A") else "upper"))
