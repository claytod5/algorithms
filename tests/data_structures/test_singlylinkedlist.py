"""Tests for linkedlist implementations."""

import pytest

from algorithms.data_structures.collections.singly_linked_list import SinglyLinkedList


@pytest.fixture()
def a_list(request):
    request.cls.a = SinglyLinkedList(14, "a", 65.7, "golf")
    yield


@pytest.mark.usefixtures("a_list")
class TestSinglyLinkedList:
    def test_isEmpty(self):
        assert not self.a.isEmpty()

    def test_prepend(self):
        self.a.prepend("abba")
        assert self.a.head.data == "abba"

    def test_append(self):
        self.a.append("papa")
        assert self.a.tail.data == "papa"

    def test_pop_first(self):
        res = self.a.pop_first()
        assert res.data == 14
        assert self.a.head.data == "a"

    def test_remove(self):
        self.a.remove("golf")
        assert self.a.remove("golf") == "Not Found"

    def test_index(self):
        assert self.a.index("a") == 1
        assert self.a.index("golf") == 3
