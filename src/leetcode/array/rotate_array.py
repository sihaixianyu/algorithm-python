import unittest
from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        @Prob: Rotate Array
        @Link: https://leetcode.cn/problems/rotate-array/?envType=study-plan-v2&envId=top-100-liked
        @Tags: ["Array", "Math", "TwoPointers"]
        """

        def reverse(left: int, right: int) -> None:
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        k = k % len(nums)
        reverse(0, len(nums) - 1)
        reverse(0, k - 1)
        reverse(k, len(nums) - 1)


class SolutionTest(unittest.TestCase):
    def test_case_0(self):
        nums = [1, 2, 3, 4, 5, 6, 7]
        k = 3
        Solution().rotate(nums, k)
        exp = [5, 6, 7, 1, 2, 3, 4]
        self.assertEqual(nums, exp)

    def test_case_1(self):
        nums = [-1, -100, 3, 99]
        k = 2
        Solution().rotate(nums, k)
        exp = [3, 99, -1, -100]
        self.assertEqual(nums, exp)


if __name__ == "__main__":
    unittest.main()
