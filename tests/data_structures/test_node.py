"""Tests for node.py: A python implementation of a Node"""

from algorithms.data_structures.node import Node


class TestNode:

    a = Node("A")
    b = Node("B")
    a.next = b

    def test_node_data(self):
        assert self.a.data == "A"
        assert self.b.data == "B"

    def test_node_next(self):
        assert self.a.next == self.b
