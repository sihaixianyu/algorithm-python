from typing import List


def left_bound(nums: List[int], tar: int) -> int:
    lp, rp = 0, len(nums)

    while lp < rp:
        mid = lp + (rp - lp) // 2
        if nums[mid] == tar:
            rp = mid
        elif nums[mid] < tar:
            lp = mid + 1
        elif nums[mid] > tar:
            rp = mid
        
    if lp == len(nums):
        return -1
        
    return lp if nums[lp] == tar else -1


def left_bound2(nums: List[int], tar: int) -> int:
    lp, rp = 0, len(nums) - 1

    while lp <= rp:
        mid = lp + (rp - lp) // 2
        if nums[mid] == tar:
            rp = mid - 1
        elif nums[mid] < tar:
            lp = mid + 1
        elif nums[mid] > tar:
            rp = mid - 1

    if lp >= len(nums):
        return -1
        
    return lp if nums[lp] == tar else -1


if __name__ == "__main__":
    nums = [1, 2, 2, 3]
    tar = 2
    res = left_bound2(nums, tar)
    assert res == 1, res
    
    nums = [1, 2, 3, 4, 4]
    tar = 4
    res = left_bound2(nums, tar)
    assert res == 3, res
    
    nums = [1, 2, 3, 4, 5]
    tar = 5
    res = left_bound2(nums, tar)
    assert res == 4, res
