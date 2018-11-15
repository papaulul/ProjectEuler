"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13
"""


def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

m = []
count = 2

while len(m) != 10001:
    if is_prime(count):
        m.append(count)
    count += 1

print(max(m))
