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

    def test_remove_edge_does_nothing_if_edge_invalid(self) -> None:
        # Arrange
        exp: list = [[0] * 5] * 5
        g: DirectedGraph = DirectedGraph()
        for _ in range(5):
            g.add_vertex()

        # Act
        g.remove_edge(0, 5)

        # Assert
        self.assertListEqual(exp, g.adj_matrix)

    def test_remove_edge_updates_edge_if_valid(self) -> None:
        # Arrange
        exp: list = [
            [0, 10, 0, 0, 0],
            [0, 0, 0, 0, 15],
            [0, 0, 0, 0, 0],
            [0, 5, 7, 0, 0],
            [12, 0, 0, 3, 0]
        ]
        g: DirectedGraph = DirectedGraph()
        for _ in range(5):
            g.add_vertex()

        edges: list = [(0, 1, 10), (4, 0, 12), (1, 4, 15), (4, 3, 3), (3, 1, 5), (2, 1, 23), (3, 2, 7)]
        for src, dst, weight in edges:
            g.add_edge(src, dst, weight)

        # Act
        g.remove_edge(2, 1)

        # Assert
        self.assertListEqual(exp, g.adj_matrix)

    def test_is_valid_edge_returns_true_if_valid(self) -> None:
        # Arrange
        g: DirectedGraph = DirectedGraph()
        for _ in range(2):
            g.add_vertex()

        # Act/Assert
        self.assertTrue(g._is_valid_edge(0, 1))
        self.assertTrue(g._is_valid_edge(1, 0))

    def test_is_valid_edge_returns_false_if_valid(self) -> None:
        # Arrange
        g: DirectedGraph = DirectedGraph()
        for _ in range(2):
            g.add_vertex()

        # Act/Assert
        self.assertFalse(g._is_valid_edge(0, 0))
        self.assertFalse(g._is_valid_edge(1, 1))
        self.assertFalse(g._is_valid_edge(0, 2))
        self.assertFalse(g._is_valid_edge(2, 0))
        self.assertFalse(g._is_valid_edge(2, 2))

    def test_get_vertices_example_1(self) -> None:
        # Arrange
        exp: list = [0, 1, 2, 3, 4]
        edges: list = [(0, 1, 10), (4, 0, 12), (1, 4, 15), (4, 3, 3), (3, 1, 5), (2, 1, 23), (3, 2, 7)]
        g: DirectedGraph = DirectedGraph(edges)

        # Act
        vertices: list = g.get_vertices()

        # Assert
        self.assertListEqual(exp, vertices)

    def test_get_edges_example_1(self) -> None:
        # Arrange
        exp: list = [(0, 1, 10), (1, 4, 15), (2, 1, 23), (3, 1, 5), (3, 2, 7), (4, 0, 12), (4, 3, 3)]
        edges: list = [(0, 1, 10), (4, 0, 12), (1, 4, 15), (4, 3, 3), (3, 1, 5), (2, 1, 23), (3, 2, 7)]
        g: DirectedGraph = DirectedGraph(edges)

        # Act
        edges: list = g.get_edges()

        # Assert
        self.assertListEqual(exp, edges)

    def test_is_valid_path_example_1(self) -> None:
        # Arrange
        exp: list = [True, False, False, True, True, True]
        edges: list = [(0, 1, 10), (4, 0, 12), (1, 4, 15), (4, 3, 3), (3, 1, 5), (2, 1, 23), (3, 2, 7)]
        g: DirectedGraph = DirectedGraph(edges)
        test_cases: list = [[0, 1, 4, 3], [1, 3, 2, 1], [0, 4], [4, 0], [], [2]]

        # Act/Assert
        i: int = 0
        for path in test_cases:
            valid: bool = g.is_valid_path(path)
            self.assertEqual(exp[i], valid)
            i += 1

    def test_are_adjacent_returns_false_if_no_outgoing_edge_from_src_to_dst(self) -> None:
        # Arrange
        g: DirectedGraph = DirectedGraph()
        g.add_vertex()
        g.add_vertex()
        g.add_edge(0, 1)

        # Act
        adj: bool = g.are_adjacent(1, 0)

        # Assert
        self.assertFalse(adj)

    def test_are_adjacent_returns_true_if_outgoing_edge_from_src_to_dst(self) -> None:
        # Arrange
        g: DirectedGraph = DirectedGraph()
        g.add_vertex()
        g.add_vertex()
        g.add_edge(0, 1)

        # Act
        adj: bool = g.are_adjacent(0, 1)

        # Assert
        self.assertTrue(adj)

    def test_neighbors_returns_all_neighbors_of_vertex(self) -> None:
        # Arrange
        exp: list = [1, 3]
        edges: list = [(0, 1, 1), (0, 3, 1)]
        g: DirectedGraph = DirectedGraph(edges)

        # Act
        neighbors: list = g.neighbors(0)

        # Assert
        self.assertListEqual(exp, neighbors)

    def test_dfs_example_1(self) -> None:
        # Arrange
        exp: list = [
            [0, 1, 4, 3, 2],
            [1, 4, 0, 3, 2],
            [2, 1, 4, 0, 3],
            [3, 1, 4, 0, 2],
            [4, 0, 1, 3, 2]
        ]
        edges: list = [(0, 1, 10), (4, 0, 12), (1, 4, 15), (4, 3, 3), (3, 1, 5), (2, 1, 23), (3, 2, 7)]
        g: DirectedGraph = DirectedGraph(edges)

        # Act/Assert
        i: int = 0
        for start in range(5):
            dfs: list = g.dfs(start)
            self.assertListEqual(exp[i], dfs)
            i += 1

    def test_bfs_example_1(self) -> None:
        # Arrange
        exp: list = [
            [0, 1, 4, 3, 2],
            [1, 4, 0, 3, 2],
            [2, 1, 4, 0, 3],
            [3, 1, 2, 4, 0],
            [4, 0, 3, 1, 2]
        ]
        edges: list = [(0, 1, 10), (4, 0, 12), (1, 4, 15), (4, 3, 3), (3, 1, 5), (2, 1, 23), (3, 2, 7)]
        g: DirectedGraph = DirectedGraph(edges)

        # Act/Assert
        i: int = 0
        for start in range(5):
            dfs: list = g.bfs(start)
            self.assertListEqual(exp[i], dfs)
            i += 1

    def test_reversed_returns_graph_with_reversed_edges(self) -> None:
        # Arrange
        exp: list = [
            (0, 1, 1),
            (0, 2, 1),
            (2, 1, 1),
            (3, 2, 1)
        ]
        edges: list = [
            (1, 0, 1),
            (2, 0, 1),
            (1, 2, 1),
            (2, 3, 1)
        ]
        g: DirectedGraph = DirectedGraph(edges)

        # Act
        g_reversed: DirectedGraph = g.reversed()

        # Assert
        self.assertCountEqual(exp, g_reversed.get_edges())

    def test_connected_components_graph_with_disconnected_vertices_returns_each_vertex_as_component(self) -> None:
        # Arrange
        exp: list = [[0], [1]]
        g: DirectedGraph = DirectedGraph()

        g.add_vertex()
        g.add_vertex()

        # Act
        comp: list = g.connected_components()

        # Assert
        self.assertCountEqual(exp, comp)

    def test_connected_components_connected_graph_returns_single_component(self) -> None:
        # Arrange
        exp: list = [[0, 1, 2, 3]]
        edges: list = [
            (0, 1, 1),
            (0, 2, 1),
            (0, 3, 1),
            (1, 2, 1),
            (1, 3, 1),
            (2, 3, 1)
        ]
        g: DirectedGraph = DirectedGraph(edges)

        # Act
        comp: list = g.connected_components()

        # Assert
        self.assertEqual(len(exp), len(comp))
        self.assertCountEqual(exp[0], comp[0])

    def test_connected_components_disconnected_graph_returns_all_components(self) -> None:
        # Arrange
        exp: list = [[0, 1], [2, 3], [4]]
        g: DirectedGraph = DirectedGraph()

        g.add_vertex()
        g.add_vertex()
        g.add_vertex()
        g.add_vertex()
        g.add_vertex()

        g.add_edge(0, 1)
        g.add_edge(2, 3)

        # Act
        comp: list = g.connected_components()

        # Assert
        self.assertEqual(len(exp), len(comp))
        i: int = 0
        while i < len(exp):
            self.assertCountEqual(sorted(exp)[i], sorted(comp)[i])
            i += 1


if __name__ == "__main__":
    unittest.main()
