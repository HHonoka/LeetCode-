# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        stack1 = [root.left]
        stack2 = [root.right]
        while stack1 and stack2:
            n1 = stack1.pop()
            n2 = stack2.pop()
            if not n1 and not n2:
                continue
            if (not n1 and n2) or (n1 and not n2) or (n1.val != n2.val):
                return False
            stack1.append(n1.left)
            stack2.append(n2.right)
            stack1.append(n1.right)
            stack2.append(n2.left)
        return True if not (stack1 and stack2) else False

#Iteratively

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        def helper(n1, n2):
            if not n1 and not n2:
                return True
            if (not n1 and n2) or (n1 and not n2) or (n1.val != n2.val):
                return False
            return helper(n1.left, n2.right) and helper(n1.right, n2.left)
        return helper(root.left, root.right)
#Recursive