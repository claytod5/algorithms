"""Fibonacci sequence algorithm with memoization via a decorator."""


def fibo_meme(func):
    """Return memoized results from func(n).

    Args:
        func: A function. Can be wrapped normally or using decorator syntax.

    Returns:
        memoize: a wrapped function that performs lookups in a dict
    """
    mem = {}

    def memoize(n):
        if n not in mem:
            mem[n] = func(n)

        return mem[n]

    return memoize


@fibo_meme
def fibonacci(n):
    """Return Fibonacci sequence of n.

    Args: 
        n (int): An integer

    Returns:
        sum of nth term in fibonacci
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
