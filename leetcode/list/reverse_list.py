import os
import sys

sys.path.append(os.path.dirname(__file__) + "/../..")
from structure.linked_list import LinkedList, ListNode, traverse


class Solution:
    def reverse(self, left: ListNode, right: ListNode) -> ListNode:
        prev = None
        curr = left

        while curr is not right:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        return prev


if __name__ == "__main__":
    head = LinkedList([1, 2, 3]).head
    new_head = Solution().reverse(head, head.next.next.next)
    print(traverse(new_head))
