#!/usr/bin/python3

def addd(argv):
    argc = len(argv)
    add = 0
    if argc <= 1:
        print("{:d}".format(add))
        return
    else:
        i = 1
        while i < argc:
            add += int(argv[i])
            i += 1
        print("{:d}".format(add))

if __name__ == "__main__":
    import sys
    addd(sys.argv)
