# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if self.search(s, t):
            return True
        if not s or not t:
            return False
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

    def search(self, s, t):
        if not s and not t:
            return True
        if (not s and t) or (s and not t):
            return False
        return s.val == t.val and self.search(s.left, t.left) and self.search(s.right, t.right)