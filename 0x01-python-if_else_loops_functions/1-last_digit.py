#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number < 0:
    last = number % -10
else:
    last = number % 10
if last == 0:
    print(f"Last digit of {number:d} is {last:d} and is 0")
elif last > 5:
    print(f"Last digit of {number:d} is {last:d} and is greater than 5")
else:
    print(f"Last digit of {number:d} is {last:d} and is less than 6 and not 0")
