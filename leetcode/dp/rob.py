from typing import List


# 打家劫舍问题：https://leetcode.cn/problems/house-robber/
class Solution:
    # Compressed DP
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp_i_2 = 0
        dp_i_1 = nums[0]

        dp_i = 0
        for i in range(2, n + 1):
            dp_i = max(dp_i_1, dp_i_2 + nums[i - 1])
            dp_i_2 = dp_i_1
            dp_i_1 = dp_i

        return dp_i

    # Bottom-up DP
    def rob_(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * (n + 1)
        dp[0] = 0
        dp[1] = nums[0]

        for i in range(2, n + 1):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i - 1])

        return dp[-1]

    # Top-down recursion
    def rob__(self, nums: List[int]) -> int:
        memo = [-1] * len(nums)

        def dp(i: int) -> int:
            if i >= len(nums):
                return 0

            if memo[i] != -1:
                return memo[i]

            res = max(nums[i] + dp(i + 2), dp(i + 1))
            memo[i] = res
            return res

        return dp(0)


if __name__ == "__main__":
    nums = [1, 2, 3, 1]
    res = Solution().rob(nums)
    assert 4 == res, res

    nums = [2, 7, 9, 3, 1]
    res = Solution().rob(nums)
    assert 12 == res, res

    nums = [2, 1, 1, 2]
    res = Solution().rob(nums)
    assert 4 == res, res
