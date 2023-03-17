import unittest
from typing import List, Optional


class ListNode:
    def __init__(self, val: int):
        self.val = val
        self.Left = None
        self.Right = None


class LinkedList:
    def __init__(self):
        self.root: Optional[ListNode] = None

    @staticmethod
    def from_list(nums: List[int]):
        pass


class TestLinkedList(unittest.TestCase):
    def test_from_list():
        pass

    def test_levelorder_traverse():
        pass
