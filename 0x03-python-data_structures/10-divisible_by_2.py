#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    multiples = []
    if my_list:
        for x in my_list:
            multiples.append(False if x % 2 else True)
        return multiples

