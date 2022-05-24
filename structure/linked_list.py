from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self, nums=None):
        if nums is None or len(nums) == 0:
            self.head = None
            return

        self.head = ListNode(nums[0])
        curr = self.head

        for v in nums[1:]:
            curr.next = ListNode(v)
            curr = curr.next


def traverse(head: ListNode) -> List[int]:
    res = []
    curr = head

    while curr is not None:
        res.append(curr.val)
        curr = curr.next

    return res


if __name__ == "__main__":
    list = LinkedList(nums=[1, 2, 3, 4, 5])
    print(traverse(list.head))
