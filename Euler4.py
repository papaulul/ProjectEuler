"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is
9009 = 91 x 91

Find the largest palindrome made from the product of two 3-digit numbers
"""


def is_pali(num):
    tostr = len(str(num))
    check = list(str(num))
    if tostr % 2 == 1:
        middle = (tostr+1)/2-1
        check.pop(int(middle))
    return is_pali2(check)


def is_pali2(list):
    for i in range(0,len(list)-1):
        if list[i] != list[len(list)-1-i]:
            return False
    return True


all_pali = []

for n in range(999, 100, -1):
    for i in range(999, 100, -1):
        if is_pali(n*i):
            all_pali.append(n*i)
            break

print(max(all_pali))
