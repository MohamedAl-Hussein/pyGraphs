# Course: CS261 - Data Structures
# Author: Mohamed Al-Hussein
# Assignment: 06
# Description: Directed graph implementation.

from collections import deque
import heapq


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
        Return True if the provided path is valid.

        An empty path or a path with a single vertex is considered valid.
        """

        # Check if path is empty or contains only a single vertex.
        if len(path) == 0:
            return True
        elif len(path) == 1:
            if 0 <= path[0] < self.v_count:
                return True
            else:
                return False

        # Iterate through vertices in path, checking if they are adjacent to each other so that they form a path.
        step: int = 0
        while step < len(path) - 1:
            src, dst = path[step], path[step + 1]
            if not self.are_adjacent(src, dst):
                return False

            step += 1

        return True

    def dfs(self, v_start: int, v_end: int = None) -> []:
        """
        Return list of vertices visited during DFS search from v_start vertex up to optional v_end vertex.

        If v_start is not in the graph, returns empty list.
        If v_end is not in the graph, will treat it as having no v_end parameter.

        Vertices are picked in ascending order.
        """

        visited: list = list()

        # Check if v_start is in graph.
        if not 0 <= v_start < self.v_count:
            return visited

        # Check if v_end is in graph.
        if isinstance(v_end, int) and not 0 <= v_end < self.v_count:
            v_end = None

        # Traverse graph until we either reach v_end or traverse every vertex.
        return self._dfs(v_start, v_end)

    def bfs(self, v_start: int, v_end: int = None) -> []:
        """
        Return list of vertices visited during BFS search from v_start vertex up to optional v_end vertex.

        If v_start is not in the graph, returns empty list.
        If v_end is not in the graph, will treat it as having no v_end parameter.

        Vertices are picked in ascending order.
        """

        visited: list = list()

        # Check if v_start is in graph.
        if not 0 <= v_start < self.v_count:
            return visited

        # Check if v_end is in graph.
        if isinstance(v_end, int) and not 0 <= v_end < self.v_count:
            v_end = None

        # Traverse graph until we either reach v_end or traverse every vertex.
        vertices: deque = deque()
        vertices.appendleft(v_start)
        while len(vertices) > 0:
            v: int = vertices.pop()
            if v not in visited:
                # Add vertex to visited vertices.
                visited.append(v)

                # Stop if vertex is equal to v_end.
                if v == v_end:
                    break

                # Add all neighbors of vertex in descending order so that they are popped in ascending order.
                for neighbor in self.neighbors(v):
                    vertices.appendleft(neighbor)

        return visited

    def has_cycle(self):
        """Return True if graph contains a cycle."""

        # If any of the strongly connected components (SCC) of the graph contain more than one vertex, then that SCC
        # contains a cycle and so does the graph.
        for component in self.connected_components():
            if len(component) > 1:
                return True

        return False

    def dijkstra(self, src: int) -> []:
        """
        Returns a list of distances of src vertex to every other vertex.

        If a vertex is not reachable, then its distance is infinity.
        """

        distances: list = list()

        if self.is_empty() or not 0 <= src < self.v_count:
            return distances

        # Create priority queue containing first vertex with distance 0.
        vertices: list = list()
        heapq.heappush(vertices, (0, src))
        visited: dict = dict()

        # Iterate through priority queue, updating min distance for each vertex.
        while vertices:
            dist_v, v = heapq.heappop(vertices)
            if v not in visited:
                visited[v] = dist_v
                for neighbor in self.neighbors(v):
                    d_neighbor: int = self.adj_matrix[v][neighbor]
                    heapq.heappush(vertices, (dist_v + d_neighbor, neighbor))

        # Update distances with min distance for each vertex, or inf if they are not reachable.
        for v in self.get_vertices():
            dist: int = visited.get(v, float("inf"))
            distances.append(dist)

        return distances

    def are_adjacent(self, src: int, dst: int) -> bool:
        """Returns True if src vertex has an outgoing edge that connects to dst vertex."""

        # Check if vertices are valid.
        if not self._is_valid_edge(src, dst):
            return False

        return self.adj_matrix[src][dst] > 0

    def connected_components(self) -> []:
        """
        Return a list of lists containing all strongly connected components (SCC) of the graph.

        Uses Kosaraju's algorithm to detect all SCCs.
        """

        components: list = list()

        if self.is_empty():
            return components

        # Iterate through all vertices via DFS.
        # The top_stack maintains a topological sorting of all visited vertices.
        top_stack: deque = deque()
        vertices: deque = deque()
        for v in self.get_vertices():
            vertices.appendleft(v)

        _: list = self._dfs_complete(vertices, top_stack=top_stack)

        # Reverse graph to perform second round of DFS.
        d_reverse: DirectedGraph = self.reversed()
        self.adj_matrix, d_reverse.adj_matrix = d_reverse.adj_matrix, self.adj_matrix

        # Iterate through all vertices in reverse order via DFS.
        components = self._dfs_complete(top_stack)

        # Reverse graph again to return to original form.
        self.adj_matrix = d_reverse.adj_matrix

        return components

    def reversed(self) -> "DirectedGraph":
        """Returns a new DirectedGraph with outgoing edges swapped with incoming and vice versa."""

        # Initialize new empty digraph with similar number of vertices.
        d_graph: DirectedGraph = DirectedGraph()
        for _ in range(self.v_count):
            d_graph.add_vertex()

        # Reflect edges over matrix diagonal to reverse their orientation then add them to new digraph.
        for i in range(self.v_count):
            for j in range(self.v_count):
                d_graph.adj_matrix[i][j] = self.adj_matrix[j][i]

        return d_graph

    def neighbors(self, v: int) -> []:
        """Return all vertices that vertex v has an outgoing edge to."""

        neighbors: list = list()

        for i in range(self.v_count):
            if self.adj_matrix[v][i] > 0:
                neighbors.append(i)

        return neighbors

    def is_empty(self) -> bool:
        """Return True if the graph contains no vertices."""

        return self.v_count == 0

    def _is_valid_edge(self, src: int, dst: int) -> bool:
        """
        Returns True if an edge between a src and dst vertex is valid.

        An edge is invalid if the src and dst point to the same vertex, or if either vertex is not on the graph.
        """

        return src != dst and 0 <= src < self.v_count and 0 <= dst < self.v_count

    def _dfs_complete(self, vertices: deque, top_stack: deque = None) -> []:
        """
        Returns a list of weakly connected components using DFS traversal.

        An optional top_stack parameter tracks the topological sorting of the graph and in turn ensures that
        the returned components are strongly connected.
        """

        components: list = list()
        unvisited: list = [True] * self.v_count

        while vertices:
            v: int = vertices.popleft()

            # Grab the next vertex that hasn't been visited.
            while not unvisited[v] and vertices:
                v = vertices.popleft()

            # All vertices have been visited, so we can stop.
            if v is None:
                break

            component: list = self._dfs(v_start=v, unvisited=unvisited, top_stack=top_stack)
            if len(component) > 0:
                components.append(component)

        return components

    def _dfs(self, v_start: int, v_end: int = None, unvisited: list = None, top_stack: deque = None) -> []:
        """
        Returns a list containing all vertices visited starting from the vertex v_start up to the optional vertex
        v_end via DFS.

        An optional list of unvisited vertices ensures vertices are visited exactly once during multiple calls to
        this method.

        An optional top_stack parameter maintains a topological sorting of all visited vertices.
        """

        # The backstack holds any visited vertices in the order that they were visited.
        backstack: deque = deque()

        vertices: deque = deque()
        visited: list = list()

        if unvisited is None:
            unvisited = [True] * self.v_count

        vertices.appendleft(v_start)
        while vertices:
            v: int = vertices.popleft()

            if unvisited[v]:
                unvisited[v] = False
                visited.append(v)
                backstack.appendleft(v)

                # Unroll backstack so that its top points to a vertex with at least one unvisited neighbor. Update
                # top_stack in the process.
                if top_stack is not None:
                    self._backtrack(unvisited, backstack, top_stack)

                if v == v_end:
                    break

                # Neighbors are pushed in descending order so that they are visited in ascending order.
                for neighbor in reversed(self.neighbors(v)):
                    if unvisited[neighbor]:
                        vertices.appendleft(neighbor)

        return visited

    def _backtrack(self, unvisited: list, backstack: deque, top_stack: deque) -> None:
        """
        While the vertex at the top of the backstack has no unvisited neighbors, pops the vertex and pushes it to the
        top_stack.

        This effectively rolls back the backstack so that either the stack is emptied or the top points to a vertex
        that has unvisited neighbors.

        The top_stack will contain the topological sorting of the graph in return.
        """

        while backstack:
            v: int = backstack[0]
            v_unvisited: list = list()
            for neighbor in self.neighbors(v):
                if unvisited[neighbor]:
                    v_unvisited.append(neighbor)

            if not v_unvisited:
                top_stack.appendleft(backstack.popleft())
            else:
                break
