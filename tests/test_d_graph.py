import unittest

from d_graph import DirectedGraph


class TestDirectedGraph(unittest.TestCase):
    def test_add_vertex_example_1(self) -> None:
        # Arrange
        exp: list = [[0] * 5] * 5
        g: DirectedGraph = DirectedGraph()

        # Act
        for _ in range(5):
            g.add_vertex()

        # Assert
        self.assertListEqual(exp, g.adj_matrix)

    def test_add_edge_example_1(self) -> None:
        # Arrange
        exp: list = [
            [0, 10, 0, 0, 0],
            [0, 0, 0, 0, 15],
            [0, 23, 0, 0, 0],
            [0, 5, 7, 0, 0],
            [12, 0, 0, 3, 0]
        ]
        g: DirectedGraph = DirectedGraph()
        for _ in range(5):
            g.add_vertex()

        edges: list = [(0, 1, 10), (4, 0, 12), (1, 4, 15), (4, 3, 3), (3, 1, 5), (2, 1, 23), (3, 2, 7)]

        # Act
        for src, dst, weight in edges:
            g.add_edge(src, dst, weight)

        # Assert
        self.assertListEqual(exp, g.adj_matrix)


if __name__ == "__main__":
    unittest.main()
