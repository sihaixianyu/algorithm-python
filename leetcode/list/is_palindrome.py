import os
import sys

sys.path.append(os.path.dirname(__file__) + "/../..")
from structure.linked_list import LinkedList, ListNode


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head is not None or head.next is not None:
            return True

        slow, fast = head, head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next

        new_head = reversePartial(head, slow)
        if fast is not None:
            slow = slow.next

        p1, p2 = new_head, slow
        while p1 is not None and p2 is not None:
            if p1.val != p2.val:
                return False
            p1, p2 = p1.next, p2.next

        if p1 is not None or p2 is not None:
            return False

        return True


def reversePartial(left: ListNode, right: ListNode) -> ListNode:
    prev = None
    curr = left

    while curr is not right:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next

    return prev


if __name__ == "__main__":
    head = LinkedList([1, 2, 2, 1]).head
    res = Solution().isPalindrome(head)
    assert res is True, res

    head = LinkedList([1, 2]).head
    res = Solution().isPalindrome(head)
    assert res is False, res

    head = LinkedList([1, 0, 1]).head
    res = Solution().isPalindrome(head)
    assert res is True, res
