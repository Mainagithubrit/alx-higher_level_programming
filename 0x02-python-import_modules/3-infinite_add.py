#!/usr/bin/python3

if __name__ == "__main__":
    """Prints the sum of arguments"""
    import sys

    add = 0
    for x in range(len(sys.argv) - 1)
        add += int(sys.argv[x + 1])
    print("{}".format(add))
