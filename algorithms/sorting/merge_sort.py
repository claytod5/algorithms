"""Python implementation of merge sort."""

from random import randrange
from timeit import Timer


def merge_sort(a_list):
    """Sort list using merge_sort algorithm.

    :param a_list: list of items
    :param a: starting index of a_list
    :param b: ending index of a_list

    :returns: sorted list

    """
    if len(a_list) > 1:

        mid = len(a_list) // 2

        left_half = a_list[:mid]
        right_half = a_list[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i, j, k = 0, 0, 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] <= right_half[i]:
                a_list[k] = left_half[i]
                i = i + 1
            else:
                a_list[k] = right_half[j]
                j = j + 1
            k = k + 1

        while i < len(left_half):
            a_list[k] = left_half[i]
            i = i + 1
            k = k + 1

        while j < len(right_half):
            a_list[k] = right_half[j]
            j = j + 1
            k = k + 1


if __name__ == "__main__":
    test_list = [randrange(0, 1000) for each in range(0, 1000)]
    t1 = Timer(
        "merge_sort(test_list)",
        "from __main__ import merge_sort, test_list",
    )
    print("merge_sort(test_list): ", t1.timeit(number=1), "milliseconds")
    # t2 = Timer("test_list.sort()", "from __main__ import test_list")
    # print("test_list.sort(): ", t2.timeit(number=1000), "milliseconds")
    # merge_sort(test_list)
    # print(test_list)
