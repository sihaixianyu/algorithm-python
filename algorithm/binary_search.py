import unittest
from typing import List, Optional


def search(nums: List[int], target: int) -> Optional[int]:
    left, right = 0, len(nums)

    while left < right:
        mid = left + (right - left) // 2
        if target == nums[mid]:
            return mid
        elif target > nums[mid]:
            left = mid + 1
        elif target < nums[mid]:
            right = mid

    return None


def left_bound(nums: List[int], target: int) -> Optional[int]:
    left, right = 0, len(nums)

    while left < right:
        mid = left + (right - left) // 2
        if target == nums[mid]:
            right = mid
        elif target > nums[mid]:
            left = mid + 1
        elif target < nums[mid]:
            right = mid

    if left < 0 or left >= len(nums):
        return None

    return left if nums[left] == target else None


def right_bound(nums: List[int], target: int) -> Optional[int]:
    left, right = 0, len(nums)

    while left < right:
        mid = left + (right - left) // 2
        if target == nums[mid]:
            left = mid + 1
        elif target > nums[mid]:
            left = mid + 1
        elif target < nums[mid]:
            right = mid

    return left - 1 if nums[left - 1] == target else None


class TestSearch(unittest.TestCase):
    def test_case_1(self):
        nums = [1, 2, 3, 4, 5]
        idx_tgt = search(nums, 4)
        self.assertEqual(idx_tgt, 3)

    def test_case_2(self):
        nums = [1, 2, 3, 4, 5]
        idx_tgt = search(nums, 6)
        self.assertIsNone(idx_tgt)


class TestLeftBound(unittest.TestCase):
    def test_case_1(self):
        nums = [1, 3, 3, 3, 5]
        idx_tgt = left_bound(nums, 3)
        self.assertEqual(idx_tgt, 1)

    def test_case_2(self):
        nums = [1, 3, 3, 3, 5]
        idx_tgt = left_bound(nums, 6)
        self.assertIsNone(idx_tgt)


class TestRightBound(unittest.TestCase):
    def test_case_1(self):
        nums = [1, 3, 3, 3, 5]
        idx_tgt = right_bound(nums, 3)
        self.assertEqual(idx_tgt, 3)

    def test_case_2(self):
        nums = [1, 3, 3, 3, 5]
        idx_tgt = right_bound(nums, 6)
        self.assertIsNone(idx_tgt)


if __name__ == "__main__":
    unittest.main(verbosity=2)
