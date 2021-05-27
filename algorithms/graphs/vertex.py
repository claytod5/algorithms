class Vertex:
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
