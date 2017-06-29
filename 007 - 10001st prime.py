"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
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


def find_prime(index):
    """
    Index needs to be at least 1. Finds the prime number at position "index".
    """

    i = 3
    prime_list = [2]

    while len(prime_list) < index:
        if is_prime(i, prime_list):
            prime_list.append(i)
        i += 1

    return prime_list[-1]


print(find_prime(10001))