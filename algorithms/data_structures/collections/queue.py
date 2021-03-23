"""Implementation of a Queue ADT in Python."""


class Queue:
    """Queue ADT.

    A queue is structured as an ordered collection of items which are added at
    one end, called the “rear,” and removed from the other end, called the “front.”
    Queues maintain a FIFO ordering property.
    """

    def __init__(self, *args):
        """Instantiate object."""
        self.items = [*args]

    def enqueue(self, item):
        """Add a new item to the rear of the queue.

        Note:
            Because this implementation uses a Python list, enqueue() takes log(n),
            whereas a proper implementation should be constant.
        """
        self.items.insert(0, item)

    def dequeue(self):
        """Remove the front item from the queue."""
        return self.items.pop()

    def size(self):
        """Return the number of items in the queue."""
        return len(self.items)

    def isEmpty(self):
        """Test to see whether the queue is empty."""
        if self.items:
            return False
        else:
            return True
