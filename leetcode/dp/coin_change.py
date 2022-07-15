import sys
from typing import List


# 硬币兑换：https://leetcode.cn/problems/coin-change/
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def dp(amount):
            if amount == 0:
                return 0
            if amount < 0:
                return -1
            if amount in memo:
                return memo[amount]

            res = sys.maxsize
            for coin in coins:
                sub_res = dp(amount - coin)
                if sub_res == -1:
                    continue
                res = min(res, sub_res + 1)

            memo[amount] = res if res != sys.maxsize else -1
            return memo[amount]

        return dp(amount)

    def coinChange_(self, coins: List[int], amount: int) -> int:
        dp = [sys.maxsize] * (amount + 1)
        dp[0] = 0

        for i in range(0, amount + 1):
            for coin in coins:
                if i - coin < 0:
                    continue
                dp[i] = min(dp[i], dp[i - coin] + 1)

        return dp[-1] if dp[-1] != sys.maxsize else -1


if __name__ == "__main__":
    coins = [1, 2, 5]
    amount = 11
    res = Solution().coinChange(coins, amount)
    assert 3 == res, res
    res = Solution().coinChange_(coins, amount)
    assert 3 == res, res
