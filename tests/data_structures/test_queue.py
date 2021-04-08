"""Tests for algorithms/data_structures/collections/queue.py"""

from algorithms.data_structures.collections.queue import Queue


class TestQueue:

    a = Queue(5, "brian", 24, "holy grail", "john cleese", "spam", "circus")

    def test_size(self):
        assert self.a.size() == 7

    def test_isEmpty(self):
        assert self.a.isEmpty() is False

    def test_enqueue(self):
        self.a.enqueue("ni")
        assert self.a.head.data == "ni"

    def test_dequeue(self):
        popped = self.a.dequeue()
        popped.data == "circus"
        assert self.test_size
