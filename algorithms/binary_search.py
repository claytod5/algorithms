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
    a = [1, 8, 3, 2, 0, 4, 3, 5, 6].sort()
    print(binary_search(a, 4))
