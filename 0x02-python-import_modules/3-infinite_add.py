#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    j = len(sys.argv)
    i = 0
    for n in range(1, j):
        if n < 1:
            continue
        i += int(sys.argv[n])
    print(i)
