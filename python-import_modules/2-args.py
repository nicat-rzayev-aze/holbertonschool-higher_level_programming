#!/usr/bin/python3
import sys


if __name__ == "__main__":
    arg_count = len(sys.argv) - 1

    if arg_count == 0:
        print("{} arguments.".format(arg_count))
    elif arg_count == 1:
        print("{} argument:".format(arg_count))
    else:
        print("{} arguments:".format(arg_count))

    for i in range(1, len(sys.argv)):
        print("{}: {}".format(i, sys.argv[i]))
