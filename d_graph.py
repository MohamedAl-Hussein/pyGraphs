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

        If weight is not positive, does nothing and returns.
        If src and dst point to the same vertex, does nothing and returns.
        If edge already exists, updates weight of edge.
        """

        # Only update weight if src and dst don't point to same vertex and weight is positive.
        if src != dst and weight >= 1:
            self.adj_matrix[src][dst] = weight

    def remove_edge(self, src: int, dst: int) -> None:
        """
        TODO: Write this implementation
        """
        pass

    def get_vertices(self) -> []:
        """
        TODO: Write this implementation
        """
        pass

    def get_edges(self) -> []:
        """
        TODO: Write this implementation
        """
        pass

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
