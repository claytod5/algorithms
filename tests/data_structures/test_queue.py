<<<<<<< HEAD
"""Tests for queue.py"""
=======
"""Tests for algorithms/data_structures/queue.py"""
>>>>>>> 542da92e6a305d13a939d219906dda66fb39d6fc

from algorithms.data_structures.collections.queue import Queue


<<<<<<< HEAD
class TestQueue:

    a = Queue(5, "brian", 24, "holy grail", "john cleese", "spam", "circus")

    def test_size(self):
        assert self.a.size() == 7

    def test_isEmpty(self):
        assert self.a.isEmpty() is False

    def test_enqueue(self):
        self.a.enqueue("ni")
        assert self.a.items[0] == "ni"

    def test_dequeue(self):
        assert self.a.dequeue() == "circus"
        assert self.test_size
=======
class TestStack:

    a = Queue(5, "brian", 24, "holy grail", "john cleese", "spam", "circus")

    def test_isEmpty(self):
        assert self.a.isEmpty() is False

    def test_size(self):
        assert self.a.size() == 7

    def test_enqueue(self):
        self.a.enqueue("rabbit")
        assert self.a.items[0] == "rabbit"

    def test_dequeue(self):
        assert self.a.dequeue() == "circus"
        self.test_size()
>>>>>>> 542da92e6a305d13a939d219906dda66fb39d6fc
