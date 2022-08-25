#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    narg = len(argv) - 1
    if narg == 0:
        print("{} arguments.".format(narg))
    elif narg == 1:
        print("{}arguments".format(narg))
    else:
        print("{} arguments".format(narg))
    i = 1
    while i <= narg:
        print("{}: {}".format(i, argv[i]))
        i += 1
