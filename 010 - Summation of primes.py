"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

import math


def is_prime(num, list_smaler_primes):
    """
    Checks if the number is_prime using previous primes
    """
    sqrt = math.sqrt(num)
    for i in list_smaler_primes:
        if i > sqrt:
            break
        if num%i == 0:
            return False
    return True


def prime_gen(start, list_smaler_primes):
    """
    Generates the next prime given the list of all previous primes.
    """
    while True:
        if is_prime(start, list_smaler_primes):
            list_smaler_primes.append(start)
            yield start
        start += 1



def sum_primes(end):
    """
    Works for end 2 and up. Summarises the primes up to the last prime before the specified end point.
    """
    prime_list = [2]
    total = 0
    current_prime = 2

    for p in prime_gen(current_prime, prime_list):
        if p > end:
            break
        total += p

    return total


print(sum_primes(2000000))