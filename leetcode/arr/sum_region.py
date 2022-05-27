import pprint
from typing import List


class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        m, n = len(matrix), len(matrix[0])
        self.pre_sum = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                self.pre_sum[i][j] = (
                    matrix[i - 1][j - 1]
                    + self.pre_sum[i][j - 1]
                    + self.pre_sum[i - 1][j]
                    - self.pre_sum[i - 1][j - 1]
                )

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return (
            self.pre_sum[row2 + 1][col2 + 1]
            + self.pre_sum[row1][col1]
            - self.pre_sum[row1][col2 + 1]
            - self.pre_sum[row2 + 1][col1]
        )


if __name__ == "__main__":
    matrix = [
        [3, 0, 1, 4, 2],
        [5, 6, 3, 2, 1],
        [1, 2, 0, 1, 5],
        [4, 1, 0, 1, 7],
        [1, 0, 3, 0, 5],
    ]
    num_matrix = NumMatrix(matrix)
    pprint.pprint(num_matrix.pre_sum)
    res = num_matrix.sumRegion(2, 1, 4, 3)
    assert 8 == res, res
