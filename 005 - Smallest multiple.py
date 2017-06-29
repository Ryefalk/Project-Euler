"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

import itertools
import math


def lcm (a, b):
    """
    Finds the largest common multiple
    """
    if a > b:
        return a // gcd(a, b) * b
    else:
        return b // gcd(a, b) * a


def gcd (a, b):
    """
    Finds the greatest common divisor
    """
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def smalest_number(numbers):
    """
    Finds the smallest number that is evenly divisible by all number in the iterable
    """
    if len(numbers) == 1:
        return numbers[0]
    else:
        return lcm(numbers[0], smalest_number(numbers[1:]))

print(smalest_number(range(1,21)))