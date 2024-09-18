import unittest
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        pre = [1 for _ in range(n)]
        for i in range(1, n):
            pre[i] = pre[i - 1] * nums[i - 1]

        suf = [1 for _ in range(n)]
        for i in range(n - 2, -1, -1):
            suf[i] = suf[i + 1] * nums[i + 1]

        return [p * s for(p, s) in zip(pre, suf)]


class SolutionTest(unittest.TestCase):
    def test_case_0(self):
        nums = [1, 2, 3, 4]
        exp = [24, 12, 8, 6]
        res = Solution().productExceptSelf(nums)
        self.assertEqual(res, exp)

    def test_case_1(self):
        nums = [-1, 1, 0, -3, 3]
        exp = [0, 0, 9, 0, 0]
        res = Solution().productExceptSelf(nums)
        self.assertEqual(res, exp)


if __name__ == "__main__":
    unittest.main()
