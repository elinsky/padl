import typing

from padl.graph import Graph
from padl.search import Search


class DepthFirstSearch(Search):
    """Given an undirected unweighted graph and a source vertex, DepthFirstSearch calculates how many and which vertices
    in the graph are reachable from the source target.

    Args:
        graph : Graph to search.  Must be of type padl.Graph.
        source : source target from which to begin the depth first search."""

    def __init__(self, graph: Graph, source: typing.Hashable):
        self._count = 0
        self._marked = {}
        for vertex in graph.vertices():
            self._marked[vertex] = False

        self._dfs(source, graph)

    def marked(self, target: typing.Hashable) -> bool:
        """True if there is a path between the source vertex and the target vertex.  False if there does not exist a
        path.

        Args:
            target : target vertex.
        """
        return self._marked[target]

    def count(self) -> int:
        """Returns the number of vertices reachable from the source vertex."""
        return self._count

    def _mark(self, vertex) -> None:
        self._marked[vertex] = True
        self._count += 1

    def _dfs(self, vertex: typing.Hashable, graph: Graph) -> None:
        self._mark(vertex)
        adjacent_vertices = graph.adj(vertex)
        unmarked_adj_vertices = filter(lambda adj_vertex: not self.marked(adj_vertex), adjacent_vertices)
        for unmarked_adj in unmarked_adj_vertices:
            self._dfs(unmarked_adj, graph)
