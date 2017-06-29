"""
The sum of the squares of the first ten natural numbers is,

1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""


def _sum(num):
    """
    finds the arithmetic sum from 1 to num
    """
    return (num * (1 + num)) // 2


def diff_sum_square(num):
    """
    Finds the difference between the square sum and sum of squares between 1 and num
    """
    sum_squares = 0
    for i in range(1, num + 1):
        sum_squares += i**2

    square_sum = _sum(num)**2
    diff = square_sum - sum_squares

    return diff

print(diff_sum_square(100))