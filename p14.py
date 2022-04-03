#!/usr/bin/env python3
"""
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.

TODO: Kinda slow. Not optimized?
"""

import sys

if __name__ == "__main__":
    '''
    THOUGHTS: Once a Collatz sequence is known, it is the same forever. Large sequences will eventually hit sub-sequences already discovered.
    Save discovered sequences to a dictionary and reference them when needed e.g.:
                sequences = {
                    '13': '10'
                }
        Says that the Collatz sequence for the number '13' has length of '10', meaning it has 10 terms.
    '''
    limit = 1000000
    sequences = dict()

    def add_collatz_length(n):
        if n == 0:
            return 0
        cnt = 1
        curr = n
        while curr != 1:
            if curr in sequences:
                sequences[n] = sequences[curr] + cnt - 1
                return sequences[n]
            if curr % 2 == 0:
                curr //= 2
            else:
                curr = 3 * curr + 1
            cnt += 1
        sequences[n] = cnt
        return cnt

    for i in range(limit, 1, -1):
        add_collatz_length(i)

    print(
        f"Starting number under {limit} with longest chain: {max(sequences, key=sequences.get)}"
    )
