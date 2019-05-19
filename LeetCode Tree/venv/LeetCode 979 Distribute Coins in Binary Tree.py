# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distributeCoins(self, root: TreeNode) -> int:
        self.res = 0
        def helper(node):
            if not node:
                return 0
            left = helper(node.left)
            right = helper(node.right)
            self.res += abs(left) + abs(right)
            return node.val + left + right - 1
        helper(root)
        return self.res