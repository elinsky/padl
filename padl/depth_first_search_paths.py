import typing
from collections import deque

from padl.graph import Graph


class DepthFirstSearchPaths:
    """Given an undirected unweighted graph and a source vertex, DepthFirstSearchPaths calculates whether or not there
    exists a path from the source to the target, and if it exists, the path.

    Args:
        graph : Graph to search.  Must be of type padl.Graph.
        source : source target from which to begin the depth first search."""

    def __init__(self, graph: Graph, source: typing.Hashable):
        self._count = 0
        self._marked = {}
        self._source = source
        self._edge_to = {}
        for vertex in graph.vertices():
            self._marked[vertex] = False

        self._edge_to[source] = source
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

    def path_to(self, target: typing.Hashable) -> deque:
        """Returns a deque that contains the path from the source vertex to the target.

        Args:
            target : target vertex.
        """
        if target not in self._edge_to:
            raise PathDoesNotExistError("There does not exist a path from " + str(self._source) + " to " + str(target) + ".")
        result = deque()
        curr = target
        while curr != self._source:
            result.appendleft(curr)
            curr = self._edge_to[curr]
        result.appendleft(self._source)
        return result

    def _mark(self, vertex) -> None:
        self._marked[vertex] = True
        self._count += 1

    def _dfs(self, vertex: typing.Hashable, graph: Graph) -> None:
        self._mark(vertex)
        adjacent_vertices = graph.adj(vertex)
        unmarked_adj_vertices = filter(lambda adj_vertex: not self.marked(adj_vertex), adjacent_vertices)
        for unmarked_adj in unmarked_adj_vertices:
            self._edge_to[unmarked_adj] = vertex
            self._dfs(unmarked_adj, graph)

class PathDoesNotExistError(Exception):
    pass
