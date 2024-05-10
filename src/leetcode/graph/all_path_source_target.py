import unittest
from typing import List


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        tgt_node = len(graph) - 1
        cur_path = list()
        all_paths = list()

        def dfs(cur_node):
            if len(cur_path) > len(graph):
                return

            cur_path.append(cur_node)

            if cur_node == tgt_node:
                all_paths.append(cur_path[:])

            for next_node in graph[cur_node]:
                dfs(next_node)
                cur_path.pop()

        dfs(0)
        
        return all_paths


class SolutionTest(unittest.TestCase):
    def test_case_0(self):
        graph = [[1, 2], [3], [3], []]
        ans = Solution().allPathsSourceTarget(graph)
        self.assertEqual(ans, [[0, 1, 3], [0, 2, 3]])

    def test_case_1(self):
        graph = [[4, 3, 1], [3, 2, 4], [3], [4], []]
        ans = Solution().allPathsSourceTarget(graph)
        self.assertEqual(
            ans, [[0, 4], [0, 3, 4], [0, 1, 3, 4], [0, 1, 2, 3, 4], [0, 1, 4]]
        )
