#! /usr/bin/env python

"""
Write two Python functions to find the minimum number in a list. The first
function should compare each number to every other number on the list. O(n2).
The second function should be linear O(n).
"""

import random


def on_2(lst):
    res = lst[0]

    for x in lst:
        is_smallest = True
        for y in lst:
            if x > y:
                is_smallest = False
        if is_smallest:
            res = x

    return res


def on_1(lst):
    res = lst[0]

    for x in lst:
        if x < res:
            res = x

    return res


if __name__ == "__main__":
    # test = [x for x in range(1, 10000)]
    test = [5, 1, 3, 2, 5]
    print(on_2(test))
    # print(on_1(test))
