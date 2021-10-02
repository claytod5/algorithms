#!/usr/bin/env python

"""Various algorithms concerning primes."""


def is_prime(n):
    """Detect if a number is a prime or not (robust method).

    :param num: A positive number
    :type num: int

    :returns: boolean
    :rtype: bool
    """
    if n <= 1:
        return False
    elif n == 2:
        return True
    elif n > 2 and n % 2 == 0:
        return False
    else:
        for i in range(3, int(pow(n, 0.5)) + 1, 2):
            if n % i == 0:
                return False
        return True


def quick_prime(n):
    """Return if a number is prime or not (easy to remember method)

    This method isn't as robust as is_prime(), but it is easier to
    remember.
    """
    # we only need to check up to square root of n
    if n <= 1:
        return False
    else:
        for i in range(2, int(pow(n, 0.5)) + 1):
            if n % i == 0:
                return False
        return True


def prime_factors(n):
    """Find the prime factors of a number

    :param n: A number
    :type n: int

    :returns: Prime factors of n
    :rtype: list
    """
    prime = True
    for i in range(2, int(pow(n, 0.5)) + 1):
        if n % i == 0:
            prime = False
            return prime_factors(i) + prime_factors(n // i)
    if prime:
        return [n]


def unique_prime_factors(n):
    """Return the unique prime factors of a number

    :param n: A number
    :type n: int

    :returns: Prime factors of n
    :rtype: set
    """
    stack = [n]
    res = set()
    while stack:
        j = stack.pop()
        prime = True
        if j not in res:
            for i in range(2, int(pow(j, 0.5)) + 1):
                if j % i == 0:
                    prime = False
                    stack.append(i)
                    stack.append(j // i)
            if prime:
                res.add(j)
    return res
