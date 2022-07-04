import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        cnt = 0

        for num in nums:
            if cnt < k:
                heapq.heappush(heap, num)
                cnt += 1
            else:
                heapq.heappush(heap, num)
                heapq.heappop(heap)
            print(heap)

        return heapq.heappop(heap)


if __name__ == "__main__":
    nums = [3, 2, 1, 5, 6, 4]
    k = 2
    res = Solution().findKthLargest(nums, k)
    assert res == 5, res
