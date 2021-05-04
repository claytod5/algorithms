"""Implementation of a doubly linked-list in Python."""

from algorithms.data_structures.collections.singly_linked_list import SinglyLinkedList
from algorithms.data_structures.node import DoublyLinkedNode


class DoublyLinkedList(SinglyLinkedList):
    def append(self, item):
        temp = DoublyLinkedNode(item)
        if self.tail is None:
            self.head = temp
            self.tail = temp
        else:
            temp.prev = self.tail
            self.tail.next = temp
            self.tail = temp

    def prepend(self, item):
        temp = DoublyLinkedNode(item)
        self.head.prev = temp
        temp.next = self.head
        self.head = temp

    def popFirst(self):
        head = self.head
        self.head = self.head.next
        self.head.prev = None
        head.next = None
        return head

    def pop(self):
        tail = self.tail
        self.tail = tail.prev
        self.tail.next = None
        tail.prev = None
        return tail

    def remove(self, item):
        res = self._search(item)
        if res is not None:
            prev, curr = res
            prev.next = curr.next
            curr.next.prev = prev
        else:
            return "Not Found"


if __name__ == "__main__":
    a = DoublyLinkedList("a", "b", "c", "d", "e", "f", "g", "h", "i")
    print(a)
    print(a.popFirst())
    print(a)
    print(a.pop())
    print(a)
    print(a.remove("f"))
    print(a.head)
    print(a.tail)
