#!/usr/bin/env python


def binary_search(a, x):
    idx = None
    mid = len(a) // 2
    while idx is None:
        if x > a[mid]:
            mid = len(a[mid:]) // 2
        elif x < a[mid]:
            mid = len(a[:mid]) // 2
        else:
            idx = mid
    return mid


if __name__ == "__main__":
    test = [1, 2, 3, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15]
    print(binary_search(test, 13))
