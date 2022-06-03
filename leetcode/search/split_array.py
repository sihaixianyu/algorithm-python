from typing import List


def check(nums: List[int], max_sum: int, m: int) -> bool:
    sum, cnt = 0, 1
    for i in range(len(nums)):
        if sum + nums[i] <= max_sum:
            sum += nums[i]
        else:
            sum = nums[i]
            cnt += 1

    return cnt <= m


class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        left, right = 0, 0
        for num in nums:
            left = max(left, num)
            right += num

        while left < right:
            mid = left + (right - left) // 2
            if check(nums, mid, m):
                right = mid
            else:
                left = mid + 1

        return left


if __name__ == "__main__":
    nums = [7, 2, 5, 10, 8]
    m = 2
    res = Solution().splitArray(nums, m)
    assert res == 18, res

    nums = [1, 4, 4]
    m = 3
    res = Solution().splitArray(nums, m)
    assert res == 4, res
