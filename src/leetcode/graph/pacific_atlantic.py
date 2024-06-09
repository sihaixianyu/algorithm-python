from typing import List
from unittest import TestCase


class Solution:
    DIRECTIONS = ((-1, 0), (1, 0), (0, -1), (0, 1))

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        n = len(heights[0])

        def dfs(x, y, visited):
            if visited[x][y]:
                return
            visited[x][y] = True
            for d in Solution.DIRECTIONS:
                next_x = x + d[0]
                next_y = y + d[1]
                if next_x < 0 or next_x >= m or next_y < 0 or next_y >= n:
                    continue
                if heights[x][y] > heights[next_x][next_y]:
                    continue
                dfs(next_x, next_y, visited)

        pacific = [[False for _ in range(n)] for _ in range(m)]
        atlantic = [[False for _ in range(n)] for _ in range(m)]

        for i in range(m):
            dfs(i, 0, pacific)
            dfs(i, n - 1, atlantic)
        for j in range(n):
            dfs(0, j, pacific)
            dfs(m - 1, j, atlantic)

        result = []

        for i in range(m):
            for j in range(n):
                if pacific[i][j] and atlantic[i][j]:
                    result.append([i, j])

        return result


class SolutionTest(TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_case_0(self):
        heights = [[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]]
        valid_locs = self.solution.pacificAtlantic(heights)

        valid_locs = set(map(lambda x: tuple(x), valid_locs))
        expected = set(map(lambda x: tuple(x), [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]]))
        self.assertEqual(valid_locs, expected)

    def test_case_1(self):
        heights = [[1]]
        valid_locs = self.solution.pacificAtlantic(heights)

        valid_locs = set(map(lambda x: tuple(x), valid_locs))
        expected = set(map(lambda x: tuple(x), [[0, 0]]))
        self.assertEqual(valid_locs, expected)

    def test_case_2(self):
        heights = [[1, 2, 3], [8, 9, 4], [7, 6, 5]]
        valid_locs = self.solution.pacificAtlantic(heights)

        valid_locs = set(map(lambda x: tuple(x), valid_locs))
        expected = set(map(lambda x: tuple(x), [[0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]]))
        self.assertEqual(valid_locs, expected)
