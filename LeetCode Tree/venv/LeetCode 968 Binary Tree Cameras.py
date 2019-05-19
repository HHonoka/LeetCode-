# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        self.res = 0
        def helper(node):
            if not node:
                return 1
            left = helper(node.left)
            right = helper(node.right)
            if left == 0 or right == 0:
                self.res += 1
                return 2
            if left == 2 or right == 2:
                return 1
            else:
                return 0
        if helper(root) == 0:
            self.res += 1
        return self.res


# 0 means not covered, 1 means coverd, 2 means covered and a camera on it ****************