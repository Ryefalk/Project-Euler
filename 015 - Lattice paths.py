"""
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?
"""

def latice_paths(n, k):
    """
    The number of latice paths are equal to the binomial coefficient below.
    """
    return combinations(n + k, n)


def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)


def factorial_with_stop(n, k):
    if n <= k:
        return 1
    else:
        return n * factorial_with_stop(n - 1, k)


def combinations(n, k):
    if n - k > k:
        return factorial_with_stop(n, n - k) // factorial(k)
    else:
        return factorial_with_stop(n, k) // factorial(n - k)


print(latice_paths(20,20))