class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        def dp(i, j):
            if i < 0:
                return j + 1
            if j < 0:
                return i + 1

            if word1[i] == word2[j]:
                return dp(i - 1, j - 1)

            return min(dp(i, j - 1) + 1, dp(i - 1, j) + 1, dp(i - 1, j - 1) + 1)

        return dp(len(word1) - 1, len(word2) - 1)

    def minDistance2(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        memo = [[-1] * (n) for _ in range(m)]

        def dp(i, j):
            if i == -1:
                return j + 1
            if j == -1:
                return i + 1

            if memo[i][j] != -1:
                return memo[i][j]

            if word1[i] == word2[j]:
                memo[i][j] = dp(i - 1, j - 1)
            else:
                memo[i][j] = min(dp(i, j - 1) + 1, dp(i - 1, j) + 1, dp(i - 1, j - 1) + 1)

            return memo[i][j]

        return dp(m - 1, n - 1)

    def minDistance3(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            dp[i][0] = i
        for j in range(1, n + 1):
            dp[0][j] = j

        for i in range(1, len(word1) + 1):
            for j in range(1, len(word2) + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j - 1] + 1, dp[i][j - 1] + 1, dp[i - 1][j] + 1)

        return dp[-1][-1]


if __name__ == "__main__":
    word1, word2 = "horse", "ros"
    res = Solution().minDistance3(word1, word2)
    assert res == 3, res
