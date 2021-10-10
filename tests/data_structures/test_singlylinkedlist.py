"""Tests for linkedlist implementations."""

import unittest

from algorithms.data_structures.collections.singly_linked_list import SinglyLinkedList


class TestSinglyLinkedList(unittest.TestCase):
    def setUp(self):
        self.arr = SinglyLinkedList(14, "a", 65.7, "golf")

    def test_isEmpty(self):
        self.assertFalse(self.arr.isEmpty())

    def test_prepend(self):
        self.arr.prepend("abba")
        self.assertEqual(self.arr.head.data, "abba")

    def test_append(self):
        self.arr.append("papa")
        self.assertEqual(self.arr.tail.data, "papa")

    def test_pop_first(self):
        res = self.arr.pop_first()
        self.assertEqual(res.data, 14)
        self.assertEqual(self.arr.head.data, "a")

    def test_remove(self):
        self.arr.remove("golf")
        self.assertEqual(self.arr.remove("golf"), "Not Found")

    def test_index(self):
        self.assertEqual(self.arr.index("a"), 1)
        self.assertEqual(self.arr.index("golf"), 3)
