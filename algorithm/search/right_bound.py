from typing import List


def right_bound(nums: List[int], tar: int) -> int:
    lp, rp = 0, len(nums)

    while lp < rp:
        mid = lp + (rp - lp) // 2
        if nums[mid] == tar:
            lp = mid + 1
        elif nums[mid] < tar:
            lp = mid + 1
        elif nums[mid] > tar:
            rp = mid

    if lp == 0:
        return -1

    return lp - 1 if nums[lp - 1] == tar else -1


def right_bound2(nums: List[int], tar: int) -> int:
    lp, rp = 0, len(nums) - 1

    while lp <= rp:
        mid = lp + (rp - lp) // 2
        if nums[mid] == tar:
            lp = mid + 1
        elif nums[mid] < tar:
            lp = mid + 1
        elif nums[mid] > tar:
            rp = mid - 1

    if lp == 0:
        return -1

    return lp - 1 if nums[lp - 1] == tar else -1


if __name__ == "__main__":
    nums = [1, 2, 2, 3]
    tar = 2
    res = right_bound2(nums, tar)
    assert res == 2, res

    nums = [1, 2, 3, 4, 4]
    tar = 4
    res = right_bound2(nums, tar)
    assert res == 4, res

    nums = [1, 2, 3, 4, 5, 5]
    tar = 5
    res = right_bound2(nums, tar)
    assert res == 5, res
