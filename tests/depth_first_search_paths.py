from collections import deque

import pytest

from padl.depth_first_search_paths import DepthFirstSearchPaths, PathDoesNotExistError


class TestDepthFirstSearchPaths:

    @pytest.mark.parametrize("source, expected", [(0, 6), (3, 6), (6, 1)])
    def test_count(self, source, expected, tiny_graph):
        dfsp = DepthFirstSearchPaths(tiny_graph, source)
        actual = dfsp.count()
        assert actual == expected

    @pytest.mark.parametrize("source, marked, expected",
                             [(0, 0, True), (0, 5, True), (3, 1, True), (1, 6, False), (6, 5, False)])
    def test_marked(self, source, marked, expected, tiny_graph):
        dfsp = DepthFirstSearchPaths(tiny_graph, source)
        actual = dfsp.marked(marked)
        assert actual == expected

    @pytest.mark.parametrize("source, target, expected",
                             [(0, 3, deque([0, 1, 2, 3])), (5, 4, deque([5, 0, 1, 2, 3, 4])), (4, 0, deque([4, 2, 0])),
                              (6, 6, deque([6]))])
    def test_path_to(self, source, target, expected, tiny_graph):
        dfsp = DepthFirstSearchPaths(tiny_graph, source)
        actual = dfsp.path_to(target)
        assert actual == expected

    def test_path_to_raises_exception(self, tiny_graph):
        with pytest.raises(PathDoesNotExistError):
            dfsp = DepthFirstSearchPaths(tiny_graph, 3)
            dfsp.path_to(6)
