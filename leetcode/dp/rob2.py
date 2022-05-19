from typing import List


# 打家劫舍问题：https://leetcode.cn/problems/house-robber-ii/
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        def robRange(nums) -> int:
            n = len(nums)

            dp = [0] * (n + 1)
            dp[0] = 0
            dp[1] = nums[0]

            for i in range(2, n + 1):
                dp[i] = max(dp[i - 1], dp[i - 2] + nums[i - 1])

            return dp[-1]

        return max(robRange(nums[0:-1]), robRange(nums[1:]))


if __name__ == "__main__":
    nums = [2, 3, 2]
    res = Solution().rob(nums)
    assert 3 == res, res

    nums = [1, 2, 3, 1]
    res = Solution().rob(nums)
    assert 4 == res, res

    nums = [1, 2, 3]
    res = Solution().rob(nums)
    assert 3 == res, res
