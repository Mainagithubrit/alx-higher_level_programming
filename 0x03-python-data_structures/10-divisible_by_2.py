#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    mult = []
    if my_list:
        for x in my_list:
            mult.append(False if x % 2 else True)
            return mult
