import unittest

from algorithms.data_structures.graphs.breadth_first_search import breadth_first_search
from algorithms.data_structures.graphs.depth_first_search import (
    depth_first_search,
    dfs_iterative,
)
from algorithms.data_structures.graphs.dijkstra import dijkstra


class Test_Graph_Algos(unittest.TestCase):

    unweighted_graph = {
        "u": ["v", "x", "w"],
        "x": ["u", "v", "w", "y"],
        "v": ["u", "x", "w"],
        "w": ["v", "y", "z", "x", "u"],
        "z": ["w", "y"],
        "y": ["z", "w", "x"],
        "a": ["z"],
    }

    weighted_graph = {
        "u": {"v": 2, "x": 1, "w": 5},
        "x": {"u": 1, "v": 2, "w": 3, "y": 1},
        "v": {"u": 2, "x": 2, "w": 3},
        "w": {"v": 3, "y": 1, "z": 5, "x": 3, "u": 5},
        "z": {"w": 3, "y": 2},
        "y": {"z": 1, "w": 1, "x": 1},
    }

    def test_dfs_recursive(self):

        self.assertEqual(
            {"w", "z", "y", "u", "v", "x"},
            depth_first_search(self.unweighted_graph, "z"),
        )

    def test_dfs_iterative(self):
        self.assertEqual(
            ["z", "w", "v"], dfs_iterative(self.unweighted_graph, "z", "v")
        )
        self.assertFalse(dfs_iterative(self.unweighted_graph, "u", "a"))

    def test_bfs(self):
        self.assertEqual(
            {"w", "z", "y", "u", "v", "x"},
            breadth_first_search(self.unweighted_graph, "z"),
        )

    def test_dijkstra(self):
        self.assertEqual(dijkstra(self.weighted_graph, "u", "z"),
                "u --> x --> y --> z")


if __name__ == "__main__":
    unittest.main()
