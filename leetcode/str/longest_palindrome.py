# 最长回文子串：https://leetcode.cn/problems/longest-palindromic-substring/
class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""

        for i in range(0, len(s)):
            odd = find_palindrome(s, i, i)
            if i > 0 and s[i] == s[i - 1]:
                even = find_palindrome(s, i - 1, i)
                if len(even) > len(odd):
                    odd = even

            res = odd if len(odd) > len(res) else res

        return res


def find_palindrome(s: str, left: int, right: int) -> str:
    while left > 0 and right < len(s) - 1 and s[left - 1] == s[right + 1]:
        left, right = left - 1, right + 1

    return s[left : right + 1]


if __name__ == "__main__":
    s = "babad"
    res = Solution().longestPalindrome(s)
    assert "bab" == res, res

    s = "cbbd"
    res = Solution().longestPalindrome(s)
    assert "bb" == res, res

    s = "ccc"
    res = Solution().longestPalindrome(s)
    assert "ccc" == res, res
