"""Tests for linkedlist implementations."""

import algorithms.data_structures.collections.linked_list.LinkedList


class TestLinkedList:
    
    a = LinkedList(14, 'a', 65.7, 'golf')

    def test_isEmpty(self):
        assert self.a.isEmpty() == False 

    def test_prepend(self):
        self.a.prepend('abba')
        assert self.a.head() == 'abba'

    def test_append(self):
        self.a.append('papa')
        assert self.a.tail() == 'papa'

    def test_pop(self):
        assert self.a.pop() == 'papa'

    
