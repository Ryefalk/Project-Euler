"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

import itertools


def is_palindrome(num):
    """
    Checks if a number is a palindrome.
    """
    num_str = str(num)
    for i in range(len(num_str) // 2):
        if num_str[i] != num_str[-(1 + i)]:
            return False
    return True


def largest_palindrome():
    """
    Finds the largest palindrome number multiplying 2 3-digit numbers
    """
    largest = 0

    for x, y in itertools.combinations(range(1000, 100, -1), 2):
        n = x*y
        if is_palindrome(n) and n > largest:
            largest = n

    return largest


print(largest_palindrome())
