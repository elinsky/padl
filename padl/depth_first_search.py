import typing

from padl.graph import Graph


class DepthFirstSearch:
    """Given an undirected unweighted graph and a source vertex, DepthFirstSearch calculates how many and which vertices
    in the graph are reachable from the source vertex.

    Args:
        graph : Graph to search.  Must be of type padl.Graph.
        source : source vertex from which to begin the depth first search."""

    def __init__(self, graph: Graph, source: typing.Hashable):
        self.graph = graph
        self.source = source
        self._count = 0
        self._marked = {}
        for vertex in graph.vertices():
            self._marked[vertex] = False

        self._mark(source)
        self._dfs(source, graph)

    def marked(self, vertex: typing.Hashable) -> bool:
        """True if there is a path between the source vertex and this vertex.  False if there does not exist a path."""
        return self._marked[vertex]

    def count(self) -> int:
        """Returns the number of vertices reachable from the source vertex."""
        return self._count

    def _mark(self, vertex) -> None:
        self._marked[vertex] = True
        self._count += 1

    def _dfs(self, vertex: typing.Hashable, graph: Graph) -> None:
        for adjacent_vertex in graph.adj(vertex):
            if not self.marked(adjacent_vertex):
                self._mark(adjacent_vertex)
                self._dfs(adjacent_vertex, graph)
