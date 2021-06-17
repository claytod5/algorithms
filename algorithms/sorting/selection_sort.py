"""Implementation of Selection sort algorithm in Python.

Running time: O(n**2)
"""


def selection_sort(a_list):
    for i in range(len(a_list)):
        min_idx = len(a_list) - 1
        for j in range(i, len(a_list)):
            if a_list[j] < a_list[min_idx]:
                min_idx = j
        if min_idx != i:
            a_list[min_idx], a_list[i] = a_list[i], a_list[min_idx]
