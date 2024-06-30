import collections
import unittest
from typing import List


class Solution:
    _DIRECTIONS = ((-1, 0), (1, 0), (0, -1), (0, 1))

    def orangesRotting(self, grid: List[List[int]]) -> int:
        num_rows = len(grid)
        num_cols = len(grid[0])
        depth = 0

        queue = collections.deque()
        for i, _ in enumerate(grid):
            for j, val in enumerate(grid[i]):
                if val == 2:
                    queue.append((i, j, depth))

        def find_neighbors(row, col):
            for move_row, move_col in self._DIRECTIONS:
                next_row = row + move_row
                next_col = col + move_col
                if 0 <= next_row < num_rows and 0 <= next_col < num_cols:
                    yield (next_row, next_col)


        while queue:
            r, c, depth = queue.popleft()
            for next_row, next_col in find_neighbors(r, c):
                if grid[next_row][next_col] == 1:
                    grid[next_row][next_col] = 2
                    queue.append((next_row, next_col, depth+1))

        if any(1 in row for row in grid):
            return -1

        return depth


class SolutionTest(unittest.TestCase):
    def test_case_0(self):
        grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
        ans = Solution().orangesRotting(grid)
        self.assertEqual(ans, 4)

    def test_case_1(self):
        grid = [[2, 1, 1], [0, 1, 1], [1, 0, 1]]
        ans = Solution().orangesRotting(grid)
        self.assertEqual(ans, -1)

    def test_case_2(self):
        grid = [[0, 2]]
        ans = Solution().orangesRotting(grid)
        self.assertEqual(ans, 0)


if __name__ == "__main__":
    unittest.main()
