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


def fib_iter(n):
    if n < 2:
        return n
    else:
        a = 0
        b = 1
        for _ in range(n - 1):
            a, b = b, a + b
        return b


def fib_identify(n):
    a = 5 * (n ** 2)
    plus = a + 4
    minus = a - 4
    plus_chk = int((plus ** 0.5)) ** 2
    minus_chk = int((minus ** 0.5)) ** 2
    if plus_chk == plus or minus_chk == minus:
        return True
    else:
        return False


if __name__ == "__main__":
    print(fib_identify(787))
