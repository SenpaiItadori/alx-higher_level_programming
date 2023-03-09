#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    j = len(sys.argv)
    if j == 1:
        print("0 arguments.")
    elif j == 2:
        print("1 argument:")
    else:
        print("{} arguments:".format(j - 1))
    for i in range(j):
        if i == 0:
            continue
        print("{}: {}".format(i, sys.argv[i]))
