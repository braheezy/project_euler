#!/usr/bin/env python3
"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

TODO: NOT OPTIMIZED
"""

if __name__ == "__main__":

    END = 20
    r = range(1, END + 1)

    def is_divisble_by_range(n, span):
        for i in span:
            if n % i != 0:
                return False
        return True

    i = END * 2
    while not is_divisble_by_range(i, r):
        i += 1
    print(
        f"The smallest positive number evenly divisible by all numbers from 1 to {END}: {i}"
    )
