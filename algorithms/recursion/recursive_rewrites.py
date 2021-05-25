#!/usr/bin/env python

"""Rewriting some common functions with recursion."""


def recursive_sum(a):
    if len(a) == 1:
        return a[0]
    else:
        return a[0] + recursive_sum(a[1:])


def recursive_count(a):
    if len(a) == 0:
        return 0
    else:
        return recursive_count(a[1:]) + 1


def recursive_max(a):
    if len(a) == 1:
        return a
    elif a[1] >= a[0]:
        return recursive_max(a[1:])
    else:
        return recursive_max(a[:1] + a[2:])


def reverse_str(string):
    """
    Base case: length of string
    Modification: str slice
    """

    if len(string) == 1:
        return string

    return reverse_str(string[1:]) + string[0]
