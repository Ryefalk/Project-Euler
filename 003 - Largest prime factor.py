"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

from math import sqrt


def is_multiple (number, divisor):
    """
    Checks if the number is a multiple of the divisor.
    """
    if float(number // divisor) == number / divisor:
        return True
    return False


def largest_prime_factor(n):
    """
    Finds the largest prime factor of n
    """
    current_number = 2
    top = n

    while current_number < top:
        if is_multiple(top, current_number):
            top = top // current_number
        else:
            current_number += 1
    return current_number


print(largest_prime_factor(600851475143))





