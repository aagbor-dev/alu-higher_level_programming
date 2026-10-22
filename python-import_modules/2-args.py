#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argv = sys.argv[1:]
    n = len(argv)
    if n == 0:
        print("0 arguments.")
    elif n == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(n))
    for i in range(n):
        print("{}: {}".format(i + 1, argv[i]))
