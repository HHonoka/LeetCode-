# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        stack1 = []
        stack2 = []
        res1 = []
        res2 = []
        if root1:
            stack1 = [root1]
            while stack1:
                node = stack1.pop()
                if not node.left and not node.right:
                    res1.append(node.val)
                else:
                    if node.right:
                        stack1.append(node.right)
                    if node.left:
                        stack1.append(node.left)
        if root2:
            stack2 = [root2]
            while stack2:
                node = stack2.pop()
                if not node.left and not node.right:
                    res2.append(node.val)
                else:
                    if node.right:
                        stack2.append(node.right)
                    if node.left:
                        stack2.append(node.left)

        return res1 == res2
#Iteratively

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        r1 = []
        r2 = []
        def helper(node, res):
            if node:
                if not node.left and not node.right:
                    res.append(node.val)
                helper(node.left, res)
                helper(node.right, res)
        helper(root1, r1)
        helper(root2, r2)
        return r1 == r2

#Recursive