"""Tests for sort algorithms."""


import random
import unittest

from algorithms.sorting.insertion_sort import insertion_sort
from algorithms.sorting.merge_sort import merge_sort
from algorithms.sorting.quicksort import pysort, quicksort
from algorithms.sorting.selection_sort import selection_sort


class TestSortingAlgorithms(unittest.TestCase):
    def setUp(self):
        self.rand1 = [
            random.randint(0, 50) for _ in range(0, 10)
        ]  # a list of random ints
        self.rand2 = self.rand1.copy()

    def test_selection_sort(self):
        selection_sort(self.rand1)
        self.rand2.sort()
        self.assertEqual(self.rand1, self.rand2)

    def test_insertion_sort(self):
        insertion_sort(self.rand1)
        self.rand2.sort()
        self.assertEqual(self.rand1, self.rand2)

    def test_quicksort(self):
        quicksort(self.rand1, 0, len(self.rand1) - 1)
        self.rand2.sort()
        self.assertEqual(self.rand1, self.rand2)

    def test_pysort(self):
        self.assertEqual(pysort(self.rand1), sorted(self.rand2))

    @unittest.expectedFailure
    def test_merge_sort(self):
        merge_sort(self.rand1)
        self.rand2.sort()
        self.assertEqual(self.rand1, self.rand2)


if __name__ == "__main__":
    unittest.main()
