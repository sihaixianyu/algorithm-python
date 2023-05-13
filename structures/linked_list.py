import unittest
from typing import List, Optional


class ListNode:
    def __init__(self, val: int):
        self.val = val
        self.Left = None
        self.Right = None


class LinkedList:
    def __init__(self, nums: List[int] | None):
        if not nums:
            self.root: Optional[ListNode] = None
            return

        return LinkedList._from_list(nums)

    @staticmethod
    def _from_list(nums: List[int]):
        pass


class TestLinkedList(unittest.TestCase):
    def test_new(self):
        pass

    def test_traverse(self):
        pass
