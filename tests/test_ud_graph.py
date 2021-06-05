import unittest

from ud_graph import UndirectedGraph


class TestUDGraph(unittest.TestCase):
    def test_add_vertex_example_1(self) -> None:
        # Arrange
        exp: dict = {'A': ["new"], 'B': [], 'C': [], 'D': [], 'E': []}
        g: UndirectedGraph = UndirectedGraph()

        # Act
        for v in "ABCDE":
            g.add_vertex(v)

        # Ensure existing vertex is not overwritten.
        g.adj_list['A'].append("new")
        g.add_vertex('A')

        # Assert
        self.assertDictEqual(exp, g.adj_list)


if __name__ == "__main__":
    unittest.main()
