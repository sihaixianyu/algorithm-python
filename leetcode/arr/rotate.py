from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for i in range(0, n - 1):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for i in range(n):
            for j in range(0, int(n / 2)):
                arr = matrix[i]
                arr[j], arr[n - 1 - j] = arr[n - 1 - j], arr[j]


if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]
    Solution().rotate(matrix)
    assert [
        [7, 4, 1],
        [8, 5, 2],
        [9, 6, 3],
    ] == matrix, matrix

    matrix = [
        [5, 1, 9, 11],
        [2, 4, 8, 10],
        [13, 3, 6, 7],
        [15, 14, 12, 16],
    ]
    Solution().rotate(matrix)
    assert [
        [15, 13, 2, 5],
        [14, 3, 4, 1],
        [12, 6, 8, 9],
        [16, 7, 10, 11],
    ] == matrix, matrix
