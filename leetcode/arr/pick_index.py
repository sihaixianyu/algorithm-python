from bisect import bisect_left
from random import randint
from typing import List


class Solution:
    def __init__(self, w: List[int]):
        n = len(w)
        self.pref_sum = [0] * (n + 1)

        for i in range(1, n + 1):
            self.pref_sum[i] = self.pref_sum[i - 1] + w[i - 1]

    def pickIndex(self) -> int:
        rand_num = randint(1, self.pref_sum[-1])
        idx = bisect_left(self.pref_sum, rand_num)

        return idx - 1


if __name__ == "__main__":
    solution = Solution([1, 3])

    res = solution.pickIndex()
    print(res)
    res = solution.pickIndex()
    print(res)
    res = solution.pickIndex()
    print(res)
    res = solution.pickIndex()
    print(res)
