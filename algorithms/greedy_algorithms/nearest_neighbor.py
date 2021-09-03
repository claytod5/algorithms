#!/usr/bin/env python
"""The nearest neighbour algorithm was one of the first algorithms used
to solve the travelling salesman problem approximately. In that problem,
the salesman starts at a random city and repeatedly visits the nearest
city until all have been visited.  The algorithm quickly yields a short
tour, but usually not the optimal one.

https://en.wikipedia.org/wiki/Nearest_neighbour_algorithm
"""

import heapdict


def nearest_neighbor(graph, start):
    visited = set(start)
    traversed = [start]
    for _ in graph[traversed[-1]]:
        pq = heapdict.heapdict(
            {k: v for k, v in graph[traversed[-1]].items() if k not in visited}
        )
        nearest = pq.popitem()[0]
        traversed.append(nearest)
        visited.add(nearest)

    return " --> ".join(traversed)


if __name__ == "__main__":
    graph = {
        "A": {"B": 20, "C": 42, "D": 35},
        "B": {"A": 20, "C": 30, "D": 34},
        "C": {"A": 42, "B": 30, "D": 12},
        "D": {"A": 35, "B": 34, "C": 12},
    }
    print(nearest_neighbor(graph, "C"))
