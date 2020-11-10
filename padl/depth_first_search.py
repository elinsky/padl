class DepthFirstSearch:
    """Given a graph and a source vertex, DepthFirstSearch calculates how many vertices in the graph are connected to
    the source vertex, and which are connected.

    Args:
        graph (TODO): graph
        source_vertex (TODO): source vertex"""

    def __init__(self, graph, source_vertex):
        self.graph = graph
        self.source_vertex = source_vertex


    def marked(self, vertex):
        """True if there is a path between the source vertex and this vertex.  False if there does not exist a path."""
        # TODO
        return True
