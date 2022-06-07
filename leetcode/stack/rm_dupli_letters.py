# 去除重复元素：https://leetcode.cn/problems/remove-duplicate-letters/
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stk = []
        cnt = {}
        in_stk = set()

        for c in s:
            cnt[ord(c)] += 1

        for c in s:
            cnt[ord(c)] -= 1

            if in_stk[ord(c)]:
                continue

            while len(stk) > 0 and ord(stk[-1]) > ord(c):
                if cnt[ord(stk[-1])] == 0:
                    break
                in_stk[ord(stk.pop())] = False

            stk.append(c)
            in_stk[ord(c)] = True

        res = "".join(stk)

        return res


if __name__ == "__main__":
    s = "bcabc"
    res = Solution().removeDuplicateLetters(s)
    print(res)
    assert res == "abc", res

    s = "cbacdcbc"
    res = Solution().removeDuplicateLetters(s)
    print(res)
    assert res == "acbd", res
