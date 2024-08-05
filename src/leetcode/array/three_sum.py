import unittest
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []

        nums.sort()

        for k in range(n - 2):
            if nums[k] > 0:
                continue
            if k > 0 and nums[k] == nums[k - 1]:
                continue

            i = k + 1
            j = n - 1
            while i < j:
                if nums[k] + nums[i] + nums[j] < 0:
                    i += 1
                    continue

                if nums[k] + nums[i] + nums[j] > 0:
                    j -= 1
                    continue

                res.append([nums[k], nums[i], nums[j]])
                while i < j and nums[i + 1] == nums[i]:
                    i += 1
                while i < j and nums[j - 1] == nums[j]:
                    j -= 1
                i += 1
                j -= 1

        return res


class SolutionTest(unittest.TestCase):
    def setUp(self) -> None:
        self._solution = Solution()

    def test_case_0(self):
        nums = [-1, 0, 1, 2, -1, -4]
        res = self._solution.threeSum(nums)
        self.assertEqual(res, [[-1, -1, 2], [-1, 0, 1]])

    def test_case_1(self):
        nums = [0, 1, 1]
        res = self._solution.threeSum(nums)
        self.assertEqual(res, [])

    def test_case_2(self):
        nums = [0, 0, 0]
        res = self._solution.threeSum(nums)
        self.assertEqual(res, [[0, 0, 0]])

    def test_case_3(self):
        nums = [-2, 0, 0, 2, 2]
        res = self._solution.threeSum(nums)
        self.assertEqual(res, [[-2, 0, 2]])


if __name__ == "__main__":
    unittest.main()
