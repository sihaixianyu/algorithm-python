from typing import List


class Border:
    def __init__(self, up, down, left, right):
        self.up = up
        self.down = down
        self.left = left
        self.right = right

    def check(self) -> bool:
        if self.up - self.down == 1 or self.left - self.right == 1:
            return False

        return True


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        border = Border(0, len(matrix) - 1, 0, len(matrix[0]) - 1)

        i, j = 0, 0
        direction = (0, 1)
        while border.check():
            res.append(matrix[i][j])

            if i + direction[0] < border.up:
                border.left += 1
                direction = (0, 1)
            elif i + direction[0] > border.down:
                border.right -= 1
                direction = (0, -1)
            elif j + direction[1] < border.left:
                border.down -= 1
                direction = (-1, 0)
            elif j + direction[1] > border.right:
                border.up += 1
                direction = (1, 0)

            i += direction[0]
            j += direction[1]

        return res


if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]
    res = Solution().spiralOrder(matrix)
    assert res == [1, 2, 3, 6, 9, 8, 7, 4, 5], res
