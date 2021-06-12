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

    def test_connected_components_connected_graph_returns_all_vertices_as_components(self) -> None:
        # Arrange
        exp: list = [[0], [1], [2], [3]]
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
        exp: list = [[0], [1], [2], [3], [4]]
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

    def test_connected_components_returns_all_components_for_connected_graph(self) -> None:
        """Example based off of: https://www.youtube.com/watch?v=HOOmetF56BI"""

        # Arrange
        exp: list = [
            [1], [4, 7], [8], [3, 0, 5, 10], [6, 2, 9]
        ]
        edges: list = [
            (4, 7, 1),
            (7, 4, 1),
            (4, 0, 1),
            (0, 3, 1),
            (3, 0, 1),
            (0, 5, 1),
            (5, 6, 1),
            (5, 10, 1),
            (10, 0, 1),
            (10, 9, 1),
            (9, 6, 1),
            (6, 2, 1),
            (2, 9, 1),
            (1, 8, 1),
            (8, 10, 1)
        ]
        g: DirectedGraph = DirectedGraph(edges)

        # Act
        components: list = g.connected_components()

        # Assert
        self.assertEqual(len(exp), len(components))
        i: int = 0
        exp = sorted(exp, key=sum)
        comp = sorted(components, key=sum)
        while i < len(exp):
            self.assertCountEqual(exp[i], comp[i])
            i += 1

    def test_has_cycle_example_1(self) -> None:
        # Arrange
        exp: list = [True, True, False, False, False, False, True]
        edges: list = [(0, 1, 10), (4, 0, 12), (1, 4, 15), (4, 3, 3), (3, 1, 5), (2, 1, 23), (3, 2, 7)]
        g: DirectedGraph = DirectedGraph(edges)

        edges_to_remove: list = [(3, 1), (4, 0), (3, 2)]
        edges_to_add: list = [(4, 3), (2, 3), (1, 3), (4, 0)]

        # Act/Assert
        idx: int = 0
        for src, dst in edges_to_remove:
            g.remove_edge(src, dst)
            self.assertEqual(exp[idx], g.has_cycle())
            idx += 1

        for src, dst in edges_to_add:
            g.add_edge(src, dst)
            self.assertEqual(exp[idx], g.has_cycle())
            idx += 1

    def test_has_cycle_example_2(self) -> None:
        # Arrange
        edges: list = [
            (0, 1, 15),
            (0, 2, 2),
            (2, 3, 6),
            (2, 6, 3),
            (3, 8, 11),
            (4, 7, 19),
            (4, 11, 8),
            (6, 7, 18),
            (7, 12, 4),
            (8, 0, 13),
            (8, 5, 18),
            (10, 12, 12),
            (12, 8, 8)
        ]
        g: DirectedGraph = DirectedGraph(edges)

        # Act/Assert
        self.assertTrue(g.has_cycle())

    def test_has_cycle_example_3(self) -> None:
        # Arrange
        edges: list = [
            (0, 12, 16),
            (3, 0, 2),
            (2, 0, 9),
            (2, 11, 3),
            (11, 10, 2),
            (10, 11, 8),
            (10, 4, 14),
            (10, 9, 5),
            (7, 9, 15),
            (7, 6, 10),
            (6, 1, 19),
            (6, 12, 1),
            (5, 12, 17),
            (5, 6, 18)
        ]
        g: DirectedGraph = DirectedGraph(edges)

        # Act/Assert
        self.assertTrue(g.has_cycle())

    def test_has_cycle_example_4(self) -> None:
        # Arrange
        edges: list = [
            (0, 1, 19), (0, 6, 13), (0, 8, 14),
            (2, 4, 10),
            (3, 4, 14),
            (7, 10, 14),
            (11, 3, 13),
            (12, 1, 20), (12, 2, 7), (12, 4, 18), (12, 10, 13), (12, 11, 4)
        ]
        g: DirectedGraph = DirectedGraph(edges)

        # Act/Assert
        self.assertFalse(g.has_cycle())

    def test_dijkstra_example_1(self) -> None:
        # Arrange
        exp: list = [
            [0, 10, 35, 28, 25],
            [27, 0, 25, 18, 15],
            [50, 23, 0, 41, 38],
            [32, 5, 7, 0, 20],
            [12, 8, 10, 3, 0],
            [0, 10, float("inf"), float("inf"), 25],
            [27, 0, float("inf"), float("inf"), 15],
            [50, 23, 0, float("inf"), 38],
            [32, 5, 7, 0, 20],
            [12, 22, float("inf"), float("inf"), 0]
        ]
        edges: list = [(0, 1, 10), (4, 0, 12), (1, 4, 15), (4, 3, 3), (3, 1, 5), (2, 1, 23), (3, 2, 7)]
        g: DirectedGraph = DirectedGraph(edges)

        for i in range(5):
            d: list = g.dijkstra(i)
            e: list = exp[i]
            self.assertListEqual(e, d)

        g.remove_edge(4, 3)

        for i in range(0, 5):
            d: list = g.dijkstra(i)
            e: list = exp[i+5]
            self.assertListEqual(e, d)


if __name__ == "__main__":
    unittest.main()
