import unittest
import collections
from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Surrounded Regions: https://leetcode.cn/problems/surrounded-regions/
        """
        m, n = len(board), len(board[0])

        def bfs(x, y):
            directions = ((-1, 0), (1, 0), (0, -1), (0, 1))
            sinkable_locs = {(x, y)}
            level_locs = collections.deque()
            level_locs.append((x, y))

            while level_locs:
                cur_loc = level_locs.popleft()
                for d in directions:
                    next_loc = (cur_loc[0] + d[0], cur_loc[1] + d[1])
                    next_x, next_y = next_loc[0], next_loc[1]
                    if next_x < 0 or next_x >= m or next_y < 0 or next_y >= n:
                        return
                    if board[next_x][next_y] == "X" or next_loc in sinkable_locs:
                        continue
                    level_locs.append(next_loc)
                    sinkable_locs.add(next_loc)

            for loc in sinkable_locs:
                board[loc[0]][loc[1]] = "X"

        for x in range(m):
            for y in range(n):
                if board[x][y] == "X":
                    continue
                bfs(x, y)


class SolutionTest(unittest.TestCase):
    def test_case_0(self):
        board = [["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"]]
        Solution().solve(board)
        self.assertEqual(
            board, [["X", "X", "X", "X"], ["X", "X", "X", "X"], ["X", "X", "X", "X"], ["X", "O", "X", "X"]]
        )

    def test_case_1(self):
        board = [["X"]]
        Solution().solve(board)
        self.assertEqual(board, [["X"]])


if __name__ == "__main__":
    unittest.main()
