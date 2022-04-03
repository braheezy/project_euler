#!/usr/bin/env python3
"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a2 + b2 = c2

For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""
import sys
import math
if __name__ == "__main__":

    limit = 1000
    for a in range(1, limit):
        for b in range(a + 1, limit):
            # print(f"index: {a}, {b}")
            c_sq = (a * a) + (b * b)
            # print(f"{a * a} * {b * b} = {c_sq}")
            c = math.isqrt(c_sq)
            # print(f"c: {c}")
            if math.isqrt(c_sq)**2 == c_sq and (a + b + c) == limit:
                print(
                    f"Found a Pythagorean triplet such that (a + b + c) = {limit}"
                )
                print(f"\ta={a} b={b} c={c}")
                print(f"\t{a} * {b} * {c} = {a * b * c}")
