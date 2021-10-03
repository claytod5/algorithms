#!/usr/bin/env python

"""Tests for algorithms in main directory of algorithms package."""

import unittest

from algorithms.binary_search import binary_search
from algorithms.dynamic_programming.fibonacci import fib_iter, fibonacci
from algorithms.is_prime import (
    is_prime,
    prime_factors,
    quick_prime,
    unique_prime_factors,
)


class TestFibonacci(unittest.TestCase):

    test_cases = [
        (10, 55),
        (54, 86267571272),
        (0, 0),
        (1, 1),
        (2, 1),
        (7, 13),
        (165, 13598018856492162040239554477268290),
    ]

    def test_fibonacci_generate(self):
        for i in self.test_cases:
            with self.subTest():
                self.assertEqual(fibonacci(i[0]), i[1])
                self.assertEqual(fib_iter(i[0]), i[1])


class TestBinarySearch(unittest.TestCase):

    test_array = [each for each in range(13, 1000000, 3)]
    test_cases = [
        (0, None),
        (13, 0),
        (736, 241),
        (712318, 237435),
        (532552, 177513),
        (296332, 98773),
    ]

    def test_binary_search(self):
        for i in self.test_cases:
            with self.subTest():
                self.assertEqual(binary_search(self.test_array, i[0]), i[1])


class TestPrimeDetectFunctions(unittest.TestCase):

    true_cases = [2, 7, 10290281]
    false_cases = [0, 1, 4, 10]

    def test_prime_checkers(self):
        for each in self.true_cases:
            with self.subTest():
                self.assertTrue(is_prime(each))
                self.assertTrue(quick_prime(each))

        for each in self.false_cases:
            with self.subTest():
                self.assertFalse(is_prime(each))
                self.assertFalse(quick_prime(each))


class TestPrimeFactorFunctions(unittest.TestCase):

    # prime_factors returns a list, so i[1] is that result
    # unique_prime_factors returns a set, so i[2] handles that
    test_cases = [
        (0, [0], {0}),
        (1, [1], {1}),
        (2, [2], {2}),
        (7, [7], {7}),
        (13, [13], {13}),
        (24, [2, 2, 2, 3], {2, 3}),
        (56, [2, 2, 2, 7], {2, 7}),
        (324, [2, 2, 3, 3, 3, 3], {2, 3}),
        (764, [2, 2, 191], {2, 191}),
        (10788, [2, 2, 3, 29, 31], {2, 3, 29, 31}),
    ]

    def test_prime_factors(self):
        for i in self.test_cases:
            with self.subTest():
                self.assertEqual(prime_factors(i[0]), i[1])
                self.assertEqual(unique_prime_factors(i[0]), i[2])


if __name__ == "__main__":
    unittest.main()
