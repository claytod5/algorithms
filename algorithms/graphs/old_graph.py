#!/usr/bin/env python

from collections import deque


class Graph:
    def __init__(self):
        self.vertices = {}
        self.weights = {}

    def __contains__(self, n):
        return n in self.vertices

    def add_edge(self, f, t, weight=0):
        if t not in self.vertices:
            self.vertices[t] = []
            self.weights[t] = {}
        if f not in self.vertices:
            self.vertices[f] = [t]
            self.weights[f] = {}
            self.weights[f][t] = weight
        else:
            self.vertices[f].append(t)
            self.weights[f][t] = weight

    def bfs(self, start):
        """Return a set which contains the paths available from start."""
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

    def bfs_path(self, start, end):
        "Return a list showing the shortest path from start to end."
        visited = set()
        queue = deque()
        queue.appendleft([start])

        while queue:
            path = queue.pop()  # pop a list starting with 'start' from queue

            vertex = path[-1]  # access last vertex in path list

            if vertex == end:
                return path

            elif vertex not in visited:
                for adjacent_vertex in self.vertices[vertex]:
                    new_path = list(path)  # create a temp list using list of paths
                    # built so far
                    new_path.append(adjacent_vertex)  # append current vertex
                    queue.appendleft(new_path)  # add new potential path to queue

                    if adjacent_vertex == end:  # did we find the goal?
                        return new_path

                visited.add(vertex)  # add vertex to set to limit rechecking

    def _generate_costs_table(self, start):
        costs = {}
        for each in self.vertices[start]:
            costs[each] = self.weights[start][each]
        return costs

    def _generate_parents_table(self, start):
        parents = {}
        for each in self.vertices[start]:
            parents[each] = start
        return parents

    # def _find_lowest_cost_node(self, weights):
    #     lowest_cost = float("inf")
    #     lowest_cost_node = None
    #     for node in costs:
    #         cost = costs[node]
    #         if cost < lowest_cost and node not in processed:
    #             pass
                
    def djikstra_path(self, start, end):
        costs = self._generate_costs_table(start)
        parents = self._generate_parents_table(start)
        processed = []
        node = self._find_lowest_cost_node(self.weights)


if __name__ == "__main__":
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2, 25)
    g.add_edge(1, 2)
    g.add_edge(3, 2, 5)
    g.add_edge(3, 4, 10)
    g.add_edge(4, 2)
    g.add_edge(4, 1)
    g.add_edge(4, 3)
    print(g.weights[0][2])
