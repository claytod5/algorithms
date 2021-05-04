#!/usr/bin/env python

"""Detect if a number is a prime or not.

Uses trial division between 2 and the square root of the input number. Also, eliminates
numbers divisible by 2 as part of search space to cut down on time.
"""


def is_prime(n):
    """Detect if a number is a prime or not.

    Args:
        num (int): A positive integer
    Returns:
        boolean
    """
    if n <= 1:
        return False
    elif n == 2:
        return True
    elif n > 2 and n % 2 == 0:
        return False
    else:
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True


if __name__ == "__main__":
    print(f"Is 2 prime: {is_prime(2)}")
    print(f"Is 4 prime: {is_prime(4)}")
    print(f"Is 7 prime: {is_prime(7)}")
    print(f"Is 10290281 prime: {is_prime(10290281)}")
