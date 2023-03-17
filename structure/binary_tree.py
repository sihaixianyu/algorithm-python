import sys
import unittest
from typing import Final, List, Optional

null: Final[int] = sys.maxsize


class TreeNode:
    def __init__(self, val: int):
        self.val = val
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, root=None):
        self.root: Optional[TreeNode] = root

    def traverse_level(self) -> List[int]:
        return level_traverse(self.root)

    def traverse_preorder(self) -> List[int]:
        return preorder_traverse(self.root)

    def traverse_inorder(self) -> List[int]:
        return inorder_traverse(self.root)

    def traverse_postorder(self) -> List[int]:
        return postorder_traverse(self.root)

    @staticmethod
    def from_list(nums: List[int]) -> "BinaryTree":
        if len(nums) == 0:
            return BinaryTree()

        root = TreeNode(nums[0])
        nodes = [root]

        for v in nums[1:]:
            nodes.append(TreeNode(v) if v != null else None)

        for idx, node in enumerate(nodes[: len(nodes) // 2]):
            if node is None:
                continue

            node.left = nodes[idx * 2 + 1]
            node.right = nodes[idx * 2 + 2]

        return BinaryTree(root)


def level_traverse(root: TreeNode) -> List[int]:
    if root is None:
        return []

    ans = []
    queue = [root]

    while len(queue) > 0:
        node = queue.pop(0)
        ans.append(node.val)

        if node.left is not None:
            queue.append(node.left)

        if node.right is not None:
            queue.append(node.right)

    return ans


def preorder_traverse(root: TreeNode) -> List[int]:
    ans = []

    def helper(root: TreeNode):
        if root is None:
            return

        ans.append(root.val)
        helper(root.left)
        helper(root.right)

    helper(root)

    return ans


def inorder_traverse(root: TreeNode) -> List[int]:
    ans = []

    def helper(root: TreeNode):
        if root is None:
            return

        helper(root.left)
        ans.append(root.val)
        helper(root.right)

    helper(root)

    return ans


def postorder_traverse(root: TreeNode) -> List[int]:
    ans = []

    def helper(root: TreeNode):
        if root is None:
            return

        helper(root.left)
        helper(root.right)
        ans.append(root.val)

    helper(root)

    return ans


class TestBinaryTree(unittest.TestCase):
    def test_from_list(self):
        nums = [1, 2, 3, null, 4, null, 5]
        tree = BinaryTree.from_list(nums)

        ans = tree.traverse_preorder()
        self.assertEqual(ans, [1, 2, 4, 3, 5])

        ans = tree.traverse_inorder()
        self.assertEqual(ans, [2, 4, 1, 3, 5])

    def test_level_traverse(self):
        nums = [1, 2, 3, null, 4, null, 5]
        tree = BinaryTree.from_list(nums)

        ans = level_traverse(tree.root)
        self.assertEqual(ans, [1, 2, 3, 4, 5])


if __name__ == "__main__":
    unittest.main()
