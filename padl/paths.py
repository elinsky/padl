import typing
from abc import ABC, abstractmethod
from collections import deque


class Paths(ABC):
    """Defines the path-finding operations that work on a undirected, unweighted graph."""

    @abstractmethod
    def path_to(self, target: typing.Hashable) -> deque:
        """Returns a path from the source vertex to the target vertex.  This path is not guaranteed to be the only path
        that exists, or the shortest path.
        """
        pass

    @abstractmethod
    def has_path_to(self, target: typing.Hashable) -> bool:
        """True if there exists a path between the source and target vertices."""
        pass
