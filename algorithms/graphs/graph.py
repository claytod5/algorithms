from collections import deque

from vertex import Vertex

# from algorithms.data_structures.collections.queue import Queue


class Graph:
    def __init__(self):
        self.vertices = {}
        self.numVertices = 0

    def _addVertex(self, key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertices[key] = newVertex
        # return newVertex

    def get_vertex(self, n):
        if n in self.vertices:
            return self.vertices[n]
        else:
            return None

    def add_edge(self, f, t, weight=0):
        if f not in self.vertices:
            self._addVertex(f)
        if t not in self.vertices:
            self._addVertex(t)
        self.vertices[f].add_neighbor(self.vertices[t], weight)

    def get_vertices(self):
        return self.vertices.keys()

    def bfs(self, start):
        start = self.get_vertex(start)
        if start is not None:
            visited = set()
            vertex_queue = deque()
            vertex_queue.appendleft(start)

            while vertex_queue:
                current_vertex = vertex_queue.pop()

                for nbr in current_vertex.get_connections():
                    if nbr not in visited:
                        nbr.pred = current_vertex
                        vertex_queue.appendleft(nbr)
                        visited.add(nbr)

            return visited

    def bfs_path(self, start, end):
        start, end = self.get_vertex(start), self.get_vertex(end)
        path = [end.id]
        while path[-1] != start.id:
            temp = self.get_vertex(path[-1])
            if temp is not None:
                path.append(temp.pred.id)
        path.reverse()
        return path


if __name__ == "__main__":
    g = Graph()
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(1, 4)
    g.add_edge(2, 5)
    g.add_edge(2, 6)
    g.add_edge(5, 9)
    g.add_edge(5, 10)
    g.add_edge(7, 8)
    g.add_edge(11, 12)

    # print(g.get_vertex(2))

    # g.bfs(2)
    print(g.bfs_path(2, 9))
