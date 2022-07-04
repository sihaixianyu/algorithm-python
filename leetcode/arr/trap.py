from typing import List


# 接雨水问题：https://leetcode.cn/problems/trapping-rain-water/
class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0

        for i in range(len(height)):
            vol = min(max(height[: i + 1]), max(height[i:])) - height[i]
            res += vol

        return res

    def trap2(self, height: List[int]) -> int:
        res = 0

        lmax = [0] * len(height)
        lmax[0] = height[0]
        for i in range(1, len(height)):
            lmax[i] = max(lmax[i - 1], height[i])

        rmax = [0] * len(height)
        rmax[-1] = height[-1]
        for i in reversed(range(0, len(height) - 1)):
            rmax[i] = max(rmax[i + 1], height[i])

        for i in range(len(height)):
            volume = min(lmax[i], rmax[i]) - height[i]
            res += volume

        return res

    def trap3(self, height: List[int]) -> int:
        res = 0
        lp, rp = 0, len(height) - 1
        lmax, rmax = 0, 0

        while lp < rp:
            lmax = max(lmax, height[lp])
            rmax = max(rmax, height[rp])

            if lmax < rmax:
                res += lmax - height[lp]
                lp += 1
            else:
                res += rmax - height[rp]
                rp -= 1

        return res


if __name__ == "__main__":
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    res = Solution().trap3(height)
    assert 6 == res, res

    height = [4, 2, 0, 3, 2, 5]
    res = Solution().trap3(height)
    assert 9 == res, res
