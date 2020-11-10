import pytest

from padl.graph import Graph
from padl.graph import VertexNotPresentError


class TestGraph:
    @pytest.fixture()
    def tiny_graph(self):
        graph = Graph()
        for vertex in range(0, 7):
            graph.add_vertex(vertex)
        edges = [(0, 1), (0, 2), (0, 5), (1, 2), (2, 3), (2, 4), (3, 4), (3, 5)]
        for v, w in edges:
            graph.add_edge(v, w)
        return graph

    def test_v(self, tiny_graph):
        actual = tiny_graph.v()
        expected = 7
        assert actual == expected

    def test_e(self, tiny_graph):
        actual = tiny_graph.e()
        expected = 8
        assert actual == expected

    @pytest.mark.parametrize("vertex, expected", [(-1, False), (0, True), (5, True), (6, True), (7, False)])
    def test_has_vertex(self, vertex, expected, tiny_graph):
        actual = tiny_graph.has_vertex(vertex)
        assert actual == expected

    @pytest.mark.parametrize("vertex, expected", [(0, {1, 2, 5}), (3, {2, 4, 5}), (6, set())])
    def test_adj(self, vertex, expected, tiny_graph):
        # vertex = 0
        # expected = {1, 2, 5}
        actual = set(tiny_graph.adj(vertex))
        assert actual == expected

    def test_str(self, tiny_graph):
        expected = "0 : 1, 2, 5\n1 : 0, 2\n2 : 0, 1, 3, 4\n3 : 2, 4, 5\n4 : 2, 3\n5 : 0, 3\n6 : "
        actual = str(tiny_graph)
        assert expected == actual

    @pytest.mark.parametrize("v, w", [(-1, 0), (0, -1)])
    def test_add_edge(self, v, w, tiny_graph):
        with pytest.raises(VertexNotPresentError):
            tiny_graph.add_edge(v, w)

    def test_vertices(self, tiny_graph):
        expected = {0, 1, 2, 3, 4, 5, 6}
        actual = set(tiny_graph.vertices())
        assert expected == actual
