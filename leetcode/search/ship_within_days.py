from typing import List


# 在D天内送达包裹的能力:
# https://leetcode.cn/problems/capacity-to-ship-packages-within-d-days/
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left, right = max(weights), sum(weights)
        while left < right:
            load = left + (right - left) // 2
            if check(weights, days, load):
                right = load
            else:
                left = load + 1

        return left


def check(weights: List[int], days: int, load: int):
    load_sum = 0
    day_cnt = 1
    for w in weights:
        if load_sum + w <= load:
            load_sum += w
        else:
            day_cnt += 1
            load_sum = w

    return day_cnt <= days


if __name__ == "__main__":
    weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    days = 5
    res = Solution().shipWithinDays(weights, days)
    assert res == 15, res

    weights = [3, 2, 2, 4, 1, 4]
    days = 3
    res = Solution().shipWithinDays(weights, days)
    assert res == 6, res

    weights = [1, 2, 3, 1, 1]
    days = 4
    res = Solution().shipWithinDays(weights, days)
    assert res == 3, res
