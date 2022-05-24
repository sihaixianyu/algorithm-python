import os
import sys
from typing import List

sys.path.append(os.path.dirname(__file__) + "/../..")
from structure.binary_tree import BinaryTree, TreeNode, null


# 打家劫舍问题：https://leetcode.cn/problems/house-robber-iii/submissions/
class Solution:
    def rob(self, node: TreeNode) -> int:
        def robNode(node: TreeNode) -> List[int]:
            if node is None:
                return [0, 0]

            left_res = robNode(node.left)
            right_res = robNode(node.right)

            res = [0, 0]
            res[0] = max(left_res) + max(right_res)
            res[1] = node.val + left_res[0] + right_res[0]

            return res

        return max(robNode(node))

    def rob_(self, root: TreeNode) -> int:
        memo = {}

        def robNode(node):
            if node is None:
                return 0

            if node in memo.keys():
                return memo[node]

            case1 = node.val
            if node.left is not None:
                case1 += robNode(node.left.left) + robNode(node.left.right)
            if node.right is not None:
                case1 += robNode(node.right.left) + robNode(node.right.right)

            case2 = 0
            case2 += robNode(node.left)
            case2 += robNode(node.right)

            res = max(case1, case2)
            memo[node] = max(case1, case2)
            return res

        return robNode(root)

    def rob__(self, root: TreeNode) -> int:
        def robNode(node):
            if node is None:
                return 0

            case1 = node.val
            if node.left is not None:
                case1 += robNode(node.left.left) + robNode(node.left.right)
            if node.right is not None:
                case1 += robNode(node.right.left) + robNode(node.right.right)

            case2 = 0
            case2 += robNode(node.left)
            case2 += robNode(node.right)

            return max(case1, case2)

        return robNode(root)


if __name__ == "__main__":
    root = BinaryTree([3, 2, 3, null, 3, null, 1]).root
    res = Solution().rob(root)
    assert res == 7, res

    root = BinaryTree([3, 4, 5, 1, 3, null, 1]).root
    res = Solution().rob(root)
    assert res == 9, res

    root = BinaryTree([2, 1, 3, null, 4]).root
    res = Solution().rob(root)
    assert res == 7, res
