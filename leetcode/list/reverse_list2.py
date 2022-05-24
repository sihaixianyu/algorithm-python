import os
import sys

sys.path.append(os.path.dirname(__file__) + "/../..")
from structure.linked_list import LinkedList, ListNode, traverse


class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if left == 1:
            return self.reverseN(head, right)

        head.next = self.reverseBetween(head.next, left - 1, right - 1)

        return head

    def reverseN(self, head: ListNode, n: int) -> ListNode:
        if n == 1:
            self.successor = head.next
            return head

        tail = self.reverseN(head.next, n - 1)
        head.next.next = head
        head.next = self.successor

        return tail


if __name__ == "__main__":
    head = LinkedList([1, 2, 3, 4, 5]).head
    head = Solution().reverseBetween(head, 2, 4)
    assert [1, 4, 3, 2, 5] == traverse(head)
