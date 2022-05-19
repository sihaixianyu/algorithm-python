from collections import deque
from typing import List

null = None


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTree:
    def __init__(self, nums: List[int] = None):
        if nums is None or len(nums) == 0:
            self.root = None
            return

        self.root = TreeNode(nums[0])
        queue = deque([self.root])

        idx = 1
        skip = 0
        while idx < len(nums) and len(queue) > 0:
            if nums[idx] == null:
                skip += 1
                idx += 1
            else:
                curr = queue[0]
                node = TreeNode(nums[idx])

                if curr.left is None:
                    if skip == 0:
                        curr.left = node
                        queue.append(node)
                        idx += 1
                    else:
                        skip -= 1
                    continue

                if curr.right is None:
                    if skip == 0:
                        curr.right = node
                        queue.append(node)
                        idx += 1
                    else:
                        skip -= 1
                    queue.popleft()


def levelorder_traverse(root: TreeNode) -> List[int]:
    if root is None:
        return []

    res = []
    queue = deque([root])

    while len(queue) > 0:
        curr = queue.popleft()
        res.append(curr.val)

        if curr.left is not None:
            queue.append(curr.left)
        if curr.right is not None:
            queue.append(curr.right)

    return res


if __name__ == "__main__":
    nums = [1, 2, 3, null, 4]
    tree = BinaryTree(nums)
    res = levelorder_traverse(tree.root)
    print(res)
