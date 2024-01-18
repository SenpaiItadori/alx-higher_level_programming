#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    argv = sys.argv
    argc = len(argv)

    if argc <= 1:
        print("0 arguments.")
    elif argc == 2:
        print("{:d} argument:".format(argc - 1))
    else:
        print("{:d} arguments:".format(argc - 1))
    for i in range(1, len(argv)):
        print("{:d}: {:s}".format(i, argv[i]))
