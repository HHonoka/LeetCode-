# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        count = 0
        if not root:
            return count
        stack = [root]
        while stack:
            temp = []
            count += 1
            for node in stack:
                if not node.left and not node.right:
                    return count
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            stack = temp
        return count
#Iteratively

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        if not root.left:
            return 1 + self.minDepth(root.right)
        if not root.right:
            return 1 + self.minDepth(root.left)
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))

#Recursive