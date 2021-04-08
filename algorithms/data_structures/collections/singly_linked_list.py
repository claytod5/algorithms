"""Implementation of a singly linked-list in Python."""

from algorithms.data_structures.node import Node


class SinglyLinkedList:

    """Docstring for LinkedList. """

    def __init__(self, *items):
        """Constructor method."""
        if items:
            self.tail = None
            for each in items:
                self.append(each)
        else:
            self.head = None
            self.tail = None

    def isEmpty(self):
        if self.head is None:
            return True
        else:
            return False

    def prepend(self, item):
        temp = Node(item)
        temp.next = self.head
        self.head = temp

    def append(self, item):
        temp = Node(item)
        if self.tail is None:
            self.head = temp
            self.tail = temp
        else:
            self.tail.next = temp
            self.tail = temp

    def popFirst(self):
        head = self.head
        self.head = self.head.next
        head.next = None
        return head

    def _search(self, item):
        previous = None
        current = self.head

        while current.next is not None:
            if current.data == item:
                return previous, current
            else:
                previous = current
                current = current.next
        else:
            return None

    def remove(self, item):
        res = self._search(item)
        if res is not None:
            prev, curr = res
            prev.next = curr.next
        else:
            return "Not Found"

    def index(self, item):
        node = self.head
        counter = 0

        while node is not None:
            if node.data == item:
                return counter
            else:
                counter += 1
                node = node.next

    def __str__(self):
        node = self.head
        out = []

        while node is not None:
            out.append(node.data)
            node = node.next

        return " -> ".join(out)


if __name__ == "__main__":
    a = SinglyLinkedList("a", "b", "c", "d", "e", "f", "g", "h", "i")
    print(a)
    # print(a.popFirst())
    # print(a)
    # print(a.pop())
    print(a.remove("z"))
    print(a)
    # input()
