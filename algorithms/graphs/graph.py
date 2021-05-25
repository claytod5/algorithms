#!/usr/bin/env python

from collections import deque


class Graph:
    def __init__(self):
        self.vertices = {}

    def __contains__(self, n):
        return n in self.vertices

    def add_edge(self, f, t):
        if t not in self.vertices:
            self.vertices[t] = []
        if f not in self.vertices:
            self.vertices[f] = [t]
        else:
            self.vertices[f].append(t)

    def bfs(self, start):
        visited = set()
        queue = deque()
        queue.appendleft(start)
        visited.add(start)

        while queue:
            vertex = queue.pop()

            for adjacent_vertex in self.vertices[vertex]:
                if adjacent_vertex not in visited:
                    queue.appendleft(adjacent_vertex)
                    visited.add(adjacent_vertex)

        return visited


if __name__ == "__main__":
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(3, 2)
    g.add_edge(3, 4)
    g.add_edge(4, 2)
    g.add_edge(4, 1)
    g.add_edge(4, 3)
    print(g.bfs(3))
