# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.res = float('-inf')
        self.helper(root)
        return self.res - 1 if self.res != float('-inf') else 0
    def helper(self, node):
        if not node:
            return 0
        left = self.helper(node.left)
        right = self.helper(node.right)
        self.res = max(self.res, 1 + left + right)
        return 1 + max(left, right)