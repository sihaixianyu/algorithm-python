import unittest
from typing import List
from collections import deque


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """Number of Islands: https://leetcode.cn/problems/number-of-islands/

        An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically

        Args:
            grid: A m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number
            of islands.

        Returns:
            Total num of islands under above definition.
        """
        num_islands = 0
        num_rows = len(grid)
        num_cols = len(grid[0])
        direction = ((1, 0), (-1, 0), (0, 1), (0, -1))

        def bfs(grid, x, y):
            level_locs = deque([(x, y)])
            while level_locs:
                loc = level_locs.popleft()
                for d in direction:
                    next_loc = (loc[0] + d[0], loc[1] + d[1])
                    if next_loc[0] < 0 or next_loc[0] >= num_rows or next_loc[1] < 0 or next_loc[1] >= num_cols:
                        continue
                    if grid[next_loc[0]][next_loc[1]] == "0":
                        continue
                    grid[next_loc[0]][next_loc[1]] = "0"
                    level_locs.append(next_loc)

        for i in range(num_rows):
            for j in range(num_cols):
                if grid[i][j] == "0":
                    continue
                num_islands += 1
                grid[i][j] = "0"
                bfs(grid, i, j)

        return num_islands


class SolutionTest(unittest.TestCase):
    def test_case_0(self):
        grid = [
            ["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"],
        ]
        num_islands = Solution().numIslands(grid)
        self.assertEqual(num_islands, 1)

    def test_case_1(self):
        grid = [
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"],
        ]
        num_islands = Solution().numIslands(grid)
        self.assertEqual(num_islands, 3)


if __name__ == "__main__":
    unittest.main()
