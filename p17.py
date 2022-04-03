#!/usr/bin/env python3
"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens.
For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters.
The use of "and" when writing out numbers is in compliance with British usage.
"""
import sys

words = '''one,two,three,four,five,six,seven,eight,nine,ten,eleven,twelve,thirteen,fourteen,fifteen,sixteen,seventeen,eighteen,nineteen,twenty'''.split(
    ',')
more_words = '''thirty,forty,fifty,sixty,seventy,eighty,nintey,hundred,and,thousand'''.split(
    ',')
key_list = [30, 40, 50, 60, 70, 80, 90, 'hundred', 'and', 'thousand']

if __name__ == "__main__":
    # Make a lookup table for numbers and their word length
    letter_counts = {i + 1: len(word) for i, word in enumerate(words)}
    more_letter_counts = {
        key: len(word)
        for word, key in zip(more_words, key_list)
    }
    all_letter_counts = letter_counts | more_letter_counts

    curr_hun_digit = 0
    cnt = 0
    limit = 1000
    for i in range(1, limit):
        # peel off the optional hundreds digit
        n = i % 100
        if n == 0:
            # Just hit a new hundreds level. Add text count and move on
            curr_hun_digit += 1
            cnt += all_letter_counts[curr_hun_digit] + all_letter_counts[
                'hundred']
            continue
        if curr_hun_digit:
            # Add the boilerplate '<curr_hun_digit> hundred and' word count
            cnt += all_letter_counts[curr_hun_digit] + all_letter_counts[
                'hundred'] + all_letter_counts['and']
        # Uniquely named numbers
        if 1 <= n <= 19 or n % 10 == 0:
            cnt += all_letter_counts[n]
        else:
            # Peel of the digits and add the appropriate word count
            ones_digit = n % 10
            tens_digit = n // 10
            cnt += all_letter_counts[tens_digit *
                                     10] + all_letter_counts[ones_digit]

    # Dont forget the text for 1000!
    cnt += all_letter_counts[1] + all_letter_counts['thousand']
    print(f"Number of letters for 1 - {limit} written in words: {cnt}")