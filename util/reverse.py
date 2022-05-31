from typing import List


def reverse(nums: List[int]):
    n = len(nums)
    for i in range(int(n / 2)):
        nums[i], nums[n - 1 - i] = nums[n - 1 - i], nums[i]


if __name__ == "__main__":
    nums = [1, 2, 3]
    reverse(nums)
    assert [3, 2, 1] == nums, nums

    nums = [1, 2, 3, 4]
    reverse(nums)
    assert [4, 3, 2, 1] == nums, nums
