import typing
from abc import ABC, abstractmethod


class Search(ABC):
    """Defines the graph search operations that work on an undirected, unweighted graph."""

    @abstractmethod
    def marked(self, target: typing.Hashable) -> bool:
        """Returns true if the target vertex is reachable from the source vertex."""
        pass

    @abstractmethod
    def count(self) -> int:
        """Returns the number of vertexes that are reachable from the source vertex.  Includes the source vertex."""
        pass
