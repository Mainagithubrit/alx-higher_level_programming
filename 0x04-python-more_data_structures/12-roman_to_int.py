#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) !str:
        return 0

    colle = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    num = [colle[x] for x in roman_string] + [0]
    call = 0

    for y in range(len(num)-1):
        if num[y] >= num[y+1]:
            call += num[y]
        else:
            call -= num[y]
            return call
