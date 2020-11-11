import typing
from collections import deque
from queue import Queue

from padl.depth_first_search_paths import PathDoesNotExistError
from padl.graph import Graph
from padl.paths import Paths
from padl.search import Search


# TODO WRITE DOCSTRINGS

class BreadthFirstSearchPaths(Paths, Search):
    """Given an undirected unweighted graph and a source vertex, BreadthFirstPaths calculates the shortest path between
    the source vertex and all other vertices.

    Args:
        graph:  Graph to search.  Must be of type padl.Graph.
        source : source target from which to begin the breadth first search.
    """

    def __init__(self, graph: Graph, source: typing.Hashable):
        self._graph = graph
        self._source = source
        self._marked = {}  # Has this vertex been visited?
        self._edge_to = {}  # For key vertex, value indicates the vertex we came from
        self._queue = Queue()  # FIFO queue of vertices to further explore from

        self._marked[source] = True
        self._edge_to[source] = source
        self._queue.put(source)
        self._bfs()

    def marked(self, target: typing.Hashable) -> bool:
        """Returns true if the target vertex is reachable from the source vertex."""
        return target in self._marked

    def count(self) -> int:
        """Returns the number of vertices reachable from the start vertex."""
        return len(self._marked)

    def path_to(self, target: typing.Hashable) -> deque:
        """Returns the path from source to target in deque form.  This is guaranteed to be the shortest path, although
        it may not be the only shortest path that exists.  Throws an exception if the path does not exist."""
        if target not in self._marked:
            raise PathDoesNotExistError("There does not exist a path from the source to target vertex.")
        result = deque()  # Used as a stack.  Left side is the top.
        curr = target
        while curr != self._source:
            result.appendleft(curr)
            curr = self._edge_to[curr]
        result.appendleft(self._source)
        return result

    def has_path_to(self, target: typing.Hashable) -> bool:
        """Returns true if there exists a path between the source and target vertices."""
        return target in self._marked

    def _bfs(self):
        while not self._queue.empty():
            curr_vertex = self._queue.get()
            for adj_vertex in self._graph.adj(curr_vertex):
                if not self.marked(adj_vertex):
                    self._marked[adj_vertex] = True
                    self._edge_to[adj_vertex] = curr_vertex
                    self._queue.put(adj_vertex)
