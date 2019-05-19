# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        self.ans = float('-inf')
        self.helper(root, None)
        return self.ans - 1 if self.ans != float('-inf') else 0
    def helper(self, node, parent):
        if not node:
            return 0
        left = self.helper(node.left, node)
        right = self.helper(node.right, node)
        self.ans = max(self.ans, 1 + left + right)
        if parent and node.val == parent.val:
            return 1 + max(left, right)
        else:
            return 0