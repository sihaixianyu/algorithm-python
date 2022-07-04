from typing import List


class Solution:
    def __init__(self):
        self.cnt = 0
        self.nums: List[int] = None

    def reversePairs(self, nums: List[int]) -> int:
        self.nums = nums
        self.sort(nums, 0, len(nums) - 1)
        return self.cnt

    def sort(self, nums, left, right):
        if left == right:
            return

        mid = left + (right - left) // 2
        self.sort(nums, left, mid)
        self.sort(nums, mid + 1, right)
        self.merge(nums, left, mid, right)

    def merge(self, nums, left, mid, right):
        i, j = left, mid + 1
        while i <= mid:
            while j <= right and nums[i] > 2 * nums[j]:
                j += 1
            self.cnt += j - mid - 1
            i += 1

        temp = []
        lp, rp = left, mid + 1
        while lp <= mid and rp <= right:
            if nums[lp] <= nums[rp]:
                temp.append(nums[lp])
                lp += 1
            else:
                temp.append(nums[rp])
                rp += 1

        if rp == right + 1:
            temp.extend(nums[lp : mid + 1])
        else:
            temp.extend(nums[rp : right + 1])

        nums[left : right + 1] = temp


if __name__ == "__main__":
    nums = [2, 4, 3, 5, 1]
    res = Solution().reversePairs(nums)
    assert res == 3, res

    nums = [-5, -5]
    res = Solution().reversePairs(nums)
    assert res == 1, res
