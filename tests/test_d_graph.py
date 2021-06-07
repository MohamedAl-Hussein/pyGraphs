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


if __name__ == "__main__":
    unittest.main()
