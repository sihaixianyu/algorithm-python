from typing import List


# 股票买卖问题：https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-iv/
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        dp_empty = [[0] * (k + 1) for _ in range(len(prices))]
        dp_full = [[0] * (k + 1) for _ in range(len(prices))]

        for i in range(0, len(prices)):
            for j in range(1, k+1):
                if i == 0:
                    dp_empty[i][j] = 0
                    dp_full[i][j] = -prices[i]
                    print(f"day:{i} cnt: {j}:", dp_empty[i], dp_full[i])
                    continue

                dp_empty[i][j] = max(dp_empty[i - 1][j], dp_full[i - 1][j] + prices[i])
                dp_full[i][j] = max(
                    dp_full[i - 1][j], dp_empty[i - 1][j - 1] - prices[i]
                )
                print(f"day:{i} cnt: {j}:", dp_empty[i], dp_full[i])

        return dp_empty[-1][-1]


if __name__ == "__main__":
    prices = [2, 4, 1]
    res = Solution().maxProfit(2, prices)
    assert 2 == res, res

    prices = [3, 2, 6, 5, 0, 3]
    res = Solution().maxProfit(2, prices)
    assert 7 == res, res
