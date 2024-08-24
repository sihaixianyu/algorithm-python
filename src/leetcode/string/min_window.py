import unittest
from collections import defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ans: str = ""
        req_cnt = 0
        req_chars = defaultdict(int)

        for c in t:
            req_cnt += 1
            req_chars[c] += 1

        left = 0
        right = 0

        while right < len(s):
            add_char = s[right]
            right += 1

            if add_char in req_chars:
                if req_chars[add_char] > 0:
                    req_cnt -= 1
                req_chars[add_char] -= 1

            if req_cnt == 0:
                while req_cnt == 0:
                    rm_char = s[left]
                    left += 1
                    if rm_char in req_chars:
                        req_chars[rm_char] += 1
                        if req_chars[rm_char] > 0:
                            req_cnt += 1

                sub_s = s[left - 1 : right]
                if ans == "":
                    ans = sub_s
                else:
                    ans = sub_s if len(sub_s) < len(ans) else ans

        return ans


class SolutionTest(unittest.TestCase):
    def test_case_0(self):
        s = "ADOBECODEBANC"
        t = "ABC"
        ans = Solution().minWindow(s, t)
        exp = "BANC"
        self.assertEqual(ans, exp)

    def test_case_1(self):
        s = "a"
        t = "a"
        ans = Solution().minWindow(s, t)
        exp = "a"
        self.assertEqual(ans, exp)

    def test_case_2(self):
        s = "a"
        t = "aa"
        ans = Solution().minWindow(s, t)
        exp = ""
        self.assertEqual(ans, exp)

    def test_case_3(self):
        s = "ab"
        t = "a"
        ans = Solution().minWindow(s, t)
        exp = "a"
        self.assertEqual(ans, exp)


if __name__ == "__main__":
    unittest.main()
