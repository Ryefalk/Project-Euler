"""
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284.
The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""

import math


def find_proper_divisors_sum(num):
    """
    Finds the sum of the proper divisors of the given number.
    """
    total = 0
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            total += (num // i) + i
    total += 1
    return total


def d(num, n):
    """
    Checks if the number is part of an amicable pair below the number n.
    If so it returns the set of those two numbers.
    """
    nums = set()
    num2 = find_proper_divisors_sum(num)
    if num != num2 and num2 < n and find_proper_divisors_sum(num2) == num:
        nums.add(num)
        nums.add(num2)
        return nums


def find_sum_amicable(end):
    """
    Finds the sum of all the amicable numbers below n.
    """
    amicable = set()
    for num in range(1, end):
        temp = d(num, end)
        if temp != None:
            amicable = amicable.union(temp)
    return sum(amicable)


print(find_sum_amicable(10000))