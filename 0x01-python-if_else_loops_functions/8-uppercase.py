#!/usr/bin/python3

def uppercase(str):
    ans = ""
    for c in str:
        if ord(c) >= 97 and ord(c) <= 122:
            ans += chr(ord(c) - 32)
        else:
            ans += c
            print(result)
