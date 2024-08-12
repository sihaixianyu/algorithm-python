import unittest
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        m = len(s)
        n = len(p)

        if m < n:
            return res

        window = [0 for _ in range(26)]
        pattern = [0 for _ in range(26)]

        for i in range(n):
            window[ord(s[i]) - ord("a")] += 1
            pattern[ord(p[i]) - ord("a")] += 1

        if window == pattern:
            res.append(0)

        for i in range(n, m):
            window[ord(s[i - n]) - ord("a")] -= 1
            window[ord(s[i]) - ord("a")] += 1
            if window == pattern:
                res.append(i - n + 1)

        return res


class SolutionTest(unittest.TestCase):
    def setUp(self) -> None:
        self._solution = Solution()

    def test_case_0(self):
        s = "cbaebabacd"
        p = "abc"
        res = self._solution.findAnagrams(s, p)
        exp = [0, 6]
        self.assertEqual(res, exp)

    def test_case_1(self):
        s = "abab"
        p = "ab"
        res = self._solution.findAnagrams(s, p)
        exp = [0, 1, 2]
        self.assertEqual(res, exp)

    def test_case_2(self):
        s = "abacbabc"
        p = "abc"
        res = self._solution.findAnagrams(s, p)
        exp = [1, 2, 3, 5]
        self.assertEqual(res, exp)

    def test_case_3(self):
        s = "abaacbabc"
        p = "abc"
        res = self._solution.findAnagrams(s, p)
        exp = [3, 4, 6]
        self.assertEqual(res, exp)


if __name__ == "__main__":
    unittest.main()
