"""Implementation of a Queue ADT in Python."""

from algorithms.data_structures.collections.doubly_linked_list import DoublyLinkedList


class Queue(DoublyLinkedList):
    """Queue ADT.

    A queue is structured as an ordered collection of items which are added at
    one end, called the “rear,” and removed from the other end, called the “front.”
    Queues maintain a FIFO ordering property.
    """

    def enqueue(self, item):
        """Add a new item to the rear of the queue.

        Note:
            Because this implementation uses a Python list, enqueue() takes log(n),
            whereas a proper implementation should be constant.
        """
        # self.items.insert(0, item)
        DoublyLinkedList.prepend(item)

    def dequeue(self):
        """Remove the front item from the queue."""
        # return self.items.pop()
        DoublyLinkedList.pop()

    def size(self):
        """Return the number of items in the queue."""
        # return len(self.items)
        pass

    def isEmpty(self):
        """Test to see whether the queue is empty."""
        # if self.items:
        #     return False
        # else:
        #     return True
        DoublyLinkedList.isEmpty()
