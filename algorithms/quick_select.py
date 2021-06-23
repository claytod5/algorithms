#!/usr/bin/env python

"""Python implementation of QuickSelect algorithm.

Allows for finding of kth smallest element in O(n) time. Assumes that each item is
distinct and data is unsorted.
"""


def quick_select(a, k):
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
        return quick_select(left, k)
    else:
        return quick_select(right, k - (index + 1))
