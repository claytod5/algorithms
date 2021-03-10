#!/usr/bin/env python

"""Tests for algorithms in main directory of algorithms package."""

import pytest
import pytest_mock

from algorithms.fibonacci import fibonacci


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
