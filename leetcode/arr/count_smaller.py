from collections import namedtuple
from typing import List

Pair = namedtuple("Pair", ["idx", "val"])


class Solution:
    def __init__(self):
        self.cnts = []
        self.pairs = []

    def countSmaller(self, nums: List[int]) -> List[int]:
        self.cnts = [0] * len(nums)
        self.pairs = [Pair(i, v) for i, v in enumerate(nums)]

        self.sort(0, len(self.pairs) - 1)

        return self.cnts

    def sort(self, left, right):
        if left == right:
            return

        mid = left + (right - left) // 2
        self.sort(left, mid)
        self.sort(mid + 1, right)

        self.merge(left, mid, right)

    def merge(self, left, mid, right):
        temp = []

        lp, rp = left, mid + 1
        while lp <= mid and rp <= right:
            if self.pairs[lp].val <= self.pairs[rp].val:
                self.cnts[self.pairs[lp].idx] += rp - mid - 1
                temp.append(self.pairs[lp])
                lp += 1
            else:
                temp.append(self.pairs[rp])
                rp += 1

        if rp == right + 1:
            while lp <= mid:
                self.cnts[self.pairs[lp].idx] += rp - mid - 1
                temp.append(self.pairs[lp])
                lp += 1
        else:
            temp.extend(self.pairs[rp : right + 1])

        self.pairs[left : right + 1] = temp


if __name__ == "__main__":
    nums = [5, 2, 6, 1]
    res = Solution().countSmaller(nums)
    assert res == [2, 1, 1, 0], res

    nums = [1, 2, 0]
    res = Solution().countSmaller(nums)
    assert res == [1, 1, 0], res
