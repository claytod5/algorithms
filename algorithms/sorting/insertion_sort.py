#!/usr/bin/env python


def insertion_sort(a):
    for i in range(len(a)):
        current = a[i]
        j = i - 1

        while j >= 0 and a[j] > current:
            a[j + 1] = a[j]
            j -= 1

        a[j + 1] = current


if __name__ == "__main__":
    a = [9, 3, 1, 4, 2, 15]
    insertion_sort(a)
    print(a)
