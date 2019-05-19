# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        self.ans = 0
        self.helper(root, 0)
        return self.ans

    def helper(self, root, count):
        if not root:
            return
        if not root.left and not root.right:
            self.ans += count * 10 + root.val
        self.helper(root.left, count * 10 + root.val)
        self.helper(root.right, count * 10 + root.val)
#Recursive

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        res = 0
        if not root:
            return 0
        stack = [(root, 0)]
        while stack:
            node, count = stack.pop()
            if node:
                if not node.left and not node.right:
                    res += count * 10 + node.val
                stack.append((node.left, count * 10 + node.val))
                stack.append((node.right, count * 10 + node.val))
        return res

#Iteratively