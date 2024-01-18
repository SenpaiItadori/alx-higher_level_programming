#!/usr/bin/python3

import sys

argv = sys.argv
argc = len(argv)

if argc <= 1:
    print("0 arguments.")
elif argc == 2:
    print("{} argument:".format(argc - 1))
else:
    print("{} arguments:".format(argc - 1))
for i in range(1, len(argv)):
    print("{}: {}".format(i, argv[i]))
