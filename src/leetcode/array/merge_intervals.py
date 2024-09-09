import unittest
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        @Prob: Merge Intervals
        @Link: https://leetcode.cn/problems/merge-intervals/description/?envType=study-plan-v2&envId=top-100-liked
        @Tags: ["array", "sorting"]
        """
        ans = []

        intervals.sort(key=lambda x: x[0])

        for interval in intervals:
            if ans and ans[-1][1] >= interval[0]:
                ans[-1][1] = max(ans[-1][1], interval[1])
                continue
            ans.append(interval)

        return ans


class SolutionTest(unittest.TestCase):
    def test_case_0(self):
        intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
        ans = Solution().merge(intervals)
        exp = [[1, 6], [8, 10], [15, 18]]
        self.assertEqual(ans, exp)

    def test_case_1(self):
        intervals = [[1, 4], [4, 5]]
        ans = Solution().merge(intervals)
        exp = [[1, 5]]
        self.assertEqual(ans, exp)


if __name__ == "__main__":
    unittest.main()
