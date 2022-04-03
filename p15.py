#!/usr/bin/env python3
"""
Starting in the top left corner of a 2x2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20x20 grid?

Thanks: https://en.wikipedia.org/wiki/Binomial_coefficient#Factorial_formula
"""
import sys
import math

if __name__ == "__main__":
    '''
    This question is basically asking "How many ways can you K items from N items?" aka Binomial coefficient

    For a 2x2 grid, 
                N = 4 because the 'bag' of items is 'RRDD'
                K = 2 because you have to do each unique move twice (you MUST have 2 'R' in your move)
    For a 7x7 grid,
                N = 14 b/c the 'bag' of items is 'RRRRRRRDDDDDDD'
                K = 7 b/c you have to do each unique move 7 times                
    '''
    fact = lambda x: math.factorial(x)

    grid_size = 20
    n = grid_size * 2

    num_paths_factorial = fact(n) // (fact(grid_size) * fact(n - grid_size))
    num_paths_comb = math.comb(n, grid_size)
    if num_paths_factorial == num_paths_comb:
        print(
            f"There are {num_paths_comb} possible paths in a {grid_size}x{grid_size} grid"
        )
