fiblist = [0,1]
def fib(n):
    if n< 0:
        print('no')
    elif n <= len(fiblist):
        return fiblist[n-1]
    else:
        f = fib(n-1) + fib(n-2)
        fiblist.append(f)
        return f

print(fib(100))
