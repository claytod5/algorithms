#!/usr/bin/env python


from collections import deque


def breadth_first_search(graph, start):
    search_queue = deque()
    search_queue += start
    visited = set()

    while search_queue:
        node = search_queue.popleft()
        for each in graph[node]:
            if each not in visited:
                search_queue += graph[each]
        visited.add(node)

    return visited
