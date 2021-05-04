"""Tests for sort algorithms."""


import random

import pytest

from algorithms.sorting.selection_sort import selection_sort


@pytest.fixture
def random_list():
    rand = [random.randint(0, 50) for i in range(0, 100)]  # a list of random ints
    pysorted = sorted(rand)  # a sorted copy of rand, done with python's built-in
    return rand, pysorted


def test_selection_sort(random_list):
    selection_sort(random_list[0])
    assert random_list[0] == random_list[1]  # does selection_sort(rand) == pysorted ?
