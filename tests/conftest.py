import pytest

from padl.graph import Graph


@pytest.fixture()
def tiny_graph():
    graph = Graph()
    for vertex in range(0, 7):
        graph.add_vertex(vertex)
    edges = [(0, 1), (0, 2), (0, 5), (1, 2), (2, 3), (2, 4), (3, 4), (3, 5)]
    for v, w in edges:
        graph.add_edge(v, w)
    return graph
