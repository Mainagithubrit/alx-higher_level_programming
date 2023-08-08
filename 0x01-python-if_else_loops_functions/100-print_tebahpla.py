#!/usr/bin/python3
for v in range(122, 96, -1):
    if v % 2 != 0:
        v = v - 32
    print("{}".format(chr(v)), end="")
