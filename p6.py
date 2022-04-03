#!/usr/bin/env python3
"""
The sum of the squares of the first ten natural numbers is,
    1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,
    (1 + 2 + ... + 10)^2 = 55^2 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is
    3025 - 385 = 2640
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

if __name__ == "__main__":
    N = 100

    def sum_squares(x):
        total = 0
        for i in range(x + 1):
            total += i**2
        return total

    def square_sum(x):
        return sum(range(1, x + 1))**2

    print(
        f"I think there's a typo in the wording. Here's the answer to whatever the question is: {square_sum(N) - sum_squares(N)}"
    )
