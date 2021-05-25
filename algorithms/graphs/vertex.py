class Vertex:
    def __init__(self, key):
        self.id = key
        self.neighbors = {}

    def add_neighbor(self, nbr, weight=0):
        self.neighbors[nbr] = weight

    def get_weight(self, nbr):
        return self.neighbors[nbr]

    def get_neighbors(self):
        return self.neighbors.keys()


if __name__ == "__main__":
    t = Vertex("T")
    b = Vertex("B")
    t.add_neighbor(b, 10)
    print(t.neighbors.keys())
