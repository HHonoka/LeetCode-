# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.ans = float('-inf')
        self.helper(root)
        return self.ans
    def helper(self, node):
        if not node:
            return 0
        left = max(0, self.helper(node.left))
        right = max(0, self.helper(node.right))
        self.ans = max(self.ans, node.val + left + right)
        return node.val + max(left, right)