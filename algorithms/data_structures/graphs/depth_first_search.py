#!/usr/bin/env python

from algorithms.data_structures.graphs.backtrace import backtrace


def depth_first_search(graph, start, visited=set()):
    """Recursive version"""
    visited.add(start)
    for next_vertex in graph[start]:
        if next_vertex not in visited:
            return depth_first_search(graph, next_vertex, visited)
    return visited


def dfs_iterative(graph, start, end):
    visited = set(start)
    parent = dict()
    stack = [start]
    while stack:
        vertex = stack.pop()
        if vertex == end:
            return backtrace(parent, start, end)
        for node in reversed(graph[vertex]):
            if node not in visited:
                visited.add(node)
                stack.append(node)
                parent[node] = vertex

    return False


if __name__ == "__main__":
    graph = {
        "u": ["v", "x", "w"],
        "x": ["u", "v", "w", "y"],
        "v": ["u", "x", "w"],
        "w": ["v", "y", "z", "x", "u"],
        "z": ["w", "y"],
        "y": ["z", "w", "x"],
    }
    # print(depth_first_search(graph, "z"))
    print(dfs_iterative(graph, "z", "v"))
