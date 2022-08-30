#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    lo = len(sys.argv) - 1
    print("{} argument{}{}"
          .format(lo, "" if lo == 1 else "s", "." if lo == 0 else ":"))
    for i in range(lo):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
