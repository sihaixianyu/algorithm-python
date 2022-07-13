import random
from typing import List


def quick_sort(nums: List[int]):
    random.shuffle(nums)
    sort(nums, 0, len(nums) - 1)


def sort(nums: List[int], left, right):
    if left >= right:
        return

    pivot = nums[left]
    lp, rp = left, right
    while lp < rp:
        while lp < rp and nums[rp] >= pivot:
            rp -= 1
        while lp < rp and nums[lp] <= pivot:
            lp += 1
        nums[lp], nums[rp] = nums[rp], nums[lp]

    nums[left], nums[lp] = nums[lp], nums[left]

    sort(nums, left, lp - 1)
    sort(nums, lp + 1, right)


if __name__ == "__main__":
    nums = [2, 5, 3, 4, 1]
    quick_sort(nums)
    print(nums)
    
    nums = [1, 2, 3, 4, 5]
    quick_sort(nums)
    print(nums)

    nums = [5, 4, 3, 2, 1]
    quick_sort(nums)
    print(nums)
