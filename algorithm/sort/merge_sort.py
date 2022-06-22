from typing import List


def merge_sort(nums: List[int]):
    sort(nums, 0, len(nums) - 1)


def sort(nums: List[int], left: int, right: int):
    if left == right:
        return

    mid = left + (right - left) // 2
    sort(nums, left, mid)
    sort(nums, mid + 1, right)

    merge(nums, left, mid, right)


def merge(nums: List[int], left: int, mid: int, right: int):
    temp = []

    lp, rp = left, mid + 1
    while lp <= mid and rp <= right:
        if nums[lp] < nums[rp]:
            temp.append(nums[lp])
            lp += 1
        else:
            temp.append(nums[rp])
            rp += 1

    if lp == mid + 1:
        temp.extend(nums[rp : right + 1])
    else:
        temp.extend(nums[lp : mid + 1])

    nums[left : right + 1] = temp


if __name__ == "__main__":
    nums = [3, 5, 1, 4, 2]
    merge_sort(nums)
    print(nums)
