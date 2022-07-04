from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid) == 0:
            return 0

        cnt = 0
        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                if grid[i][j] == "1":
                    cnt += 1
                    dfs(grid, i, j)

        return cnt


def dfs(grid, i, j):
    if not valid(grid, i, j):
        return
    if grid[i][j] == "0":
        return

    grid[i][j] = "0"
    dfs(grid, i - 1, j)
    dfs(grid, i + 1, j)
    dfs(grid, i, j - 1)
    dfs(grid, i, j + 1)


def valid(grid, i, j) -> bool:
    height = len(grid)
    width = len(grid[0])

    if (0 <= i < height) and (0 <= j < width):
        return True

    return False


if __name__ == "__main__":
    grid = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"],
    ]
    res = Solution().numIslands(grid)
    assert 1 == res, res
