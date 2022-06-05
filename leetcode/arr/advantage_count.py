from queue import PriorityQueue
from typing import List


class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums1)
        res = [0] * n
        nums1.sort()

        queue = PriorityQueue()
        for i, v in enumerate(nums2):
            queue.put((-v, i))

        lp, rp = 0, n - 1
        while not queue.empty():
            pair = queue.get()
            num2, idx_num2 = -pair[0], pair[1]

            if nums1[rp] > num2:
                res[idx_num2] = nums1[rp]
                rp -= 1
            else:
                res[idx_num2] = nums1[lp]
                lp += 1

        return res


if __name__ == "__main__":
    nums1 = [2, 7, 11, 15]
    nums2 = [1, 10, 4, 11]
    res = Solution().advantageCount(nums1, nums2)
    assert res == [2, 11, 7, 15], res

    nums1 = [12, 24, 8, 32]
    nums2 = [13, 25, 32, 11]
    res = Solution().advantageCount(nums1, nums2)
    assert res == [24, 32, 8, 12], res
