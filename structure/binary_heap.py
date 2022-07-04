from typing import Callable


class BinaryHeap:
    def __init__(self, less: Callable[[int, int], int]):
        self.nums = []
        self.less = less

    def push(self, num: int):
        self.nums.append(num)
        self.heapify_up(len(self.nums) - 1)

    def pop(self) -> int:
        if len(self.nums) == 0:
            return -1

        self.nums[0], self.nums[-1] = self.nums[-1], self.nums[0]
        res = self.nums.pop()
        self.heapify_down(0)

        return res

    def heapify_up(self, idx: int):
        if idx == 0:
            return

        parent = (idx - 1) // 2
        if self.less(self.nums[idx], self.nums[parent]):
            self.nums[idx], self.nums[parent] = self.nums[parent], self.nums[idx]
            self.heapify_up(parent)

    def heapify_down(self, idx: int):
        child = 2 * idx + 1
        if child >= len(self.nums):
            return

        if child + 1 < len(self.nums) and self.less(self.nums[child + 1], self.nums[child]):
            child += 1

        if self.less(self.nums[child], self.nums[idx]):
            self.nums[idx], self.nums[child] = self.nums[child], self.nums[idx]
            self.heapify_down(child)


class MinHeap(BinaryHeap):
    def __init__(self):
        super().__init__(lambda x, y: x < y)


class MaxHeap(BinaryHeap):
    def __init__(self):
        super().__init__(lambda x, y: x > y)


if __name__ == "__main__":
    k = 2
    heap = MinHeap()
    nums = [3, 1, 6, 2, 4, 5]

    cnt = 0
    for num in nums:
        if cnt < k:
            heap.push(num)
            cnt += 1
        else:
            heap.push(num)
            heap.pop()

    print(heap.pop())
