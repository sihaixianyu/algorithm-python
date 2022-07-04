from typing import List


class Solution:
    def __init__(self):
        self.lower = None
        self.upper = None
        self.res = 0

    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        self.lower = lower
        self.upper = upper

        pre_sum = [0] * (len(nums) + 1)
        for i, v in enumerate(nums):
            pre_sum[i + 1] = pre_sum[i] + v

        self.sort(pre_sum, 0, len(pre_sum) - 1)

        return self.res

    def sort(self, pre_sum, left, right):
        if left == right:
            return

        mid = left + (right - left) // 2
        self.sort(pre_sum, left, mid)
        self.sort(pre_sum, mid + 1, right)
        self.merge(pre_sum, left, mid, right)

    def merge(self, pre_sum, left, mid, right):
        for i in range(left, mid + 1):
            start, end = mid + 1, mid + 1
            while start <= right and pre_sum[start] - pre_sum[i] < self.lower:
                start += 1
            while end <= right and pre_sum[end] - pre_sum[i] <= self.upper:
                end += 1
            self.res += end - start

        temp = []
        lp, rp = left, mid + 1
        while lp <= mid and rp <= right:
            if pre_sum[lp] <= pre_sum[rp]:
                temp.append(pre_sum[lp])
                lp += 1
            else:
                temp.append(pre_sum[rp])
                rp += 1

        if lp == mid + 1:
            temp.extend(pre_sum[rp : right + 1])
        else:
            temp.extend(pre_sum[lp : mid + 1])

        pre_sum[left : right + 1] = temp


if __name__ == "__main__":
    nums = [-2, 5, -1]
    res = Solution().countRangeSum(nums, -2, 2)
    assert res == 3, res
