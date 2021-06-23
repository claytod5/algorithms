#!/usr/bin/env python

import heapdict
from backtrace import backtrace


def dijkstra(graph, start, end):
    parent = {}  # track predecessors

    # track distance relative to starting node
    distance = {each: float("inf") for each in graph.keys()}
    distance[start] = 0

    pq = heapdict.heapdict({each: distance[each] for each in graph.keys()})

    while pq:
        current_vertex = pq.popitem()[0]
        for next_vert in graph[current_vertex]:
            new_distance = distance[current_vertex] + graph[current_vertex][next_vert]
            if new_distance < distance[next_vert]:
                distance[next_vert] = new_distance
                parent[next_vert] = current_vertex
                pq[next_vert] = new_distance
    breakpoint()
    return " --> ".join(backtrace(parent, start, end))


if __name__ == "__main__":
    graph = {
        "u": {"v": 2, "x": 1, "w": 5},
        "x": {"u": 1, "v": 2, "w": 3, "y": 1},
        "v": {"u": 2, "x": 2, "w": 3},
        "w": {"v": 3, "y": 1, "z": 5, "x": 3, "u": 5},
        "z": {"w": 3, "y": 2},
        "y": {"z": 1, "w": 1, "x": 1},
    }
    print(dijkstra(graph, "u", "z"))
