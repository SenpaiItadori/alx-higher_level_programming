#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        a = i % 3
        b = i % 5
        if a == 0 and not b == 0:
            i = "Fizz"
        elif b == 0 and not a == 0:
            i = "Buzz"
        elif a == 0 and b == 0:
            i = "FizzBuzz"
        print(f"{i}", end=" ")
