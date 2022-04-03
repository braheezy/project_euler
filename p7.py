#!/usr/bin/env python3
"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""
import sys
if __name__ == "__main__":

    def list_of_primes(n):
        '''Return list indicating primes from 1 to n'''
        # sieve of Eratosthenes
        a = [True for i in range(n + 1)]

        for i in range(2, int(n**0.5) + 1):
            if a[i]:
                for j in range(i**2, n + 1, i):
                    a[j] = False
        return a

    # MAGIC NUMBER ALERT
    primes = list_of_primes(110000)
    # Remove 0 and 1, not counted by prompt
    primes = primes[2:]

    count = 0
    # The Nth prime to find
    target = 10001
    for i, elem in enumerate(primes):
        if elem is True:
            count += 1
        if count == target:
            print(f"The {target}-th prime: {i + 2}")
            sys.exit()