import unittest
from typing import Final, List, Optional

null: Final[int] = (1 << 31) - 1


class TreeNode:
    def __init__(self, val: int):
        self.val = val
        self.left: Optional[TreeNode] = None
        self.right: Optional[TreeNode] = None


class BinaryTree:
    def __init__(self, root=None):
        self.root: TreeNode | None = root

    @staticmethod
    def from_list(nums: List[int]) -> "BinaryTree":
        if len(nums) == 0:
            return BinaryTree()

        root = TreeNode(nums[0])
        nodes: list[TreeNode | None] = [root]

        for v in nums[1:]:
            nodes.append(TreeNode(v) if v != null else None)

        for idx, node in enumerate(nodes[: len(nodes) // 2]):
            if node is None:
                continue

            node.left = nodes[idx * 2 + 1]
            node.right = nodes[idx * 2 + 2]

        return BinaryTree(root)


def level_traverse(root: TreeNode | None) -> List[int]:
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


def preorder_traverse(root: TreeNode | None) -> List[int]:
    ans = []

    def helper(root: TreeNode | None):
        if root is None:
            return

        ans.append(root.val)
        helper(root.left)
        helper(root.right)

    helper(root)

    return ans


def inorder_traverse(root: TreeNode | None) -> List[int]:
    ans = []

    def helper(root: TreeNode | None):
        if root is None:
            return

        helper(root.left)
        ans.append(root.val)
        helper(root.right)

    helper(root)

    return ans


def postorder_traverse(root: TreeNode | None) -> List[int]:
    ans = []

    def helper(root: TreeNode | None):
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

        ans = preorder_traverse(tree.root)
        self.assertEqual(ans, [1, 2, 4, 3, 5])

        ans = inorder_traverse(tree.root)
        self.assertEqual(ans, [2, 4, 1, 3, 5])

    def test_level_traverse(self):
        nums = [1, 2, 3, null, 4, null, 5]
        tree = BinaryTree.from_list(nums)

        ans = level_traverse(tree.root)
        self.assertEqual(ans, [1, 2, 3, 4, 5])


if __name__ == "__main__":
    unittest.main()
