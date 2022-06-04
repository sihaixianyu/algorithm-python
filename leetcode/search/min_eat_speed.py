from math import ceil
from typing import List


def check(piles: List[int], h: int, k: int) -> bool:
    time = 0
    for p in piles:
        time += ceil(p / k)

    return time <= h


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        while left < right:
            k = left + (right - left) // 2
            if check(piles, h, k):
                right = k
            else:
                left = k + 1

        return left


if __name__ == "__main__":
    piles = [3, 6, 7, 11]
    h = 8
    res = Solution().minEatingSpeed(piles, h)
    assert res == 4, res

    piles = [30, 11, 23, 4, 20]
    h = 5
    res = Solution().minEatingSpeed(piles, h)
    assert res == 30, res
