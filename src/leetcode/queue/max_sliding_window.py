import unittest
from collections import deque
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        ans = []
        que = deque()

        for i in range(n):
            while len(que) > 0 and que[0] == i - k:
                que.popleft()
            while len(que) > 0 and nums[que[-1]] < nums[i]:
                que.pop()
            que.append(i)

            if i >= k - 1:
                ans.append(nums[que[0]])

        return ans


class SolutionTest(unittest.TestCase):
    def test_case_0(self):
        nums = [1, 3, -1, -3, 5, 3, 6, 7]
        k = 3
        res = Solution().maxSlidingWindow(nums, k)
        exp = [3, 3, 5, 5, 6, 7]
        self.assertEqual(res, exp)

    def test_case_1(self):
        nums = [1]
        k = 1
        res = Solution().maxSlidingWindow(nums, k)
        exp = [1]
        self.assertEqual(res, exp)

    def test_case_2(self):
        nums = [7, 2, 4]
        k = 2
        res = Solution().maxSlidingWindow(nums, k)
        exp = [7, 4]
        self.assertEqual(res, exp)


if __name__ == "__main__":
    unittest.main()
