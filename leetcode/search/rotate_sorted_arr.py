from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lp, rp = 0, len(nums) - 1

        while lp <= rp:
            mid = lp + (rp - lp) // 2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                if nums[mid] > nums[rp] and target <= nums[rp]:
                    lp = mid + 1
                else:
                    rp = mid - 1
            elif target > nums[mid]:
                if nums[mid] <= nums[rp] and target > nums[rp]:
                    rp = mid - 1
                else:
                    lp = mid + 1

        return -1


if __name__ == "__main__":
    # nums = [4, 5, 6, 7, 0, 1, 2]
    # target = 0
    # res = Solution().search(nums, target)
    # assert 4 == res, res

    nums = [4, 5, 6, 7, 8, 1, 2, 3]
    target = 8
    res = Solution().search(nums, target)
    assert 4 == res, res
