import unittest

from algorithms.data_structures.graphs.breadth_first_search import breadth_first_search
from algorithms.data_structures.graphs.depth_first_search import (
    depth_first_search,
    dfs_iterative,
)


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

    def test_dfs_recursive(self):

        self.assertEqual(
            {"w", "z", "y", "u", "v", "x"},
            depth_first_search(self.unweighted_graph, "z"),
        )

    def test_dfs_iterative(self):
        self.assertEqual(
            ["z", "w", "v"], dfs_iterative(self.unweighted_graph, "z", "v")
        )
        self.assertFalse(
                dfs_iterative(self.unweighted_graph, "u", "a")
                )

    def test_bfs(self):
        self.assertEqual(
            {"w", "z", "y", "u", "v", "x"},
            breadth_first_search(self.unweighted_graph, "z"),
        )


if __name__ == "__main__":
    unittest.main()
