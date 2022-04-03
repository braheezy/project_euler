#!/usr/bin/env python3
"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

if __name__ == "__main__":
    x = 600851475143

    def is_prime(n: int) -> bool:
        if n <= 3:
            return n > 1
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i**2 <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    for i in range(int(x**0.5) + 1, 1, -1):
        if x % i == 0 and is_prime(i):
            print(f"The largest primge factor of {x}: {i}")
            break
