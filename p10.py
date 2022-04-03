#!/usr/bin/env python3
"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
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

    N = 2000000

    primes = list_of_primes(N)
    primes = primes[2:]

    count = 0
    for i, elem in enumerate(primes):
        if elem is True:
            count += i + 2
    print(f"Sum of all primes below {N}: {count}")