"""Tests for algorithms/data_structures/stack.py"""

from algorithms.data_structures.collections.stack import Stack


class TestStack:

    a = Stack(5, "brian", 24, "holy grail", "john cleese", "spam", "circus")

    def test_peek(self):
        assert self.a.peek() == "circus"

    def test_size(self):
        assert self.a.size() == 7

    def test_push(self):
        self.a.push("rabbit")
        assert self.a.peek() == "rabbit"

    def test_pop(self):
        assert self.a.pop() == "rabbit"
        self.test_size()

    def test_isEmpty(self):
        assert self.a.isEmpty() is False
