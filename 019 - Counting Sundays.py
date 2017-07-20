"""
You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""

def even_div(n, div):
    return n % div == 0

def how_many_sundays():
    """
    Calculates the number of sundays between 1 Jan 1901 to 31 Dec 2000 that have fallen on the first in a month.
    """
    #modify february on leap years
    months = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    months_leap = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

    # to switch from mondays to sundays.
    day_count = 1
    sundays = 0

    for year in range(1900, 2000 + 1):
        if year == 1901:
            sundays = 0
        if even_div(year, 4):
            if even_div(year, 400) or not even_div(year, 100):
                leap_year = True
            else:
                leap_year = False
        else:
            leap_year = False

        if year == 1950:
            assert not leap_year
        if year == 1984:
            assert leap_year

        for month in range(1, 12 + 1):
            if leap_year:
                day_count += months_leap.get(month)
            else:
                day_count += months.get(month)

            #finding sundays on the firs
            if day_count % 7 == 0:
                sundays += 1

    return sundays

print(how_many_sundays())
