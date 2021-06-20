from collections import deque

from vertex import Vertex

from algorithms.data_structures.trees.priority_queue import PriorityQueue

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
        start_vertex = self.get_vertex(start)
        if start_vertex is not None:
            start_vertex.visited = True
            vertex_queue = deque()
            vertex_queue.appendleft(start_vertex)

            while vertex_queue:
                current_vertex = vertex_queue.pop()

                for nbr in current_vertex.get_connections():
                    if nbr.visited is False:
                        nbr.pred = current_vertex
                        vertex_queue.appendleft(nbr)
                        nbr.visited = True

    def path(self, start, end):
        # bfs or dfs needs to be ran prior to this to create the predecessor hierarchy
        start, end = self.get_vertex(start), self.get_vertex(end)
        path = [end.id]
        while path[-1] != start.id:
            temp = self.get_vertex(path[-1])
            if temp is not None:
                path.append(temp.pred.id)
        path.reverse()
        return path

    def dfs(self, start):
        start_vertex = self.get_vertex(start)
        start_vertex.visited = True
        for next_vertex in start_vertex.get_connections():
            if next_vertex.visited is False:
                next_vertex.pred = start_vertex
                self.dfs(next_vertex.id)

    def dijkstra(self, start):
        pq = PriorityQueue()
        start.distance = 0

        # key is each vertex distance
        pq.build_heap([(v.distance, v) for v in self.vertices])

        while not pq.is_empty():
            current_vert = pq.pop_min()  # get minimum-distanced vertex from pq

            # loop through each of that vertex's connections
            for next_vert in current_vert.get_connections():
                # calculate the next vertex's distance when going via current vert
                new_dist = current_vert.distance + current_vert.get_weight(next_vert)

            # if the new calcuated distance is cheaper...
            if new_dist < next_vert.distance:
                next_vert.distance = new_dist  # set the distance to the new dist

                # mark the current vertex as the predecessor of next_vert
                next_vert.pred = current_vert

                # update next_vert's key in priority queue with the new distance
                # this will cause next_vert to be closer to the root and thus a
                # higher priority
                pq.decrease_key(next_vert, new_dist)


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

    g.dfs(1)
    print(g.path(1, 9))
