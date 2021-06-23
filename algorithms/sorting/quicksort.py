"""Concise implementation of QuickSort, however it violates the space complexity
since this version appends to new lists during the partitioning. QuickSort should
do in-place paritioning."""


def quicksort(a):
    if len(a) < 2:
        return a
    else:
        pivot, *rest = a
        left, right = [], []
        for each in rest:
            (left if each <= pivot else right).append(each)

        return quicksort(list(left)) + [pivot] + quicksort(list(right))
