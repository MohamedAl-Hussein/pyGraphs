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


    def test_degree_returns_degree_of_vertex_if_it_exists(self) -> None:
        # Arrange
        exp: int = 2
        g: UndirectedGraph = UndirectedGraph()

        g.add_vertex('A')
        g.add_vertex('B')
        g.add_vertex('C')

        g.add_edge('A', 'B')
        g.add_edge('A', 'C')

        # Act
        deg: int = g.degree('A')

        # Assert
        self.assertEqual(exp, deg)

    def test_degree_raises_if_vertex_does_not_exist(self) -> None:
        # Arrange
        g: UndirectedGraph = UndirectedGraph()

        # Act/Assert
        with self.assertRaises(KeyError):
            g.degree('A')

    def test_are_adjacent_returns_true_if_vertices_adjacent(self) -> None:
        # Arrange
        g: UndirectedGraph = UndirectedGraph()

        g.add_vertex('A')
        g.add_vertex('B')

        g.add_edge('A', 'B')

        # Act
        adj: bool = g.are_adjacent('A', 'B')

        # Assert
        self.assertTrue(adj)

    def test_are_adjacent_returns_false_if_vertices_not_adjacent(self) -> None:
        # Arrange
        g: UndirectedGraph = UndirectedGraph()

        g.add_vertex('A')
        g.add_vertex('B')
        g.add_vertex('C')

        g.add_edge('A', 'B')

        # Act
        adj: bool = g.are_adjacent('A', 'C')

        # Assert
        self.assertFalse(adj)

    def test_are_adjacent_raises_if_one_or_more_vertices_dont_exist(self) -> None:
        # Arrange
        g: UndirectedGraph = UndirectedGraph()
        g.add_vertex('A')
        g.add_vertex('B')
        g.add_vertex('C')

        # Act/Assert
        with self.assertRaises(KeyError):
            g.are_adjacent('A', 'D')

        with self.assertRaises(KeyError):
            g.are_adjacent('D', 'E')


if __name__ == "__main__":
    unittest.main()
