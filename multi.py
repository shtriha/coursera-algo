"""Multiply

Usage:
    multiply.py <x> <y>

"""

from docopt import docopt


def num_len(x, cnt=1):
    if x > 10:
        cnt += 1
        return num_len(x/10, cnt)
    return cnt


def multiply(v1, v2, n):
    if n < 2:
        return v1*v2

    div = 10**n
    a = v1 // div
    c = v2 // div
    b = v1 % div
    d = v2 % div
    ac = multiply(a, c, n//2)
    bd = multiply(b, d, n//2)
    abc = multiply(a + b, c + d, n//2)
    return 10**(2*n)*ac + 10**n*(abc - ac - bd) + bd


if __name__ == '__main__':
    arguments = docopt(__doc__, version='1.0')
    x, y = int(arguments['<x>']), int(arguments['<y>'])
    n = max(num_len(x), num_len(y))
    x = 3141592653589793238462643383279502884197169399375105820974944592
    y = 2718281828459045235360287471352662497757247093699959574966967627
    result = multiply(x, y, n)
    print(result)
    print(x*y == result)
