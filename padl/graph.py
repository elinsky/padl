class Graph:
    """Data structure for unweighted undirected graphs.  Vertices must be immutable hashable objects.  Self-loops and
    parallel edges are not supported."""

    def __init__(self):
        self._adjacency_matrix = {}
        self._num_edges = 0

    def v(self):
        """Returns the number of vertices in the graph."""
        return len(self._adjacency_matrix)

    def e(self):
        """Returns the number of edges in the graph."""
        return self._num_edges

    def add_edge(self, v, w):
        """Adds an edge to the graph between vertices V and W.  Vertices V and W must already be present"""
        if v not in self._adjacency_matrix:
            raise VertexNotPresentError("Vertex " + str(v) + " not present in graph.")
        if w not in self._adjacency_matrix:
            raise VertexNotPresentError("Vertex " + str(w) + " not present in graph.")
        if self.has_edge(v, w):
            return
        else:
            self._adjacency_matrix[v].add(w)
            self._adjacency_matrix[w].add(v)
            self._num_edges += 1
            return

    def vertices(self):
        """Returns an iterator of vertices in the graph."""
        return iter(self._adjacency_matrix.keys())

    def add_vertex(self, v):
        """Adds vertex V to the graph.  If the vertex already exists, nothing happens."""
        if v not in self._adjacency_matrix:
            self._adjacency_matrix[v] = set()

    def adj(self, v):
        """Returns an iterable of vertices adjacent to vertex V."""
        return iter(self._adjacency_matrix[v])

    def has_edge(self, v, w):
        """Returns True if edge between V and W is present in graph.  Else returns False."""
        return True if w in self._adjacency_matrix[v] else False

    def has_vertex(self, v):
        """Returns True if vertex is present in graph.  Else returns False."""
        return True if v in self._adjacency_matrix else False

    def __str__(self):
        result = ""
        for v in self._adjacency_matrix:
            result += str(v)
            result += " : "
            if len(self._adjacency_matrix[v]) > 0:
                for e in self._adjacency_matrix[v]:
                    result += str(e)
                    result += ", "
                result = result[:-2]
                result += "\n"
        return result

# TODO should I have type hints?
# TODO should I have an interface for this?

class VertexNotPresentError(Exception):
    pass
