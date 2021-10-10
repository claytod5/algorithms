import unittest

from algorithms.data_structures.collections.doubly_linked_list import DoublyLinkedList


class Test_DoublyLinkedList(unittest.TestCase):
    def setUp(self):
        self.arr = DoublyLinkedList(1, "a", 124.4, "golf")

    def test_append(self):
        self.arr.append("b")
        self.assertEqual(self.arr.tail.data, "b")

    def test_prepend(self):
        self.arr.prepend(25)
        self.assertEqual(self.arr.head.data, 25)

    def test_popleft(self):
        res = self.arr.popleft()
        self.assertEqual(res.data, 1)
        self.assertNotEqual(self.arr.head.data, 1)

    def test_pop(self):
        res = self.arr.pop()
        self.assertEqual(res.data, "golf")
        self.assertNotEqual(self.arr.tail.data, "golf")

    def remove(self):
        self.arr.remove(124.4)
        self.assertEqual(self.arr.remove(124.4), "Not Found")
