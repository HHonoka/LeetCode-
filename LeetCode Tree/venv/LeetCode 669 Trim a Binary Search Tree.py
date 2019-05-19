# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def trimBST(self, root: TreeNode, L: int, R: int) -> TreeNode:
        return self.helper(root, L, R)

    def helper(self, node, L, R):
        if not node:
            return
        if node.val < L:
            return self.helper(node.right, L, R)
        if node.val > R:
            return self.helper(node.left, L, R)
        node.left = self.helper(node.left, L, R)
        node.right = self.helper(node.right, L, R)
        return node
