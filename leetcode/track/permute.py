from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        used = [0] * len(nums)
        backtrack(res, nums, path, used)

        return res


def backtrack(res, nums, path, used):
    if len(path) == len(nums):
        res.append(path.copy())
        return

    for i in range(len(nums)):
        if used[i] != 0:
            continue

        used[i] = 1
        path.append(nums[i])
        backtrack(res, nums, path, used)
        path.pop()
        used[i] = 0


if __name__ == "__main__":
    nums = [1, 2, 3]
    res = Solution().permute(nums)
    print(res)
