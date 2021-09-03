#!/usr/bin/env python

"""Tests for algorithms in main directory of algorithms package."""

import pytest

from algorithms.binary_search import binary_search
from algorithms.dynamic_programming.fibonacci import fibonacci
from algorithms.is_prime import is_prime


@pytest.mark.parametrize(
    "n, result",
    [
        (10, 55),
        (54, 86267571272),
        (0, 0),
        (1, 1),
        (2, 1),
        (7, 13),
        (165, 13598018856492162040239554477268290),
    ],
)
def test_fibonacci(n, result):
    assert fibonacci(n) == result


@pytest.mark.parametrize(
    "n, result",
    [
        (0, None),
        (13, 0),
        (736, 241),
        (712318, 237435),
        (532552, 177513),
        (296332, 98773),
    ],
)
def test_binary_search(n, result):
    a = [each for each in range(13, 1000000, 3)]
    assert binary_search(a, n) == result


@pytest.mark.parametrize(
    "n, result",
    [
        (0, False),
        (1, False),
        (2, True),
        (3, True),
        (4, False),
        (984, False),
        (10342, False),
        (12347, True),
    ],
)
def test_is_prime(n, result):
    assert is_prime(n) == result
