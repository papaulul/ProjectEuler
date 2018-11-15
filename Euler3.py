"""
The prime factors of 13195 are 5, 7, 13, and 29.
What is the largest prime factor of the number 600851475143?
"""


def check_prime(small):
    for nn in range(2, small):
        if small % nn == 0:
            return False
    return True


n = 600851475143

primes = []
for i in range(2, 13195000):
    if n % i == 0:
        if check_prime(i):
            primes.append(i)

print(primes)