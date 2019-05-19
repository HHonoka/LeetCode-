# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        self.ans = []
        def inorder(node):
            if node:
                inorder(node.left)
                self.ans.append(node.val)
                inorder(node.right)
        res = float('inf')
        inorder(root)
        for i in range(1, len(self.ans)):
            res = min(res, self.ans[i] - self.ans[i - 1])
        return res