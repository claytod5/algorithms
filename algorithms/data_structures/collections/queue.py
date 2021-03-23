"""Queue: implementation of Queue ADT as a Python list"""


class Queue:
    def __init__(self, *items):
        self.items = [*items]

    def isEmpty(self):
        if self.items:
            return False
        else:
            return True

    def size(self):
        return len(self.items)

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()
