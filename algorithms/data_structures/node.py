"""A thing that holds data and points to the next thing

This exists in the top of the directory since several data structures use the concept
of a Node (i.e. Linked Lists, Trees, Graphs)
"""


class Node:
    """A holder of data with a pointer to another Node.

    Attributes:
        data: An object to be held inside Node
        next (Node): A pointer to another Node object
    """

    def __init__(self, d):
        """Construct object."""
        self.data = d
        self.next = None

    def __str__(self):
        """Print user-friendly representation of object."""
        return self.data


class DoublyLinkedNode:
    """A holder of data with a pointer to both previous and next nodes.

    Attributes:
        data: An object to be held inside Node
        next (Node): A pointer to the next Node object
        prev (Node): A pointer to the previous Node object

    """

    def __init__(self, data):
        """Construct object."""
        self.data = data
        self.next = None
        self.prev = None

    def __str__(self):
        """Print user-friendly representation of object."""
        return self.data
