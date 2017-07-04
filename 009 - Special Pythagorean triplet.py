"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

import math
import itertools


def find_pytagorean_triplet(num):
    """
    Finds the product of the Pythagorean triplet for which a + b + c = num
    """
    for a, b in itertools.combinations(range(num // 2), 2):
        c = math.sqrt(a**2 + b**2)

        if int(c) == c:
            c = int(c)

        if isinstance(c, int) and a + b + c == 1000:
            return a * b * c
    return -1

print(find_pytagorean_triplet(1000))