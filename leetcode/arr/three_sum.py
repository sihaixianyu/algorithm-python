from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        n = len(nums)
        for i in range(n - 2):
            if nums[i] > 0:
                break

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            lp, rp = i + 1, n - 1
            while lp < rp:
                sum = nums[i] + nums[lp] + nums[rp]
                if sum < 0:
                    lp += 1
                elif sum > 0:
                    rp -= 1
                else:
                    res.append([nums[i], nums[lp], nums[rp]])
                    lp, rp = lp + 1, rp - 1
                    while lp < rp and nums[lp] == nums[lp - 1]:
                        lp += 1
                    while lp < rp and nums[rp] == nums[rp + 1]:
                        rp -= 1

        return res


if __name__ == "__main__":
    nums = [-1, 0, 1, 2, -1, -4]
    res = Solution().threeSum(nums)
    assert [[-1, -1, 2], [-1, 0, 1]] == res, res

    nums = []
    res = Solution().threeSum(nums)
    assert [] == res, res

    nums = [0]
    res = Solution().threeSum(nums)
    assert [] == res, res

    nums = [0, 0, 0, 0]
    res = Solution().threeSum(nums)
    assert [[0, 0, 0]] == res, res

    nums = [1, -1, -1, 0]
    res = Solution().threeSum(nums)
    assert [[-1, 0, 1]] == res, res

    nums = [-2, 0, 0, 2, 2]
    res = Solution().threeSum(nums)
    assert [[-2, 0, 2]] == res, res
