#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    ll = len(argv)
    print("{:d} {:s}{:s}".format(ll - 1, "argument" if ll <= 2 else "arguments",
                                 "." if ll == 1 else ":"))
    for i, s in enumerate(argv):
        if i > 0:
            print("{:d}: {:s}".format(i, s))
