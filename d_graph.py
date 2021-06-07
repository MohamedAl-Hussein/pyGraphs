# Course: CS261 - Data Structures
# Author:
# Assignment:
# Description:


class DirectedGraph:
    """
    Class to implement directed weighted graph
    - duplicate edges not allowed
    - loops not allowed
    - only positive edge weights
    - vertex names are integers
    """

    def __init__(self, start_edges=None):
        """
        Store graph info as adjacency matrix
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.v_count = 0
        self.adj_matrix = []

        # populate graph with initial vertices and edges (if provided)
        # before using, implement add_vertex() and add_edge() methods
        if start_edges is not None:
            v_count = 0
            for u, v, _ in start_edges:
                v_count = max(v_count, u, v)
            for _ in range(v_count + 1):
                self.add_vertex()
            for u, v, weight in start_edges:
                self.add_edge(u, v, weight)

    def __str__(self):
        """
        Return content of the graph in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        if self.v_count == 0:
            return 'EMPTY GRAPH\n'
        out = '   |'
        out += ' '.join(['{:2}'.format(i) for i in range(self.v_count)]) + '\n'
        out += '-' * (self.v_count * 3 + 3) + '\n'
        for i in range(self.v_count):
            row = self.adj_matrix[i]
            out += '{:2} |'.format(i)
            out += ' '.join(['{:2}'.format(w) for w in row]) + '\n'
        out = f"GRAPH ({self.v_count} vertices):\n{out}"
        return out

    def add_vertex(self) -> int:
        """
        Adds new vertex to the graph.

        Returns new number of vertices in graph.
        """

        # Extend matrix by one column.
        for row in self.adj_matrix:
            row.append(0)

        # Extend matrix by one row.
        self.adj_matrix.append([0] * (self.v_count + 1))

        # Update vertex count.
        self.v_count += 1

        return self.v_count

    def add_edge(self, src: int, dst: int, weight=1) -> None:
        """
        Adds a new edge to the graph, connecting src vertex to dst vertex.

        If src and dst point to the same vertex, or if weight is not positive, does nothing and returns.
        If edge already exists, updates weight of edge.
        """

        # Only update weight if src and dst exist and don't point to same vertex and weight is positive.
        if self._is_valid_edge(src, dst) and weight >= 1:
            self.adj_matrix[src][dst] = weight

    def remove_edge(self, src: int, dst: int) -> None:
        """
        Removes an edge between src and dst vertices.

        If either vertex does not exist in the graph, or if there is no edge between them, does nothing and returns.
        """

        # Only remove edge if vertices exist.
        if self._is_valid_edge(src, dst):
            self.adj_matrix[src][dst] = 0

    def get_vertices(self) -> []:
        """Returns a list of vertices of the graph."""

        return [_ for _ in range(self.v_count)]

    def get_edges(self) -> []:
        """
        Returns a list of 3-tuples containing the source vertex, destination vertex, and edge weight for all edges
        in graph.
        """

        edges: list = list()

        for i in range(self.v_count):
            for j in range(self.v_count):
                # Edge exists between vertex i and j.
                if self.adj_matrix[i][j] > 0:
                    edges.append((i, j, self.adj_matrix[i][j]))

        return edges

    def is_valid_path(self, path: []) -> bool:
        """
        TODO: Write this implementation
        """
        pass

    def dfs(self, v_start, v_end=None) -> []:
        """
        TODO: Write this implementation
        """
        pass

    def bfs(self, v_start, v_end=None) -> []:
        """
        TODO: Write this implementation
        """
        pass

    def has_cycle(self):
        """
        TODO: Write this implementation
        """
        pass

    def dijkstra(self, src: int) -> []:
        """
        TODO: Write this implementation
        """
        pass

    def _is_valid_edge(self, src: int, dst: int) -> bool:
        """
        Returns True if an edge between a src and dst vertex is valid.

        An edge is invalid if the src and dst point to the same vertex, or if either vertex is not on the graph.
        """

        return src != dst and 0 <= src < self.v_count and 0 <= dst < self.v_count
