#!/usr/bin/env python3
"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

if __name__ == "__main__":
    n = 1000
    x = 3
    y = 5

    sum = 0
    for i in range(1, n):
        if (i % x) == 0 or (i % y) == 0:
            sum += i
    print(f"The sum of all multiples of {x} or {y} below {n}: {sum}")