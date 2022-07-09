from typing import List


def binary_search(nums: List[int], tar: int) -> int:
    lp, rp = 0, len(nums)

    while lp < rp:
        mid = lp + (rp - lp) // 2
        if nums[mid] == tar:
            return mid
        elif nums[mid] < tar:
            lp = mid + 1
        elif nums[mid] > tar:
            rp = mid

    return -1


if __name__ == "__main__":
    nums = [1, 2, 3]
    tar = 2
    res = binary_search(nums, tar)
    assert res == 1, res
    
    nums = [1, 2, 3, 4]
    tar = 3
    res = binary_search(nums, tar)
    assert res == 2, res
