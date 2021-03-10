"""Stack ADT implemented using a list."""


class Stack:
    def __init__(self, *items):
        self.items = [*items]

    def peek(self):
        return self.items[-1]

    def push(self, i):
        self.items.append(i)

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def isEmpty(self):
        if len(self.items) == 0:
            return True
        else:
            return False
