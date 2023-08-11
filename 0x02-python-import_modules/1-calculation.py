#!/usr/bin/python3
if __name__ == "__main__":
    from calculation_1 import add, sub, mul, div
    """Prints the sum, subtraction, multiplication and divission of two numbers"""
    a = 10
    b = 5

    print("{} + {} = {}".format(a, b, add(a, b)))
    print("{} - {} = {}".format(a, b, sub(a, b)))
    print("{} * {} = {}".format(a, b, mul(a, b)))
    print("{} / {} = {}".format(a, b, div(a, b)))
