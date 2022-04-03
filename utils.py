import operator
from itertools import accumulate


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


def is_palindrome(n):
    a = list(str(n))
    b = list(reversed(a))
    return a == b


def is_divisble_by_range(n, span):
    for i in span:
        if n % i != 0:
            return False
    return True


def sum_squares(x):
    total = 0
    for i in range(x + 1):
        total += i**2
    return total


def square_sum(x):
    return sum(range(1, x + 1))**2


def list_of_primes(n):
    '''Return list indicating primes from 1 to n'''
    # sieve of Eratosthenes
    a = [True for i in range(n + 1)]

    for i in range(2, int(n**0.5) + 1):
        if a[i]:
            for j in range(i**2, n + 1, i):
                a[j] = False
    return a


def get_product(arr):
    arr = [int(char) for char in arr]
    return list(accumulate(arr, operator.mul))[-1]


def sliding_window_product(arr, window_length):
    '''Use the sliding window technique to calculate the greatest product of consecutive digits. Does not work if there are zeros'''
    curr_product = get_product(arr[0:window_length])
    max_product = curr_product
    for i in range(1, len(arr) - window_length + 1):
        curr_product /= int(arr[i - 1])
        curr_product *= int(arr[i + window_length - 1])
        max_product = max(max_product, curr_product)
    return max_product


def sliding_window_max_product(arr, window_length):
    '''Use the sliding window technique to calculate the greatest product of consecutive digits.
            Adapted from: https://www.geeksforgeeks.org/minimum-product-subarray-of-size-k-including-negative-integers/'''
    max_result = 0
    prod = 1
    zeros = 0
    k = window_length
    x = len(arr)
    for i in range(k):
        if (arr[i] == "0"):
            zeros += 1
        else:
            prod *= int(arr[i])

    if zeros == 0:
        res = prod
    else:
        res = 0

    for right in range(k, x):
        if arr[right] == "0":
            zeros += 1
        else:
            prod *= int(arr[right])

        if arr[right - k] == "0":
            zeros -= 1
        else:
            prod //= int(arr[right - k])

        if zeros == 0:
            res = max(res, prod)
            max_result = max(res, max_result)
        elif res > 0:
            res = 0

    return max_result
