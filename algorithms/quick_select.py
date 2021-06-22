#!/usr/bin/env python

"""Python implementation of QuickSelect algorithm.

Allows for finding of kth smallest element in O(n) time. Assumes that each item is
distinct and data is unsorted.
"""
from random import randint
from timeit import Timer

from algorithms.sorting.quicksort import quicksort
from algorithms.sorting.selection_sort import selection_sort


def quick_select(a, k):
    pivot = a[0]
    left = [each for each in a[1:] if each <= pivot]
    right = [each for each in a[1:] if each > pivot]
    a = left + [pivot] + right
    index = len(left)

    if index == k - 1:
        return a[index]
    elif index > k - 1:
        return quick_select(left, k)
    else:
        return quick_select(right, k - (index + 1))


if __name__ == "__main__":
    a = [randint(1, 1000) for i in range(1, 10000)]

    t1 = Timer("quick_select(a, 63)", "from __main__ import a, quick_select")
    print("quick_select(a, 63): ", t1.timeit(number=1), "milliseconds")

    t2 = Timer("quicksort(a)[63]", "from __main__ import a, quicksort")
    print("quicksort(a): ", t2.timeit(number=1), "milliseconds")

    t3 = Timer("selection_sort(a)[63]", "from __main__ import a, selection_sort")
    print("selection_sort(a)[63]: ", t3.timeit(number=1), "milliseconds")
