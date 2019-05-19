# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        if not root:
            return True
        if root.left:
            if root.left.val != root.val:
                return False
        if root.right:
            if root.right.val != root.val:
                return False
        return self.isUnivalTree(root.left) and self.isUnivalTree(root.right)
#Recursive

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        if not root:
            return True
        v = root.val
        stack = [root]
        while stack:
            node = stack.pop()
            if node.val != v:
                return False
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return True
#Iteratively