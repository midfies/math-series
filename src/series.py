'''Fibonacci Series.'''


def fib(num):
    """Return fibonacci numbers based on n."""
    if num == 0:
        return 0
    elif num == 1:
        return num
    else:
        return fib(num - 1) + fib(num - 2)


def lucas(num):
    """Return lucas numbers based on n."""
    x = 2
    y = 1
    for i in range(num):
        temp = x
        x = y
        y += temp
    return x


def lucas_rec(num):
    """Recursive lucas."""
    if num == 0:
        return 2
    elif num == 1:
        return 1
    else:
        return lucas_rec(num - 1) + lucas_rec(num - 2)


def sum_series(num, x=0, y=1):
    '''Return a numbers based on 2 starting numbers in a string of numbers.'''
    if num == 0:
        return x
    elif num == 1:
        return y
    else:
        return sum_series(num - 1, x, y) + sum_series(num - 2, x, y)


if __name__ == "__main__":
    print('This module defines functions that implement mathematical series.')
    print('...')
    print('fib(n):')
    print('Returns the nth value in the fibonacci series')
    print('>>> fib(5)')
    print(fib(5))
    print('...')
    print('lucas_rec(n):')
    print('Returns the nth value in the lucas series')
    print('>>> lucas_rec(7)')
    print(lucas_rec(7))
    print('...')
    print('sum_series(n, x, y):')
    print('Returns the nth value in a series made with the optional x and y')
    print('>>> sum_series(5, 7, 12)')
    print(sum_series(5, 7, 12))
    print('...')
