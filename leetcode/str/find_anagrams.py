from typing import List


# 找到字符串中所有的字母异位词：https://leetcode.cn/problems/find-all-anagrams-in-a-string/
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        start_idxs = []
        need, window = {}, {}
        for c in p:
            need[c] = need.get(c, 0) + 1

        valid = 0
        lp, rp = 0, 0
        while rp < len(s):
            c = s[rp]
            rp += 1
            if c in need.keys():
                window[c] = window.get(c, 0) + 1
                if window[c] == need[c]:
                    valid += 1

            while lp < rp and valid == len(need):
                if rp - lp == len(p):
                    start_idxs.append(lp)

                c = s[lp]
                lp += 1

                if c in need.keys():
                    window[c] -= 1
                    if window[c] < need[c]:
                        valid -= 1
                        break

        return start_idxs


if __name__ == "__main__":
    solution = Solution()

    s = "cbaebabacd"
    p = "abc"
    res = solution.findAnagrams(s, p)
    assert [0, 6] == res, res

    s = "abab"
    p = "ab"
    res = solution.findAnagrams(s, p)
    assert [0, 1, 2] == res, res
