# The following iterative sequence is defined for the set of positive integers:
#
# n → n/2 (n is even)
# n → 3n + 1 (n is odd)
#
# Using the rule above and starting with 13, we generate the following sequence:
#
# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains
#10 terms. Although it has not been proved yet (Collatz Problem), it is thought
#that all starting numbers finish at 1.
#
# Which starting number, under one million, produces the longest chain?
#
# NOTE: Once the chain starts the terms are allowed to go above one million.


def check_even(n):
    if n % 2 == 0:
        return True
    else:
        return False
def if_even(n):
    return n/2

def if_odd(n):
    return 3*n+1

def game(n):
    counter = 0
    while n!= 1:
        if check_even(n):
            n = if_even(n)
        else:
            n = if_odd(n)
        counter+=1
    return counter

L = 0
for i in range(1000000,500000,-1):
    if game(i) > L:
        L = game(i)
        answer = i
print(L,answer)
