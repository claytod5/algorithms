#!/usr/bin/env python

from timeit import Timer


def binary_search(a, x):
    """Find index of x in a in logarithmic time."""
    low = 0
    high = len(a) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = a[mid]

        if guess == x:
            return mid
        elif guess < x:
            low = mid + 1
        else:
            high = mid - 1

    return None


def simple_search(a, x):
    """Implement simple search to compare time complexity with binary_search."""
    for i, each in enumerate(a):
        if each == x:
            return i
    else:
        return None


if __name__ == "__main__":
    test = [each for each in range(0, 100000000)]

    t1 = Timer("binary_search(test, 624)", "from __main__ import test, binary_search")
    print("binary_search(test, 96240000): ", t1.timeit(number=1000), "milliseconds")

    t2 = Timer("simple_search(test, 624)", "from __main__ import test, simple_search")
    print("simple_search(test, 96240000): ", t2.timeit(number=1000), "milliseconds")
