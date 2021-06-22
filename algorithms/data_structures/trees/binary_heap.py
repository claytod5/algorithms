"""Implementation of a Binary Heap in Python."""


class BinaryHeap:
    def __init__(self):
        self.heap_list = [0]  # this zero is not used; it is there for integer division
        self.current_size = 0

    def _perc_up(self, i):
        """Percolate a node up the tree."""
        while i // 2 > 0:
            parent = i // 2

            if self.heap_list[i] < self.heap_list[parent]:
                # tmp = self.heap_list[parent]
                self.heap_list[parent], self.heap_list[i] = (
                    self.heap_list[i],
                    self.heap_list[parent],
                )
            i = parent

    def _perc_down(self, i):
        while (i * 2) <= self.current_size:
            mc = self._min_child(i)
            if self.heap_list[i] > self.heap_list[mc]:
                self.heap_list[i], self.heap_list[mc] = (
                    self.heap_list[mc],  # swap
                    self.heap_list[i],
                )
            i = mc

    def _min_child(self, i):
        right_child_idx = (i * 2) + 1
        left_child_idx = i * 2  # because heap_list is not zero-indexed, these are the
        # formulas for left and right children
        if right_child_idx > self.current_size:
            return left_child_idx
        else:
            if self.heap_list[left_child_idx] < self.heap_list[right_child_idx]:
                return left_child_idx
            else:
                return right_child_idx

    def insert(self, k):
        """Add a new item to the heap."""
        self.heap_list.append(k)
        self.current_size = self.current_size + 1
        self._perc_up(self.current_size)

    def find_min(self):
        """Return the item with the minimum key value, leaving item in the heap."""
        pass

    def pop_min(self):
        """Return the item with the minimum keyvalue, removing \
        the item from the heap."""
        ret_val = self.heap_list[1]
        self.heap_list[1] = self.heap_list[self.current_size]
        self.current_size = self.current_size - 1
        self.heap_list.pop()
        self._perc_down(1)
        return ret_val

    def isEmpty(self):
        """Return true if the heap is empty, false otherwise."""
        pass

    def size(self):
        """Return the number of items in the heap."""
        pass

    def build_heap(self, items):
        """Build a new heap from a list of keys (a.k.a. heapify)."""
        i = len(items) // 2
        self.current_size = len(items)
        self.heap_list = [0] + items[:]
        while (i > 0):
            self._perc_down(i)
            i -= 1

    def print_tree(self):
        """Print string prepresentation of the tree."""
        root = self.heap_list[1]
        heap = [str(each) for each in self.heap_list[2:]]  # get nodes as strings
        spaces = len(heap) * 4
        tree = str(root).center(spaces * 2) + "\n\n"  # add root to tree, centered
        level = 1
        while len(heap) > 2 ** level:
            # since a complete binary heap's number of nodes per level is 2^l (where 'l'
            # is the level), we can print each level out according to that calculation
            r = 2 ** level
            tmp = [each.center(spaces) for each in heap[:r]]
            tree += "".join(tmp)
            tree += "\n\n"
            level += 1
            spaces = spaces // 2
            heap = heap[r:]  # reset heap, only including nodes beyond current level

        # if 2^l was greater than the number of nodes left in the tree, concat tree and
        # the leftover nodes
        return tree + "".join([each.center(spaces) for each in heap])


if __name__ == "__main__":
    b = BinaryHeap()
    b.insert(5)
    b.insert(9)
    b.insert(11)
    b.insert(14)
    b.insert(18)
    b.insert(19)
    b.insert(21)
    b.insert(33)
    b.insert(17)
    b.insert(27)
    b.pop_min()
    b.pop_min()
    b.pop_min()
    print(b.print_tree())
