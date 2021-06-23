#!/usr/bin/env python


from collections import deque
from backtrace import backtrace


def breadth_first_search(graph, start, end):
    parent = dict()
    search_queue = deque()
    search_queue += start
    visited = set()

    while search_queue:
        node = search_queue.popleft()
        if node == end:
            return backtrace(parent, start, end)
        for each in graph[node]:
            if each not in visited:
                search_queue += graph[node]
                parent[each] = node
                visited.add(node)

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
    print(breadth_first_search(graph, "z", "v"))
