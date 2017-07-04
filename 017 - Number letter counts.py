"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115
(one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
"""

nb = {
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
    20: 'twenty',
    30: 'thirty',
    40: 'forty',
    50: 'fifty',
    60: 'sixty',
    70: 'seventy',
    80: 'eighty',
    90: 'ninety',
    100: 'hundred',
    1000: 'thousand',
}

def letter_sum(num):
    """
    Works up to 1000. Counts the number of letters in the numbers from one to num as specified above.
    """
    total = 0

    for i in range(1, num + 1):
        if i >= 1000:
            total += len(nb[i])
            total += len(nb[i // 1000])

        if i % 1000 >= 100:
            hundreds = (i // 100) % 10
            total += len(nb[hundreds])
            total += len(nb[100])
            if i % 100 != 0:
                total += len("and")

        if i % 100 >= 20:
            tens = ((i // 10) % 10) * 10
            total += len(nb[tens])

        if i % 100 >= 10 and i % 100 < 20:
            teens = i % 100
            total += len(nb[teens])
        elif i % 10 != 0:
            ones = i % 10
            total += len(nb[ones])
    return total

print(letter_sum(1000))
