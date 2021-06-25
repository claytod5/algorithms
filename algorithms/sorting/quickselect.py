#!/usr/bin/env python

"""Python implementation of QuickSelect algorithm.

Allows for finding of kth smallest element in O(n) time. Assumes that each item is
distinct and data is unsorted.
"""
from quicksort import lomuto_partition as partition


def pyselect(a, k):
    """Concise implementation of QuickSelect. Violates the space complexity
    because it does not partition in-place."""
    pivot, *rest = a
    left, right = [], []
    for each in rest:
        (left if each <= pivot else right).append(each)

    index = len(left)

    if index == k - 1:
        return pivot
    elif index > k - 1:
        return pyselect(left, k)
    else:
        return pyselect(right, k - (index + 1))


def quickselect(a, k, low, high):
    if low == high:
        return a[low]

    index = partition(a, low, high)

    if index == k - 1:
        return a[index]
    if index < k - 1:
        return quickselect(a, k, index, high)
    else:
        return quickselect(a, k, low, index - 1)


if __name__ == "__main__":
    a = [8, 123, 67, 1, 3, 2, 9, 1083, 313]
    print(quickselect(a, 5, 0, len(a) - 1))
    print(sorted(a)[5 - 1])
