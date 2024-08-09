import unittest
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        total_water = 0

        left_tops = [0 for _ in range(n)]
        right_tops = [0 for _ in range(n)]

        left_tops[0], left_tops[-1] = height[0], height[-1]
        right_tops[0], right_tops[-1] = height[0], height[-1]

        for i in range(1, n - 1):
            left_tops[i] = max(height[i], left_tops[i - 1])
            right_tops[n - i - 1] = max(height[n - i - 1], right_tops[n - i])

        for i in range(1, n - 1):
            total_water += min(left_tops[i], right_tops[i]) - height[i]

        return total_water


class SolutionTest(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_case_0(self):
        height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
        exp = 6
        res = self.solution.trap(height)
        self.assertEqual(res, exp)

    def test_case_1(self):
        height = [4, 2, 0, 3, 2, 5]
        exp = 9
        res = self.solution.trap(height)
        self.assertEqual(res, exp)


if __name__ == "__main__":
    unittest.main()
