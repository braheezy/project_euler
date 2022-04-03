#!/usr/bin/env python3
"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""
import sys
if __name__ == "__main__":

    def is_palindrome(n):
        a = list(str(n))
        b = list(reversed(a))
        return a == b

    p = []
    for i in range(999, 1, -1):
        for j in range(999, 1, -1):
            if is_palindrome(i * j):
                p.append(i * j)

    print(
        f"The largest palindrome made from product of two 3-digit numbers: {max(p)}"
    )
