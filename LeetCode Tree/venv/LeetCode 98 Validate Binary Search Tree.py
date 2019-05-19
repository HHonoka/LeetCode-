# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def valid(node, minval, maxval):
            if not node:
                return True
            if node.val >= maxval or node.val <= minval:
                return False
            return valid(node.left, minval, min(maxval, node.val)) and valid(node.right, max(minval, node.val), maxval)
        return valid(root, float('-inf'), float('inf'))

#Recursive

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        stack = [(root, float('inf'), float('-inf'))]
        while stack:
            node, maxval, minval = stack.pop()
            if node:
                if node.val <= minval or node.val >= maxval:
                    return False
                else:
                    stack.append((node.left, min(maxval, node.val), minval))
                    stack.append((node.right, maxval, max(minval, node.val)))
        return True
#Iteratively

#BST concept！！！！
#Wrong Answer！
# class Solution:
#     def isValidBST(self, root: TreeNode) -> bool:
#         if not root:
#             return True
#         stack = [root]
#         while stack:
#             node = stack.pop()
#             if node.left:
#                 if node.left.val >= node.val:
#                     return False
#                 else:
#                     stack.append(node.left)
#             if node.right:
#                 if node.right.val <= node.val:
#                     return False
#                 else:
#                     stack.append(node.right)
#         return True