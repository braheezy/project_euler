#!/usr/bin/env python3
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
import sys

if __name__ == "__main__":
    MONTHS = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    LEAP_MONTHS = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    def is_leap_year(year):
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            return False
        elif year % 4 == 0:
            return True
        else:
            return False

    def day_of_week(d):
        # Rata Die method
        # https://en.wikipedia.org/wiki/Determination_of_the_day_of_the_week#Rata_Die
        known_day = 1  # Monday
        return (known_day + d) % 7

    # Start date is 1 year after our known date and 1900 is not a leap year
    days_since = 365

    count_of_sundays = 0
    for year in range(1901, 2001):
        # Pick the set of months we should use
        if is_leap_year(year):
            months = LEAP_MONTHS
        else:
            months = MONTHS

        # Check the 1st of each month and see if it's a Sunday
        for month in months:
            if day_of_week(days_since) == 0:
                count_of_sundays += 1
            # By incrementing by the # of days in each month, `days_since`
            # always points to the 1st of each month
            days_since += month

    print(f"Number of Sundays on the first of the month: {count_of_sundays} ")
