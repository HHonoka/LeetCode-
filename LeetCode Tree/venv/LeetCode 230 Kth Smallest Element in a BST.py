# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        if not root:
            return 0
        stack = []
        curnode = root
        res = 0
        count = 0
        while curnode or stack:
            while curnode:
                stack.append(curnode)
                curnode = curnode.left
            node = stack.pop()
            count += 1
            if count == k:
                return node.val
            curnode = node.right
#Iteratively

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.res = 0
        self.k = k
        def helper(node):
            if node:
                helper(node.left)
                self.k -= 1
                if self.k == 0:
                    self.res = node.val
                    return
                helper(node.right)
        helper(root)
        return self.res
#Recursive