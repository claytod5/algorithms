"""Implementation of a Queue ADT in Python."""

from algorithms.data_structures.collections.doubly_linked_list import DoublyLinkedList


class Queue(DoublyLinkedList):
    """Queue ADT.

    A queue is structured as an ordered collection of items which are added at
    one end, called the “rear,” and removed from the other end, called the “front.”
    Queues maintain a FIFO ordering property.
    """

    def enqueue(self, item):
        """Add a new item to the rear of the queue."""
        DoublyLinkedList.prepend(self, item)

    def dequeue(self):
        """Remove the front item from the queue."""
        return DoublyLinkedList.pop(self)

    def size(self):
        """Return the number of items in the queue."""
        return self.index(self.tail.data) + 1

    def isEmpty(self):
        """Test to see whether the queue is empty."""
        return DoublyLinkedList.isEmpty(self)
