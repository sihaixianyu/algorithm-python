from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        size = len(nums)
        if size < 4:
            return []

        res = []
        nums.sort()

        for i in range(0, size - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, size - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                two_sum = target - nums[i] - nums[j]
                m, n = j + 1, size - 1

                while m < n:
                    sum = nums[m] + nums[n]
                    if sum == two_sum:
                        res.append([nums[i], nums[j], nums[m], nums[n]])
                        m, n = m + 1, n - 1
                        while m < n and nums[m] == nums[m - 1]:
                            m += 1
                        while m < n and nums[n] == nums[n + 1]:
                            n -= 1
                    elif sum < two_sum:
                        m += 1
                    elif sum > two_sum:
                        n -= 1

        return res


if __name__ == "__main__":
    nums = [1, 0, -1, 0, -2, 2]
    target = 0
    res = Solution().fourSum(nums, target)
    assert res == [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]], res

    nums = [2, 2, 2, 2, 2]
    target = 8
    res = Solution().fourSum(nums, target)
    assert res == [[2, 2, 2, 2]], res

    nums = [-3, -2, -1, 0, 0, 1, 2, 3]
    target = 0
    res = Solution().fourSum(nums, target)
    assert res == [
        [-3, -2, 2, 3],
        [-3, -1, 1, 3],
        [-3, 0, 0, 3],
        [-3, 0, 1, 2],
        [-2, -1, 0, 3],
        [-2, -1, 1, 2],
        [-2, 0, 0, 2],
        [-1, 0, 0, 1],
    ], res
