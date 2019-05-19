# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.firstnode = None
        self.secondnode = None
        self.prenode = None
        self.inorder(root)
        self.firstnode.val, self.secondnode.val = self.secondnode.val, self.firstnode.val
    def inorder(self, node):
        if node:
            self.inorder(node.left)
            if self.prenode and self.prenode.val > node.val:
                if not self.firstnode:
                    self.firstnode = self.prenode
                self.secondnode = node
            self.prenode = node
            self.inorder(node.right)

#Recursive

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        stack = []
        first = None
        second = None
        pre = None
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                if pre and pre.val > root.val:
                    if not first:
                        first = pre
                    second = root
                pre = root
                root = root.right
        first.val, second.val = second.val, first.val
#Iteratively