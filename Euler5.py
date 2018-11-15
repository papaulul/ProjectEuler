"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

what is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20
"""


def by_twenty(number):
    for i in range(1, 21):
        if number % i != 0:
            return False
    return True


start = 116396280 * 16


for n in range(10, start, 10):
    if by_twenty(n):
        print(n)
        break

