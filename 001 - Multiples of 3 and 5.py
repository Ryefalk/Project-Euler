"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""



def is_multiple (number, divisor):
    """
    Checks if the number is a multiple of the divisor.
    """
    if float(number // divisor) == number / divisor:
        return True
    return False



def sum_of_multiples(top, divisor_list):
    """
    Returns the sum of the numbers below a given number that are divisible by
    the given numbers in a list.
    """
    total = 0

    for current_num in range(1, top):
        for divisor in divisor_list:
            if is_multiple(current_num, divisor):
                total += current_num
                break

    return total


print(sum_of_multiples(1000, [3, 5]))