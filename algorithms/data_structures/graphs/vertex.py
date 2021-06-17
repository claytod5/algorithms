class Vertex:
    """A node/vertex containing a key and data pertaining to edges.

    Attributes:
        id: The key that this vertex holds.
        connected_to (dict): A dictionary of vertex objects that this vertex has edges
            with. If weight is included as an argument to add_neighbor(), the weight is
            included as the value in the {key: value} pair.
        pred: Tracks which vertex is the predecessor of the current vertex.
        distance (int): Represents the cost of a path from the starting node. Infinity
        by default
        visited: Tracks whether or not this node has already been visited in a search
            algorithm.
    """

    def __init__(self, key):
        self.id = key
        self.connected_to = {}
        self.pred = None
        self.distance = float("inf")
        self.visited = False

    def add_neighbor(self, nbr, weight=0):
        self.connected_to[nbr] = weight

    def get_weight(self, nbr):
        return self.neighbors[nbr]

    def get_connections(self):
        return self.connected_to.keys()  # returns dict_keys object


if __name__ == "__main__":
    t = Vertex("T")
    b = Vertex("B")
    t.add_neighbor(b, 10)
    d = t.get_connections()
