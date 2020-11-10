import pytest

from padl.depth_first_search import DepthFirstSearch


class TestDepthFirstSearch:

    @pytest.mark.parametrize("source, expected", [(0, 6), (3, 6), (6, 1)])
    def test_count(self, source, expected, tiny_graph):
        dfs = DepthFirstSearch(tiny_graph, source)
        actual = dfs.count()
        assert actual == expected

    @pytest.mark.parametrize("source, marked, expected",
                             [(0, 0, True), (0, 5, True), (3, 1, True), (1, 6, False), (6, 5, False)])
    def test_marked(self, source, marked, expected, tiny_graph):
        dfs = DepthFirstSearch(tiny_graph, source)
        actual = dfs.marked(marked)
        assert actual == expected
