#!/usr/bin/python3

def to_uper(c):
    if ord(c) >= 97 and ord(c) <= 122:
        return (ord(c) - 32)
    else:
        return ord(c)

def uppercase(str):
    str_new =""
    for c in str:
        str_new += "%c"%to_uper(c)
    print("{:S}".format(str_new))
